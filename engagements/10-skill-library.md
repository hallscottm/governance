# Engagements — Skill Library

Status: Draft — pending review
Ratified: No
Last updated: 2026-09-23

Covers `eng-skill` (01-definitions.md). Reviewed with the user in a
standalone design pass before being written here.

## Build-on-Demand Principle

Resolves a question raised earlier and never settled: predict and
pre-build the skills an org might need, or compose fresh each time?
**Neither, wholesale.** A Skill gets built the first time a Task
genuinely needs that exact capability and nothing close enough already
exists in the Library — never in anticipation of a need that hasn't
shown up yet. Once built, it's registered and every subsequent match
reuses it. Grows from real usage, not upfront guessing — the same
instinct behind not enumerating every task a company might need, and
Anthropic's own "start simple, add complexity only when necessary"
guidance (00-standards-alignment.md).

**"Close enough" test:** required Capability Scope and Tool Permission
Scope must match exactly — these are the governance-load-bearing
fields; an inexact match on either is a different Skill, not a reuse.

## Skill Library entry

```yaml
skill_id: skill-lib/<slug>-v<N>
name: <human name>
description: <what it does>
version: N
status: draft | sandbox-tested | approved | deprecated
owning_domain: <domain this skill's knowledge draws from, if any>
requires_capability_scope: <ref>
requires_tool_permission_scope: <ref>
typical_risk_tier: Low | Moderate | High
eval_suite: <harness-eval-suite reference>
provenance: hand-authored | factory-built <factory run id>
created_date: <date>
last_updated: <date>
used_by: [Task IDs that reference this Skill — reuse visibility, not a permission list]
```

A new version (`-v2`, etc.) is minted rather than editing a Skill in
place once it's `approved` — same reasoning as Harness's Model Version
Pin requiring a fresh Eval Suite Run on change, not a silent in-place
update.

## Registered Skills

First entry, registered 2026-09-23 via the first completed Factory Run
(implementation/factory-runs/csv-to-markdown-summary/). Implementation lives at
implementation/skills/csv-to-markdown-summary-v1/ (a reference-runtime
detail - not duplicated here, this row is the governance record).

```yaml
skill_id: skill-lib/csv-to-markdown-summary-v1
name: CSV to Markdown Summary
description: >
  Reads a CSV file and produces a markdown file containing (a) a markdown
  table rendering of the CSV's rows and columns, and (b) one summary line
  stating the row count and column count. Runs the bundled script against
  the input CSV to produce the output file; does not fabricate table
  contents from memory.
version: 1
status: approved
owning_domain: null
requires_capability_scope: >
  Read one local CSV file supplied as input; write one local markdown
  file as output. No other file, network, or system access.
requires_tool_permission_scope: >
  Read: the single input CSV path passed to it. Write: the single output
  markdown path passed to it. Execute: the bundled script only
  (standard library only, no external packages, no network access).
typical_risk_tier: Low
eval_suite: implementation/factory-runs/csv-to-markdown-summary/sandbox/eval-result.md
  (5/5 cases passed, first attempt - normal input, ragged rows, embedded
  pipe character, empty CSV, missing-file error path, plus a static
  Tool Permission Scope check)
provenance: factory-built factory-run-csv-to-markdown-summary
created_date: 2026-09-23
last_updated: 2026-09-23
used_by: []
```

## Registered Skills (continued)

Second entry, registered 2026-09-23 via the second completed Factory
Run (implementation/factory-runs/dq-metrics-dummy-data-generator/), after a retry that fixed a
scope-compliance failure on the first attempt (see the pilot log for
the full incident). Implementation lives at
implementation/skills/dq-metrics-dummy-data-generator-v1/ (a real
SKILL.md package, not just a script + registry record).

```yaml
skill_id: skill-lib/dq-metrics-dummy-data-generator-v1
name: Data Quality Metrics Dummy Data Generator
description: >
  Generates a synthetic "weekly data-quality metrics" CSV shaped like a
  real BI/data-quality export: one row per (check_name, table_name,
  week_ending), with pass_count, fail_count, pass_rate. Parameterized by
  weeks, pairs, and a random seed - same seed always produces
  byte-identical output. Pass rates modeled to look like real DQ
  metrics (mostly high, occasional bad weeks) rather than uniform
  random. Synthetic test data only - not a substitute for a real,
  connected data-quality-checks source in a live report.
version: 1
status: approved
owning_domain: null
requires_capability_scope: >
  No read access to any input file or live data source. Write one
  local CSV file as output, at the single output path supplied as an
  argument. No network access.
requires_tool_permission_scope: >
  Read: none (all inputs are CLI parameters). Write: the single output
  CSV path passed to it. Execute: the bundled script only (standard
  library only - argparse, csv, datetime, random - no external
  packages, no network access).
typical_risk_tier: Low
eval_suite: implementation/factory-runs/dq-metrics-dummy-data-generator/sandbox/eval-result.md
  (5/5 cases passed on independent re-verification after an isolated
  retry - reproducibility, seed sensitivity, 3 bad-input cases)
provenance: factory-built factory-run-dq-dummy-data-generator (2 attempts - first attempt failed scope compliance, reverted; second attempt isolated and independently verified)
created_date: 2026-09-23
last_updated: 2026-09-23
used_by: []
```

