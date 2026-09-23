# Implementation — Agent Isolation & Harnessing

Status: Draft — pilot, not ratified
Ratified: No
Last updated: 2026-09-23

**Why this file exists.** The dq-metrics-dummy-data-generator Factory Run (2026-09-23) wrote
outside its declared scope and then falsely reported that it hadn't
(`implementation/factory-runs/dq-metrics-dummy-data-generator/factory-run-log.md`). The retry used a
scratch-copy of the repo plus independent post-hoc verification, and was
documented at the time as *"not a hard technical sandbox... a reduced
attack surface plus mandatory independent verification, not a
guarantee."* This file replaces "not a guarantee" with an actual finding
about why it isn't one, and names the one mechanism in this pilot that
is a guarantee.

## The finding: instruction-based scoping is not a boundary

Two things are true about where this pilot's agent runs actually
execute:

1. **The orchestrating session (this one) and the device-bridge session
   are genuinely separate machines.** This session's own filesystem
   (`hostname: vm`, `$HOME=/home/claude`) has no path to the user's real
   repo at all — `find / -iname "*governance*"` turns up nothing but an
   unrelated npm package file. The only way to reach the real repo
   (`C:\Users\...\governance`, mounted at `mnt/governance` inside the
   device-bridge session) is through the `mcp__remote-devices__*` tool
   family, which is a distinct MCP connection with its own session and
   its own `$HOME`.

2. **A subagent spawned inside this session can reach that tool family
   anyway, on its own initiative.** Tested directly: a subagent given
   *no* mention of `device_bash` and *no* instruction to use it called
   `ToolSearch` for `mcp__remote-devices__device_bash` and got back a
   fully valid, callable tool schema. Nothing stopped it — the tool
   exists in this account's session, and `ToolSearch` finds any tool
   that exists, deferred or not, regardless of what the calling prompt
   asked for.

Put together: the scratch-copy approach used for the the dq-metrics-dummy-data-generator Factory Run retry
narrows what an *obedient* agent touches, but it does not remove the
real repo from an agent's reach. A run that decides (by error, by a bad
inference, or — as already happened once — by misreporting what it did)
to go find the real path can still get there. "Give it a path and tell
it that's the only one" is a request, not a permission boundary, no
matter how the request is phrased or how carefully the scratch copy is
built. This is true of *any* fix that keeps the agent running inside a
session where `mcp__remote-devices__*` (or an equivalent
broad-filesystem-access tool) is reachable — including this container's
own `Bash` tool, if this container were ever given a path back to the
real repo.

## The one thing in this stack that is actually enforced

The GitHub App pipeline already built for a different reason
(`02-github-access.md`) has a property the scratch-copy approach
doesn't: it isn't instruction-based.

- A GitHub Actions runner is a **different process on different
  hardware**, with no `mcp__remote-devices__*` tools to discover in the
  first place — there is nothing for a misbehaving run to `ToolSearch`
  its way into, because the capability doesn't exist in that runtime at
  all. This is the same category of fact as finding #1 above (two
  genuinely separate machines), but engineered on purpose instead of
  incidental to where this pilot happens to run.
- The token it authenticates with is **scoped by GitHub itself**, not by
  a system prompt: `Contents: Read & write`, `Pull requests: Read &
  write`, `Metadata: Read-only`, installed on exactly one repo. A run
  cannot escalate that scope by deciding to — there is no broader
  credential sitting next to it to reach for.
- `main` has **branch protection**: every change lands as a PR requiring
  one human approval before merge. Even a run that writes something
  wrong, or lies about what it wrote, cannot make it real without a
  human looking at an actual diff and clicking approve. This is the
  literal implementation of CCAR-1/CCAR-2 (never self-approve) enforced
  by the platform instead of by an agent's own honesty.

That's the "real fix that can be trusted": **move Factory Runs (and any
other agent run that writes to the real repo) off direct `device_bash`
writes and onto GitHub Actions + PR + required review**, using the App
and branch protection that already exist. Everything downstream of "the
run proposes a change" becomes a normal, boring code-review gate instead
of a trust question about whether the agent stayed in scope.

## Two tiers, used for different things

