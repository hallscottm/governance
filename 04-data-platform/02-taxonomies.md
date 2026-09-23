# Data Platform Domain — Taxonomies

Status: Draft
Ratified: No
Last updated: 2026-09-22
Provenance: see _qa/02-taxonomies.qa.md
Built on: 01-definitions.md (24 owned terms)

Structure: strict single-parent tree, consistent with the standard set
during Infrastructure's Taxonomy column. Only terms owned by this domain
are classified here — the 5 referenced terms (Compute Unit, Block Storage,
Replication Factor from Infrastructure; Service from System Architecture;
Sensitivity Level/Data Classification from Data/Metadata) are not
re-classified in this domain's tree.

---

## Data Platform
├── Databases & Storage
│   ├── Database (#dp-database)
│   ├── Database Schema (#dp-database-schema)
│   ├── Table (#dp-table)
│   ├── Index (#dp-index)
│   ├── Transaction (#dp-transaction)
│   ├── ACID (#dp-acid)
│   ├── Database Replica (#dp-database-replica)
│   ├── Partitioning / Sharding (#dp-partitioning-sharding)
│   ├── Connection Pool (#dp-connection-pool)
│   └── Schema Migration (#dp-schema-migration)
│
├── Analytical & Large-Scale Storage
│   ├── Data Warehouse (#dp-data-warehouse)
│   ├── Data Lake (#dp-data-lake)
│   ├── Data Lakehouse (#dp-data-lakehouse)
│   ├── Vector Database (#dp-vector-database)
│   ├── Vector Embedding (#dp-vector-embedding)
│   ├── OLTP (#dp-oltp)
│   ├── OLAP (#dp-olap)
│   └── Semantic Layer (#dp-semantic-layer)
│
└── Streaming & Pipelines
    ├── Streaming Platform (#dp-streaming-platform)
    ├── Stream / Topic (#dp-stream-topic)
    ├── Data Pipeline (#dp-data-pipeline)
    ├── Batch Processing (#dp-batch-processing)
    ├── Stream Processing (#dp-stream-processing)
    └── ETL / ELT (#dp-etl-elt)

**Quality bar check (00-framework/quality-bar.md):**
- [x] Simple — one tree, three subdomains, matches Definitions' grouping
- [x] Modular — subdomains classify independently
- [x] Easy to update — a new storage/streaming paradigm adds a leaf
- [x] Easy to maintain — mirrors 01-definitions.md's subdomain headings
      exactly, no separate structure to keep in sync by hand
- [x] Easy to replace — pure classification, no tooling/vendor lock-in
