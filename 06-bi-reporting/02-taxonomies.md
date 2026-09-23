# Business Intelligence / Reporting Domain — Taxonomies

Status: Draft
Ratified: No
Last updated: 2026-09-22
Provenance: see _qa/02-taxonomies.qa.md
Built on: 01-definitions.md (10 owned terms)

Structure: strict single-parent tree, consistent with every domain's
Taxonomies column. Only terms owned by this domain are classified here —
the 4 referenced terms (Semantic Layer, Metric, Data Lineage, Data
Warehouse/Lakehouse) are not re-classified in this domain's tree.

---

## Business Intelligence / Reporting
├── Delivered Artifacts
│   ├── Report (#bi-report)
│   ├── Dashboard (#bi-dashboard)
│   └── Visualization (#bi-visualization)
│
├── Report-Level Models
│   ├── Report Data Model (#bi-report-data-model)
│   ├── Calculated Field / Measure (#bi-calculated-field)
│   ├── Data Extract (#bi-data-extract)
│   └── Report Refresh Schedule (#bi-refresh-schedule)
│
└── Documentation & Governance
    ├── Source-to-Target Mapping (#bi-source-to-target-mapping)
    ├── Certified Dataset/Report (#bi-certified)
    └── Row-Level Security (Report-Level) (#bi-row-level-security)

**Quality bar check (00-framework/quality-bar.md):**
- [x] Simple — one tree, three subdomains, matches Definitions' grouping
- [x] Modular — subdomains classify independently
- [x] Easy to update — a new BI concept adds a leaf
- [x] Easy to maintain — mirrors 01-definitions.md's subdomain headings
      exactly, no separate structure to keep in sync by hand
- [x] Easy to replace — pure classification, no tooling/vendor lock-in
