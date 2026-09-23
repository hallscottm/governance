# System Architecture Layer — Ontologies

Status: Draft — pending review
Ratified: No
Last updated: 2026-09-22
Provenance: see _qa/03-ontologies.qa.md
Relation vocabulary: 00-framework/relation-types.md
Built on: 01-definitions.md, 02-taxonomies.md

Relationships may reference anchors owned by other layers (Infrastructure,
Networking) where a genuine cross-layer relationship exists — this is
distinct from the "Referenced Terms" mechanism in Definitions, which is
about term ownership, not relationships between terms. Per the
reverse-pointer rule in 00-framework/relation-types.md, every cross-layer
relationship below has a matching reverse pointer added to the target
layer's ontology file.

---

## Architectural Patterns & Styles

- `sysarch-monolithic-architecture` --[contains]--> `sysarch-component`
  Rationale: a monolith bundles all of an application's components into one deployable unit.
- `sysarch-microservices-architecture` --[contains]--> `sysarch-service`
  Rationale: microservices architecture is composed of independently deployable services.
- `sysarch-soa` --[contains]--> `sysarch-service`
  Rationale: SOA is likewise composed of discrete services, coordinated by shared middleware.
- `sysarch-n-tier-architecture` --[contains]--> `sysarch-component`
  Rationale: N-tier architecture organizes an application into layered components.
- `sysarch-event-driven-architecture` --[requires]--> `sysarch-event-bus`
  Rationale: event-driven architecture depends on a mechanism to distribute events between producers and consumers.
- `sysarch-serverless-architecture` --[runs-on]--> `infra-compute-unit`
  Rationale: cross-layer — a serverless function still executes on underlying compute, even though the caller doesn't manage it directly.

## Application Building Blocks

- `sysarch-application` --[contains]--> `sysarch-service`
  Rationale: an application is composed of one or more services (or components, for simpler applications).
- `sysarch-service` --[contains]--> `sysarch-component`
  Rationale: a service is internally organized into components.
- `sysarch-component` --[contains]--> `sysarch-module`
  Rationale: a component is composed of code modules.
- `sysarch-module` --[requires]--> `sysarch-library`
  Rationale: modules commonly depend on external libraries for shared functionality.
- `sysarch-package` --[contains]--> `sysarch-library`
  Rationale: a package is a distributable bundle of a library (or set of modules).
- `sysarch-build` --[produces]--> `sysarch-build-artifact`
  Rationale: a build process produces a build artifact as its output.
- `sysarch-service` --[runs-on]--> `infra-container`
  Rationale: cross-layer — a service instance commonly runs inside a container (the isolated runtime), though not exclusively.

## Interfaces & APIs

- `sysarch-api` --[contains]--> `sysarch-endpoint`
  Rationale: an API is composed of one or more endpoints.
- `sysarch-api-contract` --[constrains]--> `sysarch-api`
  Rationale: the contract defines and limits what the API may do without a version change.
- `sysarch-api-schema` --[measured-by]--> `sysarch-api-contract`
  Rationale: a machine-readable API schema is how an API contract's shape is formally captured and checked.
- `sysarch-rest` --[constrains]--> `sysarch-api`
  Rationale: REST is a style that constrains how an API's resources, methods, and URLs are designed.
- `sysarch-rpc` --[constrains]--> `sysarch-api`
  Rationale: RPC is an alternative style constraining API design toward procedure-call semantics.
- `sysarch-webhook` --[requires]--> `sysarch-endpoint`
  Rationale: a webhook delivers events to a consumer-provided endpoint.
- `sysarch-sdk` --[requires]--> `sysarch-api-contract`
  Rationale: an SDK is built against a specific API contract and breaks if that contract changes incompatibly.

## Databases & Storage

- `sysarch-database` --[contains]--> `sysarch-database-schema`
  Rationale: a database's structure is defined by its schema.
- `sysarch-database-schema` --[contains]--> `sysarch-table`
  Rationale: a schema is composed of table definitions.
- `sysarch-table` --[contains]--> `sysarch-index`
  Rationale: an index is defined on and belongs to a specific table.
- `sysarch-database` --[requires]--> `sysarch-acid`
  Rationale: a (relational) database's transactional guarantees depend on ACID properties.
- `sysarch-transaction` --[requires]--> `sysarch-acid`
  Rationale: a transaction is only meaningful as a unit of work governed by ACID guarantees.
- `sysarch-database-replica` --[requires]--> `sysarch-database`
  Rationale: a replica exists only in relation to a primary database it mirrors.
- `sysarch-database` --[scales-via]--> `sysarch-partitioning-sharding`
  Rationale: partitioning/sharding is a primary mechanism for scaling a database beyond a single instance's capacity.
- `sysarch-connection-pool` --[requires]--> `sysarch-database`
  Rationale: a connection pool exists to manage reusable connections to a specific database.
- `sysarch-schema-migration` --[produces]--> `sysarch-database-schema`
  Rationale: applying a migration produces a new version of the database schema.
- `sysarch-database` --[runs-on]--> `infra-compute-unit`
  Rationale: cross-layer — a database engine executes on underlying compute, whether self-managed or a managed service.
- `sysarch-database` --[requires]--> `infra-block-storage`
  Rationale: cross-layer — relational and most transactional databases require durable block storage for their data files.

## Integration & Messaging

- `sysarch-pubsub` --[requires]--> `sysarch-event-bus`
  Rationale: the publish/subscribe pattern is typically implemented via an event bus distributing published events to subscribers.
