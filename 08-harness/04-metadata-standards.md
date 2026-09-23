# Harness Domain — Metadata Standards

Status: Draft — pending review
Ratified: No
Last updated: 2026-09-23
Provenance: see _qa/04-metadata-standards.qa.md
Built on: 01-definitions.md, 02-taxonomies.md, 03-ontologies.md

Same shape as every prior domain's Metadata Standards (shared field
registry + entity-type applicability matrix).

## Referenced Fields (owned elsewhere)

- **Resource ID** — [01-infrastructure/01-definitions.md#infra-resource-id](../01-infrastructure/01-definitions.md#infra-resource-id) — applies unchanged
- **Cost Center Tag** — [01-infrastructure/01-definitions.md#infra-cost-center-tag](../01-infrastructure/01-definitions.md#infra-cost-center-tag) — applies unchanged
- **Environment (lifecycle)** — [01-infrastructure/01-definitions.md#infra-environment-lifecycle](../01-infrastructure/01-definitions.md#infra-environment-lifecycle) — applies unchanged; an Agent's own Sandbox usage (`cc-sandbox`) is recorded via the Sandbox Tested Flag below, not by setting Environment to Sandbox on the Agent's permanent record.
- **Owning Team / Owning Team Lead** — [cross-cutting/roles-and-departments/01-definitions.md#ccrole-owning-team-lead](../cross-cutting/roles-and-departments/01-definitions.md#ccrole-owning-team-lead) — typically AI/ML Platform (`ccdept-ai-ml-platform`, this domain's default owning department) for a general-purpose Agent, but any department may own one it operates.

## Field Registry (owned by this domain)

| Field | Definition | Source Term | Required/Optional (default) |
|---|---|---|---|
| **Agent Name** | The canonical, unique name identifying this Agent. | `harness-agent` | Required for Agent entity type |
| **Agent Type** | Assistant, Autonomous, or Multi-Agent. | `harness-agent-type` | Required for Agent entity type |
| **Model Version Pin Reference** | The specific, pinned model version this Agent runs on. | `harness-model-version-pin` | Required for Agent entity type |
| **Capability Scope Reference** | Link to this Agent's defined Capability Scope. | `harness-capability-scope` | Required for Agent entity type |
| **Tool Permission Scope Reference** | Link to this Agent's defined Tool Permission Scope. | `harness-tool-permission-scope` | Required for Agent entity type |
| **Escalation Path Reference** | Link to this Agent's defined Escalation Path. | `harness-escalation-path` | Required for Autonomous, Multi-Agent types; Recommended for Assistant type |
| **Sandbox Tested Flag** | Whether this Agent's current Capability Scope/Tool Permission Scope combination has been exercised in a Sandbox (`cc-sandbox`) before any Production-scoped grant. | (cross-domain — `cc-sandbox`) | Required for Agent entity type where Environment = Production |
| **Latest Eval Suite Run Reference** | Link to the most recent Eval Suite Run's results for this Agent's current Model Version Pin. | `harness-eval-suite` | Required for Agent entity type |
| **Trace Reference** | Link to the Agent Trace/Transcript for one Agent Run. | `harness-trace` | Required for Agent Run entity type |

## Entity Types & Field Applicability

| Entity Type | Required Fields | Optional/Recommended Fields |
|---|---|---|
| **Agent** | Resource ID, Agent Name, Agent Type, Model Version Pin Reference, Capability Scope Reference, Tool Permission Scope Reference, Latest Eval Suite Run Reference, Sandbox Tested Flag (if Production), Owning Team, Environment, Cost Center Tag | Escalation Path Reference (recommended for Assistant) |
| **Agent Run** | Resource ID, Trace Reference, Environment | — |

---

**Open items:**
- **Sandbox Tested Flag** is a boolean here rather than a link to a
  specific Sandbox test record — a fuller audit trail (which Sandbox
  run, when, by whom) is deferred to this domain's own Procedures/Tooling
  columns rather than expanded into a second field here, same
  "field just requires a value be recorded" posture Workflow/Process took
  with Incident Severity's scale.
- Enforcement (mandatory-blocking vs. recommended) is deferred to
  Policies (column 6), next.

**Quality bar check (00-framework/quality-bar.md):**
- [x] Simple — one field registry (plus referenced fields), one matrix
- [x] Modular — a field's definition changes once, applies everywhere referenced
- [x] Easy to update — add an entity type as one matrix row
- [x] Easy to maintain — fields reference Definitions terms where one exists
- [x] Easy to replace — tool-agnostic, ISO/IEC 11179-grounded, same standard as every prior domain
