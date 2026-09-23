# Business Intelligence / Reporting Domain — Policies

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

### BIPOL-1 — Certified Status Required for Broad Distribution
**Rule:** A Report or Dashboard cannot be set to Organization-wide or
External Distribution Scope (04-metadata-standards.md) unless its
Certification Status is Certified. Internal and Departmental scope remain
available to Draft reports without restriction — self-service modeling
is not prohibited, only its blast radius while ungoverned.
**Applies to:** All environments, Report/Dashboard entity types.
**Enforcement:** Hard block.
**Rationale:** This is the policy this domain was created to write — the
founding governance concern raised when Business Intelligence / Reporting
was split out as its own domain (00-framework/ea-framework-alignment.md,
cross-cutting/roles-and-departments/00-qa.md Q8): a report builder's
parallel model is a real, common workflow, not a mistake to eliminate,
but it should not reach a broad audience un-reviewed. Explicitly chosen
as a hard block, not an approval gate with an override — the whole point
is that Certified status must exist *before* wide exposure, not be
requested after the fact.

### BIPOL-2 — Complete Source-to-Target Mapping Required for Certification
**Rule:** A Report Data Model cannot be promoted to Certified status
unless every Calculated Field with a claimed relationship to an existing
Metric has a complete Source-to-Target Mapping on file.
**Applies to:** All environments, Report Data Model entity type.
**Enforcement:** Hard block on the certification transition itself (not
on the Report Data Model's existence — an uncertified model with
incomplete mapping is allowed to exist and be used at Internal/
Departmental scope).
**Rationale:** This is the direct policy restatement of the Ontology
relationship already established (`bi-certified --[requires]-->
bi-source-to-target-mapping`, 03-ontologies.md) — Policies makes it
enforceable rather than merely descriptive, the same treatment DPPOL-5
gave the Semantic Layer relationship in Data Platform.

### BIPOL-3 — Row-Level Security Required (Scaled by Sensitivity)
**Rule:** A Report Data Model whose underlying data has a Sensitivity
Level (inherited from source) of Confidential or Restricted must have
Row-Level Security enabled:
- **Confidential:** Row-Level Security required, configuration reviewed
  by a BI Analyst/Developer.
- **Restricted, or Contains PII = true:** Row-Level Security required,
  configuration reviewed by a BI Analyst/Developer AND Security/
  Compliance.
**Applies to:** All environments, Report Data Model entity type where
Sensitivity Level is Confidential or Restricted.
**Enforcement:** Hard block (Certified status cannot be reached without
this) at Confidential; hard block plus mandatory Security/Compliance
review at Restricted/PII, mirroring System Architecture's SAPOL-5/SAAR-2
escalation pattern.
**Rationale:** A Report is a distribution mechanism for its underlying
data's sensitivity — the sensitivity classification set at the source
(Data/Metadata) doesn't stop mattering once the data reaches a report,
consistent with how every other domain's Risk Tiers treats Sensitivity
Level as inherited, not reset, at each layer.

### BIPOL-4 — Data Extract Refresh Schedule Required
**Rule:** A Report/Dashboard flagged as using a Data Extract cannot be
provisioned without a declared Report Refresh Schedule
(`bi-refresh-schedule`).
**Applies to:** All environments, Report/Dashboard entity types where
Data Extract Flag is true.
**Enforcement:** Hard block.
**Rationale:** An extract with no declared refresh cadence has an
undefined staleness — the same "cheap to prevent at provisioning,
expensive to discover later" reasoning DPPOL-2 used for streaming
retention windows in Data Platform.

---

**Cross-references:**
- BIPOL-1 and BIPOL-2 together implement the Certified/Draft lifecycle
  already established in 01-definitions.md's `bi-certified` term — BIPOL-1
  gates *where* a report can go, BIPOL-2 gates *what's required to get
  there*.
- BIPOL-3 mirrors Data/Metadata's DPOL-1/DPOL-3 sensitivity-scaled
  treatment and System Architecture's SAPOL-5 escalation pattern — the
  third domain in this framework to use a two-tier (Confidential vs.
  Restricted/PII) escalation for a sensitivity-driven policy.
- Data Platform's DPPOL-5 (Semantic Layer as sole source for Certified
  Metrics) and this domain's BIPOL-1/BIPOL-2 are the two halves of the
  same governance concern from opposite sides: DPPOL-5 keeps the
  official Semantic Layer authoritative on the Data Platform side;
  BIPOL-1/BIPOL-2 keep an un-reviewed report-level model from reaching a
  broad audience on the reporting side. Neither restates the other.

**Open items:**
- Who qualifies as the reviewing BI Analyst/Developer for BIPOL-1/2/3 is
  deferred to Access Rules (column 7), next.
- BIPOL-1's enforcement mechanism (what actually prevents a Distribution
  Scope change from being saved) is deferred to Tooling (column 10) —
  likely native to whatever BI platform is in use, not a separate gate
  this framework builds.

**Quality bar check (00-framework/quality-bar.md):**
- [x] Simple — 4 domain-specific policies plus inherited cross-cutting ones
- [x] Modular — each BIPOL stands alone; BIPOL-1/2 are sequenced but independently statable
- [x] Easy to update — cross-cutting rules update once, apply here automatically
- [x] Easy to maintain — every policy traces to a specific term/field
- [x] Easy to replace — enforcement mechanisms deferred to Access Rules/Procedures/Tooling where tool-specific
