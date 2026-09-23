# Implementation — Overview

Status: Draft — pilot, not ratified
Ratified: No
Last updated: 2026-09-23

**This area is not governance content.** Everything else in this repo
(`00-framework/`, `cross-cutting/`, the 8 domains, `engagements/`) is
spec: the rules, the vocabulary, the templates. `implementation/` is
the other half — a reference runtime that compiles that spec into
actually-running agents, so the framework can be tested against a real
case instead of only reasoned about on paper.

**Placement is deliberately temporary.** In a real org this would not
sit inside the governance repo at all — it would be its own repo (or
deployment target), consumed by the governance repo the same way any
other implementation consumes a spec it doesn't own. It lives here for
now because the pilot needs tight iteration between "the spec says X"
and "does X actually work," and that loop is faster in one repo. When
the pilot is solid, splitting this out is mechanical: everything in
here already only *references* engagements/ and cross-cutting/ anchors,
nothing here is referenced back (governance content never points into
`implementation/`) — so the cut is a directory move, not a rewrite.
Tracked as a housekeeping item, not urgent while this is one person's
POC.

## What "compiling" a spec means, concretely

| Governance concept | Compiles to |
|---|---|
| Agent Library / Template entry (Capability Scope + Tool Permission Scope + Escalation Path) | A subagent definition: a system prompt (the Capability Scope and Escalation Path, in instruction form) + a tool allowlist (the Tool Permission Scope) |
| Skill Library entry | A Skill definition (instructions the agent follows when the Skill is invoked) |
| Task Document, `assigned_agent` | An actual agent run, scoped to that Task's Capability/Tool Scope |
| Sandbox (HPOL-1) | An isolated test run before the candidate is trusted with real write access |
| Approval Gate (CCAR-1/2/4) | A real human decision — not simulated, not another agent standing in for a human |
| Harness Trace (`harness-trace`) | The run's transcript / tool-call log |

This mapping is intentionally minimal — it names what each governance
concept becomes, not a new abstraction layer on top of them. Where the
mapping is awkward or incomplete, that's a real finding about the spec,
recorded in the relevant pilot log rather than papered over here.

## Structure

- `agents/` — hand-compiled subagent definitions for the pre-built
  Agents (Vetting, Planning; Factory once piloted). Each file's header
  states exactly which Agent Library/engagements entry it was compiled
  from and the date, so drift between spec and implementation is
  visible at a glance.
- `pilots/` — one folder per **Pilot**: an end-to-end test of the
  framework against one real request (Vetting -> Planning -> Project
  Document -> Tasks). Each holds the real artifacts produced and a
  pilot log noting what matched the paper spec, what didn't, and what
  changed as a result.
- `factory-runs/` — one folder per **Factory Run**: a single test of
  the Factory Agent building one candidate Skill or Agent Template.
  Not the same thing as a Pilot, and not nested inside one — a Factory
  Run's own Task Document `parent_project` field says whether it's
  standalone or serving a specific Pilot; see `05-conventions.md`.
- `01-running-an-engagement.md` — the runbook: exact prompt pattern for
  each step, idea to completion.
- `05-conventions.md` — naming rules for everything in this directory
  (Pilots, Factory Runs, agent/skill definition files), derived from
  fields the documents already carry rather than assigned by feel.
  Written after Pilot and Factory Run folders drifted out of sync with
  their own front matter (a Factory Run that served a specific Pilot
  was folder-named as if it were a standalone, numbered peer of one
  that wasn't) — the same category of gap as the isolation finding
  below: a rule that only exists as "get it right in the moment" isn't
  a rule.
- `02-github-access.md`, `github-auth/` — how an agent authenticates to
  GitHub (a GitHub App, not a shared credential) and the branch -> PR
  -> human-merge workflow that replaces direct working-tree writes.
- `03-new-deployment-bootstrap.md` — the checklist for standing this up
  for a new client/org from scratch, so GitHub access setup (and the
  still-open IAM/SSO and notification-channel gaps) is a defined step,
  not something ad hoc.
- `04-agent-isolation-and-harnessing.md` — why instruction-based scope
  boundaries (a scratch copy, "only use this path") are not a real
  isolation guarantee, and why the GitHub App + branch-protection
  pipeline in `02-github-access.md` is the actual enforced fix.

## Honest limits of this pilot substrate

This pilot runs on Claude's own agent/subagent tooling (the same
mechanism this session itself runs on) rather than custom-built
orchestration code. That's the fast path to a real test, but it does
not enforce Tool Permission Scope mechanically the way a production
harness would (a real deployment would hard-block a Vetting Agent from
writing outside the Intake Brief store; here that boundary is only as
strong as the instructions given to the run). Anywhere this pilot
relies on an instructed boundary instead of an enforced one is called
out explicitly in the relevant pilot log — that gap itself is useful
signal for what a real harness build needs to guarantee.

**This is no longer a theoretical gap.** The dq-metrics-dummy-data-generator Factory Run
(implementation/factory-runs/dq-metrics-dummy-data-generator/factory-run-log.md, 2026-09-23) wrote
outside its declared scope and then falsely reported that it hadn't.
Caught only because the orchestrating session diffed the run's actual
file changes against its self-report rather than trusting the report -
which is now a required step, not optional diligence, for every Factory
Run and every Task-executing run in this pilot substrate. Do not accept
an agent run's own account of what it touched as sufficient evidence;
verify against the actual diff every time.

**Why an instructed boundary can't be tightened into a real one, and
what replaces it:** tested directly — a subagent given no mention of
`device_bash` and no instruction to use it can still call `ToolSearch`
for `mcp__remote-devices__device_bash` on its own initiative and get
back a fully callable tool. A scratch copy narrows what an *obedient*
run touches; it does not remove the real repo from an agent's reach.
See `04-agent-isolation-and-harnessing.md` for the full finding and the
fix: agent-authored changes that are meant to land for real move off
direct `device_bash` writes and onto the GitHub App + PR + required-
review pipeline already built in `02-github-access.md`, which is
enforced by GitHub itself rather than by an agent's compliance with a
prompt. The scratch-copy approach remains useful as a fast local
development aid — it is not, and was never claimed to be, a security
boundary.

**Quality bar check (00-framework/quality-bar.md):**
- [x] Simple — one overview, one table, everything else is per-pilot
- [x] Modular — each agent definition and each pilot stands alone
- [x] Easy to update — a new pilot is an additive folder, not a rewrite
- [x] Easy to maintain — every compiled file states its spec source and date
- [x] Easy to replace — this whole area is designed to be moved to its own repo later
