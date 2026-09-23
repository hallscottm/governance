# System Architecture Domain — Conventions

Status: Draft — pending review
Ratified: No
Last updated: 2026-09-22
Provenance: see _qa/05-conventions.qa.md
Built on: 01-definitions.md, 04-metadata-standards.md

Scope: naming conventions for services, applications, APIs, and
databases. Code/repository layout conventions remain reserved for
Workflow/Process (07-workflow-process/05-conventions.md, not yet
drafted), same boundary established in Infrastructure's and Networking's
Conventions.

**Design departure from Infrastructure/Networking naming:** those domains
embed `<env>` in the resource name because each environment has a
physically/logically distinct resource instance. A Service/Application is
a stable identity that exists conceptually the same way across
environments — `<env>` is tracked via the Environment metadata field
(04-metadata-standards.md), not the name. Confirmed explicitly as a real
decision, not a silent departure.

---

## Service / Application Naming Convention

**Pattern:** `<domain>-<function>[-<type>]`

| Segment | Values | Notes |
|---|---|---|
| `<domain>` | Free text, kebab-case, one word/compound preferred (e.g. `orders`, `billing`, `identity`) | Represents the business/technical domain the service belongs to — not tied to Owning Team (a team can own services in multiple domains) |
| `<function>` | Free text, kebab-case (e.g. `api`, `worker`, `processor`) | What the service does |
| `<type>` (optional) | `api`, `svc`, `worker`, `job`, `ui` | This domain's abbreviation registry, below — omit if `<function>` already makes the type obvious |

**Examples:** `orders-api`, `billing-invoice-worker`, `identity-auth-svc`

**Rules:** lowercase, hyphen-separated, globally unique across the
organization (Service Name is used as the join key across Metadata
Standards fields — Repository Reference, Dependency List — so collisions
break traceability).

## Database Naming Convention

**Moved to Data Platform** (04-data-platform/05-conventions.md) as of
2026-09-22, alongside the Database term itself (`dp-database`) — this
domain now only references a Database by its name (e.g., in Dependency
List, 04-metadata-standards.md), it doesn't own the naming pattern.

## API Versioning Convention

Major version is expressed in the API's path or contract identifier,
tied to Semantic Version (`sysarch-semver`) — a MAJOR version bump is the
trigger for a new API version identifier; MINOR/PATCH changes do not
change it.

**Pattern:** `/v<major>/...` (for REST APIs); RPC/other API styles use
an equivalent major-version identifier in their contract.

**Example:** `/v1/orders`, `/v2/orders`

## Entity-Type Abbreviation Registry

| Full Term | Abbreviation | Anchor |
|---|---|---|
| API | `api` | `sysarch-api` |
| Service (general) | `svc` | `sysarch-service` |
| Asynchronous worker/consumer | `worker` | `sysarch-asynchronous-integration` |
| Scheduled/batch job | `job` | (no dedicated Definitions term — scheduling itself is a Workflow/Process concern) |
| User-facing interface | `ui` | `sysarch-application` |

---

**Open items:**
- `<domain>` vocabulary is intentionally left free-text rather than a
  fixed enum — a controlled domain list would need organizational input
  (business domain boundaries) this framework doesn't have yet. Revisit
  if uncontrolled domain naming causes real drift once this is used.
- (Resolved 2026-09-22) `job` abbreviation's scheduling concept is now
  owned by Workflow/Process's Pipeline Trigger (`wf-pipeline-trigger`,
  specifically its schedule-based Trigger Type) — this abbreviation
  remains a System Architecture-local naming convenience, distinct from
  that domain's own Conventions.

**Quality bar check (00-framework/quality-bar.md):**
- [x] Simple — three small patterns (service, database, API version), one abbreviation table
- [x] Modular — Environment stays a metadata concern, not baked into the name, so a service's identity survives environment promotion unchanged
- [x] Easy to update — add an abbreviation as a new table row
- [x] Easy to maintain — Service Name uniqueness rule keeps it usable as a join key across the framework
- [x] Easy to replace — pattern is a convention, no tooling dependency
