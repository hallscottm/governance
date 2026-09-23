# Engagements — Project Document Template

Status: Draft — pending review
Ratified: No
Last updated: 2026-09-23 (workflow_pattern field; Department/Domain note; source_control_and_delivery block added)

Instance of `eng-project-document` (01-definitions.md). Required for
Project and Decommission Engagement Types; optional wrapper for
Maintenance and Governance/Review; not used for Monitoring & Alerting or
the standalone types (02-engagement-types.md).

**Department vs. Domain — not the same field.** `owning_department` is org-chart (`ccdept-*`, cross-cutting/roles-and-departments) — who asked, who's accountable day to day. `applicable_domains` is the technical axis (00-framework/domain-axis-definition.md) — which domains' governance/taxonomy/policy actually applies. A project requested by one Department routinely touches several Domains (a Marketing-requested report touches Data/Metadata and BI/Reporting, not a "Marketing domain" — Marketing isn't a row on that axis). Keep both fields filled independently; don't infer one from the other.

**Source control, CI/CD, and IaC are planned here, not left implicit.** Workflow/Process (07-workflow-process) already owns the vocabulary — Repository, Branching Strategy, Pipeline, Deployment Gate, Infrastructure as Code — this schema's `source_control_and_delivery` block is where a specific Project's choices from that vocabulary get recorded, the same reference-not-restate pattern used everywhere else in this framework.

## Front matter (machine-readable)

```yaml
project_id: <slug>
engagement_type: Project | Maintenance | Governance-Review | Decommission
status: proposed | approved | in-progress | complete | archived
created_by: <Engagement Planning Agent name> + <human requester>
created_date: <date>
last_updated: <date>

owning_department: <ccdept-* anchor>
owning_team_lead: <ccrole-owning-team-lead instance>
requester: <ccrole-requester instance>
approver: <ccrole-approver instance>   # never the same as requester — CCAR-2

risk_tier: Low | Moderate | High        # computed, not asserted
cost_center_tag: <infra-cost-center-tag>
target_timeline: <start> to <target end, if applicable>

applicable_domains: [list of the 8 domains this touches]
applicable_policies: [list of POL/AR anchors that apply]
applicable_taxonomy_terms: [list of anchors]
applicable_conventions: [list of anchors]
sandbox_required: true | false          # ties to cc-sandbox

storage_location: <where files/data will live, if not source-controlled>

source_control_and_delivery:
  # required once applicable_domains includes System Architecture,
  # Infrastructure, Networking, or Data Platform (a deliverable that is
  # code, config, or infrastructure); optional/partial otherwise (e.g. a
  # pure report Engagement may only fill repository, or omit this block).
  # Planning-time record only - once a Service/Application entity is
  # registered, its own Repository Reference field
  # (03-system-architecture/04-metadata-standards.md) is the ongoing
  # source of truth; not duplicated here after creation.
  repository:
    name: <follows wf-repository's Repository Naming Convention, 07-workflow-process/05-conventions.md>
    location: <the org's Git host + org/repo path>
    scaffolding_template: <wf-repository-scaffolding reference used>
    branching_strategy: <wf-branching-strategy reference>
  ci_cd:
    pipeline: <wf-pipeline reference>
    deployment_gates: [wf-deployment-gate references that apply, per applicable_domains]
    rollback_plan: <wf-rollback reference - required once risk_tier is Moderate or High>
  iac:
    used: true | false
    state_file_location: <wf-state-file reference, if used>
    plan_review_required: true | false   # ties to wf-iac-plan / wf-iac-apply

participants:
  - name: <human name, or agent role_name>
    kind: human | agent
    role: <their function on this engagement>
    raci: Responsible | Accountable | Consulted | Informed
    # exactly one Accountable; see eng-accountability-boundary (07)

tools_and_mcp_servers: [list]            # includes Channels — see eng-channel, 06
tool_configurations: [list of standardized config profiles used]

workflow_pattern: single-agent | sequential | parallel | orchestrator-workers | evaluator-optimizer
  # shape of how this Project's Agents/Tasks coordinate, not per-task detail
  # (that's each Task's own dependencies list, below). Named patterns per
  # Anthropic's "Building Effective AI Agents" (engagements/00-standards-
  # alignment.md). single-agent for the common one-Agent case; the rest
  # only matter once agents_required has more than one entry.

agents_required:
  - role_name: <string>
    templated_agent_used: <Agent Library reference, or "dynamically composed">
    capability_scope: <ref>
    tool_permission_scope: <ref>
    prompt_template: <harness-prompt-template reference + delta>
    escalation_path: <ref>
    model_version_pin: <ref>              # set from the Model Catalog, see 09-open-decisions.md #8
    sandbox_tested_flag: true | false

tasks: [list of Task Document IDs]
```

## Body (human-readable narrative)

- **Goal / Objective** — what success looks like, in plain language
- **Scope boundary** — explicitly what's in and out
- **Definition of Done** — the acceptance criteria
- **Stakeholders** — who's affected or consulted, beyond the assigned Participants above
- **Reasoning** — why this approach, why these Agents/Skills, any alternatives considered
- **Approval log** — who approved what, when (append-only, same discipline as this framework's own `_qa` logs)
- **Collaboration Log** — threaded discussion anchored to specific passages (`eng-collaboration-log`, 06)

**Quality bar check:**
- [x] Simple — one schema, type-driven requiredness, no per-type duplication
- [x] Modular — front matter (machine) and body (human) can each change independently
- [x] Easy to update — new fields are additive; nothing here is generated, so no regeneration dependency
- [x] Easy to maintain — every field either computed (risk_tier) or a reference into an existing registry, nothing free-text that drifts
- [x] Easy to replace — plain YAML + Markdown, no tooling dependency
