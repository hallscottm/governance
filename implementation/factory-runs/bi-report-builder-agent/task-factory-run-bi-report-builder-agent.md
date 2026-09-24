# Task Document — factory-run-bi-report-builder-agent

## Front matter

```yaml
task_id: factory-run-bi-report-builder-agent
parent_project: dq-metrics-dashboard
engagement_type: Request / Ad Hoc
status: complete

assigned_agent:
  role_name: Factory Agent
  capability_scope: "Draft a candidate Agent Template (BI Report
    Builder Agent) in status: draft only — per engagements/13-factory.md.
    Excludes approving its own work, writing to Production, or editing
    an existing approved Library entry in place."
  tool_permission_scope: "Read: entire Anchor layer, the existing
    Agent Library (re-check the 'close enough' test wasn't missed).
    Write: Agent Library store, draft status only."
  model_version_pin: OPEN — Model Catalog (engagements/12-model-catalog.md)
    has zero populated entries; human decision required, not guessed.

participants:
  - name: Factory Agent
    kind: agent
    role: Draft the candidate Agent Template
    raci: Responsible
  - name: Approver (unnamed — same open item as the Project Document)
    kind: human
    role: Sign off before status flips draft -> approved
    raci: Accountable

skills_invoked: []
knowledge_references:
  - engagements/11-agent-library.md
  - engagements/09-open-decisions.md #10 ("close enough" test)
  - engagements/13-factory.md
  - 06-bi-reporting/01-definitions.md through 07-access-rules.md
    (what the candidate Agent needs to respect: BIPOL-1/2/3/4, BIAR-1/2)
  - 04-data-platform/01-definitions.md#dp-semantic-layer

tools_and_mcp_servers:
  - cc-sandbox (cross-cutting/sandbox-activation.md)
  - Agent Library store (write, draft status only)

risk_tier: Low   # per 13-factory.md: "Own Risk Tier: Low (drafting only, no Production execution)"
approval_required: true
approved_by: user (hallscottm@gmail.com), direct chat confirmation, 2026-09-23

attempt_count: 0   # Factory-Run-specific field, 13-factory.md — increments on Sandbox/Eval failure

dependencies: []

result:
  output_location: implementation/agents/bi-report-builder-agent.md
    (compiled definition); implementation/factory-runs/bi-report-builder-agent/sandbox/agent-entry.yaml
    (draft Library entry, agent-lib/bi-report-builder-agent-v1)
  completed_date: "2026-09-23"
  outcome_summary: >
    Drafted and Eval-checked (7/7 cases, see sandbox/eval-result.md),
    then approved by real human decision (hallscottm@gmail.com, direct
    chat confirmation, 2026-09-23 - CCAR-1: this Agent never
    self-approved its own draft) and registered as
    agent-lib/bi-report-builder-agent-v1 in
    engagements/11-agent-library.md. Closes the honest process
    deviation recorded in implementation/pilots/dq-metrics-dashboard's
    pilot-log.md ("Run 2").
```

## Body

### Description
No entry in engagements/11-agent-library.md matches the Capability
Scope + Tool Permission Scope this Project needs (read existing DQ
check output / dp-semantic-layer; write bi-report-data-model,
bi-dashboard at Draft status). The Library file was read directly and
contains only its schema and process — zero registered rows. The
`agent-lib/bi-analyst-developer-v1` id used in
engagements/08-worked-example.md is illustrative narrative only, not a
real Library entry. This Task is the Factory escalation that gap
requires: draft the "BI Report Builder Agent" candidate, Sandbox-test
it (HPOL-1), run an Eval Suite, and get a human Approver's sign-off
before it is trusted with any real work.

### Inputs / Outputs
**Inputs:** this Project's required Capability Scope/Tool Permission
Scope (Project Document, `agents_required`); the Anchor layer content
those scopes must respect (06-bi-reporting policies/access-rules).
**Outputs:** a new `agent-lib/bi-report-builder-agent-v1` entry (or
whatever id the Factory assigns), `status: draft` until Sandbox+Eval+
Approval complete, then `approved`.

### Reasoning
Per this Planning Agent's explicit scope boundary, inventing this
Agent Template directly rather than routing it through the Factory
would be out of scope. This Task exists instead of that shortcut — it
is the mechanism engagements/13-factory.md itself prescribes for
exactly this situation (an ordinary Task Document, `engagement_type:
Request / Ad Hoc`, naming the Factory Agent). dq-dash-t2-build-report
names this Task (and factory-run-build-bi-report-skill) as prerequisites
in its own Description/Reasoning text - **correction, 2026-09-23:** its
`dependencies:` front-matter field itself only ever listed
`dq-dash-t1-define-metrics`, not these two Factory Run ids. That was a
real inconsistency between the prose and the machine-readable field,
caught while finally running this Task for real; dq-dash-t2 already
shipped (`status: complete`) with an honestly-recorded process
deviation before this was caught, so its historical `dependencies`
field is left as-authored rather than rewritten after the fact -
recorded here instead, plus in dq-dash-t2's own file, so the
inconsistency isn't silently dropped.
