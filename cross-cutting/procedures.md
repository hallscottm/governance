# Cross-Cutting Procedures

Status: Draft — pending review
Ratified: No
Last updated: 2026-09-22

Authored registry of procedures executing the cross-cutting policies/
access rules (cross-cutting/policies.md, cross-cutting/access-rules.md).
A domain's own Procedures column (08-procedures.md) references these and
adds only steps genuinely specific to that domain's resources.

---

### CCPROC-1 — Production Provisioning Request & Approval
**Executes:** CCP-3, CCAR-1, CCAR-2
**Steps:**
1. Requester (human or AI Agent/Harness drafting on a human's behalf)
   submits a provisioning request specifying the resource and its
   required metadata fields (per the owning domain's Metadata Standards).
2. Request is validated against CCP-1 (metadata completeness) before it
   reaches an Approver — incomplete requests are rejected at this step.
3. A designated Approver (not the Requester) reviews and approves or
   rejects the request, per CCAR-2.
4. On approval, the resource is provisioned and assigned a Resource ID
   per the owning domain's naming convention.
5. On rejection, the Requester is notified with the reason; no resource
   is created.
**Domain-specific extensions:** a domain may add steps to this flow (e.g.,
Infrastructure's PROC-1 adds a DR Tier confirmation sub-step during
Approver review) without altering the base sequence above.

### CCPROC-2 — Metadata Completeness Validation
**Executes:** CCP-1
**Steps:**
1. At provisioning time, the requested resource's declared fields are
   checked against the Required fields for its entity type (owning
   domain's Metadata Standards).
2. If any Required field is missing, provisioning halts before reaching
   Approver review (CCPROC-1 step 2).
3. The only path past a failed check is CCPROC-4's break-glass override —
   no separate "partial approval" path exists.

### CCPROC-3 — Cost Attribution Validation
**Executes:** CCP-2
**Steps:**
1. A provisioning request missing a Cost Center Tag is rejected at
   submission — this check happens before any other validation, since
   CCP-2 applies to all environments.
2. No override path exists other than CCPROC-4's break-glass process —
   cost attribution is not treated as a lesser concern than metadata
   completeness.

### CCPROC-4 — Break-Glass Override
**Executes:** CCAR-3
**Steps:**
1. Requester or Approver identifies a case where a hard-block policy
   (e.g., CCP-1, CCP-2, or a domain-specific hard-block policy) must be
   bypassed for a legitimate reason.
2. Request for override is submitted with the specific policy being
   bypassed and the reason, routed per CCAR-3 (Infrastructure Admin
   alone for Low/Moderate risk; Infrastructure Admin + Security/
   Compliance for High risk).
3. Approver(s) per CCAR-3 approve or deny.
4. Every override is logged with: which policy was bypassed, who
   approved it, and the stated reason — this log is the audit trail that
   makes a "hard block" actually hard rather than silently bypassable.

---

**Quality bar check (00-framework/quality-bar.md):**
- [x] Simple — 4 procedures, each executing a specific cross-cutting rule cluster
- [x] Modular — domains extend, not duplicate, these base sequences
- [x] Easy to update — one edit updates the flow for every referencing domain
- [x] Easy to maintain — each procedure traces to specific CCP-/CCAR- items
- [x] Easy to replace — no tooling specifics baked in; SLA/notification deferred to Tooling per domain
