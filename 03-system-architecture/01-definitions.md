# System Architecture Domain — Definitions

Status: Draft — pending review
Ratified: No
Last updated: 2026-09-22

Scope: applications and services built on the compute/network substrate.
Excludes physical/virtual compute (Infrastructure, domain 1) and
connectivity (Networking, domain 2). Excludes where data physically lives
(Data Platform, domain 4 — moved here 2026-09-22) and the *meaning* of data
(Data/Metadata, domain 5), and excludes how software is built/deployed via
pipelines (Workflow/Process, domain 7) — this domain defines what runs and
how it's structured, not where its data is stored, how it gets there, or
what that data means.

Anchor convention: `sysarch-<term-slug>`. See
00-framework/term-linking-convention.md for the DRY/anti-drift rules this
file follows.

---

## Referenced Terms (owned elsewhere)

Terms this domain uses but does not own. Do not redefine here — link to
the source.

- **Container** — see [01-infrastructure/01-definitions.md#infra-container](../01-infrastructure/01-definitions.md#infra-container)
- **Environment (lifecycle)** — see [01-infrastructure/01-definitions.md#infra-environment-lifecycle](../01-infrastructure/01-definitions.md#infra-environment-lifecycle)
- **TLS** — see [02-networking/01-definitions.md#net-tls](../02-networking/01-definitions.md#net-tls)
- **Encryption in Transit** — see [02-networking/01-definitions.md#net-encryption-in-transit](../02-networking/01-definitions.md#net-encryption-in-transit)
- **Load Balancer** — see [02-networking/01-definitions.md#net-load-balancer](../02-networking/01-definitions.md#net-load-balancer)
- **Database** — owned by Data Platform (moved here 2026-09-22) →
  [04-data-platform/01-definitions.md#dp-database](../04-data-platform/01-definitions.md#dp-database)
- **Database Schema** — owned by Data Platform (moved here 2026-09-22) →
  [04-data-platform/01-definitions.md#dp-database-schema](../04-data-platform/01-definitions.md#dp-database-schema)
- **Connection Pool** — owned by Data Platform (moved here 2026-09-22) →
  [04-data-platform/01-definitions.md#dp-connection-pool](../04-data-platform/01-definitions.md#dp-connection-pool)
- **Schema Migration** — owned by Data Platform (moved here 2026-09-22) →
  [04-data-platform/01-definitions.md#dp-schema-migration](../04-data-platform/01-definitions.md#dp-schema-migration)

---

## Architectural Patterns & Styles

### Monolithic Architecture {#sysarch-monolithic-architecture}
A single deployable unit containing all of an application's functionality.
Source: Industry-standard architectural pattern (contrasted in ISO/IEC/IEEE
42010 viewpoint terms; not itself defined by a standards body).

### Microservices Architecture {#sysarch-microservices-architecture}
An architectural style structuring an application as a collection of small,
independently deployable services, each owning its own data and
communicating over well-defined interfaces (see API Contract).
Source: Industry-standard architectural pattern.

### Service-Oriented Architecture (SOA) {#sysarch-soa}
An architectural style where functionality is provided as discrete,
reusable services, typically coordinated by a broader integration domain.
Predecessor/relative of Microservices Architecture, distinguished by
heavier shared middleware. Source: Industry-standard architectural pattern.

### Event-Driven Architecture {#sysarch-event-driven-architecture}
An architectural style where components communicate by producing and
consuming events, typically via a Message Queue or Event Bus, rather than
direct synchronous calls. Source: Industry-standard architectural pattern.

### N-Tier Architecture {#sysarch-n-tier-architecture}
An architectural style separating an application into logical domains
(e.g., presentation, application/business logic, data), each of which may
be deployed independently. Source: Industry-standard architectural pattern.

### Serverless Architecture (Function as a Service) {#sysarch-serverless-architecture}
An architectural style where individual functions are deployed and
executed without the caller managing the underlying Compute Unit directly
— the Infrastructure domain's autoscaling/provisioning concepts apply, but
this domain's concern is the function as the unit of deployment. Source:
Industry-standard architectural pattern; underlying compute concepts per
01-infrastructure/01-definitions.md.

---

## Application Building Blocks

### Application {#sysarch-application}
A complete, user- or system-facing piece of software composed of one or
more Services or Components, addressing a defined business or technical
purpose. Source: ISO/IEC/IEEE 42010 (general systems/software engineering
usage).

### Service {#sysarch-service}
An independently deployable unit of software that exposes functionality
through one or more defined interfaces (see API). The primary unit of
decomposition in Microservices and SOA. Source: ISO/IEC/IEEE 42010;
industry usage.

### Component {#sysarch-component}
An architectural building block with a well-defined interface and
boundary, smaller in scope than a Service and not necessarily
independently deployable. Source: ISO/IEC/IEEE 42010.

### Module {#sysarch-module}
A unit of code organization within a Component, Service, or Application,
typically compiled or imported as a unit. Source: General software
engineering usage.

### Library {#sysarch-library}
Reusable code packaged for inclusion in other software, not independently
deployable or runnable on its own. Source: General software engineering
usage.

### Package {#sysarch-package}
A distributable, versioned bundle of code (a Library, or a set of
Modules), typically published to and retrieved from a package repository.
Source: General software engineering usage; versioning per Semantic
Version below.

### Build Artifact {#sysarch-build-artifact}
The output of a build process — a compiled binary, container image, or
packaged bundle — that is versioned and becomes the deployable unit for a
Service or Application. Source: General software engineering usage.

---

## Interfaces & APIs

### API (Application Programming Interface) {#sysarch-api}
A defined contract through which one piece of software requests
functionality or data from another. Source: General software engineering
usage; described formally via OpenAPI Specification for REST APIs.

### Endpoint {#sysarch-endpoint}
A specific, addressable location (e.g., a URL and method) at which an API
operation is invoked. Source: OpenAPI Specification.

### API Contract {#sysarch-api-contract}
The formal or de facto agreement describing an API's inputs, outputs,
behavior, and error conditions — what a consumer can rely on not changing
without a version change. Source: General software engineering usage;
formalized via API Schema (below) where machine-readable.

### API Schema {#sysarch-api-schema}
A machine-readable description of an API's Endpoints, request/response
structures, and data types (e.g., an OpenAPI document). Distinct from
Database Schema (below) — same word, different owner-scoped meaning; see
00-framework/term-linking-convention.md. Source: OpenAPI Specification.

### REST (Representational State Transfer) {#sysarch-rest}
An architectural style for APIs built on stateless requests, standard HTTP
methods, and resource-oriented URLs. Source: General software engineering
usage; commonly described via OpenAPI Specification.

### RPC (Remote Procedure Call) {#sysarch-rpc}
An API style where a client invokes a procedure on a remote Service as if
it were a local function call, typically with a strongly-typed contract
(e.g., gRPC). Source: General software engineering usage.

### Webhook {#sysarch-webhook}
An HTTP callback: a Service-initiated request to a consumer-provided
Endpoint, used to push events rather than requiring the consumer to poll.
Source: General software engineering usage.

### SDK (Software Development Kit) {#sysarch-sdk}
A packaged set of tools, Libraries, and documentation that simplifies
integrating with a given API or platform. Source: General software
engineering usage.

---

## Integration & Messaging

### Message Queue {#sysarch-message-queue}
A component that holds messages produced by one Service until they are
consumed by another, enabling Asynchronous Integration (below). Source:
General software engineering usage; underlies Event-Driven Architecture.

### Event Bus {#sysarch-event-bus}
A component that distributes published events to multiple subscribing
Services (see Publish/Subscribe), as distinct from a Message Queue's
typically single-consumer model. Source: General software engineering
usage.

### Publish/Subscribe (Pub/Sub) {#sysarch-pubsub}
A messaging pattern where producers publish events without knowledge of
consumers, and consumers subscribe to the event types they care about.
Source: General software engineering usage.

### Synchronous Integration {#sysarch-synchronous-integration}
A Service-to-Service interaction where the caller blocks and waits for a
response before proceeding (e.g., a REST call). Source: General software
engineering usage.

### Asynchronous Integration {#sysarch-asynchronous-integration}
A Service-to-Service interaction where the caller does not block on a
response, typically via a Message Queue, Event Bus, or Webhook. Source:
General software engineering usage.

### Idempotency {#sysarch-idempotency}
A property of an operation (an API call, a message handler) whereby
performing it multiple times has the same effect as performing it once —
critical for safe retries in Asynchronous Integration. Source: General
software engineering usage; referenced in OpenAPI Specification guidance.

---

## State & Caching

### Stateless Service {#sysarch-stateless-service}
A Service that retains no client-specific data between requests, enabling
any instance to handle any request (supports Infrastructure's Horizontal
Scaling). Source: General software engineering usage.

### Stateful Service {#sysarch-stateful-service}
A Service that retains client- or workflow-specific data between
requests, typically requiring session affinity or external state storage.
Source: General software engineering usage.

### Session {#sysarch-session}
A period of interaction between a client and a Service during which
state is retained, identified by a session token or identifier. Source:
General software engineering usage; security handling per OWASP ASVS.

### Cache {#sysarch-cache}
A temporary store of previously computed or retrieved data, kept to
reduce latency and load on a Database or upstream Service. Source:
General software engineering usage.

### Cache Invalidation {#sysarch-cache-invalidation}
The process of removing or refreshing stale entries in a Cache so it does
not serve outdated data. Source: General software engineering usage.

---

## Versioning & Release Management

### Semantic Version (SemVer) {#sysarch-semver}
A three-part version number (MAJOR.MINOR.PATCH) where increments signal
the nature of change — MAJOR for breaking changes, MINOR for
backward-compatible additions, PATCH for backward-compatible fixes.
Source: Semantic Versioning 2.0.0 (semver.org).

### Build {#sysarch-build}
A single, reproducible compilation of source code into a Build Artifact,
identified by a unique build identifier. Source: General software
engineering usage.

### Release {#sysarch-release}
A Build Artifact (or set of them) that has been designated for
deployment to one or more Environments, tagged with a Semantic Version.
Source: General software engineering usage.

### Container Image {#sysarch-container-image}
A packaged, versioned Build Artifact containing an application and its
runtime dependencies, deployed as one or more instances of Infrastructure's
Container. Distinguishes the deployable artifact (owned here) from the
running isolation unit (owned by Infrastructure). Source: General
software engineering usage; NIST SP 800-190.

### API Deprecation {#sysarch-api-deprecation}
The formal, time-bounded process of retiring an API version or Endpoint,
communicated to consumers ahead of removal. Source: General API
governance practice; informed by OpenAPI Specification versioning
guidance.

### Backward Compatibility {#sysarch-backward-compatibility}
The property of a new Release or API version continuing to work correctly
for consumers built against a prior version, without requiring changes on
their part. Source: Semantic Versioning 2.0.0; general API governance
practice.

---

## Application Security

### Authentication (Application-Domain) {#sysarch-authentication}
The process by which a Service verifies the identity of a caller
(user or another Service). Distinct from Networking's Network Identity,
which authenticates at the connection/device level rather than the
application/user level. Source: OWASP ASVS.

### Authorization (Application-Domain) {#sysarch-authorization}
The process by which a Service determines what an authenticated caller
is permitted to do. Source: OWASP ASVS.

### Application Secret {#sysarch-application-secret}
Sensitive configuration data (credentials, API keys, signing keys)
required by a Service at runtime, requiring managed storage and rotation
rather than embedding in source code or Build Artifacts. Source: OWASP
ASVS; NIST SP 800-53 (SC family).

### Input Validation {#sysarch-input-validation}
The practice of checking that data received by a Service (via an API,
form, or message) conforms to expected type, format, and range before it
is processed, as a primary defense against injection and malformed-data
vulnerabilities. Source: OWASP ASVS; OWASP Top 10.

### Audit Logging (Application-Domain) {#sysarch-audit-logging}
Recording security-relevant application events (authentication attempts,
authorization decisions, data access) in a form suitable for later
review. Source: OWASP ASVS; NIST SP 800-53 (AU family, referenced at the
application layer).

---

## Quality Attributes (ISO/IEC 25010)

### Reliability (Application-Domain) {#sysarch-reliability}
The degree to which a Service performs its specified functions correctly
under stated conditions for a specified period. Source: ISO/IEC 25010.

### Availability (Application-Domain) {#sysarch-availability}
The proportion of time a Service is operational and able to serve
requests, distinct from Infrastructure's Availability Tier, which
describes the facility/hosting environment's design target rather than
the running Service's measured uptime. Source: ISO/IEC 25010.

### Scalability (Application-Domain) {#sysarch-scalability}
A Service's ability to handle increased load by taking advantage of
added resources — realized via Infrastructure's Vertical/Horizontal
Scaling, but a property assessed at this domain against Service design
(e.g., whether it is Stateless). Source: ISO/IEC 25010.

### Maintainability {#sysarch-maintainability}
The degree to which a Service or Application can be modified — corrected,
improved, or adapted — efficiently and without introducing defects.
Source: ISO/IEC 25010.

### Performance Efficiency {#sysarch-performance-efficiency}
The degree to which a Service's resource usage (time, compute, memory)
is appropriate to the conditions under which it operates. Source: ISO/IEC
25010.

### Resilience {#sysarch-resilience}
A Service's ability to continue operating, or degrade gracefully, in the
presence of failures in its dependencies (a Database, another Service, or
the underlying Infrastructure). Source: ISO/IEC 25010 (as a facet of
Reliability); general software engineering usage.

---

## Testing & Quality Gates

### Unit Test {#sysarch-unit-test}
An automated test that verifies the behavior of a single Component or
Module in isolation. Source: General software engineering usage.

### Integration Test {#sysarch-integration-test}
An automated test that verifies the behavior of multiple Components,
Services, or a Service and a Database working together. Source: General
software engineering usage.

### Test Coverage {#sysarch-test-coverage}
A measure of the proportion of source code, branches, or requirements
exercised by a test suite. Source: General software engineering usage.

### Code Review {#sysarch-code-review}
A structured examination of proposed code changes by someone other than
the author, before the change is merged or released. Source: General
software engineering usage.

### Technical Debt {#sysarch-technical-debt}
The implied future cost of choosing an expedient design or implementation
now, in place of a better approach that would take longer. Source:
General software engineering usage.

---

**Quality bar check (00-framework/quality-bar.md):**
- [x] Simple — terms grouped into 10 subdomains, each independently
      scannable
- [x] Modular — cross-domain references (Container, Environment, TLS,
      Encryption in Transit, Load Balancer) are links, not restatements;
      this domain can be updated without touching Infrastructure or
      Networking
- [x] Easy to update — new terms append to the relevant subdomain
      section without renumbering
- [x] Easy to maintain — anchors are stable slugs (`sysarch-<term>`),
      safe to link to from Taxonomies/Ontologies/later columns
- [x] Easy to replace — no term depends on a specific vendor or product
