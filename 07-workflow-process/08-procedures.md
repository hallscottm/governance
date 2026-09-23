# Workflow/Process Domain — Procedures (SOPs)

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

### WFPROC-1 — Branch Protection Enforcement
**Executes:** WFPOL-1, WFAR-1
**Steps:**
1. A Pull Request targeting a Repository's Default Branch triggers its
   configured Pipeline.
2. The merge button/mechanism is disabled until: at least one Code
   Review approval is recorded, and the Pipeline Run's Deployment Gate
   status is passing.
3. An Owning Team Lead (or, at High Risk Tier, Owning Team Lead +
   Security/Compliance, per WFAR-1) may override this block in a genuine
   emergency; every override is logged with who approved it and why,
   same audit discipline as CCPROC-4.
4. On merge, the change proceeds to the next Pipeline Stage per
   05-conventions.md's CI/CD Pipeline Flow diagram.

### WFPROC-2 — Production Promotion Gate Check
**Executes:** WFPOL-2
**Steps:**
1. A Release Candidate reaching the Production promotion point (per
   05-conventions.md's Environment Promotion Flow diagram) has its
   configured Deployment Gates evaluated.
2. Each domain-specific gate (System Architecture's SAPOL-4, Data
   Platform's DPPOL-1 where applicable, Business Intelligence /
   Reporting's BIPOL-1 where applicable) reports pass/fail independently.
3. All applicable gates must pass before promotion proceeds — any single
   failure halts promotion at that point, per WFPOL-2.
4. On full pass, the Release Candidate is promoted and becomes a Release
   (`sysarch-release`).

### WFPROC-3 — IaC Plan Review and Apply
**Executes:** WFPOL-3, WFAR-2
**Steps:**
1. An IaC Plan is generated against the current State File for a
   proposed infrastructure change.
2. The Plan is routed to the applicable approver per WFAR-2 (Infrastructure
   Admin, Data Engineer, or both plus Security/Compliance at High tier,
   depending on what's being provisioned).
3. On approval, IaC Apply executes, updating the State File to reflect
   the new actual state.
4. On rejection, the Requester is notified with the reason; no apply
   occurs.
5. Drift Detection runs on a recurring basis independent of this flow,
   flagging any resource whose actual state no longer matches the State
   File — a signal that step 1-4 was bypassed somewhere.

### WFPROC-4 — Incident Response and Post-Incident Review
**Executes:** WFPOL-4
**Steps:**
1. An Incident is declared with an initial Incident Severity assigned.
2. Response proceeds through Investigating → Mitigated → Resolved
   (05-conventions.md's Incident Lifecycle diagram), consuming any
   applicable Runbook along the way.
3. At Resolved, Incident Severity is checked: Sev3/Sev4 may close
   immediately at Owning Team discretion; Sev1/Sev2 routes to a required
   Post-Incident Review within the organization's defined window.
4. The Post-Incident Review documents timeline, root cause, and follow-up
   actions, which are typically tracked as new Change Requests (per
   03-ontologies.md's `wf-postmortem --[produces]--> wf-change-request`).

### WFPROC-5 — Emergency Change Execution and Post-Hoc Review
**Executes:** WFPOL-5, WFAR-3
**Steps:**
1. A Change Request is classified as Emergency (Change Request Type,
   04-metadata-standards.md) when normal pre-approval would materially
   worsen an active situation (typically a concurrent Sev1/Sev2 Incident,
   per WFPROC-4).
2. The change executes immediately, without waiting for the approval
   CCPROC-1 would otherwise require first.
3. Within 24 hours (WFPOL-5's default window), the change is submitted
   for post-hoc review to the same role that would have approved it under
   normal Change Request review (per WFAR-3).
4. The review outcome (approved, or flagged for follow-up/reversal) is
   logged — every Emergency Change is accounted for after the fact, even
   though none required pre-approval.

---

**Open items:** none for this pass — consistent with every other domain's
Procedures column, these were designed to close the open items surfaced
during Policies/Access Rules rather than carry them forward.

**Quality bar check (00-framework/quality-bar.md):**
- [x] Simple — 5 domain-specific procedures plus inherited cross-cutting ones
- [x] Modular — WFPROC-1 through 5 stand alone
- [x] Easy to update — cross-cutting procedures update once, apply here automatically
- [x] Easy to maintain — every procedure traces to a specific WFPOL-/WFAR- item, and to the Conventions diagrams that visualize the same flow
- [x] Easy to replace — no tooling specifics baked in; execution mechanisms deferred to Tooling (column 10)
