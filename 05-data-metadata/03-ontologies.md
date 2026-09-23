# Data/Metadata Domain — Ontologies

Status: Draft — pending review
Ratified: No
Last updated: 2026-09-22
Provenance: see _qa/03-ontologies.qa.md
Relation vocabulary: 00-framework/relation-types.md
Built on: 01-definitions.md, 02-taxonomies.md

Relationships may reference anchors owned by other domains (System
Architecture, Infrastructure) where a genuine cross-domain relationship
exists. Per the reverse-pointer rule in 00-framework/relation-types.md,
every cross-domain relationship below has a matching reverse pointer added
to the target domain's ontology file.

---

## Data Governance Roles & Structures

- `data-domain` --[requires]--> `data-owner`
  Rationale: a Data Domain cannot be governed without an accountable owner.
- `data-domain` --[requires]--> `data-steward`
  Rationale: a Data Domain requires a steward to execute governance rules day to day.
- `data-owner` --[constrains]--> `data-steward`
  Rationale: the owner's governance decisions constrain what the steward's day-to-day execution may do.
- `data-governance-council` --[constrains]--> `data-domain`
  Rationale: the council sets policy that constrains how every Data Domain is governed.
- `data-custodian` --[requires]--> `dp-database`
  Rationale: cross-domain — a custodian's technical storage/security responsibility is exercised over an actual database.

## Data Classification & Sensitivity

- `data-classification` --[produces]--> `data-sensitivity-level`
  Rationale: classifying a data asset is what assigns it a sensitivity level.
- `data-sensitivity-level` --[contains]--> `data-classification-public`
  Rationale: Public is one of the four defined values of Sensitivity Level.
- `data-sensitivity-level` --[contains]--> `data-classification-internal`
  Rationale: Internal is one of the four defined values.
- `data-sensitivity-level` --[contains]--> `data-classification-confidential`
  Rationale: Confidential is one of the four defined values.
- `data-sensitivity-level` --[contains]--> `data-classification-restricted`
  Rationale: Restricted is one of the four defined values.
- `data-pii` --[constrains]--> `data-classification`
  Rationale: the presence of PII constrains a classification decision toward Confidential or higher.
- `data-phi` --[constrains]--> `data-classification-restricted`
  Rationale: PHI, where in scope, constrains classification toward the highest tier.
- `data-sensitivity-level` --[produces]--> `data-handling-requirement`
  Rationale: a data asset's sensitivity level is what determines its concrete handling controls.
- `data-classification` --[requires]--> `data-steward`
  Rationale: classification tagging is a governance action executed by a Data Steward.

## Data Quality

- `data-quality` --[measured-by]--> `data-quality-accuracy`
  Rationale: accuracy is one of the six dimensions data quality is measured across.
- `data-quality` --[measured-by]--> `data-quality-completeness`
  Rationale: completeness is one of the six measurement dimensions.
- `data-quality` --[measured-by]--> `data-quality-consistency`
  Rationale: consistency is one of the six measurement dimensions.
- `data-quality` --[measured-by]--> `data-quality-timeliness`
  Rationale: timeliness is one of the six measurement dimensions.
- `data-quality` --[measured-by]--> `data-quality-validity`
  Rationale: validity is one of the six measurement dimensions.
- `data-quality` --[measured-by]--> `data-quality-uniqueness`
  Rationale: uniqueness is one of the six measurement dimensions.
- `data-profiling` --[produces]--> `data-quality-rule`
  Rationale: profiling a dataset is how quality rules get established or verified.
- `data-quality-rule` --[constrains]--> `dp-database`
  Rationale: cross-domain — quality rules constrain what data is considered valid within a database.

## Metadata Types

- `data-metadata` --[contains]--> `data-business-metadata`
  Rationale: business metadata is one of the three defined metadata types.
- `data-metadata` --[contains]--> `data-technical-metadata`
  Rationale: technical metadata is one of the three defined metadata types.
- `data-metadata` --[contains]--> `data-operational-metadata`
  Rationale: operational metadata is one of the three defined metadata types.
- `data-metadata-registry` --[contains]--> `data-metadata`
  Rationale: a metadata registry is the structured system holding an organization's metadata.
- `data-metadata-repository` --[requires]--> `data-metadata-registry`
  Rationale: a repository is the storage implementation of a registry's structure/standard.
- `data-technical-metadata` --[requires]--> `dp-database-schema`
  Rationale: cross-domain — technical metadata describes a data asset's structure, which for a database is its schema.

## Data Catalog & Discovery

- `data-catalog` --[contains]--> `data-asset`
  Rationale: a data catalog is an inventory composed of data assets.
- `data-catalog` --[requires]--> `data-metadata`
  Rationale: a catalog is built from the metadata describing its assets.
- `data-dataset` --[located-in]--> `dp-database`
  Rationale: cross-domain — a dataset is commonly a defined collection stored within a database.
- `data-business-glossary` --[contains]--> `data-glossary-term`
  Rationale: a glossary is composed of individual defined terms.
- `data-dictionary` --[requires]--> `dp-database-schema`
  Rationale: cross-domain — a data dictionary documents the fields of a specific schema.
