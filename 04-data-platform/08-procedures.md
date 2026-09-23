# Data Platform Domain — Procedures

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

### DPPROC-1 — Schema Migration Review (moved from System Architecture's SAPROC-2, 2026-09-22, Scaled by Risk Tier)
**Executes:** DPPOL-1, DPPAR-1
**Steps:**
1. A schema migration targeting a Production database is submitted with
   its Risk Tier already determined (per 09-risk-tiers.md).
2. Low tier: routed to any peer reviewer; approval closes the step.
3. Moderate tier: routed to a peer reviewer, then to a Data Engineer
   (per DPPAR-1) for sign-off.
4. High tier: as Moderate, plus a Data Architect sign-off and a
   documented rollback plan on file before either sign-off is requested.
5. On approval, the migration is applied. On rejection, the Requester is
   notified with the reason; no migration is applied.

### DPPROC-2 — Streaming Retention Window Validation
**Executes:** DPPOL-2
**Steps:**
1. At provisioning time, a Stream/Topic request is checked for a
   declared Streaming Retention Window.
2. A request missing this field is rejected before reaching Approver
   review (CCPROC-1 step 2) — same sequencing CCPROC-2 uses for general
   metadata completeness.
3. The only path past a failed check is CCPROC-4's break-glass override.

### DPPROC-3 — Embedding Model Reference Validation
**Executes:** DPPOL-3
**Steps:**
1. At provisioning time, and again at each batch write, a Vector
   Database request/write is checked for a declared Embedding Model
   Reference (04-metadata-standards.md's `<model_name>@<model_version>`
   format, 05-conventions.md).
2. A request/write missing this field, or declaring a reference that
   doesn't match the Vector Database's already-recorded reference (i.e.,
   a silent model change mid-index), is rejected.
3. A deliberate model change is handled as a new Vector Database
   provisioning request (CCPROC-1) with its own Embedding Model
   Reference, not as an in-place field update — re-embedding is required
   when the model changes, since old and new vectors aren't comparable.

### DPPROC-4 — Lakehouse Table Format Migration
**Executes:** DPPOL-4, DPPAR-2
**Steps:**
1. A proposed Table Format change for a Data Lakehouse is submitted with
   a documented migration plan and the Lakehouse's Risk Tier (per
   09-risk-tiers.md).
2. Data Engineer reviews the migration plan at any tier.
3. At High tier, Data Architect sign-off is additionally required before
   the migration proceeds.
4. On approval, the migration plan is executed and the Table Format
   field (04-metadata-standards.md) is updated to reflect the new format.
5. On rejection, the Lakehouse continues operating on its current Table
   Format; no partial migration is applied.

### DPPROC-5 — Semantic Layer Metric Materialization Change
**Executes:** DPPOL-5, DPPAR-3
**Steps:**
1. Analytics Engineer proposes a change to a Metric's materialization in
   the Semantic Layer.
2. The change is classified as either mechanics-only (how the Metric is
   computed/optimized, meaning unchanged) or meaning-altering (what the
   Metric represents changes).
3. Mechanics-only: Analytics Engineer applies the change directly; no
   further approval required.
4. Meaning-altering: the Metric's Data Owner (per DPPAR-3) is notified
   before the change ships — this step does not block on Data Owner
   response (see DPPAR-3's open item on this being notification, not a
   hard gate), but the notification itself is logged as part of this
   procedure's audit trail, the same discipline CCPROC-4 applies to
   break-glass overrides.
5. Any report/pipeline found computing a Certified Metric outside the
   Semantic Layer (DPPOL-5) is flagged for remediation — detection
   mechanism deferred to Tooling (column 10), consistent with the
   metadata-catalog-derived approach discussed for Business Intelligence
   / Reporting's own lineage/certification tooling.

---

**Open items:**
- DPPROC-3's "silent model change mid-index" detection assumes the
  Vector Database's already-recorded Embedding Model Reference is itself
  trustworthy (not separately tamper-checked) — same trust assumption
  every other field-completeness check in this framework makes.
- DPPROC-5 step 5's detection mechanism is a genuine forward reference to
  Tooling (column 10, this domain) and to Business Intelligence /
  Reporting's own certification tooling (06-bi-reporting/10-tooling.md,
  not yet drafted).

**Quality bar check (00-framework/quality-bar.md):**
- [x] Simple — 5 domain-specific procedures plus inherited cross-cutting ones
- [x] Modular — DPPROC-1 through 5 stand alone
- [x] Easy to update — cross-cutting procedures update once, apply here automatically
- [x] Easy to maintain — every procedure traces to a specific DPPOL-/DPPAR- item
- [x] Easy to replace — detection/scanning mechanisms deferred to column 10 and to Business Intelligence / Reporting's own tooling
