# Workflow/Process Domain — Metadata Standards

Status: Draft — pending review
Ratified: No
Last updated: 2026-09-22
Provenance: see _qa/04-metadata-standards.qa.md
Built on: 01-definitions.md, 02-taxonomies.md, 03-ontologies.md

Same shape as every prior domain's Metadata Standards (shared field
registry + entity-type applicability matrix).

## Referenced Fields (owned elsewhere)

- **Resource ID** — [01-infrastructure/01-definitions.md#infra-resource-id](../01-infrastructure/01-definitions.md#infra-resource-id) — applies unchanged
- **Cost Center Tag** — [01-infrastructure/01-definitions.md#infra-cost-center-tag](../01-infrastructure/01-definitions.md#infra-cost-center-tag) — applies unchanged
- **Environment (lifecycle)** — [01-infrastructure/01-definitions.md#infra-environment-lifecycle](../01-infrastructure/01-definitions.md#infra-environment-lifecycle) — applies unchanged
- **Owning Team / Owning Team Lead** — [03-system-architecture/04-metadata-standards.md](../03-system-architecture/04-metadata-standards.md), [cross-cutting/roles-and-departments/01-definitions.md#ccrole-owning-team-lead](../cross-cutting/roles-and-departments/01-definitions.md#ccrole-owning-team-lead) — a Repository/Pipeline inherits its Service's Owning Team rather than being scored independently
- **Service Tier / Criticality** — [03-system-architecture/04-metadata-standards.md](../03-system-architecture/04-metadata-standards.md) — informs Incident Severity's default, same inheritance pattern Data Platform used for its own Service Tier factor

## Field Registry (owned by this domain)

| Field | Definition | Source Term | Required/Optional (default) |
|---|---|---|---|
| **Default Branch Name** | The Branch new work targets by default and Branch Protection Rules apply to most strictly. | `wf-repository`, `wf-branch-protection-rule` | Required for Repository entity type |
| **Branching Strategy Reference** | Which Branching Strategy this Repository follows. | `wf-branching-strategy` | Required for Repository entity type |
| **Pipeline Definition Reference** | Link to the Pipeline's configuration-as-code file within its Repository. | `wf-pipeline` | Required for Pipeline entity type |
| **Trigger Type** | Whether a Pipeline Trigger is schedule-based, event-based (e.g. a Pull Request update), or manual. | `wf-pipeline-trigger` | Required for Pipeline entity type |
| **Deployment Gate Status** | The current pass/fail/pending state of a Pipeline Run's Deployment Gate(s). | `wf-deployment-gate` | Required for Pipeline Run entity type |
| **Incident Severity** | A relative severity classification (e.g. Sev1-Sev4) for an Incident, determining Post-Incident Review requirements (06-policies.md) and response urgency. | `wf-incident` | Required for Incident entity type |
| **Change Request Type** | Standard (pre-approved, low-risk, routine), Normal (requires approval before execution), or Emergency (executed before approval, reviewed after) — ITIL's three change categories. | `wf-change-request` | Required for Change Request entity type |
| **Rollback Target Release Reference** | The prior Release a Rollback reverts to. | `wf-rollback`, `sysarch-release` (cross-domain) | Required for Rollback entity type |

## Entity Types & Field Applicability

| Entity Type | Required Fields | Optional/Recommended Fields |
|---|---|---|
| **Repository** | Resource ID, Default Branch Name, Branching Strategy Reference, Owning Team, Environment, Cost Center Tag | — |
| **Pipeline** | Resource ID, Pipeline Definition Reference, Trigger Type, Owning Team, Environment | — |
| **Pipeline Run** | Resource ID, Deployment Gate Status, Environment | — |
| **Incident** | Resource ID, Incident Severity, Owning Team, Environment | Service Tier/Criticality (inherited) |
| **Change Request** | Resource ID, Change Request Type, Owning Team, Environment | — |
| **Rollback** | Resource ID, Rollback Target Release Reference, Environment | — |

---

**Open items:**
- **Incident Severity**'s specific scale (Sev1-Sev4 vs. a differently
  named scale) is deliberately not fixed here — an organization's
  existing incident-management practice likely already has one; this
  field just requires that a value be recorded, same posture Data/
  Metadata took with its qualitative Data volume/scale Risk Tier factor.
- Enforcement (mandatory-blocking vs. recommended) is deferred to
  Policies (column 6), next.

**Quality bar check (00-framework/quality-bar.md):**
- [x] Simple — one field registry (plus referenced fields), one matrix
- [x] Modular — a field's definition changes once, applies everywhere referenced
- [x] Easy to update — add an entity type as one matrix row
- [x] Easy to maintain — fields reference Definitions terms where one exists
- [x] Easy to replace — tool-agnostic, ISO/IEC 11179-grounded, same standard as every prior domain
