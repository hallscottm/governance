# Data Platform Domain — Definitions

Status: Draft
Ratified: No
Last updated: 2026-09-22

Definitions for the Data Platform domain — where data physically lives and
runs: databases, data lakes/lakehouses/warehouses, vector stores, and
streaming systems. Distinct from Data/Metadata (domain 5), which owns what
the data *means* (classification, stewardship, catalog, lineage) rather
than where it runs. Split out of System Architecture on 2026-09-22 — see
00-framework/ea-framework-alignment.md for why. Database/Database Schema/
Table/Index/Transaction/ACID/Database Replica/Partitioning-Sharding/
Connection Pool/Schema Migration are migrated verbatim from
03-system-architecture/01-definitions.md; System Architecture now holds
reference stubs to them instead.

## Referenced Terms (owned elsewhere)

- **Compute Unit** — owned by Infrastructure →
  [01-infrastructure/01-definitions.md#infra-compute-unit](../01-infrastructure/01-definitions.md#infra-compute-unit)
- **Block Storage** — owned by Infrastructure →
  [01-infrastructure/01-definitions.md#infra-block-storage](../01-infrastructure/01-definitions.md#infra-block-storage)
- **Replication Factor** — owned by Infrastructure →
  [01-infrastructure/01-definitions.md#infra-replication-factor](../01-infrastructure/01-definitions.md#infra-replication-factor)
- **Service** — owned by System Architecture →
  [03-system-architecture/01-definitions.md#sysarch-service](../03-system-architecture/01-definitions.md#sysarch-service)
- **Sensitivity Level, Data Classification** — owned by Data/Metadata →
  [05-data-metadata/01-definitions.md#data-sensitivity-level](../05-data-metadata/01-definitions.md#data-sensitivity-level)

---

## Databases & Storage

### Database {#dp-database}
An organized collection of structured data managed by a database
engine, accessed and modified through Transactions. Distinct from
Infrastructure's storage tiers/types, which describe the underlying media
and access pattern, not the logical data organization. Migrated from
System Architecture 2026-09-22 (originally `sysarch-database`). Source:
ANSI/ISO SQL:2016 (for relational databases); general usage for
non-relational.
Referenced by: Data/Metadata

### Database Schema {#dp-database-schema}
The structural definition of a Database — its Tables, columns, types, and
constraints. Distinct from System Architecture's API Schema
(`sysarch-api-schema`). Migrated from System Architecture 2026-09-22
(originally `sysarch-database-schema`). Source: ANSI/ISO SQL:2016.
Referenced by: Data/Metadata

### Table {#dp-table}
A structured collection of rows and columns within a relational Database.
Migrated from System Architecture 2026-09-22. Source: ANSI/ISO SQL:2016.

### Index {#dp-index}
A data structure that improves the speed of data retrieval from a Table
at the cost of additional storage and write overhead. Migrated from
System Architecture 2026-09-22. Source: ANSI/ISO SQL:2016.

### Transaction {#dp-transaction}
A unit of work against a Database that is executed according to ACID
properties (below) — it either fully completes or has no effect. Migrated
from System Architecture 2026-09-22. Source: ANSI/ISO SQL:2016.

### ACID (Atomicity, Consistency, Isolation, Durability) {#dp-acid}
The four properties that guarantee reliable processing of database
Transactions. Migrated from System Architecture 2026-09-22. Source:
ANSI/ISO SQL:2016; foundational relational database theory.

### Database Replica {#dp-database-replica}
A copy of a Database (or a subset of it) kept synchronized with a primary,
used for read scaling, failover, or geographic distribution. Related to
but distinct from Infrastructure's Replication Factor, which describes
storage-level redundancy rather than database-level replication topology.
Migrated from System Architecture 2026-09-22. Source: General database
engineering usage.

### Partitioning / Sharding {#dp-partitioning-sharding}
Splitting a Database's data across multiple physical or logical divisions
to improve scalability — partitioning within one database instance,
sharding across multiple instances. Migrated from System Architecture
2026-09-22. Source: General database engineering usage.

### Connection Pool {#dp-connection-pool}
A cache of reusable Database connections maintained by a Service to avoid
the overhead of establishing a new connection per request. Migrated from
System Architecture 2026-09-22. Source: General software/database
engineering usage.

### Schema Migration {#dp-schema-migration}
A versioned, applied change to a Database Schema, typically managed
through an ordered set of migration scripts. Migrated from System
Architecture 2026-09-22. Source: General software engineering usage.

---

## Analytical & Large-Scale Storage

### Data Warehouse {#dp-data-warehouse}
A centralized store of structured, integrated data optimized for
analytical querying and reporting rather than transactional workloads —
typically loaded from one or more source Databases via a Data Pipeline
(below) and organized around OLAP-style schemas (e.g., star/snowflake).
Source: Common industry practice (Inmon/Kimball data warehousing
methodology).

### Data Lake {#dp-data-lake}
A centralized store for raw data in its native format (structured,
semi-structured, or unstructured), retained without requiring a schema
be defined up front ("schema-on-read" rather than a Warehouse's
"schema-on-write"). Source: Common industry practice.

### Data Lakehouse {#dp-data-lakehouse}
A storage architecture that layers Data-Warehouse-style schema
enforcement, ACID transactions, and query performance on top of Data-Lake
storage (typically open table formats such as Delta Lake, Apache Iceberg,
or Apache Hudi over object storage). Source: Common industry practice.

### Vector Database {#dp-vector-database}
A database optimized for storing and querying Vector Embeddings (below)
by similarity (nearest-neighbor search) rather than exact match — the
storage layer behind retrieval-augmented generation (RAG) and other
similarity-search workloads. Source: Common industry practice.

### Vector Embedding {#dp-vector-embedding}
A numeric vector representation of data (text, image, audio, etc.)
produced by a model, positioned in a vector space such that semantically
similar inputs produce nearby vectors. Source: Common industry practice
(machine learning).

### OLTP (Online Transaction Processing) {#dp-oltp}
A workload pattern optimized for high-volume, low-latency reads/writes of
individual records — the pattern a Database (above) is typically tuned
for. Source: Common industry practice.

### OLAP (Online Analytical Processing) {#dp-olap}
A workload pattern optimized for complex queries scanning/aggregating
large volumes of data — the pattern a Data Warehouse is typically tuned
for. Source: Common industry practice.

### Semantic Layer {#dp-semantic-layer}
A queryable layer (e.g., dbt Semantic Layer, LookML) that materializes
Data/Metadata's Metric definitions (`data-metric`) against a Data
Warehouse/Lakehouse into a single, consistent, reusable object that
downstream reporting tools query instead of recalculating the metric
themselves. This is the "official" model a Business Intelligence /
Reporting domain's report-level Calculated Field (`bi-calculated-field`)
should trace back to — the mechanism that makes divergence a choice a
report builder makes (bypassing this layer) rather than something that
happens by default. Added 2026-09-22 when Business Intelligence /
Reporting was split out as its own domain — see 00-framework/
ea-framework-alignment.md. Source: Common industry practice.

---

## Streaming & Pipelines

### Streaming Platform {#dp-streaming-platform}
Infrastructure for publishing, storing, and consuming continuous streams
of events/records in order (e.g., Apache Kafka, cloud-native equivalents)
— distinct from System Architecture's Message Queue/Event Bus
(`sysarch-message-queue`, `sysarch-event-bus`), which describe integration
patterns between Services; a Streaming Platform is the durable, replayable
storage layer those patterns can be built on. Source: Common industry
practice.

### Stream / Topic {#dp-stream-topic}
A named, ordered, append-only sequence of records within a Streaming
Platform. Source: Common industry practice.

### Data Pipeline {#dp-data-pipeline}
An automated sequence of steps that moves and/or transforms data from a
Source System into a Database, Warehouse, Lake, or Lakehouse. Related to
but distinct from Data/Metadata's Data Transformation
(`data-transformation`), which describes the lineage-tracked change
itself; a Data Pipeline is the mechanism that executes it. Source: Common
industry practice.

### Batch Processing {#dp-batch-processing}
Processing data in discrete, scheduled groups ("batches") rather than as
individual events arrive. Contrast with Stream Processing (below).
Source: Common industry practice.

### Stream Processing {#dp-stream-processing}
Processing data continuously as individual records arrive on a Stream,
rather than waiting for a scheduled batch. Source: Common industry
practice.

### ETL / ELT (Extract, Transform, Load / Extract, Load, Transform) {#dp-etl-elt}
Two orderings of a Data Pipeline's core steps — ETL transforms data
before loading it into the destination; ELT loads raw data first and
transforms it in place (typically in a Warehouse or Lakehouse capable of
scalable in-place transformation). Source: Common industry practice.

**Quality bar check (00-framework/quality-bar.md):**
- [x] Simple — one file, subdomain-grouped, no nested taxonomy logic here
- [x] Modular — migrated terms keep their exact prior meaning; new terms
      added independently without touching migrated ones
- [x] Easy to update — new storage/streaming paradigms add a term without
      touching existing ones
- [x] Easy to maintain — single owner per term, DRY via reference stubs
- [x] Easy to replace — no single vendor/product named as the definition
      of a concept (Kafka, Delta Lake, etc. appear only as examples)
