# System Architecture Domain — Access Rules

Status: Draft — pending review
Ratified: No
Last updated: 2026-09-22
Provenance: see _qa/07-access-rules.qa.md
Built on: 06-policies.md, cross-cutting/access-rules.md

## Extends Cross-Cutting Access Rules

CCAR-1 (AI Agent Provisioning Authority), CCAR-2 (Production Provisioning
Approval Authority), and CCAR-3 (Hard-Block Override, Risk-Tier-Scaled)
apply to this domain's resources without restatement — see
cross-cutting/access-rules.md. CCAR-3's override authority (Infrastructure
Admin, plus Security/Compliance at High risk) covers overrides of this
domain's hard-block policies (SAPOL-1, SAPOL-3, SAPOL-4) the same as any
other domain.

## Role: Owning Team Lead (ownership transferred 2026-09-22)

**Originally introduced here** as a provisional role: the accountable
lead for a specific service, application, API, or database, as named in
that entity's Owning Team metadata field (04-metadata-standards.md).
Distinct from Infrastructure Admin, who has no natural authority over
application code or schema decisions specific to a team's own service.

**Now owned by** [cross-cutting/roles-and-departments/01-definitions.md#ccrole-owning-team-lead](../cross-cutting/roles-and-departments/01-definitions.md#ccrole-owning-team-lead)
— formalized as a cross-cutting Positional Role once Roles & Departments
was established, rather than staying a one-off local introduction. This
domain's SAAR-1/SAAR-2 below are unchanged; only the role's ownership
moved.

## Domain-Specific Access Rules

### SAAR-1 — Schema Migration Review Authority (Scaled by Risk Tier)
**Rule:** Authority to approve a SAPOL-2 schema migration is scaled by
Risk Tier:
- **Low:** any peer reviewer (no elevated role required).
- **Moderate:** peer reviewer + the Owning Team Lead for that database.
- **High:** peer reviewer + Owning Team Lead + a documented rollback plan
  (per SAPOL-2); Owning Team Lead sign-off is mandatory, not optional.
**Applies to:** Owning Team Lead role, Database entity type, Production
environment.
**Ties to:** SAPOL-2.
**Rationale:** Mirrors SAPOL-2's own tier scaling directly — no new
scaling logic introduced.

### SAAR-2 — Public-Facing Security Baseline Verification Authority
**Rule:** Verification that a public-facing Service/API meets its
required OWASP ASVS level (SAPOL-5) is performed by:
- **Low (ASVS L1):** Owning Team Lead self-attestation.
- **Moderate (ASVS L2):** Owning Team Lead + Security/Compliance review.
- **High (ASVS L3):** Security/Compliance review required; Owning Team
  Lead alone is insufficient.
**Applies to:** Owning Team Lead and/or Security/Compliance role
(scaled), Service/API entity types configured for public exposure.
**Ties to:** SAPOL-5. Distinct from Networking's NAR-1, which governs the
network-boundary exposure approval, not the service's own security
posture verification — both gates apply to the same resource
independently.
**Rationale:** Escalates from self-attestation to mandatory
Security/Compliance review as risk rises, consistent with CCAR-3's
two-tier escalation pattern.

---

**Cross-references:**
- SAAR-2 and Networking's NAR-1 both gate public exposure of the same
  resource, from different angles (this domain's security posture vs. the
  network boundary itself) — a public-facing High-risk service needs
  both NAR-1 (Infrastructure Admin or Security/Compliance approves
  network exposure) and SAAR-2 (Security/Compliance verifies ASVS L3)
  satisfied independently.
- Owning Team Lead is scoped narrowly (one team, one entity) by design —
  it is not a blanket elevated-privilege role like Infrastructure Admin.

**Open items:**
- (Resolved 2026-09-22) Owning Team Lead's ownership transferred to
  cross-cutting/roles-and-departments/, resolved earlier than the
  original plan of waiting for the Interface/Human domain.

**Quality bar check (00-framework/quality-bar.md):**
- [x] Simple — 2 domain-specific access rules plus inherited cross-cutting ones
- [x] Modular — SAAR-1/SAAR-2 stand alone from each other and from CCAR-1/2/3
- [x] Easy to update — cross-cutting rules update once, apply here automatically
- [x] Easy to maintain — each rule traces directly to its Policy
- [x] Easy to replace — role vocabulary now owned centrally by cross-cutting/roles-and-departments/ (retrofitted 2026-09-22)