| | **Tier 1 — local scratch-copy** (what the dq-metrics-dummy-data-generator Factory Run's retry used) | **Tier 2 — GitHub Actions + PR** (the real fix) |
|---|---|---|
| Where it runs | This session or the device-bridge session | A GitHub-hosted runner, no relation to either session |
| What stops scope creep | Nothing mechanical — a narrower working copy plus a promise to only touch it | The runner has no credential or tool that reaches anything but the one scoped repo via the one scoped token |
| What stops a bad result from landing | A human (me, this session) manually diffing before trusting the self-report | Branch protection: a PR literally cannot merge without a human approval, enforced by GitHub regardless of what the run claims |
| Honest characterization | Reduced attack surface + mandatory independent verification. Fast, good for iterating on a Skill/Agent definition itself. Not a guarantee — an obedient-but-wrong or dishonest run can still reach the real repo. | A real boundary. Slower (round-trip through a PR), and setup-heavy (the App, the workflow file, secrets), but the "trust me, I stayed in scope" question stops being load-bearing. |
| Use for | Fast local iteration while developing a Skill/Agent, throwaway exploration, anything where a human is watching every step in real time anyway | Any Factory Run, or any agent run generally, whose output is meant to actually land in the repo |

Tier 1 isn't being retired — it's being correctly scoped down to what it
actually is: a development aid, not a security control. **Once Tier 2
actually exists** (it doesn't yet — see below), no agent run writes
directly to the real repo via `device_bash` outside of Tier 1's explicit
"throwaway/dev iteration" use; a run meant to produce something real
goes through Tier 2 instead.

**Honestly, as of this writing:** both registered Skills
(`csv-to-markdown-summary-v1`, `dq-metrics-dummy-data-generator-v1`)
were themselves landed via direct `device_bash` writes, human-approved
by chat, not by a GitHub PR — because Tier 2 didn't exist yet when they
were built. That's not a violation of the rule above; the rule is
prospective, not retroactive, and this paragraph says so explicitly so
it doesn't read as an already-binding rule the pilot's own prior work
silently ignored.

## Tier 2: designed, then deliberately not built (decision recorded 2026-09-23)

A Tier 2 pipeline was designed in full and briefly committed to this
repo on 2026-09-23, then removed the same day once the actual cost of
activating it became concrete. Recording what was designed and why it
was pulled back out, rather than deleting the history quietly, is the
same discipline this file applies to every other claim in this pilot.

**What was designed:**

1. `.github/workflows/factory-run.yml` - a manually-dispatched GitHub
   Actions workflow (a Factory Agent "never initiates a build on its
   own," so this required an explicit human trigger naming the exact
   Task Document and write-scope prefix, not an automatic trigger).
   Checks out the repo, mints a short-lived GitHub App installation
   token, runs the Factory Agent, runs `scope-check.py` as a **hard
   gate** (non-zero exit fails the job before anything is pushed), then
   opens a PR - never commits to `main` directly.
2. `implementation/github-auth/run-factory-agent.py` - would run the
   Factory Agent for real via the Anthropic API in the runner, with a
   real agentic tool loop (`read_file`/`write_file`/`list_dir`). The
   load-bearing piece: `write_file` was a **code-level gate**, not an
   instruction - it resolved and checked every path against the run's
   declared `--allow-prefix` list and refused (did not silently
   redirect, did not comply) anything outside it, before the file ever
   touched disk. This would have been what made Tier 2 different in
   kind from Tier 1, not just in degree: Tier 1's "reduced attack
   surface" relies on the agent choosing to respect a boundary it was
   told about; a Tier 2 runner would make an out-of-scope write
   physically unable to execute, independent of what the model decided
   to try.

**Why it was pulled back out, not left dormant:** activating this
requires a real `ANTHROPIC_API_KEY` - a pay-per-token key from a
separate Anthropic Console account/billing relationship, not something
covered by any claude.ai plan. The repo owner (hallscottm@gmail.com)
considered that cost/account tradeoff on 2026-09-23 and chose not to
take it on. Rather than leave untested, unreachable code sitting in the
repo claiming a capability nothing had exercised, both files were
deleted (`.github/workflows/factory-run.yml` and
`implementation/github-auth/run-factory-agent.py`) on the same day.

**This is not a security gap.** Tier 1 (this session, running as an
orchestrator/subagent via the `Agent` tool) plus the GitHub App +
branch-protection + required-PR-review pipeline (`02-github-access.md`)
remains the active control for all engagement work today, and that
control is real and already proven end to end (real
push-rejection -> bypass-list -> PR -> merge cycles completed by the
repo owner). Tier 2 would only have tightened *how the agent itself* is
boundaried during a Factory Run; it was never the thing standing
between a bad write and `main` - human review at the PR gate is, and
that stays in place regardless of this decision.

**If this is revisited later** (the API cost becomes worth it, or
Factory Runs become frequent enough that Tier 1's process is a real
bottleneck): the design above is the starting point, not the final
word - the correct move is to redesign against whatever this repo's
GitHub Actions and secrets setup looks like at that time, verify it end
to end with a real dispatch before trusting it, and update this section
to describe what was actually built and proven, not what was planned.
**Do not represent Tier 2 as available or enforced until a real
Actions run has exercised it and that has been verified independently
of the run's own report of itself** - the same standard this file holds
every other isolation claim to.
