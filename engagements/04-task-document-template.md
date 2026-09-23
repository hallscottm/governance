# Engagements — Task Document Template

Status: Draft — pending review
Ratified: No
Last updated: 2026-09-23

Instance of `eng-task-document` (01-definitions.md). One Task, one
assigned Agent, one Capability Scope.

## Front matter

```yaml
task_id: <slug>
parent_project: <project_id, or null if standalone — Ad Hoc/Incident/Maintenance often are>
engagement_type: <inherited from parent, or set directly if standalone>
status: proposed | approved | in-progress | complete | blocked

assigned_agent:
  role_name: <string>
  capability_scope: <ref, narrowed from Project-level if applicable>
  tool_permission_scope: <ref>
  model_version_pin: <ref>

participants:
  - name: <human name, or agent role_name>
    kind: human | agent
    role: <their function on this task>
    raci: Responsible | Accountable | Consulted | Informed

skills_invoked: [registered Skill anchors, or "FACTORY" if none exists yet]
knowledge_references: [specific governance/taxonomy/ontology/convention anchors this task touches — narrower than the Project's list]
tools_and_mcp_servers: [list, task-specific — includes Channels, see eng-channel]

risk_tier: Low | Moderate | High
approval_required: true | false
approved_by: <ccrole-approver instance, if required>

dependencies: [other task_ids that must complete first]

result:
  output_location: <where the result lives>
  completed_date: <date>
  outcome_summary: <one line>
```

## Body

- **Description** — the specific action in plain language
- **Inputs / Outputs** — what this task consumes and produces
- **Reasoning** — why this Skill/Agent/Tool combination, especially if it went through the Factory rather than an existing registered Skill

A Task never starts work without `assigned_agent`, `skills_invoked`, and
(if `approval_required: true`) `approved_by` all filled — the concrete
mechanism behind "everything explicit before Agents start."

**Quality bar check:** same five checks as 03-project-document-template.md
— identical structure applied one level down; see there.