Third entry, registered 2026-09-23 via factory-run-build-bi-report-skill
(implementation/factory-runs/build-bi-report/), drafted by a subagent
scoped strictly to its own sandbox folder and independently verified
(git status confirmed it touched nothing outside that scope; the Eval
Suite was re-run from scratch by the orchestrating session rather than
trusting the drafting run's self-report). Closes the honest process
deviation recorded in implementation/pilots/dq-metrics-dashboard's
pilot-log.md ("Run 2") - a real Factory Run for this capability now
exists, so the by-hand dashboard build that pilot used is no longer
the accepted path going forward. Implementation lives at
implementation/skills/build-bi-report-v1/.

```yaml
skill_id: skill-lib/build-bi-report-v1
name: Build BI Report
description: >
  Reads a weekly data-quality-metrics CSV (one row per check_name,
  table_name, week_ending, with pass_count, fail_count, pass_rate -
  the shape produced by dq-metrics-dummy-data-generator-v1 or an
  equivalent real export) and writes a self-contained, dependency-free
  HTML dashboard: a line chart of weekly pass rate per check/table
  pair, a latest-week status table, and summary stat tiles. Does not
  author, run, or evaluate a new Data Quality Rule - visualizes
  already-existing metrics only. Internal-distribution, non-Confidential
  data only - does not implement Certified-status badging (BIPOL-1/2)
  or Row-Level Security (BIPOL-3); rejects any --distribution-scope
  wider than Internal/Departmental.
version: 1
status: approved
owning_domain: null
requires_capability_scope: >
  Read one local CSV file supplied as input (weekly DQ-metrics shape).
  Write one local HTML file as output. No other file, network, or
  system access. Never authors a new Data Quality Rule or widens
  Distribution Scope/Sensitivity beyond what it's given.
requires_tool_permission_scope: >
  Read: the single input CSV path passed to it. Write: the single
  output HTML path passed to it. Execute: the bundled script only
  (standard library only - argparse, csv, json, datetime, html,
  pathlib, sys - no external packages, no network access).
typical_risk_tier: Low
eval_suite: implementation/factory-runs/build-bi-report/sandbox/eval-result.md
  (8/8 cases passed, re-run independently of the drafting run's own
  self-report - required-flag enforcement, Distribution Scope
  rejection, malformed-CSV error path, bad-week/single-week rendering)
provenance: factory-built factory-run-build-bi-report-skill (subagent scoped to its own sandbox path, independently scope-verified)
created_date: 2026-09-23
last_updated: 2026-09-23
approved_by: user (hallscottm@gmail.com), direct chat confirmation, 2026-09-23
used_by: [dq-metrics-dashboard]
```

## Lookup, reuse, escalation

1. The Engagement Planning Agent needs a Skill for a Task (07's Skill
   Library Lookup step).
2. **Found** — reference it directly. The common path (see
   08-worked-example.md).
3. **Not found** — the Planning Agent's existing Escalation Path
   already covers this: route to the Factory (build something new) or
   a human Approver (if it's a governance gap, not a capability gap).
4. **Built** — once the Factory (next spec) produces, Sandbox-tests,
   and Eval-passes a new Skill, it's registered here with
   `status: approved` and becomes reusable. The Library only grows
   through this gate, never by direct edit.

## Deprecation

Never a hard delete — append-only, same discipline as `_qa` logs.
Three named triggers: a provider/dependency-forced retirement; a
Behavioral Drift or repeated Eval Suite failure (parallels HPOL-4's
automatic tightening — auto-flags for review, doesn't auto-remove); or
superseded-and-unused (`used_by` empty, safe low-urgency cleanup).
`status: deprecated` stops new Lookups from picking it; Tasks that
already reference it keep their historical record.

**Quality bar check (00-framework/quality-bar.md):**
- [x] Simple — one registry, one build trigger, one deprecation rule set
- [x] Modular — a Skill's Capability/Tool Permission Scope is independently replaceable per version
- [x] Easy to update — new Skills are additive; nothing here regenerates
- [x] Easy to maintain — reuses Harness's Eval Suite and Model Version Pin discipline rather than inventing new review machinery
- [x] Easy to replace — plain YAML registry, no tooling dependency
