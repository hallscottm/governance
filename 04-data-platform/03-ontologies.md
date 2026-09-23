# Data Platform Domain — Ontologies

Status: Draft
Ratified: No
Last updated: 2026-09-22
Relation vocabulary: 00-framework/relation-types.md
Built on: 01-definitions.md, 02-taxonomies.md

Relationships may reference anchors owned by other domains (Infrastructure)
where a genuine cross-domain relationship exists. Per the reverse-pointer
rule in 00-framework/relation-types.md, every cross-domain relationship
below has a matching reverse pointer added to the target domain's Ontology
file. The 10 internal relationships below are migrated verbatim (prefix
renamed `sysarch-` → `dp-`) from 03-system-architecture/03-ontologies.md's
former "Databases & Storage" section, 2026-09-22.

## Databases & Storage

- `dp-database` --[contains]--> `dp-database-schema`
  Rationale: a database's structure is defined by its schema.
- `dp-database-schema` --[contains]--> `dp-table`
  Rationale: a schema is composed of table definitions.
- `dp-table` --[contains]--> `dp-index`
  Rationale: an index is defined on and belongs to a specific table.
- `dp-database` --[requires]--> `dp-acid`
  Rationale: a (relational) database's transactional guarantees depend on ACID properties.
- `dp-transaction` --[requires]--> `dp-acid`
  Rationale: a transaction is only meaningful as a unit of work governed by ACID guarantees.
- `dp-database-replica` --[requires]--> `dp-database`
  Rationale: a replica exists only in relation to a primary database it mirrors.
- `dp-database` --[scales-via]--> `dp-partitioning-sharding`
  Rationale: partitioning/sharding is a primary mechanism for scaling a database beyond a single instance's capacity.
- `dp-connection-pool` --[requires]--> `dp-database`
  Rationale: a connection pool exists to manage reusable connections to a specific database; the Service that holds the pool is `sysarch-service` (cross-domain, see below).
- `dp-schema-migration` --[produces]--> `dp-database-schema`
  Rationale: applying a migration produces a new version of the database schema.
- `dp-database` --[runs-on]--> `infra-compute-unit`
  Rationale: cross-domain — a database engine executes on underlying compute, whether self-managed or a managed service.
- `dp-database` --[requires]--> `infra-block-storage`
  Rationale: cross-domain — relational and most transactional databases require durable block storage for their data files.
- `sysarch-service` --[requires]--> `dp-connection-pool`
  Rationale: cross-domain — a Service that talks to a Database typically holds a Connection Pool rather than opening a raw connection per request.

## Analytical, Streaming & Vector Storage

- `dp-data-warehouse` --[requires]--> `dp-data-pipeline`
  Rationale: a warehouse's data arrives through a pipeline; it is not written to directly by application Services the way an OLTP database is.
- `dp-data-lakehouse` --[requires]--> `dp-data-lake`
  Rationale: a lakehouse layers schema/transaction guarantees on top of lake-style object storage — it doesn't exist without an underlying lake.
- `dp-data-lakehouse` --[requires]--> `dp-acid`
  Rationale: what distinguishes a lakehouse from a plain data lake is ACID-transactional guarantees over the stored files.
- `dp-vector-database` --[contains]--> `dp-vector-embedding`
  Rationale: a vector database stores and indexes embeddings.
- `dp-data-pipeline` --[produces]--> `dp-vector-embedding`
  Rationale: embeddings are typically generated as a pipeline step (e.g., during ingestion into a Vector Database), not authored by hand.
- `dp-etl-elt` --[constrains]--> `dp-data-pipeline`
  Rationale: ETL vs. ELT is a design choice that constrains how a given pipeline's steps are ordered.
- `dp-stream-processing` --[requires]--> `dp-stream-topic`
  Rationale: stream processing operates on records read from a topic.
- `dp-stream-topic` --[located-in]--> `dp-streaming-platform`
  Rationale: a topic is a named subdivision of a streaming platform, not a standalone resource.
