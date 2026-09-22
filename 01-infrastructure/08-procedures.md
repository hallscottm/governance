# Infrastructure Layer — Procedures

Status: Draft — pending review
Ratified: No
Last updated: 2026-09-22
Provenance: see _qa/08-procedures.qa.md
Built on: 06-policies.md, 07-access-rules.md

Step-by-step execution of the policies and access rules already
established. These are mechanical derivations, not new judgment calls —
each procedure exists because a policy/access rule requires a defined
process to be enforceable, not just stated.

---

### PROC-1 — Production Provisioning Request & Approval
**Extends:** CCPROC-1 (cross-cutting/procedures.md)
**Executes:** POL-5, AR-1, AR-3 (which extend CCP-3, CCAR-1, CCAR-2)
**Steps:** (base sequence per CCPROC-1, with step 3 extended for this
layer's DR Tier confirmation — see CCPROC-1's "Layer-specific extensions"
note)
1. Requester (human or AI Agent/Harness drafting on a human's behalf)
   submits a provisioning request specifying the resource, its required
   metadata fields (per 04-metadata-standards.md), and a proposed
   Availability/DR Tier.
2. Request is validated against POL-1 (metadata completeness) and POL-2/
   POL-3 (tier minimums) before it reaches an Approver — incomplete
   requests are rejected at this step, not sent for approval.
3. A designated Approver (not the Requester) reviews the request,
   confirms or adjusts the proposed DR Tier as part of this review (see
   PROC-3 step 4 — this is where DR Tier is authoritatively set, not at
   submission), and approves or rejects the request.
4. On approval, the resource is provisioned and assigned a Resource ID
   and Asset Tag per 05-conventions.md's naming pattern.
5. On rejection, the Requester is notified with the reason; no resource
   is created.

### PROC-2 — Metadata Completeness Validation
**Extends:** CCPROC-2 (cross-cutting/procedures.md)
**Executes:** POL-1 (which extends CCP-1)
**Steps:** (identical to CCPROC-2, restated here for local readability)
1. At provisioning time, the requested resource's declared fields are
   checked against the Required fields for its entity type
   (04-metadata-standards.md).
2. If any Required field is missing, provisioning halts before reaching
   Approver review (see PROC-1 step 2).
3. The only path past a failed check is AR-2's break-glass override
   (see PROC-5) — there is no separate "partial approval" path.

### PROC-3 — Tier Verification (Availability & DR)
**Executes:** POL-2, POL-3
**Steps:**
1. Requester declares intended Availability Tier and DR Tier as part of
   the provisioning request.
2. For Production requests, declared Availability Tier below Tier III is
   rejected unless accompanied by an approved break-glass override
   (PROC-5).
3. For Production requests, a missing/undeclared DR Tier is rejected —
   no default is silently assigned.
4. DR Tier is proposed by the Requester at submission and confirmed (or
   adjusted) by the Approver during PROC-1 step 3 — resolved decision,
   folded into the existing provisioning approval step rather than
   creating a separate review process.

### PROC-4 — Decommissioning & Sanitization
**Executes:** POL-4, AR-4
**Steps:**
1. Requester (or system owner) initiates decommissioning, referencing the
   resource's Resource ID.
2. Storage sanitization is performed per NIST SP 800-88.
3. Infrastructure Admin or Security/Compliance role certifies sanitization
   completion — this sign-off is recorded before the resource is marked
   Decommissioned.
4. Resource's Decommission Date field (04-metadata-standards.md) is set
   only after sign-off, not at initiation.

### PROC-5 — Break-Glass Override
**Extends:** CCPROC-4 (cross-cutting/procedures.md)
**Executes:** AR-2 (which extends CCAR-3)
**Steps:** (identical to CCPROC-4, applied to this layer's hard-block policies)
1. Requester or Approver identifies a case where POL-1, POL-2, or POL-6
   must be bypassed for a legitimate reason.
2. Request for override is submitted to an Infrastructure Admin with the
   specific policy being bypassed and the reason.
3. Infrastructure Admin approves or denies. No other role may approve
   this step (per AR-2).
4. Every override is logged with: which policy was bypassed, who
   approved it, and the stated reason — this log is the audit trail
   referenced by POL-1/POL-2/POL-6's "hard block" designation (a hard
   block that can be silently bypassed isn't actually hard).

### PROC-6 — Untagged Resource Handling
**Extends:** CCPROC-3 (cross-cutting/procedures.md)
**Executes:** POL-6 (which extends CCP-2)
**Steps:** (identical to CCPROC-3, restated here for local readability)
1. A provisioning request missing a Cost Center Tag is rejected at
   submission — this check happens before any other validation, since
   POL-6 applies to all environments (not just Production).
2. No override path exists for POL-6 other than AR-2's break-glass
   process (same as PROC-5) — cost attribution is not treated as a
   lesser concern than metadata/tier compliance.

---

**Open items:**
- (Resolved 2026-09-22) Who sets DR Tier — Requester proposes, Approver
  confirms as part of PROC-1/PROC-3. No longer open.
- Approval SLA/turnaround time (how long an Approver has to respond) is
  intentionally left as an implementation detail for whichever tool
  handles this workflow (column 10, Tooling) — confirmed as the right
  boundary, not an oversight.
- Notification mechanism (how a Requester is told of approval/rejection)
  is likewise intentionally deferred to Tooling.

**Quality bar check (00-framework/quality-bar.md):**
- [x] Simple — each procedure is a short numbered sequence, no branching complexity beyond what the policy already requires
- [x] Modular — each procedure executes one policy/access-rule cluster; none depend on another procedure's internals
- [x] Easy to update — steps reference policies/rules by name, not restated logic
- [x] Easy to maintain — every step traces to a specific POL-/AR- item; no free-floating process
- [x] Easy to replace — tool-specific details (SLA, notifications) explicitly deferred to column 10, so swapping tooling doesn't require rewriting procedures
