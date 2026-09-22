# Infrastructure Layer — Access Rules

Status: Draft — pending review
Ratified: No
Last updated: 2026-09-22
Provenance: see _qa/07-access-rules.qa.md
Built on: 06-policies.md

Defines who/what can act on the rules established in Policies (column 6).

## Provisional Role Vocabulary

Roles referenced below are provisional plain-text labels, not yet formal
owned terms with anchor IDs. Role definitions properly belong to the
Interface/Human layer (07-interface-human), not yet drafted (row-major
traversal — we're still on layer 1). Once that layer exists, these
references should be converted to proper cross-layer links per
00-framework/term-linking-convention.md, with Interface/Human as owner.
Flagged here so this isn't lost.

| Role (provisional) | Description |
|---|---|
| **Requester** | Anyone requesting/initiating provisioning of a resource. |
| **Approver** | A role, distinct from Requester, authorized to approve Production provisioning. |
| **Infrastructure Admin** | Role with override/exception authority for hard-blocked policies. |
| **Security/Compliance Role** | Role authorized to certify compliance-sensitive actions (e.g., sanitization). |
| **AI Agent/Harness** | An AI system acting within a defined harness scope — treated as a first-class actor type, not a human role, with its own permission boundary. |

---

## Access Rules

### AR-1 — AI Agent Provisioning Authority
**Rule:** An AI agent/harness may draft/request a provisioning action but
may never itself grant final approval for a Production resource. Human
approval (per AR-3) is always required for Production, with no AI
exemption from POL-5.
**Applies to:** AI Agent/Harness actor type, Production environment.
**Ties to:** POL-5.

### AR-2 — Hard-Block Override (Break-Glass)
**Rule:** An exception overriding POL-1 (metadata completeness), POL-2
(Availability Tier minimum), or POL-6 (cost tag requirement) for a
Production resource requires sign-off based on the resource's Risk Tier
(09-risk-tiers.md):
- Low or Moderate risk: Infrastructure Admin role alone
- High risk: Infrastructure Admin AND Security/Compliance role (two-person
  sign-off)
**Applies to:** Infrastructure Admin role (all risk tiers); Security/
Compliance role additionally required for High-risk. No other role, and
no AI Agent/Harness, may grant this override at any risk tier.
**Ties to:** POL-1, POL-2, POL-6, and 09-risk-tiers.md's Consequences by
Tier section.
**Revision note:** originally Infrastructure Admin alone, regardless of
risk tier; revised 2026-09-22 once Risk Tiers (column 9) introduced a
two-person requirement for High-risk overrides — this rule is now
risk-tier-aware to stay consistent.

### AR-3 — Production Provisioning Approval
**Rule:** Only the Approver role may approve a Production provisioning
request. The Requester and Approver must be different actors (separation
of duties) — a Requester cannot approve their own request.
**Applies to:** Approver role, Production environment.
**Ties to:** POL-5.

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
- Role vocabulary above is provisional (see note at top) — pending formal
  ownership transfer to Interface/Human layer once drafted.
- No access rule yet defined for who may set/change a resource's DR Tier
  classification (POL-3). Revisit once Interface/Human layer clarifies
  role structure, or address directly if it becomes urgent before then.
- AI Agent/Harness is treated here as a single generic actor type; once
  the Harness layer (06-harness) is drafted, this will likely need to
  differentiate between harness scopes/roles rather than one flat
  "AI Agent" category.

**Quality bar check (00-framework/quality-bar.md):**
- [x] Simple — 4 access rules, each tied to exactly one or more named policies
- [x] Modular — each rule stands alone; changing AR-2 doesn't affect AR-3
- [x] Easy to update — role vocabulary is provisional and explicitly
      flagged for future migration, not hard-locked into this layer
- [x] Easy to maintain — every rule traces to a specific Policy; no
      free-floating access rules
- [x] Easy to replace — AI Agent/Harness treated as a distinct actor type
      from the start, so this doesn't need retrofitting later
