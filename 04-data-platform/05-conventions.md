# Data Platform Domain — Conventions

Status: Draft — pending review
Ratified: No
Last updated: 2026-09-22
Provenance: see _qa/05-conventions.qa.md
Built on: 01-definitions.md, 04-metadata-standards.md

Scope: naming conventions for databases, warehouses/lakehouses, streaming
topics, and data pipelines. The Database Naming Convention below is
migrated verbatim from 03-system-architecture/05-conventions.md,
2026-09-22, alongside the `dp-database` term itself — System Architecture
now holds a reference stub instead (same migration pattern used for
Definitions/Taxonomies/Ontologies).

---

## Database Naming Convention

**Pattern:** `<service_name>_<purpose>` (snake_case, not kebab-case)

Databases commonly restrict or discourage hyphens in identifiers
depending on engine — snake_case is used instead of the kebab-case
pattern used elsewhere in this framework, an explicit, engine-driven
exception (unchanged from its original System Architecture wording).

**Example:** `orders_primary`, `billing_reporting`

## Data Warehouse / Lakehouse Layer Naming Convention

**Pattern:** `<layer>_<domain>_<entity>` where `<layer>` follows the
common medallion pattern (`bronze` — raw/landed, `silver` — cleaned/
conformed, `gold` — business-level/aggregated) — noted as common industry
practice, not a formal Definitions term of its own (same treatment given
to `<domain>` in System Architecture's Service naming convention).

**Example:** `bronze_orders_raw`, `silver_orders_cleaned`, `gold_orders_daily_summary`

**Rule:** a `gold`-layer object is the natural candidate to be exposed
through the Semantic Layer (`dp-semantic-layer`) rather than queried
directly by a downstream report — this convention doesn't enforce that
(DPPOL-5, 06-policies.md, does), it just makes the intent legible in the
name.

## Streaming Topic Naming Convention

**Pattern:** `<domain>.<entity>.<event-type>` (dot-separated, the common
Kafka-ecosystem convention — see 00-standards-alignment.md's note on the
Kafka wire protocol).

**Example:** `orders.order.created`, `billing.invoice.paid`

## Table Naming Convention (within a Database Schema)

**Pattern:** `<entity>` or `<entity>_<qualifier>`, snake_case, singular
or plural per team convention — deliberately not prescribed further here
(a stricter rule would need org-specific input this generalized framework
doesn't have, same reasoning System Architecture used for its
free-text `<domain>` segment).

**Example:** `orders`, `order_line_items`

## Embedding Model Reference Convention

**Pattern:** `<model_name>@<model_version>` — matches the field
introduced in 04-metadata-standards.md's Embedding Model Reference,
giving it one canonical string format rather than leaving it free text.

**Example:** `text-embedding-3-large@v1`

---

**Open items:**
- Medallion layer naming (`bronze`/`silver`/`gold`) is noted as common
  industry practice, not every Data Lakehouse implementation uses this
  exact vocabulary — flagged as a convention an adopting organization may
  substitute, same "illustrative, not prescriptive" posture used
  elsewhere in this framework (e.g. cross-cutting/roles-and-departments'
  Department groupings).
- Table naming's `<qualifier>` segment is intentionally unconstrained,
  same open item already flagged for System Architecture's `<domain>`
  segment.

**Quality bar check (00-framework/quality-bar.md):**
- [x] Simple — five small patterns, no nested rule logic
- [x] Modular — each pattern (database, warehouse layer, topic, table, embedding reference) stands alone
- [x] Easy to update — a new entity type adds one more pattern without touching existing ones
- [x] Easy to maintain — Database pattern kept byte-for-byte identical through its migration, no silent meaning drift
- [x] Easy to replace — no tooling dependency; medallion terminology flagged as substitutable
