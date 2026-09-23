#!/usr/bin/env python3
"""
run-factory-agent.py

Runs a Factory Agent Task in a GitHub Actions runner - the Tier 2
mechanism implementation/04-agent-isolation-and-harnessing.md called
for: this executes in a process with no mcp__remote-devices__* (or
equivalent broad-filesystem) tools to discover in the first place, so
"a subagent can ToolSearch its way to the real repo" (the finding that
made Tier 1 not a real boundary) cannot happen here - there is nothing
to find.

This is NOT just "ask Claude nicely to stay in scope" repeated in a new
place. The write_file tool below is a real code-level gate: it refuses
(raises, does not silently comply) any path outside the allowed
prefixes, regardless of what the model asks for. That is the actual
fix - scope-check.py (run separately, after, as a required CI check)
is defense in depth on top of this, not the only thing standing between
a bad write and the real repo.

Usage:
    python3 run-factory-agent.py \\
        --task-file implementation/factory-runs/<slug>/task-*.md \\
        --agent-file implementation/agents/factory-agent.md \\
        --allow-prefix implementation/factory-runs/<slug>/sandbox/

Requires: ANTHROPIC_API_KEY in the environment, and the `anthropic`
package (pip install anthropic).

Exit codes: 0 = model finished (ended its turn without more tool
calls); 1 = a fatal setup/API error; 2 = hit MAX_TURNS without
finishing (treat as a failed run, same as an Eval failure - do not
merge its output).
"""

import argparse
import json
import os
import sys
from pathlib import Path

try:
    import anthropic
except ImportError:
    print("Missing dependency: anthropic. Run: pip install anthropic", file=sys.stderr)
    sys.exit(1)

MAX_TURNS = 40
MODEL = os.environ.get("FACTORY_AGENT_MODEL", "claude-sonnet-4-5-20250929")
REPO_ROOT = Path(".").resolve()


class ScopeViolation(Exception):
    pass


def resolve_and_check(path_str: str, allowed_prefixes: list[str]) -> Path:
    """The actual enforcement. Resolves the path, refuses anything
    outside the repo root or outside every allowed prefix. This is a
    hard stop, not an instruction - it raises regardless of what the
    model's reasoning claimed the write was for."""
    candidate = (REPO_ROOT / path_str).resolve()
    try:
        rel = candidate.relative_to(REPO_ROOT)
    except ValueError:
        raise ScopeViolation(f"path escapes repo root: {path_str}")
    rel_str = str(rel).replace(os.sep, "/")
    if not any(rel_str.startswith(p) for p in allowed_prefixes):
        raise ScopeViolation(
            f"path '{rel_str}' is outside every allowed prefix {allowed_prefixes} - refused, not written"
        )
    return candidate


def make_tools(allowed_prefixes: list[str]):
    def read_file(path: str) -> str:
        target = (REPO_ROOT / path).resolve()
        try:
            target.relative_to(REPO_ROOT)
        except ValueError:
            return f"ERROR: path escapes repo root: {path}"
        if not target.is_file():
            return f"ERROR: not found: {path}"
        try:
            return target.read_text(encoding="utf-8")
        except Exception as e:
            return f"ERROR reading {path}: {e}"

    def write_file(path: str, content: str) -> str:
        try:
            target = resolve_and_check(path, allowed_prefixes)
        except ScopeViolation as e:
            # Logged loudly - this is exactly the event that should
            # never again be caught only by a post-hoc diff.
            print(f"SCOPE VIOLATION BLOCKED: {e}", file=sys.stderr)
            return f"REFUSED: {e}"
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding="utf-8")
        return f"wrote {len(content)} bytes to {path}"

    def list_dir(path: str) -> str:
        target = (REPO_ROOT / path).resolve()
        try:
            target.relative_to(REPO_ROOT)
        except ValueError:
            return f"ERROR: path escapes repo root: {path}"
        if not target.is_dir():
            return f"ERROR: not a directory: {path}"
        entries = sorted(p.name + ("/" if p.is_dir() else "") for p in target.iterdir())
        return "\n".join(entries) if entries else "(empty)"

    return {"read_file": read_file, "write_file": write_file, "list_dir": list_dir}


