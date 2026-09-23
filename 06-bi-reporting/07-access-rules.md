# Business Intelligence / Reporting Domain — Access Rules

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

Roles referenced below are owned by
cross-cutting/roles-and-departments/01-definitions.md: **Business
Analyst / Report Builder**
([#ccrole-business-analyst-report-builder](../cross-cutting/roles-and-departments/01-definitions.md#ccrole-business-analyst-report-builder))
builds self-service Report Data Models; **BI Analyst/Developer**
([#ccrole-bi-analyst-developer](../cross-cutting/roles-and-departments/01-definitions.md#ccrole-bi-analyst-developer))
reviews and certifies them (see 00-qa.md Q8 there).

## Domain-Specific Access Rules

### BIAR-1 — Certification Authority
**Rule:** Only a BI Analyst/Developer may transition a Report Data
Model's Certification Status from Draft to Certified (BIPOL-1, BIPOL-2).
The Business Analyst/Report Builder who authored the model cannot
self-certify — separation of duties, same shape as CCAR-2's Requester/
Approver rule.
**Applies to:** BI Analyst/Developer role (approver), Business Analyst /
Report Builder role (cannot self-approve), Report Data Model entity type.
**Ties to:** BIPOL-1, BIPOL-2.
**Rationale:** Explicit separation of duties — a self-certified report
defeats the purpose of BIPOL-1/BIPOL-2's review requirement, the same
self-approval concern CCAR-2 and Data/Metadata's DAR-1 already establish
elsewhere in this framework.

### BIAR-2 — Row-Level Security Configuration Authority (Scaled by Sensitivity)
**Rule:** Authority to configure and approve BIPOL-3's Row-Level Security
requirement is scaled by Sensitivity Level:
- **Confidential:** BI Analyst/Developer configures and self-attests.
- **Restricted, or Contains PII = true:** BI Analyst/Developer configures;
  Security/Compliance independently verifies before Certified status is
  reachable.
**Applies to:** BI Analyst/Developer role (all tiers), Security/
Compliance role (Restricted/PII only), Report Data Model entity type.
**Ties to:** BIPOL-3.
**Rationale:** Directly mirrors System Architecture's SAAR-2 escalation
pattern (self-attestation → mandatory independent review as sensitivity
rises) — no new scaling logic introduced, reused deliberately for
consistency.

---

**Cross-references:**
- BIAR-1 and BIAR-2 both gate the same Certified-status transition from
  different angles (general review vs. sensitivity-specific
  verification) — a Restricted-sensitivity Report Data Model needs both
  satisfied independently before Certified status is reachable, the same
  "two independent gates on the same resource" shape SAAR-2/NAR-1 already
  established for public-facing Services in System Architecture/
  Networking.

**Open items:** none for this pass — both access rules were designed to
close the open items BIPOL-1/2/3 raised, rather than carry them forward,
consistent with how System Architecture's and Data/Metadata's Access
Rules columns handled their own Policies' open items.

**Quality bar check (00-framework/quality-bar.md):**
- [x] Simple — 2 domain-specific access rules plus inherited cross-cutting ones
- [x] Modular — BIAR-1/BIAR-2 stand alone from each other and from CCAR-1/2/3
- [x] Easy to update — cross-cutting rules update once, apply here automatically
- [x] Easy to maintain — each rule traces directly to its Policy
- [x] Easy to replace — role vocabulary owned centrally by cross-cutting/roles-and-departments/, not redefined here
