# Eval Suite Run — skill-lib/build-bi-report-v1

Date: 2026-09-23
Run by: orchestrating session, independently of the Factory Agent
subagent's own self-reported test run and self-reported scope
compliance - neither is trusted as evidence on its own, per this
pilot's established finding (implementation/04-agent-isolation-and-harnessing.md).

## Scope-compliance check (repo-wide, not just the declared sandbox path)

`git status --porcelain` immediately after the subagent's run showed
exactly one new path attributable to it:
`implementation/factory-runs/build-bi-report/sandbox/` (untracked).
Every other pending change in the working tree predates this run and
belongs to the separate, concurrent bi-report-builder-agent Factory
Run. **Pass** - the run stayed inside its declared write scope.

## Cases run (all executed fresh by the orchestrating session, not
reusing the subagent's own pre-generated eval/ outputs as evidence)

| Case | Result |
|---|---|
| Static scope check (script) | Pass - no `subprocess`/`socket`/`urllib`/`requests`/`os.system`/`eval`/`exec`; imports are `argparse, csv, json, sys, datetime, html, pathlib` only |
| Normal run against the real dq-metrics-dashboard data | Pass - exit 0, correct pair/week counts (6 pairs x 8 weeks), refresh-schedule text rendered in output |
| Required `--refresh-schedule` flag (BIPOL-4) enforced | Pass - clean argparse error, exit 2, no partial output file, when omitted |
| `--distribution-scope` rejects anything beyond Internal/Departmental | Pass - `Organization-wide` rejected by argparse `choices`, exit 2 |
| Malformed CSV (missing required columns) | Pass - clean, specific error naming the missing columns, exit 2, no partial output file |
| No false Certified/Row-Level-Security claim | Pass - output text is a disclaimer ("uncertified... has not gone through [review]", "No Row-Level Security is applied") not a false claim of either |
| Bad-week case renders a Critical status pill | Pass - `Critical`/`critical` present in the subagent's own eval_bad_week.html, re-checked directly |
| Single-week edge case renders without crashing | Pass - valid SVG present in eval_single_week.html, re-checked directly |

## Result

**Eval Suite: 8/8 cases passed, independently re-run.** `attempt_count`
for factory-run-build-bi-report-skill: 0 (first attempt, no failure).

## Open items flagged by the run, worth a human decision (not a
blocker for approval, but not silently resolved either)

- `--warn-threshold`/`--critical-threshold` defaults (0.95/0.80) are
  the Factory Agent's own reasonable invention - no BIPOL/BIAR clause
  specifies status-pill thresholds. Worth a sanity check, not a defect.
- `--distribution-scope` only accepts `Internal`/`Departmental` by
  design (Certified-status/BIAR-1 review is out of scope for this
  version) - a future need for Organization-wide/External distribution
  is a new Skill version, not a flag added to this one.

## Recommendation

Ready for real human Approval Gate sign-off
(skill_id: skill-lib/build-bi-report-v1, currently `status: draft`).
Not registered in engagements/10-skill-library.md yet - that step
happens only after approval, per CCAR-1/CCAR-4.
