# Data Platform Domain — Access Rules

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
cross-cutting/roles-and-departments/01-definitions.md: **Data Architect**
([#ccrole-data-architect](../cross-cutting/roles-and-departments/01-definitions.md#ccrole-data-architect)),
**Data Engineer**
([#ccrole-data-engineer](../cross-cutting/roles-and-departments/01-definitions.md#ccrole-data-engineer)),
and **Analytics Engineer**
([#ccrole-analytics-engineer](../cross-cutting/roles-and-departments/01-definitions.md#ccrole-analytics-engineer))
co-own this domain (see 00-qa.md Q7/Q8 there) and are the roles named
below, rather than a domain-local role being introduced here.

## Domain-Specific Access Rules

### DPPAR-1 — Schema Migration Review Authority (moved from System Architecture's SAAR-1, 2026-09-22, Scaled by Risk Tier)
**Rule:** Authority to approve a DPPOL-1 schema migration is scaled by
Risk Tier:
- **Low:** any peer reviewer (no elevated role required).
- **Moderate:** peer reviewer + Data Engineer sign-off.
- **High:** peer reviewer + Data Engineer sign-off + Data Architect
  sign-off + a documented rollback plan (per DPPOL-1).
**Applies to:** Data Engineer role (Moderate+), Data Architect role
(High only), Database entity type, Production environment.
**Ties to:** DPPOL-1.
**Rationale:** Mirrors DPPOL-1's own tier scaling directly, same as its
System Architecture predecessor — the only substantive change is which
roles hold the authority, reflecting this domain's own two-role
design/build split (Data Architect designs, Data Engineer builds/
operates) rather than System Architecture's single Owning Team Lead.

### DPPAR-2 — Lakehouse Table Format Change Authority
**Rule:** A DPPOL-4 table-format migration plan requires Data Engineer
review at any Risk Tier; a High-Risk-Tier Lakehouse additionally requires
Data Architect sign-off, since a format change at that tier is a design
decision, not just an operational one.
**Applies to:** Data Engineer role (all tiers), Data Architect role (High
only), Data Lakehouse entity type.
**Ties to:** DPPOL-4.
**Rationale:** Same design/build-vs-operate split as DPPAR-1, scaled by
Risk Tier for consistency across this domain's approval gates.

### DPPAR-3 — Semantic Layer Change Authority
**Rule:** Changes to the Semantic Layer's materialized Metric mappings
(supporting DPPOL-5) are made by the Analytics Engineer role; a change
that alters what a Metric *means* (not just how it's materialized)
requires the Metric's Data Owner (owned by Data/Metadata,
`data-owner` — typically a Business Function Department per
cross-cutting/roles-and-departments/00-qa.md Q9) to be notified before
the change ships, since the Metric's meaning isn't this domain's to
redefine unilaterally.
**Applies to:** Analytics Engineer role, Semantic Layer entity
(`dp-semantic-layer`), any environment.
**Ties to:** DPPOL-5.
**Rationale:** Reflects the Analytics Engineer's established role as the
one who "builds/assists in building the downstream models" (the role's
own defining scope, cross-cutting/roles-and-departments/00-qa.md Q8) — the
Metric's *mechanics* are Analytics Engineer's to change; its *meaning* is
the Data Owner's, mirroring Data/Metadata's DPOL-3/DAR-1 pattern for who
approves changes to something with a defined owner.

---

**Cross-references:**
- DPPAR-1 is the direct successor to System Architecture's SAAR-1 — see
  03-system-architecture/07-access-rules.md's stub.
- DPPAR-3 is the first Access Rule in this framework to route a change
  through a Business Function Department's Data Owner rather than a
  purely technical role — a direct, concrete instance of the Business
  Function Department resolution (00-qa.md Q9 in cross-cutting/
  roles-and-departments/) actually being exercised.

**Open items:**
- DPPAR-3's "notified before the change ships" is deliberately weaker
  than a hard approval gate (unlike DAR-1's Data Owner approval
  requirement in Data/Metadata) — a Semantic Layer materialization change
  that doesn't alter meaning (e.g., a performance optimization) shouldn't
  need Data Owner sign-off; only a meaning-altering change does, and
  distinguishing the two in practice is left to Analytics Engineer
  judgment and Procedures (column 8), not fully mechanized here.

**Quality bar check (00-framework/quality-bar.md):**
- [x] Simple — 3 domain-specific access rules plus inherited cross-cutting ones
- [x] Modular — DPPAR-1/2/3 stand alone from each other and from CCAR-1/2/3
- [x] Easy to update — cross-cutting rules update once, apply here automatically
- [x] Easy to maintain — each rule traces directly to its Policy
- [x] Easy to replace — role vocabulary owned centrally by cross-cutting/roles-and-departments/, not redefined here
