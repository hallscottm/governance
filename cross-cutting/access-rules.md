# Cross-Cutting Access Rules

Status: Draft — pending review
Ratified: No
Last updated: 2026-09-23

Authored registry of access rules that are genuinely universal, paired
with cross-cutting/policies.md the same way a domain's Access Rules column
(7) pairs with its Policies column (6).

Role names below (AI Agent/Harness, Approver, Requester, Infrastructure
Admin, Security/Compliance) are now real, anchored terms owned by
cross-cutting/roles-and-departments/01-definitions.md — retrofitted
2026-09-22, replacing the "provisional role vocabulary" note this file
carried since Infrastructure was first drafted.

---

### CCAR-1 — AI Agent/Harness Provisioning Authority
**Rule:** An AI agent/harness may draft/request a provisioning action but
may never itself grant final approval for a Production resource. Human
approval (per CCAR-2) is always required for Production, with no AI
exemption from CCP-3.
**Applies to:** AI Agent/Harness actor type ([ccrole-ai-agent-harness](roles-and-departments/01-definitions.md#ccrole-ai-agent-harness)), Production environment, any domain.
**Originally drafted as:** Infrastructure AR-1 (2026-09-22); generalized 2026-09-22.

### CCAR-2 — Production Provisioning Approval Authority
**Rule:** Only a designated Approver role may approve a Production
provisioning request. The Requester and Approver must be different actors
(separation of duties) — a Requester cannot approve their own request.
**Applies to:** Approver role ([ccrole-approver](roles-and-departments/01-definitions.md#ccrole-approver)), distinct from Requester ([ccrole-requester](roles-and-departments/01-definitions.md#ccrole-requester)), Production environment, any domain.
**Originally drafted as:** Infrastructure AR-3 (2026-09-22); generalized 2026-09-22.

### CCAR-3 — Hard-Block Override (Break-Glass), Risk-Tier-Scaled
**Rule:** An exception overriding a hard-block policy (e.g., CCP-1, CCP-2,
or a domain-specific hard-block policy) for a Production resource requires
sign-off based on the resource's Risk Tier:
- Low or Moderate risk: Infrastructure Admin role alone
- High risk: Infrastructure Admin AND Security/Compliance role (two-person sign-off)
**Applies to:** Infrastructure Admin role ([ccrole-infrastructure-admin](roles-and-departments/01-definitions.md#ccrole-infrastructure-admin), all risk tiers); Security/
Compliance role ([ccrole-security-compliance](roles-and-departments/01-definitions.md#ccrole-security-compliance)) additionally required for High-risk. No other role, and
no AI Agent/Harness, may grant this override at any risk tier.
**Originally drafted as:** Infrastructure AR-2 (2026-09-22, later revised
same day once Risk Tiers introduced the two-person rule); generalized 2026-09-22.

### CCAR-4 — Approval Identity Assurance
**Rule:** An Approval Gate decision, a CCAR-2 Production approval, or
any `approved_by`/Accountable designation recorded anywhere in this
framework must resolve to an identity authenticated through the
organization's own IAM/SSO system — never asserted by name or role
alone. High Risk Tier decisions require step-up (re-)authentication at
the moment of approval (NIST SP 800-63B Authenticator Assurance
Level 2 minimum; AAL3 recommended). The audit record (Harness's Agent
Trace/Transcript, `harness-trace`, or the relevant Engagement
Document's Approval log) must capture the authentication method and
timestamp, not the approver's name alone.
**Applies to:** Every Approval Gate ([harness-approval-gate](../08-harness/01-definitions.md#harness-approval-gate)),
CCAR-2/CCAR-3 sign-off, and Engagement Document `approved_by` field,
any domain — assurance strength scales with Risk Tier the same way
CCAR-3's sign-off count does.
**Enforcement:** Hard block — an approval recorded without a
resolvable authenticated identity is not a valid approval and does not
satisfy CCAR-1/CCAR-2.
**Distinct from:** System Architecture's Authentication
([sysarch-authentication](../03-system-architecture/01-definitions.md#sysarch-authentication)),
which is a Service verifying a caller's identity generally — CCAR-4
is specifically about the identity behind a governance approval
decision.
**Not built here:** the actual IAM/SSO/MFA mechanism — this framework
governs the requirement, not the implementation; use the
organization's existing identity provider rather than a parallel one,
same build-vs-buy posture as engagements/00-standards-alignment.md.
**Originally drafted as:** raised directly during the Engagements
review ("how do we verify the Approver is actually the Approver") —
generalized here since it constrains every approval gate in the
framework, not only Engagements.

---

**Role vocabulary note (resolved 2026-09-22):** Requester, Approver,
Infrastructure Admin, Security/Compliance, and AI Agent/Harness are now
owned by cross-cutting/roles-and-departments/01-definitions.md — see
that file for full definitions, Department membership, and the
Human Role/System Actor distinction (AI Agent/Harness is a System Actor,
not a Human Role).

**Quality bar check (00-framework/quality-bar.md):**
- [x] Simple — 4 access rules; CCAR-1/2/3 pair 1:1 with cross-cutting policies, CCAR-4 stands alone (identity-assurance is a cross-cutting requirement, not a new policy)
- [x] Modular — each domain still owns domain-specific access rules independently
- [x] Easy to update — one edit updates the rule for every referencing domain
- [x] Easy to maintain — "Originally drafted as" line preserves provenance
- [x] Easy to replace — domains reference by ID, not by copied text
