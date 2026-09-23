# System Architecture Domain — Taxonomies

Status: Draft — pending review
Ratified: No
Last updated: 2026-09-22
Provenance: see _qa/02-taxonomies.qa.md
Built on: 01-definitions.md (54 owned terms, 10 migrated to Data Platform 2026-09-22)

Structure: strict single-parent tree, consistent with the standard set
during Infrastructure's Taxonomy column. Only terms owned by this domain
are classified here — the 9 referenced terms (Container, Environment
lifecycle from Infrastructure; TLS, Encryption in Transit, Load Balancer
from Networking; Database, Database Schema, Connection Pool, Schema
Migration from Data Platform) are not re-classified in this domain's tree.

---

## System Architecture
├── Architectural Patterns & Styles
│   ├── Monolithic Architecture (#sysarch-monolithic-architecture)
│   ├── Microservices Architecture (#sysarch-microservices-architecture)
│   ├── Service-Oriented Architecture (SOA) (#sysarch-soa)
│   ├── Event-Driven Architecture (#sysarch-event-driven-architecture)
│   ├── N-Tier Architecture (#sysarch-n-tier-architecture)
│   └── Serverless Architecture (#sysarch-serverless-architecture)
│
├── Application Building Blocks
│   ├── Application (#sysarch-application)
│   ├── Service (#sysarch-service)
│   ├── Component (#sysarch-component)
│   ├── Module (#sysarch-module)
│   ├── Library (#sysarch-library)
│   ├── Package (#sysarch-package)
│   └── Build Artifact (#sysarch-build-artifact)
│
├── Interfaces & APIs
│   ├── API (#sysarch-api)
│   ├── Endpoint (#sysarch-endpoint)
│   ├── API Contract (#sysarch-api-contract)
│   ├── API Schema (#sysarch-api-schema)
│   ├── REST (#sysarch-rest)
│   ├── RPC (#sysarch-rpc)
│   ├── Webhook (#sysarch-webhook)
│   └── SDK (#sysarch-sdk)
│
├── Integration & Messaging
│   ├── Message Queue (#sysarch-message-queue)
│   ├── Event Bus (#sysarch-event-bus)
│   ├── Publish/Subscribe (Pub/Sub) (#sysarch-pubsub)
│   ├── Synchronous Integration (#sysarch-synchronous-integration)
│   ├── Asynchronous Integration (#sysarch-asynchronous-integration)
│   └── Idempotency (#sysarch-idempotency)
│
├── State & Caching
│   ├── Stateless Service (#sysarch-stateless-service)
│   ├── Stateful Service (#sysarch-stateful-service)
│   ├── Session (#sysarch-session)
│   ├── Cache (#sysarch-cache)
│   └── Cache Invalidation (#sysarch-cache-invalidation)
│
├── Versioning & Release Management
│   ├── Semantic Version (SemVer) (#sysarch-semver)
│   ├── Build (#sysarch-build)
│   ├── Release (#sysarch-release)
│   ├── Container Image (#sysarch-container-image)
│   ├── API Deprecation (#sysarch-api-deprecation)
│   └── Backward Compatibility (#sysarch-backward-compatibility)
│
├── Application Security
│   ├── Authentication (Application-Domain) (#sysarch-authentication)
│   ├── Authorization (Application-Domain) (#sysarch-authorization)
│   ├── Application Secret (#sysarch-application-secret)
│   ├── Input Validation (#sysarch-input-validation)
│   └── Audit Logging (Application-Domain) (#sysarch-audit-logging)
│
├── Quality Attributes (ISO/IEC 25010)
│   ├── Reliability (Application-Domain) (#sysarch-reliability)
│   ├── Availability (Application-Domain) (#sysarch-availability)
│   ├── Scalability (Application-Domain) (#sysarch-scalability)
│   ├── Maintainability (#sysarch-maintainability)
│   ├── Performance Efficiency (#sysarch-performance-efficiency)
│   └── Resilience (#sysarch-resilience)
│
└── Testing & Quality Gates
    ├── Unit Test (#sysarch-unit-test)
    ├── Integration Test (#sysarch-integration-test)
    ├── Test Coverage (#sysarch-test-coverage)
    ├── Code Review (#sysarch-code-review)
    └── Technical Debt (#sysarch-technical-debt)

---

**Quality bar check (00-framework/quality-bar.md):**
- [x] Simple — one tree, mirrors the 10 Definitions subdomains 1:1, no
      independent classification scheme to maintain
- [x] Modular — referenced (not owned) terms excluded, so this tree
      changes independently of Infrastructure's and Networking's
- [x] Easy to update — a new term appends under its existing subdomain,
      or a new subdomain appends as a new top-level branch
- [x] Easy to maintain — single-parent, no cross-branch duplication to
      keep in sync
- [x] Easy to replace — plain tree structure, no tooling dependency
