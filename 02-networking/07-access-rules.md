# Networking Domain — Access Rules

Status: Draft — pending review
Ratified: No
Last updated: 2026-09-22
Provenance: see _qa/07-access-rules.qa.md
Built on: 06-policies.md, cross-cutting/access-rules.md

## Extends Cross-Cutting Access Rules

CCAR-1 (AI Agent Provisioning Authority), CCAR-2 (Production Provisioning
Approval Authority), and CCAR-3 (Hard-Block Override, Risk-Tier-Scaled)
apply to this domain's resources without restatement — see
cross-cutting/access-rules.md.

## Role Vocabulary

Same as Infrastructure — roles are owned by
[cross-cutting/roles-and-departments/01-definitions.md](../cross-cutting/roles-and-departments/01-definitions.md)
(retrofitted 2026-09-22): [Infrastructure Admin](../cross-cutting/roles-and-departments/01-definitions.md#ccrole-infrastructure-admin), [Security/Compliance](../cross-cutting/roles-and-departments/01-definitions.md#ccrole-security-compliance).

## Domain-Specific Access Rules

### NAR-1 — Public Exposure Approval Authority
**Rule:** Only the Infrastructure Admin or Security/Compliance role may
approve NPOL-3's public-exposure step. Neither the standard Approver role
(CCAR-2) nor an AI Agent/Harness may grant this approval.
**Applies to:** Infrastructure Admin or Security/Compliance role, any
environment (per NPOL-3's scope — not Production-only).
**Ties to:** NPOL-3.
**Rationale:** Explicitly chosen — matches the elevated risk of public
exposure to the same authority level already established for break-glass
overrides (CCAR-3), rather than treating it as routine provisioning.

---

**Cross-references:**
- NAR-1 resolves NPOL-3's previously-open "who approves" question in the
  same session it was raised, rather than carrying it forward as an open
  item.

**Open items:** none for this pass.

**Quality bar check (00-framework/quality-bar.md):**
- [x] Simple — 1 domain-specific access rule plus inherited cross-cutting ones
- [x] Modular — NAR-1 stands alone
- [x] Easy to update — cross-cutting rules update once, apply here automatically
- [x] Easy to maintain — NAR-1 traces directly to NPOL-3
- [x] Easy to replace — role vocabulary now owned by cross-cutting/roles-and-departments/ (retrofitted 2026-09-22), not hard-locked into this domain
