# Harness Domain — Access Rules

Status: Draft — pending review
Ratified: No
Last updated: 2026-09-23
Provenance: see _qa/07-access-rules.qa.md
Built on: 06-policies.md, cross-cutting/access-rules.md

## Extends Cross-Cutting Access Rules

CCAR-1 (AI Agent/Harness Provisioning Authority), CCAR-2 (Production
Provisioning Approval Authority), and CCAR-3 (Hard-Block Override,
Risk-Tier-Scaled) apply to this domain's resources without restatement —
see cross-cutting/access-rules.md. CCAR-1 is worth restating in plain
terms here since it is this domain's central constraint: an Agent
(`harness-agent`) may draft or request an action, but the AI Agent/Harness
actor type may never itself be the Approver — not at any Risk Tier, not
for any Capability Scope, no exception.

## Role Vocabulary

Roles referenced below are owned by
cross-cutting/roles-and-departments/01-definitions.md: **Owning Team
Lead** ([#ccrole-owning-team-lead](../cross-cutting/roles-and-departments/01-definitions.md#ccrole-owning-team-lead))
and **Security/Compliance**
([#ccrole-security-compliance](../cross-cutting/roles-and-departments/01-definitions.md#ccrole-security-compliance)).
No new role is introduced by this domain — an Agent's Owning Team Lead is
typically drawn from AI/ML Platform (`ccdept-ai-ml-platform`, this
domain's default owning department), but the role itself is the same one
every other domain already uses for its own resources.

## Domain-Specific Access Rules

### HAR-1 — Production Tool Permission Grant Authority
**Rule:** Approving a Capability Scope/Tool Permission Scope change that
adds a Production-scoped Tool grant (HPOL-1) requires Owning Team Lead
approval, confirming Sandbox testing and a passing Eval Suite Run first.
At High Risk Tier (09-risk-tiers.md), Security/Compliance is additionally
required.
**Applies to:** Owning Team Lead role (all tiers), Security/Compliance
role (High tier only), Agent entity type, Production environment.
**Ties to:** HPOL-1, HPOL-2.
**Rationale:** Reuses CCAR-3's tier-scaling *pattern* (single approver
at Low/Moderate, two-person at High) — not CCAR-3 itself, since granting
a new Tool Permission is a routine approval-gate decision, not an
override of an existing hard block. Owning Team Lead is the correct
approver here for the same reason it's correct at every other ordinary
approval gate in this framework (contrast HAR-3, an actual hard-block
override, where CCAR-3 applies directly and Owning Team Lead is not a
valid approver).

### HAR-2 — Human-in-the-Loop Gate Resolution Authority
**Rule:** The human who resolves a Human-in-the-Loop Gate (HPOL-3) must
be the Owning Team Lead, or a role the Owning Team Lead has explicitly
named within the Agent's Escalation Path — never the Agent itself, per
CCAR-1, restated at instance level with zero exception. At High Risk
Tier, Security/Compliance is additionally required, per CCAR-3.
**Applies to:** Owning Team Lead role (all tiers), Security/Compliance
role (High tier only), Autonomous/Multi-Agent Agent Types, Production
environment.
**Ties to:** HPOL-3.
**Rationale:** This is the access-control expression of CCAR-1's
blanket rule — HPOL-3 says a gate must exist; this rule says who is
permitted to be the human on the other side of it, and explicitly
excludes the Agent from ever qualifying.

### HAR-3 — Guardrail Override Authority (Break-Glass)
**Rule:** Overriding an Agent's Guardrail (HPOL-5) requires
Infrastructure Admin approval, plus Security/Compliance — every
Guardrail override is automatically High Risk Tier per HPOL-5, so the
High-tier two-person sign-off (CCAR-3) always applies here; there is no
Low/Moderate-tier single-approver path for this specific override,
unlike Workflow/Process's WFAR-2 (an ordinary approval gate, not an
override).
**Applies to:** Infrastructure Admin role, Security/Compliance role,
Agent entity type, any environment.
**Ties to:** HPOL-5, CCAR-3.
**Rationale:** HPOL-5 fixes Guardrail override at High Risk Tier
unconditionally (09-risk-tiers.md); CCAR-3's own two-person rule for
High risk therefore applies unconditionally too, rather than scaled —
the one Access Rule in this domain with no Low/Moderate path, flagged
explicitly since every other Access Rule in this framework offers at
least a single-approver tier for something. **Corrected 2026-09-23:**
an earlier version of this rule granted the override to Owning Team
Lead — this is a hard-block override (Guardrail is HPOL-5's hard
block), squarely inside CCAR-3's exclusive authority ("No other role,
and no AI Agent/Harness, may grant this override at any risk tier");
Owning Team Lead was never a valid approver here.

---

**Cross-references:**
- HAR-2 is the sharpest instance-level expression of CCAR-1 anywhere in
  this framework — every other domain's Access Rules columns describe who
  may approve a human action; this one describes who may **not**
  (the Agent itself, categorically) alongside who may.
- HAR-1 reuses CCAR-3's tier-scaling *pattern* for an ordinary approval
  gate (Owning Team Lead, same as HAR-2 and Workflow/Process's WFAR-2).
  HAR-3 *is* CCAR-3 applied to a hard-block override (Infrastructure
  Admin, not Owning Team Lead) — same distinction Workflow/Process's
  WFAR-1 vs. WFAR-2 now makes explicitly, after both WFAR-1 and HAR-3
  were corrected 2026-09-23 to stop granting break-glass authority to
  Owning Team Lead, which CCAR-3 never permits at any risk tier.
- HAR-3's unconditional High-tier requirement (no Low/Moderate path) is a
  direct, mechanical consequence of HPOL-5/09-risk-tiers.md fixing
  Guardrail override at High Risk Tier — flagged the same way
  Workflow/Process flagged its own structurally unusual WFPOL-5.

**Open items:** none for this pass — all three access rules were
designed to close the open items HPOL-1/3/5 raised, consistent with how
every other domain's Access Rules column has handled its own Policies'
open items.

**Quality bar check (00-framework/quality-bar.md):**
- [x] Simple — 3 domain-specific access rules plus inherited cross-cutting ones
- [x] Modular — HAR-1/2/3 stand alone from each other and from CCAR-1/2/3
- [x] Easy to update — cross-cutting rules update once, apply here automatically
- [x] Easy to maintain — each rule traces directly to its Policy
- [x] Easy to replace — no new role vocabulary introduced; all authority routes through roles other domains already own