- `sysarch-asynchronous-integration` --[requires]--> `sysarch-message-queue`
  Rationale: asynchronous integration commonly relies on a message queue to decouple producer and consumer timing.
- `sysarch-asynchronous-integration` --[requires]--> `sysarch-idempotency`
  Rationale: safe retries under asynchronous, at-least-once delivery require idempotent message handling.
- `sysarch-webhook` --[requires]--> `sysarch-asynchronous-integration`
  Rationale: a webhook is a push-based, asynchronous integration mechanism.

## State & Caching

- `sysarch-stateful-service` --[requires]--> `sysarch-session`
  Rationale: a stateful service retains state associated with a session.
- `sysarch-cache` --[requires]--> `sysarch-cache-invalidation`
  Rationale: a cache without an invalidation strategy will serve stale data indefinitely.
- `sysarch-stateless-service` --[scales-via]--> `infra-horizontal-scaling`
  Rationale: cross-layer — statelessness is what makes a service safely scalable by adding interchangeable instances (Infrastructure's horizontal scaling mechanism).

## Versioning & Release Management

- `sysarch-release` --[requires]--> `sysarch-build-artifact`
  Rationale: a release designates a specific build artifact for deployment.
- `sysarch-semver` --[constrains]--> `sysarch-release`
  Rationale: semantic versioning rules constrain how a release's version number may change relative to the prior one.
- `sysarch-container-image` --[produces]--> `infra-container`
  Rationale: cross-layer — running a container image is what instantiates a container (the runtime unit).
- `sysarch-api-deprecation` --[requires]--> `sysarch-backward-compatibility`
  Rationale: a deprecation process is expected to preserve backward compatibility for the announced transition period before removal.
- `sysarch-release` --[has-lifecycle-state]--> `infra-environment-lifecycle`
  Rationale: cross-layer — a release progresses through lifecycle environments (Development, Staging/QA, Production) as it is promoted.

## Application Security

- `sysarch-authorization` --[requires]--> `sysarch-authentication`
  Rationale: a caller must be authenticated before an authorization decision about them is meaningful.
- `sysarch-input-validation` --[constrains]--> `sysarch-api`
  Rationale: input validation rules constrain what data an API will accept as well-formed.
- `sysarch-service` --[requires]--> `net-encryption-in-transit`
  Rationale: cross-layer — service-to-service and client-service calls require encryption in transit to protect data on the wire.

## Quality Attributes (ISO/IEC 25010)

- `sysarch-resilience` --[requires]--> `infra-redundancy`
  Rationale: cross-layer — an application's resilience to failure depends in part on redundancy at the infrastructure layer beneath it.
- `sysarch-scalability` --[scales-via]--> `infra-horizontal-scaling`
  Rationale: cross-layer — application-layer scalability is realized through Infrastructure's horizontal (and vertical) scaling mechanisms.
- `infra-availability-tier` --[constrains]--> `sysarch-availability`
  Rationale: cross-layer — the hosting facility's availability tier design target sets an upper bound on the application's achievable measured availability.

## Testing & Quality Gates

- `sysarch-integration-test` --[requires]--> `sysarch-service`
  Rationale: integration tests exercise multiple services (or a service and a database) working together, not a single unit in isolation.
- `sysarch-test-coverage` --[measured-by]--> `sysarch-unit-test`
  Rationale: test coverage is measured against the code exercised by the test suite, principally unit tests.
- `sysarch-code-review` --[constrains]--> `sysarch-technical-debt`
  Rationale: code review is a primary control that limits the rate at which technical debt accumulates.

---

## Cross-Layer References (relationships pointing into this layer)

Per 00-framework/relation-types.md's reverse-pointer rule, added once
Data/Metadata's ontology created relationships into this layer.

- `sysarch-database`
  Referenced by (cross-layer relationships):
  - Data/Metadata: `data-custodian --[requires]--> sysarch-database`
  - Data/Metadata: `data-quality-rule --[constrains]--> sysarch-database`
  - Data/Metadata: `data-dataset --[located-in]--> sysarch-database`
- `sysarch-database-schema`
  Referenced by (cross-layer relationships):
  - Data/Metadata: `data-technical-metadata --[requires]--> sysarch-database-schema`
  - Data/Metadata: `data-dictionary --[requires]--> sysarch-database-schema`
  - Data/Metadata: `data-logical-model --[produces]--> sysarch-database-schema`

---

**Open items:**
- `sysarch-api-schema --[measured-by]--> sysarch-api-contract` reads
  slightly unusual (a schema measuring a contract) — kept because the
  9-type vocabulary has no better fit for "formal artifact capturing an
  informal agreement"; flagged for reconsideration if a 10th relation
  type is ever added.
- `sysarch-database-replica` and `infra-replication-factor` are related
  concepts (database-level replication topology vs. storage-level
  redundancy) but no direct relationship was drawn — left unconnected
  per the "not every term needs a relationship" scope note, same as
  Networking's Transit Gateway/Private Link case.

**Quality bar check (00-framework/quality-bar.md):**
- [x] Simple — 50 relationships, grouped by subdomain, no forced edges
- [x] Modular — each relationship stands alone; cross-layer edges are
      clearly marked and reverse-pointed rather than silently assumed
- [x] Easy to update — anchor-ID based, survives renames
- [x] Easy to maintain — grouped by subdomain, matches Definitions/Taxonomy
- [x] Easy to replace — relation-type vocabulary shared across all layers, no duplication
