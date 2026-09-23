# Data/Metadata Domain — Metadata Standards

Status: Draft — pending review
Ratified: No
Last updated: 2026-09-22
Provenance: see _qa/04-metadata-standards.qa.md
Built on: 01-definitions.md, 02-taxonomies.md, 03-ontologies.md

Same shape as the three prior domains (shared field registry + entity-type
applicability matrix). Worth noting explicitly: this column is somewhat
self-referential — this domain's own subject is metadata, so this column
defines the metadata *about data assets themselves* (Data Owner,
Sensitivity Level, Retention Period), distinct from the Metadata Types
subdomain in Definitions (Business/Technical/Operational Metadata), which
classifies metadata conceptually rather than specifying required fields.

## Referenced Fields (owned elsewhere)

- **Resource ID** — field defined in Infrastructure's Metadata Standards, drawing from [01-infrastructure/01-definitions.md#infra-resource-id](../01-infrastructure/01-definitions.md#infra-resource-id) — applies to Data Assets/Datasets unchanged
- **Cost Center Tag** — field defined in Infrastructure's Metadata Standards, drawing from [01-infrastructure/01-definitions.md#infra-cost-center-tag](../01-infrastructure/01-definitions.md#infra-cost-center-tag) — applies unchanged
- **Environment (lifecycle)** — field defined in Infrastructure's Metadata Standards, drawing from [01-infrastructure/01-definitions.md#infra-environment-lifecycle](../01-infrastructure/01-definitions.md#infra-environment-lifecycle) — a dataset belongs to an environment the same way a service does

## Field Registry (owned by this domain)

| Field | Definition | Source Term | Required/Optional (default) |
|---|---|---|---|
| **Data Owner** | The accountable Data Owner role for this Data Asset. | `data-owner` | Required for all entity types |
| **Data Domain** | Which Data Domain this asset belongs to. | `data-domain` | Required for all entity types |
| **Sensitivity Level** | The asset's classification tier (Public/Internal/Confidential/Restricted). | `data-sensitivity-level` | Required for all entity types — this is the field that feeds the Data-sensitivity Risk Tier factor (09-risk-tiers.md) |
| **Contains PII** | Whether this asset contains PII, per `data-pii`. | `data-pii` | Required for all entity types (boolean) |
| **Data Retention Period** | The defined retention period before disposal eligibility. | `data-retention-period` | Required for Dataset entity type |
| **Data Quality Score** | A measured or assigned quality rating against this asset's Data Quality Rules, if defined. | `data-quality-rule`, `data-quality` | Optional |
| **Lineage Reference** | Link to this asset's recorded Data Lineage, if tracked. | `data-lineage` | Optional |
| **System of Record Flag** | Whether this asset/system is the designated System of Record for its Data Domain. | `data-system-of-record` | Optional (boolean) |
| **Business Glossary Reference** | Link to the Business Glossary Term(s) this asset's fields correspond to. | `data-glossary-term` | Optional |

## Entity Types & Field Applicability

| Entity Type | Required Fields | Optional Fields |
|---|---|---|
| **Dataset** | Resource ID, Data Owner, Data Domain, Sensitivity Level, Contains PII, Environment, Data Retention Period, Cost Center Tag | Data Quality Score, Lineage Reference, System of Record Flag, Business Glossary Reference |
| **Data Asset (general — report, model, glossary-adjacent artifact)** | Resource ID, Data Owner, Data Domain, Sensitivity Level, Contains PII | Business Glossary Reference |
| **Business Glossary Term** | Resource ID, Data Owner, Data Domain | — |

---

**Open items:**
- Sensitivity Level is Required for every entity type by design — it is
  the field this whole domain exists partly to finally give the
  cross-cutting Risk Tiers framework, so it is not treated as optional
  the way most fields are.
- Enforcement (mandatory-blocking vs. recommended) deferred to Policies
  (column 6), same boundary as all three prior domains.
- No field-level anchors, same framework-level gap flagged in all three
  prior domains' Metadata Standards.

**Quality bar check (00-framework/quality-bar.md):**
- [x] Simple — one field registry (plus referenced fields), one matrix
- [x] Modular — a field's definition changes once, applies everywhere referenced
- [x] Easy to update — add an entity type as one matrix row
- [x] Easy to maintain — fields reference Definitions terms
- [x] Easy to replace — tool-agnostic, ISO/IEC 11179-grounded (same standard already cited by all three prior domains, now cited formally in this domain's own Standards Alignment)
