# Infrastructure Domain — Access Rules

Status: Draft — pending review
Ratified: No
Last updated: 2026-09-22
Provenance: see _qa/07-access-rules.qa.md
Built on: 06-policies.md

Defines who/what can act on the rules established in Policies (column 6).

## Role Vocabulary (resolved 2026-09-22)

Roles referenced below are real, anchored terms owned by
cross-cutting/roles-and-departments/01-definitions.md, retrofitted
2026-09-22 — this section previously carried a provisional plain-text
table pending the Interface/Human domain; Roles & Departments was
established as a cross-cutting pillar instead, resolving this earlier
than row-major order would have.

- **Requester** — [cross-cutting/roles-and-departments/01-definitions.md#ccrole-requester](../cross-cutting/roles-and-departments/01-definitions.md#ccrole-requester)
- **Approver** — [cross-cutting/roles-and-departments/01-definitions.md#ccrole-approver](../cross-cutting/roles-and-departments/01-definitions.md#ccrole-approver)
- **Infrastructure Admin** — [cross-cutting/roles-and-departments/01-definitions.md#ccrole-infrastructure-admin](../cross-cutting/roles-and-departments/01-definitions.md#ccrole-infrastructure-admin)
- **Security/Compliance** — [cross-cutting/roles-and-departments/01-definitions.md#ccrole-security-compliance](../cross-cutting/roles-and-departments/01-definitions.md#ccrole-security-compliance)
- **AI Agent/Harness** — [cross-cutting/roles-and-departments/01-definitions.md#ccrole-ai-agent-harness](../cross-cutting/roles-and-departments/01-definitions.md#ccrole-ai-agent-harness)

---

## Access Rules

### AR-1 — AI Agent Provisioning Authority
**Extends:** CCAR-1 (cross-cutting/access-rules.md)
**Rule:** As CCAR-1, applied to this domain.
**Applies to:** AI Agent/Harness actor type, Production environment.
**Ties to:** POL-5 (which extends CCP-3).
**Revision note:** converted to extend CCAR-1 on 2026-09-22, first
application of a cross-cutting access rule.

### AR-2 — Hard-Block Override (Break-Glass)
**Extends:** CCAR-3 (cross-cutting/access-rules.md)
**Rule:** As CCAR-3, applied to this domain's hard-block policies (POL-1,
POL-2, POL-6).
**Applies to:** Infrastructure Admin role (all risk tiers); Security/
Compliance role additionally required for High-risk. No other role, and
no AI Agent/Harness, may grant this override at any risk tier.
**Ties to:** POL-1, POL-2, POL-6, and 09-risk-tiers.md's Consequences by
Tier section.
**Revision note:** originally Infrastructure Admin alone, regardless of
risk tier; revised 2026-09-22 once Risk Tiers (column 9) introduced a
two-person requirement for High-risk overrides. Converted to extend
CCAR-3 later the same day once Networking needed the identical rule.

### AR-3 — Production Provisioning Approval
**Extends:** CCAR-2 (cross-cutting/access-rules.md)
**Rule:** As CCAR-2, applied to this domain.
**Applies to:** Approver role, Production environment.
**Ties to:** POL-5 (which extends CCP-3).
**Revision note:** converted to extend CCAR-2 on 2026-09-22.

### AR-4 — Decommissioning Sanitization Sign-off
**Rule:** Completion of NIST SP 800-88 sanitization must be certified by
either the Infrastructure Admin role or a designated Security/Compliance
role — never self-certified by the Requester.
**Applies to:** Infrastructure Admin or Security/Compliance role, all
environments (POL-4 applies to all environments, not just Production).
**Ties to:** POL-4.

---

**Cross-references:**
- AR-1 and AR-3 together fully resolve POL-5's "who approves" gap left
  open in the Policies column.
- AR-2 fully resolves the enforcement-exception gap for POL-1/POL-2/POL-6.
- AR-4 fully resolves POL-4's "who certifies" gap.
- POL-3 (DR Tier required) has no dedicated Access Rule yet — defining a
  DR Tier is currently unconstrained as to who can set it. Flagged as an
  open item below rather than silently assumed.

**Open items:**
- (Resolved 2026-09-22) Role vocabulary now owned by cross-cutting/
  roles-and-departments/, resolved earlier than the original plan of
  waiting for the Interface/Human domain.
- No access rule yet defined for who may set/change a resource's DR Tier
  classification (POL-3). Role structure is already owned by
  cross-cutting/roles-and-departments/ (Interface/Human, the domain this
  item originally deferred to, was folded into that pillar 2026-09-22 —
  see its 00-qa.md Q11); revisit directly against that registry, or
  address now if it becomes urgent before then.
- AI Agent/Harness is treated here as a single generic actor type; once
  the Harness domain (08-harness) is drafted, this will likely need to
  differentiate between harness scopes/roles rather than one flat
  "AI Agent" category.

**Quality bar check (00-framework/quality-bar.md):**
- [x] Simple — 4 access rules, each tied to exactly one or more named policies
- [x] Modular — each rule stands alone; changing AR-2 doesn't affect AR-3
- [x] Easy to update — role vocabulary is owned centrally by
      cross-cutting/roles-and-departments/, not hard-locked into this domain
- [x] Easy to maintain — every rule traces to a specific Policy; no
      free-floating access rules
- [x] Easy to replace — AI Agent/Harness treated as a distinct actor type
      from the start, so this doesn't need retrofitting later
