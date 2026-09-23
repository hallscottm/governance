# Networking Domain — Procedures

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

### NPROC-1 — Default-Deny Ingress Verification
**Executes:** NPOL-1
**Steps:**
1. At provisioning time, a Production security boundary configuration
   (`net-acl`, `net-security-group`, `net-firewall`) is checked for a
   default-deny posture.
2. Any configuration found defaulting to allow is rejected before
   reaching Approver review (same halting pattern as CCPROC-2).
3. The only path past a failed check is CCPROC-4's break-glass override.

### NPROC-2 — Encryption in Transit Verification
**Executes:** NPOL-2
**Steps:**
1. At provisioning time, a Production network resource/connection is
   checked for `net-encryption-in-transit` (via `net-tls` or equivalent).
2. A configuration lacking encryption in transit is rejected before
   reaching Approver review.
3. The only path past a failed check is CCPROC-4's break-glass override.

### NPROC-3 — Public Exposure Approval
**Executes:** NPOL-3, NAR-1
**Steps:**
1. Requester flags a provisioning request as involving public/
   internet-facing exposure.
2. This request is routed for approval to the Infrastructure Admin or
   Security/Compliance role (per NAR-1) — separately from, and in
   addition to, the standard CCPROC-1/CCAR-2 provisioning approval.
3. Approval must be granted before the resource is provisioned publicly;
   rejection at this step blocks provisioning even if standard Production
   approval (CCPROC-1) would otherwise have passed.
4. This approval is logged the same way a break-glass override is logged
   (CCPROC-4 step 4) — who approved, when, and for what resource.

---

**Open items:** none for this pass — this domain's procedures were
designed to close, not carry forward, the open items surfaced during
Policies/Access Rules drafting (NPOL-3's "who approves" was resolved as
NAR-1, and NPROC-3 now defines how that approval actually happens).

**Quality bar check (00-framework/quality-bar.md):**
- [x] Simple — 3 domain-specific procedures plus inherited cross-cutting ones
- [x] Modular — NPROC-1/2/3 stand alone
- [x] Easy to update — cross-cutting procedures update once, apply here automatically
- [x] Easy to maintain — every procedure traces to a specific NPOL-/NAR- item
- [x] Easy to replace — enforcement mechanism/tooling specifics deferred to column 10
