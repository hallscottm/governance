# Workflow/Process Domain — Access Rules

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
cross-cutting/roles-and-departments/01-definitions.md: **Owning Team
Lead** ([#ccrole-owning-team-lead](../cross-cutting/roles-and-departments/01-definitions.md#ccrole-owning-team-lead)),
**Infrastructure Admin** ([#ccrole-infrastructure-admin](../cross-cutting/roles-and-departments/01-definitions.md#ccrole-infrastructure-admin)),
**Data Engineer** ([#ccrole-data-engineer](../cross-cutting/roles-and-departments/01-definitions.md#ccrole-data-engineer)),
and **Security/Compliance** ([#ccrole-security-compliance](../cross-cutting/roles-and-departments/01-definitions.md#ccrole-security-compliance)).
No new role is introduced by this domain — every approval authority below
routes through a role another domain already owns, since this domain's
job is to move changes other domains define, not to define a new class
of accountable owner.

## Domain-Specific Access Rules

### WFAR-1 — Branch Protection Override Authority
**Rule:** Bypassing a WFPOL-1 branch protection requirement (e.g.,
merging without a passing Pipeline Run in a genuine emergency) requires
Infrastructure Admin approval at Low/Moderate Risk Tier, and
Infrastructure Admin + Security/Compliance at High Risk Tier — this
*is* CCAR-3, not a lookalike of it: a branch-protection override is a
hard-block override of exactly the kind CCAR-3 governs exclusively
("No other role, and no AI Agent/Harness, may grant this override at
any risk tier"), so it does not get its own role assignment.
**Applies to:** Infrastructure Admin role (all tiers), Security/
Compliance role (High tier only), Repository entity type.
**Ties to:** WFPOL-1, CCAR-3.
**Rationale:** This is CCAR-3 applied to this domain's specific hard
block, not a new rule with its own authority. **Corrected 2026-09-23:**
an earlier version of this rule granted the override to Owning Team
Lead while claiming to "reuse CCAR-3's exact escalation shape" —
Owning Team Lead is never a valid override authority under CCAR-3 at
any tier; that was a real authorization-boundary bug, not a wording
issue.

### WFAR-2 — IaC Apply Approval Authority (Scaled by Risk Tier and Target Domain)
**Rule:** Authority to approve a WFPOL-3 IaC Plan before Apply depends on
what the plan provisions:
- **Infrastructure or Networking resources:** Infrastructure Admin.
- **Data Platform resources:** Data Engineer (per Data Platform's own
  DPPAR-1 authority for its resources).
- **High Risk Tier, any target:** the applicable role above, plus
  Security/Compliance.
**Applies to:** Infrastructure Admin role, Data Engineer role
(target-dependent), Security/Compliance role (High tier), Production
environment.
**Ties to:** WFPOL-3.
**Rationale:** IaC is a cross-cutting mechanism (it provisions resources
across multiple domains), so its approval authority routes to whichever
domain actually owns the target resource, rather than this domain
inventing its own generic "infrastructure approver" role that would
duplicate Infrastructure Admin/Data Engineer's existing authority.

### WFAR-3 — Emergency Change Post-Hoc Approval Authority
**Rule:** The post-hoc approval WFPOL-5 requires for an Emergency Change
Request is granted by the same role that would have approved it had it
gone through normal Change Request review (Owning Team Lead for a
Service-scoped change, Infrastructure Admin for an infrastructure-scoped
one, etc.) — WFAR-3 doesn't introduce a new approver, it confirms the
timing (after, not before) is the only thing WFPOL-5 changes about who
approves.
**Applies to:** Owning Team Lead / Infrastructure Admin / Data Engineer
roles (scoped by what the Emergency Change touched), Production
environment, Change Request entity type where Type = Emergency.
**Ties to:** WFPOL-5.
**Rationale:** Keeps approval authority consistent regardless of timing —
an Emergency Change doesn't get a different approver than a Normal one
would have had, only a different sequence, avoiding a scenario where
"emergency" becomes a way to route around the right reviewer rather than
just around the right timing.

---

**Cross-references:**
- WFAR-2 is the first Access Rule in this framework whose authority is
  explicitly conditional on which *other* domain owns the affected
  resource, rather than being scoped to one domain's own roles — a direct
  consequence of Infrastructure as Code being a genuinely cross-cutting
  mechanism.
- WFAR-1 reuses CCAR-3's escalation shape exactly; WFAR-3 reuses whatever
  role each other domain's own Access Rules already established — this
  domain deliberately introduces no new authority pattern of its own.

**Open items:** none for this pass — all three access rules were designed
to close the open items WFPOL-1/3/5 raised, consistent with how every
other domain's Access Rules column has handled its own Policies' open
items.

**Quality bar check (00-framework/quality-bar.md):**
- [x] Simple — 3 domain-specific access rules plus inherited cross-cutting ones
- [x] Modular — WFAR-1/2/3 stand alone from each other and from CCAR-1/2/3
- [x] Easy to update — cross-cutting rules update once, apply here automatically
- [x] Easy to maintain — each rule traces directly to its Policy
- [x] Easy to replace — no new role vocabulary introduced; all authority routes through roles other domains already own
