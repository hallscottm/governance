# Data/Metadata Layer — Access Rules

Status: Draft — pending review
Ratified: No
Last updated: 2026-09-22
Provenance: see _qa/07-access-rules.qa.md
Built on: 06-policies.md, cross-cutting/access-rules.md

## Extends Cross-Cutting Access Rules

CCAR-1 (AI Agent Provisioning Authority), CCAR-2 (Production Provisioning
Approval Authority), and CCAR-3 (Hard-Block Override, Risk-Tier-Scaled)
apply to this layer's resources without restatement — see
cross-cutting/access-rules.md.

## Layer-Specific Access Rules

### DAR-1 — Access Approval Separation of Duties
**Rule:** DPOL-3's Data Owner approval for new Confidential/Restricted
access cannot be granted by the Data Owner approving their own request.
When the Data Owner is themselves the requester, approval escalates to
the Data Governance Council instead.
**Applies to:** Data Owner role (standard case); Data Governance Council
role (escalation case), Confidential and Restricted Sensitivity Levels.
**Ties to:** DPOL-3.
**Rationale:** Explicitly chosen — mirrors CCAR-2's Requester/Approver
separation-of-duties rule rather than leaving DPOL-3 self-approvable,
consistent with how every other approval gate in this framework treats
self-approval.

---

**Cross-references:**
- DAR-1 resolves DPOL-3's previously-open "who approves when the
  requester is the Data Owner" question in the same session it was
  raised, rather than carrying it forward — same pattern Networking used
  for NPOL-3/NAR-1.

**Open items:** none for this pass.

**Quality bar check (00-framework/quality-bar.md):**
- [x] Simple — 1 layer-specific access rule plus inherited cross-cutting ones
- [x] Modular — DAR-1 stands alone
- [x] Easy to update — cross-cutting rules update once, apply here automatically
- [x] Easy to maintain — DAR-1 traces directly to DPOL-3
- [x] Easy to replace — role vocabulary remains provisional, consistent with all prior layers