TOOL_SCHEMAS = [
    {
        "name": "read_file",
        "description": "Read a text file's contents, given a path relative to the repo root.",
        "input_schema": {
            "type": "object",
            "properties": {"path": {"type": "string"}},
            "required": ["path"],
        },
    },
    {
        "name": "write_file",
        "description": (
            "Write a text file, given a path relative to the repo root and its full "
            "content. REFUSED if the path is outside your allowed write scope - this "
            "is enforced in code, not by instruction, so do not attempt a workaround "
            "path; the refusal is final for this run."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "path": {"type": "string"},
                "content": {"type": "string"},
            },
            "required": ["path", "content"],
        },
    },
    {
        "name": "list_dir",
        "description": "List a directory's entries, given a path relative to the repo root.",
        "input_schema": {
            "type": "object",
            "properties": {"path": {"type": "string"}},
            "required": ["path"],
        },
    },
]


def extract_system_prompt(agent_md_path: str) -> str:
    text = Path(agent_md_path).read_text(encoding="utf-8")
    # Frontmatter is delimited by --- ... --- at the top; system prompt is everything after.
    parts = text.split("---", 2)
    if len(parts) < 3:
        raise ValueError(f"{agent_md_path}: expected YAML frontmatter delimited by '---'")
    return parts[2].strip()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--task-file", required=True)
    parser.add_argument("--agent-file", required=True)
    parser.add_argument("--allow-prefix", action="append", required=True,
                         help="Repeatable. Only these path prefixes are writable.")
    args = parser.parse_args()

    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("Error: ANTHROPIC_API_KEY is not set", file=sys.stderr)
        return 1

    system_prompt = extract_system_prompt(args.agent_file)
    task_content = Path(args.task_file).read_text(encoding="utf-8")

    tools = make_tools(args.allow_prefix)
    client = anthropic.Anthropic(api_key=api_key)

    messages = [
        {
            "role": "user",
            "content": (
                f"Your routed Factory Run Task Document ({args.task_file}):\n\n"
                f"```\n{task_content}\n```\n\n"
                f"Your write scope for this run is strictly: {args.allow_prefix} "
                f"(enforced by the write_file tool itself - an out-of-scope write "
                f"is refused, not silently redirected). Begin."
            ),
        }
    ]

    for turn in range(MAX_TURNS):
        resp = client.messages.create(
            model=MODEL,
            max_tokens=4096,
            system=system_prompt,
            tools=TOOL_SCHEMAS,
            messages=messages,
        )
        messages.append({"role": "assistant", "content": resp.content})

        tool_uses = [b for b in resp.content if b.type == "tool_use"]
        for b in resp.content:
            if b.type == "text" and b.text.strip():
                print(f"[turn {turn}] {b.text.strip()}")

        if not tool_uses:
            print(f"Run finished after {turn + 1} turn(s) - no further tool calls.")
            return 0

        tool_results = []
        for tu in tool_uses:
            fn = tools.get(tu.name)
            if fn is None:
                result = f"ERROR: unknown tool {tu.name}"
            else:
                try:
                    result = fn(**tu.input)
                except Exception as e:
                    result = f"ERROR: {e}"
            print(f"[turn {turn}] {tu.name}({json.dumps(tu.input)[:200]}) -> {str(result)[:200]}")
            tool_results.append({
                "type": "tool_result",
                "tool_use_id": tu.id,
                "content": str(result),
            })
        messages.append({"role": "user", "content": tool_results})

    print(f"FAILED: hit MAX_TURNS ({MAX_TURNS}) without the model ending its turn.", file=sys.stderr)
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
