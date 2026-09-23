# Business Intelligence / Reporting Domain — Tooling / Implementation

Status: Draft — pending review
Ratified: No
Last updated: 2026-09-22
Provenance: see _qa/10-tooling.qa.md
Built on: all prior columns (00-09)

Same posture as every prior domain: capability categories only, no
specific product/vendor recommendations.

## Capability Categories

### BI / Reporting Platform
Renders Reports and Dashboards (e.g. Power BI, Tableau, Looker-class
product). Supports the Draft/Certified lifecycle natively in most modern
platforms (certification tiers/badges), which BIPOL-1/BIPROC-1 build on
rather than reinvent — this domain's Certified status maps onto the
platform's own certification feature where one exists.

### Semantic Layer Client / Consumption Tooling
The connector/driver a Report Data Model uses to query Data Platform's
Semantic Layer (`dp-semantic-layer`) directly, enabling the "Semantic
Layer Sourced" field (04-metadata-standards.md) to be true. Direct
dependency on Data Platform's own Semantic Layer Tooling category
(04-data-platform/10-tooling.md) — this is the consumption side of that
same capability, not an independent selection.

### Row-Level Security / Access Control
Implements Row-Level Security (`bi-row-level-security`) at the reporting
tool layer, enforcing BIPOL-3. Distinct from Data Platform's own
database-level access controls — this category filters at report render
time, on top of whatever the underlying Database/Warehouse already
restricts.

### Accessibility Testing
Scans Reports/Dashboards against WCAG 2.1/2.2 (00-standards-alignment.md)
— contrast, screen-reader labeling, keyboard navigation. A newer
capability category for this framework; included because this domain is
the first whose Delivered Artifacts are routinely consumed directly by
a broad, non-technical human audience, making accessibility a live
concern in a way it wasn't for the more infrastructure-facing domains.

### Data Catalog / Metadata Management Platform (shared, not separately selected)
An OpenMetadata-class platform (or DataHub/Collibra/Atlan-class
equivalent) — **the same platform already flagged in Data Platform's
Tooling column** (04-data-platform/10-tooling.md) as the likely home for
Source-to-Target Mapping auto-extraction and Certified-Metric-bypass
detection (DPPROC-5). This reconciles that column's own open item: rather
than this domain independently selecting a second catalog platform, it
consumes the same one Data Platform and Data/Metadata already share —
the catalog's visibility into "what queries which warehouse table" is
what makes `bi-source-to-target-mapping` typically tool-derived rather
than hand-authored (01-definitions.md), and what BIPROC-1's certification
review can lean on rather than re-deriving lineage by hand.

---

**Cross-category dependency notes:**
- Semantic Layer Client/Consumption Tooling is constrained by whatever
  Data Platform selected for its own Semantic Layer Tooling — not an
  independent choice.
- Data Catalog / Metadata Management Platform is explicitly the same
  selection as Data Platform's and Data/Metadata's own Tooling columns —
  this resolves the reconciliation flagged as an open item in
  04-data-platform/10-tooling.md when this domain's column wasn't yet
  drafted.
- BI / Reporting Platform and Row-Level Security/Access Control are very
  often the same product (native RLS features in most modern BI tools)
  rather than a separately selected capability — noted, not asserted as
  universal, since some organizations do layer a separate access-control
  product in front.

**Open items:**
- The Certification Status factor's "policy violation" case flagged in
  09-risk-tiers.md has no defined tooling response here yet (alerting,
  auto-revert) — left open, consistent with that column's own open item.

**Quality bar check (00-framework/quality-bar.md):**
- [x] Simple — 5 capability categories, no product lock-in
- [x] Modular — each category maps to a specific Policy/Procedure it implements
- [x] Easy to update — a category can be filled in with a specific product later without touching this structure
- [x] Easy to maintain — cross-category dependencies documented explicitly, not left implicit
- [x] Easy to replace — no product named; Data Catalog category explicitly shared rather than duplicated across three domains
