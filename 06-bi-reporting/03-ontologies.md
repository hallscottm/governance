# Business Intelligence / Reporting Domain — Ontologies

Status: Draft
Ratified: No
Last updated: 2026-09-22
Relation vocabulary: 00-framework/relation-types.md
Built on: 01-definitions.md, 02-taxonomies.md

Relationships may reference anchors owned by other domains (Data
Platform, Data/Metadata) where a genuine cross-domain relationship
exists. Per the reverse-pointer rule in 00-framework/relation-types.md,
every cross-domain relationship below has a matching reverse pointer
added to the target domain's Ontology file.

## Delivered Artifacts

- `bi-dashboard` --[contains]--> `bi-report`
  Rationale: a dashboard is composed of one or more reports/visualizations presented together.
- `bi-report` --[contains]--> `bi-visualization`
  Rationale: a report is composed of its individual charts/tables.

## Report-Level Models

- `bi-report` --[requires]--> `bi-report-data-model`
  Rationale: a report is rendered from a data model, whether that model is a thin pass-through of an upstream Semantic Layer or a self-service model built inside the tool.
- `bi-report-data-model` --[contains]--> `bi-calculated-field`
  Rationale: a report data model is composed of its calculated fields/measures.
- `bi-report-data-model` --[requires]--> `bi-data-extract`
  Rationale: a report data model draws on either a live connection or a data extract; when an extract is used, the model depends on it.
- `bi-data-extract` --[constrains]--> `bi-refresh-schedule`
  Rationale: using an extract (vs. a live connection) is what makes a refresh schedule a meaningful, necessary concept — it governs how stale the extract is allowed to get.
- `bi-report-data-model` --[requires]--> `dp-semantic-layer`
  Rationale: cross-domain — the intended, low-risk path: a report data model built on top of the official Semantic Layer rather than reinventing its own calculations. Not every Report Data Model has this relationship — its absence is itself meaningful (see Documentation & Governance below).
- `bi-calculated-field` --[constrains]--> `data-metric`
  Rationale: cross-domain — where a Calculated Field represents the same business concept as an existing Metric, the Metric definition constrains/should bound what the Calculated Field computes. Kept as `constrains` rather than `requires` because, unlike the Semantic Layer relationship above, this one is frequently absent in practice — that gap is the core risk this domain exists to surface, not an edge case to hide.

## Documentation & Governance

- `bi-source-to-target-mapping` --[requires]--> `bi-calculated-field`
  Rationale: a source-to-target mapping exists to document a specific calculated field's provenance; it has nothing to document without one.
- `bi-certified` --[requires]--> `bi-source-to-target-mapping`
  Rationale: per this domain's founding requirement — a Report Data Model cannot reach Certified status without a complete source-to-target mapping on every Calculated Field.
- `bi-row-level-security` --[constrains]--> `bi-report-data-model`
  Rationale: row-level security filters what a given viewer sees of a report data model's data.

## Cross-Domain References (relationships pointing into this domain)

None yet — this domain is new. Per 00-framework/relation-types.md's
reverse-pointer rule, this section will record any future domain that
draws a relationship into a specific BI/Reporting anchor.

---

**Open items:**
- `bi-calculated-field --[constrains]--> data-metric` is deliberately the
  domain's only "should exist but often doesn't" relationship — flagged
  here rather than treated as a data quality issue elsewhere, since
  making the gap visible (not eliminating self-service modeling
  entirely) is this domain's actual governance posture, per the founding
  discussion (00-qa.md Q8 in cross-cutting/roles-and-departments/).
- Policies/Access Rules/Risk Tiers/Tooling columns not yet drafted — the
  Certified/Draft lifecycle above anticipates a Policies-column hard
  gate ("no broad distribution without Certified status") and a
  Tooling-column pointer extending Data/Metadata's OpenMetadata entry,
  but neither is written yet; this Ontology only establishes the
  concepts the later columns will govern.

**Quality bar check (00-framework/quality-bar.md):**
- [x] Simple — 12 relationships, grouped by subdomain
- [x] Modular — cross-domain edges (2 total: into Data Platform and
      Data/Metadata) clearly marked, reverse-pointed
- [x] Easy to update — anchor-ID based, survives renames
- [x] Easy to maintain — grouped by subdomain, matches Definitions/Taxonomy
- [x] Easy to replace — relation-type vocabulary shared across all domains
