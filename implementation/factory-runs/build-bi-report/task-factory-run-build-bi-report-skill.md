# Task Document — factory-run-build-bi-report-skill

## Front matter

```yaml
task_id: factory-run-build-bi-report-skill
parent_project: dq-metrics-dashboard
engagement_type: Request / Ad Hoc
status: complete

assigned_agent:
  role_name: Factory Agent
  capability_scope: "Draft a candidate Skill ('build a BI report/
    dashboard from an existing, already-produced source — no new Data
    Quality Rule authored') in status: draft only — per
    engagements/13-factory.md."
  tool_permission_scope: "Read: entire Anchor layer, the existing
    Skill Library (re-check the 'close enough' test wasn't missed).
    Write: Skill Library store, draft status only."
  model_version_pin: OPEN — Model Catalog has zero populated entries;
    human decision required, not guessed.

participants:
  - name: Factory Agent
    kind: agent
    role: Draft the candidate Skill
    raci: Responsible
  - name: Approver (unnamed — same open item as the Project Document)
    kind: human
    role: Sign off before status flips draft -> approved
    raci: Accountable

skills_invoked: []
knowledge_references:
  - engagements/10-skill-library.md
  - engagements/09-open-decisions.md #10 ("close enough" test)
  - engagements/13-factory.md
  - 06-bi-reporting/06-policies.md (BIPOL-1, BIPOL-2, BIPOL-3, BIPOL-4)
  - 06-bi-reporting/07-access-rules.md (BIAR-1, BIAR-2)
  - 06-bi-reporting/05-conventions.md (Report/Dashboard naming)

tools_and_mcp_servers:
  - cc-sandbox (cross-cutting/sandbox-activation.md)
  - Skill Library store (write, draft status only)

risk_tier: Low
approval_required: true
approved_by: user (hallscottm@gmail.com), direct chat confirmation, 2026-09-23

attempt_count: 0

dependencies: []

result:
  output_location: implementation/factory-runs/build-bi-report/sandbox/build_bi_report.py,
    SKILL.md, eval/ (candidate script + package); skill-entry.yaml
    (draft Library entry, skill-lib/build-bi-report-v1)
  completed_date: "2026-09-23"
  outcome_summary: >
    Drafted by a subagent acting as Factory Agent, scoped to write only
    inside this Task's own sandbox path - independently verified via
    git status that it stayed in scope (see sandbox/eval-result.md).
    Eval Suite re-run independently by the orchestrating session
    (8/8 cases passed) rather than trusting the drafting run's own
    self-report, per this pilot's established finding. Approved by
    real human decision (hallscottm@gmail.com, direct chat
    confirmation, 2026-09-23) and registered as
    skill-lib/build-bi-report-v1 in engagements/10-skill-library.md;
    implementation lives at implementation/skills/build-bi-report-v1/.
    Closes the honest process deviation recorded in
    implementation/pilots/dq-metrics-dashboard's pilot-log.md ("Run 2").
```

## Body

### Description
No entry in engagements/10-skill-library.md matches either — same
direct-read result as the Agent Template gap: the file is schema/
process only, zero registered Skills. `skill-lib/build-bi-report-v3`
appears only in engagements/08-worked-example.md and
engagements/13-factory.md's own worked example, both narrative
illustrations of how the mechanism would work, not an actual entry.
This Task drafts the real Skill: assemble a Report/Dashboard entity
from an already-existing, already-produced data source (never
authoring a new Data Quality Rule), applying BIPOL-4's refresh-schedule
requirement always, and BIPOL-1/BIPOL-2/BIAR-1 only if/when
Certification is actually pursued.

### Inputs / Outputs
**Inputs:** BIPOL-1/2/3/4 and BIAR-1/2 (what the Skill's output must
satisfy); the confirmed metric set from dq-dash-t1-define-metrics.
**Outputs:** a new `skill-lib/build-bi-report-v1` entry (or whatever id
the Factory assigns), `status: draft` until Sandbox+Eval+Approval.

### Reasoning
Same reasoning as factory-run-bi-report-builder-agent.md — this is the
Factory escalation this Planning Agent's scope boundary requires
instead of inventing a Skill entry directly. Drafted as a separate
Factory Run Task from the Agent Template one (not merged into it)
because each Factory Run's `result.output_location` is a single
`skill-lib/...` or `agent-lib/...` id per engagements/13-factory.md's
Register stage — they are two distinct Library artifacts even though
one Project need triggered both gaps.
