# Task Document — dq-dash-t1-define-metrics

## Front matter

```yaml
task_id: dq-dash-t1-define-metrics
parent_project: dq-metrics-dashboard
engagement_type: Project
status: proposed

assigned_agent:
  role_name: "N/A — human-led task, no Agent required"
  capability_scope: n/a
  tool_permission_scope: n/a
  model_version_pin: n/a

participants:
  - name: BI Analyst/Developer or Business Analyst/Report Builder (unnamed)
    kind: human
    role: Confirm source system(s) and define the weekly metric set
    raci: Responsible
  - name: J. Rivera
    kind: human
    role: Confirms intent, audience, and priority among candidate metrics
    raci: Consulted

skills_invoked: []
knowledge_references:
  - data-quality (05-data-metadata/01-definitions.md#data-quality)
  - data-quality-rule (05-data-metadata/01-definitions.md#data-quality-rule)
  - data-catalog (05-data-metadata/01-definitions.md#data-catalog)

tools_and_mcp_servers: OPEN — depends on wherever the existing DQ
  checks write their output; not named in the Intake Brief.

risk_tier: Low
approval_required: false
approved_by:

dependencies: []

result:
  output_location:
  completed_date:
  outcome_summary:
```

## Body

### Description
Resolve the two data-facing open_gaps the Intake Brief could not close:
(1) which source system(s)/tool(s) actually produce the team's existing
data-quality checks, and (2) the intended audience/Distribution Scope
for the dashboard (just the BI team, or wider). Produce a confirmed list
of the specific weekly metrics to surface (pulled from what already
exists — no new Data Quality Rule authored here) and a refresh cadence
assumption to hand to Task 2.

### Inputs / Outputs
**Inputs:** Intake Brief (`implementation/pilots/dq-metrics-dashboard/intake-brief.yaml`),
direct conversation with J. Rivera, whatever data catalog/metadata
registry entries exist for the team's current DQ checks.
**Outputs:** a confirmed metric list, confirmed source system reference,
confirmed (or explicitly still-unconfirmed) Distribution Scope — all of
which Task 2 and the Project Document's open items depend on.

### Reasoning
No Agent or Skill is invoked here deliberately — this is scope
clarification and a conversation with the Requester, not an automatable
capability, so there is no Capability Scope to match against the
Library and no Factory escalation implied by leaving `assigned_agent`
unset. Contrast with dq-dash-t2-build-report, where an actual Agent
capability is needed and none exists yet.