- `data-semantic-domain` --[requires]--> `data-business-glossary`
  Rationale: a semantic domain maps technical fields to business-friendly names drawn from the glossary.
- `data-metric` --[requires]--> `data-glossary-term`
  Rationale: added 2026-09-22 — a Metric's business meaning should trace back to a defined glossary term, not exist as a free-floating formula.

## Data Modeling Concepts

- `data-conceptual-model` --[contains]--> `data-entity`
  Rationale: a conceptual model is composed of the business entities it identifies.
- `data-entity` --[contains]--> `data-attribute`
  Rationale: an entity is composed of its attributes.
- `data-relationship` --[requires]--> `data-entity`
  Rationale: a data-modeling relationship connects two entities that must exist for it to be defined.
- `data-conceptual-model` --[produces]--> `data-logical-model`
  Rationale: a conceptual model is elaborated into a logical model with full entity/attribute/relationship detail.
- `data-logical-model` --[produces]--> `dp-database-schema`
  Rationale: cross-domain — a logical model is implemented as a physical schema (System Architecture's Database Schema).

## Master & Reference Data

- `data-master-data` --[requires]--> `data-system-of-record`
  Rationale: master data's trusted definition depends on a designated authoritative source system.
- `data-deduplication` --[produces]--> `data-golden-record`
  Rationale: deduplication/reconciliation is the process that produces a golden record.
- `data-deduplication` --[requires]--> `data-survivorship-rule`
  Rationale: deduplication needs a defined rule for which conflicting value wins.
- `data-reference-data` --[constrains]--> `data-master-data`
  Rationale: reference data's permissible values constrain what a master data record's categorical fields may contain.

## Data Lineage & Provenance

- `data-lineage` --[contains]--> `data-transformation`
  Rationale: a lineage record is composed of the transformation steps data has undergone.
- `data-lineage` --[requires]--> `data-source-system`
  Rationale: a lineage trace must originate from a defined source system.
- `data-lineage` --[requires]--> `data-downstream-consumer`
  Rationale: a lineage trace extends to the consumers that use the data.
- `data-provenance` --[contains]--> `data-lineage`
  Rationale: provenance is the broader custody/ownership history, of which transformation lineage is one part.

## Data Lifecycle & Retention

- `data-retention-period` --[constrains]--> `data-disposal`
  Rationale: disposal cannot occur before the retention period expires.
- `data-legal-hold` --[constrains]--> `data-disposal`
  Rationale: an active legal hold suspends disposal regardless of retention period status.
- `data-archival` --[requires]--> `infra-archive`
  Rationale: cross-domain — data archival is realized physically through Infrastructure's Archive storage tier.
- `data-lifecycle-stage` --[constrains]--> `data-retention-period`
  Rationale: which retention period applies depends on the data's current lifecycle stage.

## Data Privacy & Regulatory

- `data-personal-data` --[contains]--> `data-pii`
  Rationale: PII is the practical/operational subset of the broader regulatory concept of personal data.
- `data-personal-data` --[requires]--> `data-subject`
  Rationale: personal data is only meaningful in relation to the data subject it identifies.
- `data-consent` --[constrains]--> `data-processing-purpose`
  Rationale: consent is scoped to and limits what processing purpose data may be used for.
- `data-minimization` --[constrains]--> `data-processing-purpose`
  Rationale: minimization limits data collection to only what a stated purpose requires.
- `data-right-to-erasure` --[constrains]--> `data-disposal`
  Rationale: an erasure request drives disposal outside the normal retention-period timeline.
- `data-cross-border-transfer` --[constrains]--> `data-personal-data`
  Rationale: cross-border transfer rules constrain how personal data may move between jurisdictions.

---

## Cross-Domain References (relationships pointing into this domain)

Per 00-framework/relation-types.md's reverse-pointer rule, added
2026-09-22 when Data Platform's Semantic Layer created the first
relationship pointing into this domain from elsewhere.

- `data-metric`
  Referenced by (cross-domain relationships):
  - Data Platform: `dp-semantic-layer --[requires]--> data-metric`
  - Business Intelligence / Reporting: `bi-calculated-field --[constrains]--> data-metric`

---

**Open items:**
- `data-golden-record` and `data-master-data` are closely related (a
  golden record IS the trusted master data instance) but were kept as
  two separate relations (`data-deduplication --[produces]--> golden-
  record`, `master-data --[requires]--> system-of-record`) rather than
  drawing a direct edge between them, since the definitional overlap is
  already explicit in prose; forcing a third relation would be
  redundant.
- Data Quality's six dimensions are each linked individually to
  `data-quality` via `measured-by` rather than nested under one another —
  flagged as consistent with how System Architecture treated its six
  Quality Attributes (ISO/IEC 25010) the same way.

**Quality bar check (00-framework/quality-bar.md):**
- [x] Simple — 59 relationships, grouped by subdomain, no forced edges
- [x] Modular — cross-domain edges (6 outbound + 1 inbound) are clearly marked and reverse-pointed
- [x] Easy to update — anchor-ID based, survives renames
- [x] Easy to maintain — grouped by subdomain, matches Definitions/Taxonomy
- [x] Easy to replace — relation-type vocabulary shared across all domains
