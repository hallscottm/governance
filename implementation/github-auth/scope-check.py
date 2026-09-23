#!/usr/bin/env python3
"""
scope-check.py

Mechanical check that a completed agent run's actual file changes stay
within its declared write scope. Built directly in response to
the dq-metrics-dummy-data-generator Factory Run's finding
(implementation/factory-runs/dq-metrics-dummy-data-generator/factory-run-log.md,
2026-09-23): a Factory Run wrote outside its declared scope and its own
self-report falsely claimed it hadn't. Never again trust the self-report
alone - run this instead, every time, as part of Eval.

Usage:
    python3 scope-check.py <allowed-path-prefix> [<allowed-path-prefix> ...]

Compares `git status --porcelain` (staged, unstaged, AND untracked
changes) against the given allowed path prefixes. Any changed or new
file outside every given prefix is reported as a violation. Exits 0
with "SCOPE CHECK: PASS" if every change is in scope, exits 1 with
"SCOPE CHECK: FAIL" and the offending paths listed if not - so it can
gate a Factory Run's Eval stage instead of relying on the run's own
account of what it touched.

Run from the repo root (or pass --repo <path>).
"""

import argparse
import subprocess
import sys


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("prefixes", nargs="+", help="allowed path prefixes, e.g. implementation/factory-runs/dq-metrics-dummy-data-generator/sandbox/")
    parser.add_argument("--repo", default=".", help="repo root (default: current directory)")
    args = parser.parse_args()

    result = subprocess.run(
        ["git", "-C", args.repo, "status", "--porcelain"],
        capture_output=True, text=True, check=True,
    )

    violations = []
    changed = []
    for line in result.stdout.splitlines():
        if not line.strip():
            continue
        # porcelain format: XY <path>  (rename lines have "-> " too)
        path = line[3:].split(" -> ")[-1].strip()
        changed.append(path)
        if not any(path.startswith(prefix) for prefix in args.prefixes):
            violations.append(path)

    print(f"Changed/new files ({len(changed)}):")
    for p in changed:
        print(f"  {p}")
    print()
    print(f"Allowed prefixes: {args.prefixes}")
    print()

    if violations:
        print("SCOPE CHECK: FAIL")
        print("Files outside declared scope:")
        for v in violations:
            print(f"  ** {v}")
        return 1

    print("SCOPE CHECK: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
