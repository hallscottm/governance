# Cross-Cutting Access Rules

Status: Draft — pending review
Ratified: No
Last updated: 2026-09-22

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

---

**Role vocabulary note (resolved 2026-09-22):** Requester, Approver,
Infrastructure Admin, Security/Compliance, and AI Agent/Harness are now
owned by cross-cutting/roles-and-departments/01-definitions.md — see
that file for full definitions, Department membership, and the
Human Role/System Actor distinction (AI Agent/Harness is a System Actor,
not a Human Role).

**Quality bar check (00-framework/quality-bar.md):**
- [x] Simple — 3 access rules, paired 1:1 with cross-cutting policies
- [x] Modular — each domain still owns domain-specific access rules independently
- [x] Easy to update — one edit updates the rule for every referencing domain
- [x] Easy to maintain — "Originally drafted as" line preserves provenance
- [x] Easy to replace — domains reference by ID, not by copied text
