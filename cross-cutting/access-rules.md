# Cross-Cutting Access Rules

Status: Draft — pending review
Ratified: No
Last updated: 2026-09-22

Authored registry of access rules that are genuinely universal, paired
with cross-cutting/policies.md the same way a layer's Access Rules column
(7) pairs with its Policies column (6).

---

### CCAR-1 — AI Agent/Harness Provisioning Authority
**Rule:** An AI agent/harness may draft/request a provisioning action but
may never itself grant final approval for a Production resource. Human
approval (per CCAR-2) is always required for Production, with no AI
exemption from CCP-3.
**Applies to:** AI Agent/Harness actor type, Production environment, any layer.
**Originally drafted as:** Infrastructure AR-1 (2026-09-22); generalized 2026-09-22.

### CCAR-2 — Production Provisioning Approval Authority
**Rule:** Only a designated Approver role may approve a Production
provisioning request. The Requester and Approver must be different actors
(separation of duties) — a Requester cannot approve their own request.
**Applies to:** Approver role, Production environment, any layer.
**Originally drafted as:** Infrastructure AR-3 (2026-09-22); generalized 2026-09-22.

### CCAR-3 — Hard-Block Override (Break-Glass), Risk-Tier-Scaled
**Rule:** An exception overriding a hard-block policy (e.g., CCP-1, CCP-2,
or a layer-specific hard-block policy) for a Production resource requires
sign-off based on the resource's Risk Tier:
- Low or Moderate risk: Infrastructure Admin role alone
- High risk: Infrastructure Admin AND Security/Compliance role (two-person sign-off)
**Applies to:** Infrastructure Admin role (all risk tiers); Security/
Compliance role additionally required for High-risk. No other role, and
no AI Agent/Harness, may grant this override at any risk tier.
**Originally drafted as:** Infrastructure AR-2 (2026-09-22, later revised
same day once Risk Tiers introduced the two-person rule); generalized 2026-09-22.

---

**Provisional role vocabulary note:** same caveat as when these roles were
first introduced in Infrastructure's Access Rules — Requester, Approver,
Infrastructure Admin, Security/Compliance, and AI Agent/Harness remain
provisional plain-text labels pending formal ownership by the
Interface/Human layer once drafted.

**Quality bar check (00-framework/quality-bar.md):**
- [x] Simple — 3 access rules, paired 1:1 with cross-cutting policies
- [x] Modular — each layer still owns layer-specific access rules independently
- [x] Easy to update — one edit updates the rule for every referencing layer
- [x] Easy to maintain — "Originally drafted as" line preserves provenance
- [x] Easy to replace — layers reference by ID, not by copied text
