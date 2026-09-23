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

**Applied to this repository's own governance work (recorded
2026-09-23):** this repository has no separate custom IAM/SSO system —
GitHub's own account authentication is the identity substrate CCAR-4
refers to here. A PR merge performed while signed into GitHub as the
repo owner's real, individual account, with two-factor authentication
enabled (something-you-know + something-you-have — NIST AAL2), and
GitHub's own merge-event record (author, timestamp, and whether a
protection bypass was used) as the audit record, satisfies CCAR-4's
requirement for this deployment — see `implementation/02-github-access.md`
for the mechanics. This assumes 2FA is actually turned on for that
account; if it isn't yet, enable it (GitHub → Settings → Password and
authentication → Two-factor authentication) before relying on this as
AAL2-equivalent. High Risk Tier work would still need step-up/AAL3-
equivalent assurance beyond GitHub's standard 2FA — not yet a gap this
deployment has had to close, since no High-risk action has been routed
through this pipeline.

### CCAR-2 exception: solo-operator deployments (recorded 2026-09-23)

CCAR-2's separation-of-duties requirement assumes the Requester and the
Approver are different people. A deployment run by exactly one person —
this repository, currently — cannot satisfy that literally: the same
individual (hallscottm@gmail.com) originates the request, holds
`ccrole-approver` at the Planning-approval step
(`implementation/01-running-an-engagement.md` step 3), and is the one
GitHub account that reviews and merges every PR. This is a documented,
accepted deviation for this deployment, not a satisfied requirement —
writing it down here is what keeps it from being silently assumed away.

What still holds despite the gap:
- Every change to `main` still passes through a real PR; GitHub's own
  audit trail (author, timestamp, diff, merge event, whether protection
  was bypassed) is real and immutable even when Requester and Approver
  are the same person. Reviewing your own diff before merging is still
  review, even though it is not *independent* review.
- CCAR-3's break-glass two-person High-risk rule is a separate
  requirement from CCAR-2's separation-of-duties rule; this exception
  covers CCAR-2 only. A genuinely High-risk break-glass action under a
  solo deployment would fail CCAR-3 outright (no second Infrastructure
  Admin/Security-Compliance signer exists) and is covered by the
  revisit trigger below, not by this exception.

**Revisit trigger — this exception stops being acceptable when:**
- A second real, independent human joins this repository with a
  legitimate stake in outcomes. At that point real separation of duties
  is achievable, and CCAR-2 applies as written — no exception.
- Any action this framework governs reaches genuine Production
  consequence for a system *other than this governance repository
  itself* (actually provisioning real infrastructure, not documenting
  how one would). At that point CCAR-2's and CCAR-3's requirements are
  not optional, and a second approver must be found before proceeding —
  even if that means pausing the work.

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