- `dp-batch-processing` --[constrains]--> `dp-data-pipeline`
  Rationale: batch vs. stream is a design choice that constrains how a given pipeline executes, same relation shape as ETL/ELT above.
- `dp-oltp` --[constrains]--> `dp-database`
  Rationale: OLTP is a workload pattern that constrains how a database is tuned/indexed (favoring fast, small reads/writes).
- `dp-olap` --[constrains]--> `dp-data-warehouse`
  Rationale: OLAP is the workload pattern a warehouse is tuned for (favoring large aggregating scans).
- `dp-semantic-layer` --[requires]--> `dp-data-warehouse`
  Rationale: added 2026-09-22 — a semantic layer materializes metrics against a warehouse/lakehouse; it has nothing to query without one.
- `dp-semantic-layer` --[requires]--> `data-metric`
  Rationale: cross-domain, added 2026-09-22 — a semantic layer exists to materialize Data/Metadata's official Metric definitions, not to invent its own.

## Cross-Domain References (relationships pointing into this domain)

Per 00-framework/relation-types.md's reverse-pointer rule. Migrated from
System Architecture 2026-09-22 (Data/Metadata's relationships originally
targeted `sysarch-database`/`sysarch-database-schema`; renamed here to
match the migrated anchors — see 05-data-metadata/03-ontologies.md for the
source of truth on these edges).

- `dp-database`
  Referenced by (cross-domain relationships):
  - Data/Metadata: `data-custodian --[requires]--> dp-database`
  - Data/Metadata: `data-quality-rule --[constrains]--> dp-database`
  - Data/Metadata: `data-dataset --[located-in]--> dp-database`
  - Harness: `harness-retrieval-source --[requires]--> dp-database` (added 2026-09-23)
- `dp-database-schema`
  Referenced by (cross-domain relationships):
  - Data/Metadata: `data-technical-metadata --[requires]--> dp-database-schema`
  - Data/Metadata: `data-dictionary --[requires]--> dp-database-schema`
  - Data/Metadata: `data-logical-model --[produces]--> dp-database-schema`
- `dp-semantic-layer`
  Referenced by (cross-domain relationships), added 2026-09-22:
  - Cross-Cutting Roles & Departments: `ccrole-analytics-engineer --[requires]--> dp-semantic-layer`
  - Business Intelligence / Reporting: `bi-report-data-model --[requires]--> dp-semantic-layer`
- `dp-data-pipeline`
  Referenced by (cross-domain relationships), added 2026-09-22:
  - Workflow/Process: `wf-dag --[requires]--> dp-data-pipeline`

---

**Open items:**
- `dp-database-replica` and `infra-replication-factor` are related
  concepts (database-level replication topology vs. storage-level
  redundancy) but no direct relationship was drawn — left unconnected
  per the "not every term needs a relationship" scope note (same
  judgment made when this note first appeared in System Architecture's
  Ontology column, carried over with the migration).
- New Analytical/Streaming/Vector relationships above are a first pass,
  not exhaustively cross-checked against System Architecture's
  Integration & Messaging terms (`sysarch-message-queue`,
  `sysarch-event-bus`) — Streaming Platform vs. Message Queue/Event Bus
  distinction is noted in 01-definitions.md but no ontology edge drawn
  between them yet; revisit once Workflow/Process (CI/CD, pipeline
  orchestration) is drafted and the full picture of how these interact
  is clearer.

**Quality bar check (00-framework/quality-bar.md):**
- [x] Simple — 25 relationships (plus 9 documented inbound cross-domain edges: 6 from Data/Metadata, 2 from Cross-Cutting Roles & Departments/Business Intelligence / Reporting, 1 from Workflow/Process, added 2026-09-22), grouped by subdomain
- [x] Modular — migrated relationships kept their exact prior meaning;
      new relationships added independently
- [x] Easy to update — new storage/streaming paradigms add relationships
      without touching existing ones
- [x] Easy to maintain — reverse-pointer discipline followed for all
      cross-domain edges (into Infrastructure and from Data/Metadata)
- [x] Easy to replace — no vendor/product named in any relationship
