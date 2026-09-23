# Business Intelligence / Reporting Domain — Procedures (SOPs)

Status: Draft — pending review
Ratified: No
Last updated: 2026-09-22
Provenance: see _qa/08-procedures.qa.md
Built on: 06-policies.md, 07-access-rules.md, cross-cutting/procedures.md

## Extends Cross-Cutting Procedures

CCPROC-1 (Production Provisioning Request & Approval), CCPROC-2
(Metadata Completeness Validation), CCPROC-3 (Cost Attribution
Validation), and CCPROC-4 (Break-Glass Override) apply to this domain's
resources without restatement — see cross-cutting/procedures.md.

## Domain-Specific Procedures

### BIPROC-1 — Certification Review
**Executes:** BIPOL-1, BIPOL-2, BIAR-1
**Steps:**
1. Business Analyst / Report Builder submits a Report Data Model for
   certification review once it is ready for broader distribution.
2. Submission is checked for a complete Source-to-Target Mapping on
   every Calculated Field claiming a relationship to an existing Metric
   (BIPOL-2) — incomplete mappings halt the review here.
3. A BI Analyst/Developer (not the submitter, per BIAR-1) reviews the
   model's Semantic Layer Sourced status, Source-to-Target Mapping
   completeness, and general correctness.
4. On approval, Certification Status is set to Certified, the `[CERTIFIED]`
   title prefix (05-conventions.md) is applied, and Distribution Scope
   may now be widened per BIPOL-1.
5. On rejection, the submitter is notified with the reason; Certification
   Status remains Draft and Distribution Scope remains restricted to
   Internal/Departmental.

### BIPROC-2 — Row-Level Security Validation (Scaled by Sensitivity)
**Executes:** BIPOL-3, BIAR-2
**Steps:**
1. As part of BIPROC-1's certification review, a Report Data Model's
   inherited Sensitivity Level is checked.
2. Confidential: BI Analyst/Developer confirms Row-Level Security is
   enabled and correctly scoped; this step closes on their sign-off.
3. Restricted, or Contains PII = true: as Confidential, plus Security/
   Compliance independently verifies the Row-Level Security
   configuration before BIPROC-1 step 4 can complete.
4. A Report Data Model failing this validation cannot reach Certified
   status regardless of BIPROC-1's other checks passing.

### BIPROC-3 — Data Extract Refresh Schedule Validation
**Executes:** BIPOL-4
**Steps:**
1. At provisioning time, a Report/Dashboard is checked for its Data
   Extract Flag.
2. If true, the request is checked for a declared Report Refresh
   Schedule — a request missing this is rejected before reaching
   Approver review (CCPROC-1 step 2), same sequencing CCPROC-2 uses for
   general metadata completeness.
3. The only path past a failed check is CCPROC-4's break-glass override.

---

**Open items:** none for this pass — consistent with System Architecture's
and Data/Metadata's Procedures columns, this domain's procedures were
designed to close the open items surfaced during Policies/Access Rules
rather than carry them forward.

**Quality bar check (00-framework/quality-bar.md):**
- [x] Simple — 3 domain-specific procedures plus inherited cross-cutting ones
- [x] Modular — BIPROC-1 through 3 stand alone (BIPROC-2 nests inside BIPROC-1's flow by design, mirroring how System Architecture's SAPROC-5 nested inside its own certification-style flow)
- [x] Easy to update — cross-cutting procedures update once, apply here automatically
- [x] Easy to maintain — every procedure traces to a specific BIPOL-/BIAR- item
- [x] Easy to replace — no tooling specifics baked in; enforcement mechanism deferred to Tooling (column 10)
