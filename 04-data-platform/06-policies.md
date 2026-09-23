# Data Platform Domain — Policies

Status: Draft — pending review
Ratified: No
Last updated: 2026-09-22
Provenance: see _qa/06-policies.qa.md
Built on: 01-definitions.md, 04-metadata-standards.md, cross-cutting/policies.md, cross-cutting/risk-tiers.md

## Extends Cross-Cutting Policies

This domain's resources are subject to CCP-1 (Metadata Completeness),
CCP-2 (Cost Attribution), and CCP-3 (Production Provisioning Approval)
from cross-cutting/policies.md, applied to this domain's own entity types
(04-metadata-standards.md). Not restated here.

## Domain-Specific Policies

### DPPOL-1 — Database Schema Migration Review (Scaled by Risk Tier) (moved from System Architecture's SAPOL-2, 2026-09-22)
**Rule:** A Schema Migration (`dp-schema-migration`) targeting a
Production database requires review before being applied, scaled by the
database entity's Risk Tier (09-risk-tiers.md, extending
cross-cutting/risk-tiers.md):
- **Low:** peer review sufficient.
- **Moderate:** peer review + Data Engineer sign-off.
- **High:** peer review + Data Engineer sign-off + Data Architect
  sign-off + a documented rollback plan on file before the migration is
  applied.
**Applies to:** Production environment, Database entity type.
**Enforcement:** Approval gate, scaled as above. Who qualifies as
reviewer is deferred to this domain's Access Rules (column 7).
**Rationale:** Wording unchanged from its original System Architecture
form except the approving role — Owning Team Lead (a System
Architecture/Service-scoped role) is replaced by Data Engineer/Data
Architect (this domain's own co-owning roles, see cross-cutting/
roles-and-departments/00-qa.md Q7), since this is now recognized as a
Data Platform-owned resource, not a Service-owned one.

### DPPOL-2 — Streaming Retention Window Required
**Rule:** A Stream/Topic cannot be provisioned without a declared
Streaming Retention Window (04-metadata-standards.md).
**Applies to:** All environments, Stream/Topic entity type.
**Enforcement:** Hard block.
**Rationale:** Explicitly chosen as a hard block, same treatment CCP-1
gives missing Required metadata generally — an unbounded-retention topic
is a cost and compliance risk (indefinitely retained data with no
Data/Metadata retention policy wired to it) that's cheap to prevent at
provisioning time and expensive to discover later.

### DPPOL-3 — Embedding Model Reference Required (Vector Database)
**Rule:** A Vector Database cannot be provisioned, and a batch of Vector
Embeddings cannot be written to one, without a declared Embedding Model
Reference (04-metadata-standards.md).
**Applies to:** All environments, Vector Database entity type.
**Enforcement:** Hard block.
**Rationale:** Explicitly chosen as a hard block — mixing embeddings
from two different models in the same similarity-search index produces
silently wrong results (nearest-neighbor distances aren't comparable
across models), a correctness failure rather than a mere governance gap,
which is why this is stricter than a Recommended field.

### DPPOL-4 — Lakehouse Table Format Declared, Changes Require Migration Plan
**Rule:** A Data Lakehouse's Table Format (04-metadata-standards.md) must
be declared at provisioning and cannot be changed without a documented
migration plan reviewed by a Data Engineer.
**Applies to:** All environments, Data Lakehouse entity type.
**Enforcement:** Hard block on missing declaration; approval gate on change.
**Rationale:** A silent table-format change (e.g. Delta Lake to Iceberg)
breaks every downstream reader relying on that format's specific
transaction log/metadata layout — treated with the same severity as
SAPOL-1's backward-compatibility requirement for Production APIs, the
closest analog in System Architecture.

### DPPOL-5 — Semantic Layer as Sole Source for Certified Metrics
**Rule:** A Warehouse/Lakehouse-level Metric that is to be treated as
Certified (per Business Intelligence / Reporting's Certified Dataset/
Report concept, `bi-certified-dataset-report`) must be materialized
through the Semantic Layer (`dp-semantic-layer`), not recomputed directly
against warehouse tables by a downstream report or pipeline.
**Applies to:** All environments, Data Warehouse/Data Lakehouse entity
types where a Metric (`data-metric`) is exposed for reporting use.
**Enforcement:** Approval gate — a report/pipeline bypassing the Semantic
Layer for a Metric it claims is Certified is rejected at the BI/Reporting
domain's certification step (see `bi-source-to-target-mapping`); this
policy is the Data Platform-side half of that same governance concern
first raised when Business Intelligence / Reporting was split out as its
own domain (00-framework/ea-framework-alignment.md).
**Rationale:** This is the policy expression of the exact divergence risk
that motivated adding Business Intelligence / Reporting as domain 6 in
the first place — recomputing a metric outside the Semantic Layer is
technically easy and is exactly the failure mode this framework exists to
catch, so it's made an explicit, named policy rather than left implicit
in the Semantic Layer's Definitions/Ontology entries alone.

---

**Cross-references:**
- DPPOL-1 is the direct successor to System Architecture's SAPOL-2 —
  ownership moved, wording otherwise preserved (see
  03-system-architecture/06-policies.md's stub).
- DPPOL-5 connects directly to `dp-semantic-layer --[requires]--> data-metric`
  (03-ontologies.md) and `bi-report-data-model --[requires]--> dp-semantic-layer`
  (06-bi-reporting/03-ontologies.md) — the ontology already asserts this
  dependency; DPPOL-5 is what makes bypassing it a governance violation
  rather than merely an unusual choice.
- DPPOL-3's correctness rationale (mixed embedding models) is distinct in
  kind from every other Hard Block in this framework so far — the others
  (SAPOL-3 secrets, DPOL-1 PII) are risk/compliance hard blocks; this one
  is a data-correctness hard block, flagged as a new category worth
  watching for as more AI/ML-adjacent domains (Harness, domain 8) are built.

**Open items:**
- Who qualifies as a Data Engineer/Data Architect reviewer for DPPOL-1
  and DPPOL-4 is deferred to Access Rules (column 7), next.
- DPPOL-5's enforcement mechanism (how a report/pipeline is actually
  checked against Semantic Layer usage) is deferred to Procedures
  (column 8) and Tooling (column 10) — likely metadata-catalog-derived
  (OpenMetadata-class tooling), consistent with the tooling-delegation
  posture discussed when Business Intelligence / Reporting was built.

**Quality bar check (00-framework/quality-bar.md):**
- [x] Simple — 5 domain-specific policies plus inherited cross-cutting ones
- [x] Modular — each DPPOL stands alone; DPPOL-1 migrated cleanly without altering SAPOL-4/SAPOL-1's independent logic in System Architecture
- [x] Easy to update — cross-cutting rules update once, apply here automatically
- [x] Easy to maintain — every policy traces to a specific term/field
- [x] Easy to replace — enforcement mechanisms deferred to Procedures/Tooling where tool-specific
