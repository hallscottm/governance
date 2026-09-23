# Task Document — dq-dash-t2-build-report

## Front matter

```yaml
task_id: dq-dash-t2-build-report
parent_project: dq-metrics-dashboard
engagement_type: Project
status: proposed

assigned_agent:
  role_name: BI Report Builder Agent
  capability_scope: "Read: dp-semantic-layer and/or the existing DQ
    check output confirmed by dq-dash-t1-define-metrics. Write:
    bi-report-data-model, bi-dashboard — Draft Certification Status
    only until BIAR-1 review."
  tool_permission_scope: OPEN — finalized only once
    factory-run-bi-report-builder-agent completes Sandbox + Approval.
  model_version_pin: OPEN — Model Catalog has zero populated entries;
    human decision required.

participants:
  - name: BI Report Builder Agent
    kind: agent
    role: Build the Report Data Model and Dashboard
    raci: Responsible
  - name: BI Analyst/Developer (unnamed)
    kind: human
    role: Review, and certify per BIAR-1 if Distribution Scope
      warrants it
    raci: Consulted
  - name: J. Rivera
    kind: human
    role: Confirms the built dashboard matches intent; content/business
      accuracy sign-off
    raci: Accountable

skills_invoked: [FACTORY]
  # Real gap, not a placeholder: no skill-lib/build-bi-report entry
  # exists yet (confirmed by direct read of engagements/10-skill-library.md).
  # See factory-run-build-bi-report-skill.md, which this Task depends on.

knowledge_references:
  - dp-semantic-layer (04-data-platform/01-definitions.md#dp-semantic-layer)
  - bi-report-data-model, bi-dashboard, bi-certified, bi-row-level-security,
    bi-data-extract, bi-refresh-schedule (06-bi-reporting/01-definitions.md)
  - BIPOL-1, BIPOL-4 (always applicable); BIPOL-2, BIPOL-3 (only if
    Certification/Sensitivity apply — depends on dq-dash-t1's findings)
  - BIAR-1, BIAR-2 (06-bi-reporting/07-access-rules.md)
  - 06-bi-reporting/05-conventions.md (naming)

tools_and_mcp_servers: OPEN — BI platform/tool not yet named (Intake
  Brief open_gap); data source connection likewise unnamed pending
  dq-dash-t1-define-metrics.

risk_tier: Moderate   # inherits the Project's computed tier; see
  Project Document Reasoning for the Environment-factor ambiguity this
  depends on resolving before Approval.
approval_required: true
  # CCAR-1: an Agent may draft/request but never self-approve. Also:
  # BIAR-1 requires independent BI Analyst/Developer review before any
  # Certified-status transition, and this is a Moderate-tier Task
  # producing a real Production-facing artifact.
approved_by:

dependencies:
  - dq-dash-t1-define-metrics
  - factory-run-bi-report-builder-agent
  - factory-run-build-bi-report-skill

result:
  output_location:
  completed_date:
  outcome_summary:
```

## Body

### Description
Build the actual Report Data Model and Dashboard from the metrics
confirmed in dq-dash-t1-define-metrics, using the Agent Template and
Skill produced by the two Factory Run Tasks. Apply BIPOL-4 (declared
Refresh Schedule) unconditionally; apply BIPOL-1/BIPOL-2 (Certified
status) only if Distribution Scope ends up wider than Internal;
apply BIPOL-3/BIAR-2 (Row-Level Security) only if the underlying data's
Sensitivity Level is Confidential or above.

### Inputs / Outputs
**Inputs:** confirmed metric list + source (Task 1); approved BI Report
Builder Agent Template (Factory Run 1); approved build-bi-report Skill
(Factory Run 2).
**Outputs:** a Dashboard entity (and its backing Report Data Model),
`status: proposed` until a human Approver signs off, matching this
Task's own `status` field, not asserted as already built.

### Reasoning
This is the one Task in this Project that actually needs an automated
Capability — everything upstream (scoping, Factory drafting) is either
human-led or explicitly gated behind Sandbox/Eval/Approval before this
Task can even start. `skills_invoked: [FACTORY]` is used exactly as
engagements/04-task-document-template.md specifies: "to explicitly flag
a real gap, never as a placeholder" — this gap was directly confirmed,
not assumed.
