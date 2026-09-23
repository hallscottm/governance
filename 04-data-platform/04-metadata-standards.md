# Data Platform Domain — Metadata Standards

Status: Draft — pending review
Ratified: No
Last updated: 2026-09-22
Provenance: see _qa/04-metadata-standards.qa.md
Built on: 01-definitions.md, 02-taxonomies.md, 03-ontologies.md

Same shape as every prior domain's Metadata Standards (shared field
registry + entity-type applicability matrix).

## Referenced Fields (owned elsewhere)

- **Resource ID** — [01-infrastructure/01-definitions.md#infra-resource-id](../01-infrastructure/01-definitions.md#infra-resource-id) — applies unchanged
- **Cost Center Tag** — [01-infrastructure/01-definitions.md#infra-cost-center-tag](../01-infrastructure/01-definitions.md#infra-cost-center-tag) — applies unchanged
- **Environment (lifecycle)** — [01-infrastructure/01-definitions.md#infra-environment-lifecycle](../01-infrastructure/01-definitions.md#infra-environment-lifecycle) — applies unchanged
- **Service Tier / Criticality** — [03-system-architecture/04-metadata-standards.md](../03-system-architecture/04-metadata-standards.md) — a Database/Warehouse typically inherits the criticality of the Service(s) that depend on it rather than being scored independently
- **Sensitivity Level, Contains PII** — [05-data-metadata/01-definitions.md#data-sensitivity-level](../05-data-metadata/01-definitions.md#data-sensitivity-level) — governs this domain's Risk Tiers (column 9) the same way it does for every other domain
- **Data Retention Period** — owned by Data/Metadata (`data-retention-period`) — this domain's Retention Policy Reference field (below) points to it rather than duplicating the value

## Field Registry (owned by this domain)

| Field | Definition | Source Term | Required/Optional (default) |
|---|---|---|---|
| **Database Engine Type** | The storage paradigm of a Database/Warehouse (relational, document, key-value, columnar, graph, vector). | `dp-database`, `dp-vector-database` | Required for Database, Data Warehouse, Vector Database entity types |
| **Table Format** | For a Data Lakehouse, the open table format in use (e.g. Delta Lake, Apache Iceberg, Apache Hudi — see 00-standards-alignment.md). | `dp-data-lakehouse` | Required for Data Lakehouse entity type; N/A elsewhere |
| **Retention Policy Reference** | Link to the Data Retention Period (owned by Data/Metadata) this entity enforces — this domain records that a policy is wired up, Data/Metadata owns the policy's actual value. | `data-retention-period` (cross-domain) | Required for Data Warehouse, Data Lake, Data Lakehouse entity types |
| **Replica Topology** | The Database Replica configuration (count, read/failover/geo-distribution purpose) for this entity, if any. | `dp-database-replica` | Optional for Database, Data Warehouse entity types |
| **Streaming Retention Window** | How long records remain available on a Stream/Topic before eviction. | `dp-stream-topic` | Required for Stream/Topic entity type |
| **Topic Partition Count** | The number of partitions a Stream/Topic is split across, for parallel consumption. | `dp-stream-topic` | Required for Stream/Topic entity type |
| **Schema Registry Reference** | Link to the record-schema contract governing a Stream/Topic's payload structure, if the topic carries structured records. | `dp-stream-topic` | Recommended for Stream/Topic entity type; N/A for unstructured/binary streams |
| **Embedding Model Reference** | Which model (name + version) produced the Vector Embeddings stored in a Vector Database, so similarity search isn't silently run across embeddings from two different, incompatible models. | `dp-vector-embedding` | Required for Vector Database entity type |
| **Orchestration Reference** | Link to the scheduling/orchestration definition that runs a Data Pipeline (format/convention owned by Workflow/Process, domain 7 — this field only requires that a reference exists). | (cross-domain, forward reference — Workflow/Process not yet built) | Required for Data Pipeline entity type |
| **ETL/ELT Mode** | Whether a Data Pipeline transforms before loading (ETL) or after (ELT). | `dp-etl-elt` | Required for Data Pipeline entity type |

## Entity Types & Field Applicability

| Entity Type | Required Fields | Optional/Recommended Fields |
|---|---|---|
| **Database** | Resource ID, Database Engine Type, Environment, Cost Center Tag, Sensitivity Level | Replica Topology, Service Tier/Criticality |
| **Data Warehouse / Data Lakehouse** | Resource ID, Retention Policy Reference, Environment, Cost Center Tag, Sensitivity Level | Table Format (Lakehouse only), Replica Topology |
| **Data Lake** | Resource ID, Retention Policy Reference, Environment, Cost Center Tag, Sensitivity Level | — |
| **Vector Database** | Resource ID, Database Engine Type, Embedding Model Reference, Environment, Cost Center Tag | Sensitivity Level (if source data is sensitive) |
| **Stream / Topic** | Resource ID, Streaming Retention Window, Topic Partition Count, Environment, Cost Center Tag | Schema Registry Reference |
| **Data Pipeline** | Resource ID, Orchestration Reference, ETL/ELT Mode, Environment, Cost Center Tag | — |

---

**Open items:**
- (Resolved 2026-09-22) **Orchestration Reference** now points to
  Workflow/Process's Orchestration Engine (`wf-orchestration-engine`) and
  DAG (`wf-dag`) — see `wf-dag --[requires]--> dp-data-pipeline`
  (07-workflow-process/03-ontologies.md) and that domain's Data Pipeline
  Orchestration Engine tooling category (10-tooling.md).
- **Embedding Model Reference** has no formal versioning-scheme
  convention yet (that belongs in this domain's own Conventions, column
  5) — this field only requires that a reference exists.
- Enforcement (mandatory-blocking vs. recommended) is deferred to
  Policies (column 6), same boundary every prior domain's Metadata
  Standards used.

**Quality bar check (00-framework/quality-bar.md):**
- [x] Simple — one field registry (plus referenced fields), one matrix
- [x] Modular — a field's definition changes once, applies everywhere referenced
- [x] Easy to update — add an entity type as one matrix row
- [x] Easy to maintain — fields reference Definitions terms where one exists, flagged explicitly where one doesn't
- [x] Easy to replace — tool-agnostic, ISO/IEC 11179-grounded, same standard as every prior domain
