# Data Platform Domain — Tooling / Implementation

Status: Draft — pending review
Ratified: No
Last updated: 2026-09-22
Provenance: see _qa/10-tooling.qa.md
Built on: all prior columns (00-09)

Same posture as every prior domain: capability categories only, no
specific product/vendor recommendations.

## Capability Categories

### Relational / OLTP Database Engine
Runs Databases tuned for OLTP workloads (`dp-oltp`). Enforces
DPPOL-1/DPPROC-1's schema migration gate at the tooling level (migration
runner). Category is deliberately broad (relational, document, key-value,
graph engines all need this) rather than one relational-only
recommendation — inherited scope note from System Architecture's original
"Database Platform & Migration Tooling" category, moved here 2026-09-22.

### Analytical Warehouse / Lakehouse Platform
Runs Data Warehouses and Data Lakehouses tuned for OLAP workloads
(`dp-olap`). Enforces DPPOL-4's table-format declaration and change gate.
Direct dependency on the Table Format capability below — a Lakehouse
platform choice and its underlying table-format choice are typically
bundled, not selected independently.

### Table Format / Open Lakehouse Storage
Implements the open table-format specification (Delta Lake, Apache
Iceberg, Apache Hudi — 00-standards-alignment.md) a Data Lakehouse is
built on. Direct dependency on Infrastructure's object storage/Block
Storage selection (01-infrastructure/10-tooling.md) — the table format
sits on top of whatever durable storage Infrastructure provides.

### Vector Database Platform
Runs Vector Databases and enforces DPPOL-3's Embedding Model Reference
requirement (typically as an index-level metadata field the platform
itself supports natively). Distinct capability from the Relational/OLTP
category above even though some platforms offer both.

### Streaming Platform
Runs Streaming Platforms/Topics, enforces DPPOL-2's retention window
requirement, and supports Topic Partition Count and Schema Registry
Reference (04-metadata-standards.md) as native concepts. Overlaps
functionally with System Architecture's Message Queue/Event Bus tooling
— likely the same product family for organizations that use one platform
for both durable event storage and lighter-weight service integration,
flagged the same way API Gateway and Load Balancer tooling were flagged
as a likely-shared product family between System Architecture and
Networking.

### Data Pipeline Orchestration
Schedules and runs Data Pipelines (Orchestration Reference,
04-metadata-standards.md). This category's actual execution/scheduling
mechanism is Workflow/Process's Data Pipeline Orchestration Engine
category (07-workflow-process/10-tooling.md) — resolved 2026-09-22;
listed here because the pipeline concept and its metadata fields are
owned by this domain, even though the orchestration engine itself is
owned by Workflow/Process.

### Semantic Layer Tooling
Implements the Semantic Layer (`dp-semantic-layer`) that materializes
Data/Metadata's Metric definitions and enforces DPPOL-5's
Certified-Metric-via-Semantic-Layer requirement. Direct dependency on the
Analytical Warehouse/Lakehouse Platform category (a semantic layer
queries a warehouse/lakehouse, it doesn't store data itself).

### Data Catalog / Metadata Management Platform
An OpenMetadata-class platform (or DataHub/Collibra/Atlan-class
equivalent) that auto-derives technical lineage across this domain's
Databases, Warehouses, Lakehouses, and Pipelines — the tooling-delegation
posture discussed when Business Intelligence / Reporting's Source-to-
Target Mapping (`bi-source-to-target-mapping`) was defined as typically
tool-derived rather than hand-authored. This category is where DPPROC-5's
"flag a report computing a Certified Metric outside the Semantic Layer"
detection mechanism most naturally lives — the catalog already has
visibility into what queries which warehouse table. Shared with
Data/Metadata's own Tooling column (05-data-metadata/10-tooling.md) —
one platform typically serves both domains, not independently selected.

---

**Cross-category dependency notes:**
- Analytical Warehouse/Lakehouse Platform and Table Format/Open Lakehouse
  Storage are very likely the same vendor selection, not independent
  choices, for most Lakehouse products.
- Table Format/Open Lakehouse Storage is constrained by Infrastructure's
  object storage selection, same shape as System Architecture's Container
  Image Registry being constrained by Infrastructure's Container Runtime.
- Streaming Platform likely overlaps with System Architecture's Message
  Queue/Event Bus tooling.
- Data Catalog / Metadata Management Platform is very likely one
  org-wide/cross-domain tool shared with Data/Metadata (and eventually
  Business Intelligence / Reporting), not a Data-Platform-only selection
  — same "org-wide tool, not per-domain" flag already raised for Secrets
  Management in System Architecture.

**Open items:**
- (Resolved 2026-09-22) Data Pipeline Orchestration's actual mechanism is
  Workflow/Process's Orchestration Engine — same resolution now recorded
  in 06-policies.md and 08-procedures.md.
- (Resolved 2026-09-22) DPPROC-5's detection mechanism cross-checked
  against Business Intelligence / Reporting's own Tooling column, now
  drafted (06-bi-reporting/10-tooling.md) — both domains explicitly share
  one Data Catalog / Metadata Management Platform selection rather than
  each asserting an independent one, resolving this item as anticipated.

**Quality bar check (00-framework/quality-bar.md):**
- [x] Simple — 7 capability categories, no product lock-in
- [x] Modular — each category maps to a specific Policy/Procedure it implements
- [x] Easy to update — a category can be filled in with a specific product later without touching this structure
- [x] Easy to maintain — cross-category dependencies documented explicitly, not left implicit
- [x] Easy to replace — no product named, so no migration cost baked into the framework itself
