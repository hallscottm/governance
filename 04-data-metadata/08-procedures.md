# Data/Metadata Layer — Procedures

Status: Draft — pending review
Ratified: No
Last updated: 2026-09-22
Provenance: see _qa/08-procedures.qa.md
Built on: 06-policies.md, 07-access-rules.md, cross-cutting/procedures.md

## Extends Cross-Cutting Procedures

CCPROC-1 (Production Provisioning Request & Approval), CCPROC-2
(Metadata Completeness Validation), CCPROC-3 (Cost Attribution
Validation), and CCPROC-4 (Break-Glass Override) apply to this layer's
resources without restatement — see cross-cutting/procedures.md.

## Layer-Specific Procedures

### DPROC-1 — PII/Restricted Data Protection Verification
**Executes:** DPOL-1
**Steps:**
1. At provisioning time, a Data Asset flagged Contains PII or classified
   Restricted is checked for encryption at rest and a defined
   need-to-know access group.
2. A configuration missing either control is rejected before reaching
   Approver review.
3. The only path past a failed check is CCPROC-4's break-glass override.

### DPROC-2 — Retention Period Enforcement
**Executes:** DPOL-2
**Steps:**
1. At provisioning time, a Dataset without a declared Data Retention
   Period is rejected before reaching Approver review.
2. On an ongoing basis, each Dataset's retention period is checked
   against its age; a Dataset past expiry with no active Legal Hold is
   flagged for Data Disposal.
3. Disposal proceeds per Infrastructure's NIST SP 800-88-aligned media
   sanitization practice (01-infrastructure/08-procedures.md), applied
   here to the data itself rather than the underlying resource.
4. A Legal Hold placed on a Dataset suspends step 2/3 until the hold is
   lifted.

### DPROC-3 — Confidential/Restricted Access Grant Approval
**Executes:** DPOL-3, DAR-1
**Steps:**
1. Requester submits an access request for Confidential or Restricted
   data.
2. If the Requester is not the Data Owner, the request routes to the
   Data Owner for approval.
3. If the Requester IS the Data Owner, the request routes to the Data
   Governance Council instead (per DAR-1).
4. On approval, access is granted and logged (who approved, when, scope
   of access). On rejection, the Requester is notified with the reason.

### DPROC-4 — Right to Erasure Request Handling
**Executes:** DPOL-4
**Steps:**
1. A Right to Erasure request is logged with its received date, starting
   the 30-day SLA clock (or an org-adjusted equivalent, per DPOL-4).
2. The request is checked against active Legal Holds or other lawful
   exceptions; if one applies, the requester is notified of the
   exception and the reason erasure cannot proceed as requested.
3. Absent an exception, the Data Owner coordinates Data Disposal across
   every Source System and Downstream Consumer identified in the data's
   Data Lineage — not just the primary System of Record.
4. Completion (or a documented exception) is logged before the SLA
   deadline.

---

**Open items:** none for this pass.

**Quality bar check (00-framework/quality-bar.md):**
- [x] Simple — 4 layer-specific procedures plus inherited cross-cutting ones
- [x] Modular — DPROC-1 through 4 stand alone
- [x] Easy to update — cross-cutting procedures update once, apply here automatically
- [x] Easy to maintain — every procedure traces to a specific DPOL-/DAR- item
- [x] Easy to replace — specific scanning/tracking mechanisms deferred to column 10
