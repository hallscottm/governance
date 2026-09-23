# Business Intelligence / Reporting Domain — Metadata Standards

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
- **Sensitivity Level, Contains PII** — [05-data-metadata/01-definitions.md#data-sensitivity-level](../05-data-metadata/01-definitions.md#data-sensitivity-level) — inherited from the Report Data Model's underlying sources; governs this domain's Risk Tiers (column 9)
- **Data Owner** — [05-data-metadata/01-definitions.md#data-owner](../05-data-metadata/01-definitions.md#data-owner) — the Metric's Data Owner (not the Report's own owner, see Report Owner below), relevant where a Calculated Field claims to represent an owned Metric

## Field Registry (owned by this domain)

| Field | Definition | Source Term | Required/Optional (default) |
|---|---|---|---|
| **Report Owner** | The Business Analyst/Report Builder or BI Analyst/Developer accountable for a Report/Dashboard's content and accuracy. | (cross-cutting/roles-and-departments/01-definitions.md — `ccrole-business-analyst-report-builder`, `ccrole-bi-analyst-developer`) | Required for Report, Dashboard entity types |
| **Certification Status** | Draft or Certified, per `bi-certified`. | `bi-certified` | Required for Report, Dashboard, Report Data Model entity types (default: Draft) |
| **Source-to-Target Mapping Reference** | Link to the Source-to-Target Mapping documenting a Calculated Field's/Report Data Model's provenance. | `bi-source-to-target-mapping` | Required for Certified status; N/A while Draft |
| **Distribution Scope** | Who can view this Report/Dashboard: Internal (owning team only), Departmental, Organization-wide, or External. | (no dedicated Definitions term — an access/visibility classification, not a technical artifact) | Required for Report, Dashboard entity types |
| **Semantic Layer Sourced** | Whether the Report Data Model's Calculated Fields are built on top of Data Platform's Semantic Layer (`dp-semantic-layer`) rather than computed independently. | `bi-report-data-model`, `dp-semantic-layer` (cross-domain) | Required for Report Data Model entity type |
| **Data Extract Flag** | Whether this Report/Dashboard uses a Data Extract (cached snapshot) vs. a live connection to its source. | `bi-data-extract` | Required for Report, Dashboard entity types |
| **Row-Level Security Enabled** | Whether Row-Level Security is configured on this Report Data Model. | `bi-row-level-security` | Required for Report Data Model entity type (default: false) |

## Entity Types & Field Applicability

| Entity Type | Required Fields | Optional/Recommended Fields |
|---|---|---|
| **Report** | Resource ID, Report Owner, Certification Status, Distribution Scope, Data Extract Flag, Environment, Cost Center Tag | Source-to-Target Mapping Reference (Certified only) |
| **Dashboard** | Resource ID, Report Owner, Certification Status, Distribution Scope, Data Extract Flag, Environment, Cost Center Tag | Source-to-Target Mapping Reference (Certified only) |
| **Report Data Model** | Resource ID, Certification Status, Semantic Layer Sourced, Row-Level Security Enabled, Environment | Source-to-Target Mapping Reference (Certified only), Sensitivity Level (inherited from sources) |

---

**Open items:**
- **Distribution Scope** has no owning Definitions term — it's an
  access/visibility classification, not a technical artifact in its own
  right, same boundary System Architecture hit with "Owning Team" (now
  candidate for cross-cutting/roles-and-departments/ ownership, same
  resolution path). Flagged, not resolved here.
- Enforcement (mandatory-blocking vs. recommended, and specifically the
  Certification Status → Distribution Scope interaction — can a Draft
  report have Organization-wide Distribution Scope?) is deferred to
  Policies (column 6), next.

**Quality bar check (00-framework/quality-bar.md):**
- [x] Simple — one field registry (plus referenced fields), one matrix
- [x] Modular — a field's definition changes once, applies everywhere referenced
- [x] Easy to update — add an entity type as one matrix row
- [x] Easy to maintain — fields reference Definitions terms where one exists, flagged explicitly where one doesn't
- [x] Easy to replace — tool-agnostic, ISO/IEC 11179-grounded, same standard as every prior domain
