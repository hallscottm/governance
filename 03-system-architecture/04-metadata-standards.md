# System Architecture Domain — Metadata Standards

Status: Draft — pending review
Ratified: No
Last updated: 2026-09-22
Provenance: see _qa/04-metadata-standards.qa.md
Built on: 01-definitions.md, 02-taxonomies.md, 03-ontologies.md

Same shape as Infrastructure's and Networking's Metadata Standards
(shared field registry + entity-type applicability matrix), reused
without re-asking since it's established as the standard approach for
this column.

## Referenced Fields (owned elsewhere)

- **Resource ID** — field defined in Infrastructure's Metadata Standards, drawing from [01-infrastructure/01-definitions.md#infra-resource-id](../01-infrastructure/01-definitions.md#infra-resource-id) — applies to services, databases, and other System Architecture entities unchanged
- **Cost Center Tag** — field defined in Infrastructure's Metadata Standards, drawing from [01-infrastructure/01-definitions.md#infra-cost-center-tag](../01-infrastructure/01-definitions.md#infra-cost-center-tag) — applies unchanged
- **Environment (lifecycle)** — field defined in Infrastructure's Metadata Standards, drawing from [01-infrastructure/01-definitions.md#infra-environment-lifecycle](../01-infrastructure/01-definitions.md#infra-environment-lifecycle) — a service/database/release belongs to an environment the same way a compute or network resource does

## Field Registry (owned by this domain)

| Field | Definition | Source Term | Required/Optional (default) |
|---|---|---|---|
| **Service Name** | The canonical, unique name identifying this service/application. | `sysarch-service`, `sysarch-application` | Required for Service, Application entity types |
| **Owning Team** | The team or individual accountable for this service/database/API. | (organizational, no single Definitions term) | Required — no default owner assumed |
| **Semantic Version** | The current version of this service/API/package, per SemVer. | `sysarch-semver` | Required for Service, API, Package entity types |
| **API Contract Reference** | Link to the current API Schema/contract document for this service's exposed API, if any. | `sysarch-api-schema`, `sysarch-api-contract` | Required for API entity type; N/A for internal-only services |
| **Database Engine** | The database engine/technology this entity is built on (e.g., relational, document, key-value — engine name is a Tooling-column concern, not named here). | `dp-database` (owned by Data Platform as of 2026-09-22; field kept in this shared registry since it's recorded alongside Service metadata) | Required for Database entity type |
| **Repository Reference** | Link to the source code repository for this service/application (format/convention owned by Workflow/Process, domain 7 — this field just requires that a reference exists). | (cross-domain, forward reference — Workflow/Process not yet built) | Required for Service, Application entity types |
| **Service Tier / Criticality** | A relative criticality classification for this service, used to prioritize incident response and inform Risk Tier determination (column 9). | (informs `sysarch-availability`, `sysarch-reliability`) | Required for Service, Database entity types |
| **Health Check Endpoint** | The endpoint (see `sysarch-endpoint`) used to programmatically verify this service is operational. | `sysarch-endpoint` | Recommended for Service entity type |
| **Dependency List** | The other services/databases this entity requires to function (see Ontology's `requires` relation type — this field is the per-instance record of that relationship). | `sysarch-service`, `dp-database` | Recommended for Service entity type |

## Entity Types & Field Applicability

| Entity Type | Required Fields | Optional Fields |
|---|---|---|
| **Service** | Resource ID, Service Name, Owning Team, Semantic Version, Environment, Repository Reference, Service Tier/Criticality, Cost Center Tag | API Contract Reference, Health Check Endpoint, Dependency List |
| **Application** | Resource ID, Service Name, Owning Team, Environment, Repository Reference, Cost Center Tag | Dependency List |
| **API** | Resource ID, Owning Team, Semantic Version, API Contract Reference, Environment | — |
| **Database** | Resource ID, Owning Team, Database Engine, Environment, Service Tier/Criticality, Cost Center Tag | Dependency List |

---

**Open items:**
- **Owning Team** has no owning Definitions term — it's an organizational
  concept, not a system-architecture one. Flagged, same boundary
  Infrastructure and Networking both hit with role/ownership fields;
  candidate for formal ownership once the Interface/Human domain (7) is
  drafted.
- **Repository Reference** and its naming/URL convention are a forward
  reference to Workflow/Process (domain 7, not yet built) — this field
  only asserts that a reference must exist, not its format. Revisit once
  that domain defines repository conventions.
- **Data Classification** (e.g., what sensitivity level a database holds)
  is explicitly out of scope here — owned by Data/Metadata (domain 5),
  not yet built. A Database entity type here does not include it.
- Enforcement (whether these fields are mandatory-blocking vs.
  recommended) is deferred to Policies (column 6), same boundary as
  Infrastructure's and Networking's Metadata Standards.
- Same framework-level gap already flagged in Infrastructure's and
  Networking's Metadata Standards: no field-level anchors, so no
  reverse-pointer mechanism at that granularity yet.

**Quality bar check (00-framework/quality-bar.md):**
- [x] Simple — one field registry (plus referenced fields), one matrix
- [x] Modular — a field's definition changes once, applies everywhere referenced
- [x] Easy to update — add an entity type as one matrix row
- [x] Easy to maintain — fields reference Definitions terms where one exists, flagged explicitly where one doesn't
- [x] Easy to replace — tool-agnostic, ISO/IEC 11179-grounded (same standard as Infrastructure and Networking)
