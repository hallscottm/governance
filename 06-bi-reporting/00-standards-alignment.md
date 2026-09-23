# Business Intelligence / Reporting Domain — Standards Alignment

Status: Draft — pending review
Ratified: No
Last updated: 2026-09-22

Reference panel for this domain, consulted before extending Definitions.
Scope per 00-framework/domain-axis-definition.md: reports, dashboards,
self-service report-level models, and metrics as consumed — where data
becomes a decision-facing artifact. Definitions/Taxonomies/Ontologies
were already drafted before this column, so this panel is written
retroactively, same treatment Infrastructure's and Data Platform's
Standards Alignment received.

| Standard | Body | Covers |
|---|---|---|
| **WCAG 2.1/2.2 (Web Content Accessibility Guidelines)** | W3C | Accessibility requirements for web-delivered Reports/Dashboards (color contrast, screen-reader support, keyboard navigation) — most modern BI tools deliver through a browser, making this domain's Delivered Artifacts subject to it. |
| **XMLA (XML for Analysis)** | Originally Microsoft/Hyperion; now a de facto cross-vendor interoperability protocol, not a formal standards-body publication | OLAP/BI tool interoperability — the closest thing to a formal interchange standard in this space, relevant to how a Report Data Model connects to an upstream Semantic Layer (`dp-semantic-layer`). |
| **ISO 8000 (Data Quality)** | ISO | Already cited by Data/Metadata; relevant here too — a Report inherits its source data's quality dimensions, and a Data Extract can additionally introduce staleness as its own quality concern. |
| **NIST SP 800-53 (AC family — Access Control)** | NIST | Access-control guidance directly relevant to Row-Level Security (`bi-row-level-security`) enforcement. |
| **DAMA-DMBOK** | DAMA International | Primary home is Data/Metadata (domain 5), not this domain — flagged here only to note the boundary: this domain governs how data is *presented and consumed*, DAMA-DMBOK's governance vocabulary governs what it *means*. |

**Noted but not cited as a formal standard:**
- **dbt Semantic Layer / MetricFlow specification** — an open-source
  project specification (not a standards body), already the grounding
  reference for `dp-semantic-layer` in Data Platform; relevant here as
  the consumption-side protocol a Report Data Model built on the
  Semantic Layer typically speaks.
- **TDWI (The Data Warehousing Institute) BI governance maturity
  models** — widely-referenced industry practice for structuring a
  Certified/self-service BI governance program (the Draft/Certified
  lifecycle this domain's Definitions already establish echoes this
  practice), not issued by a formal standards body.

**Not yet consulted, candidate for future passes:**
- **GDPR/CCPA** — relevant if/when a Report/Dashboard surfaces personal
  data to a broad distribution audience; same deferred status Data/
  Metadata and Networking already flagged.
- **PCI-DSS** — relevant if/when a Report surfaces payment-card data;
  same deferred status flagged elsewhere.

**Note on citation confidence:** WCAG and NIST SP 800-53 are stable,
well-established standards. XMLA and the dbt Semantic Layer/MetricFlow
spec are community/industry-originated, not ISO or government
standards — cited as the de facto references practitioners use, distinct
in authority from WCAG/NIST, consistent with how System Architecture and
Data Platform each flagged their own community-originated citations.

**Quality bar check (00-framework/quality-bar.md):**
- [x] Simple — one table, scoped to what this domain actually covers
- [x] Modular — independent of the other domains' panels, no forced overlap beyond the genuine DAMA-DMBOK boundary note
- [x] Easy to update — new standard cited later just adds a row
- [x] Easy to maintain — written retroactively against 01-definitions.md's actual citations, same reconciliation done for every other domain
- [x] Easy to replace — no single standard is load-bearing for the whole domain
