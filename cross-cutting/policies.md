# Cross-Cutting Policies

Status: Draft — pending review
Ratified: No
Last updated: 2026-09-22

Authored registry (not generated) of policies that are genuinely universal
— they don't depend on any one domain's specific resource types or
standards, only on concepts every domain shares (Environment,
Compute Environment, Cost Center Tag, a metadata field registry, a
provisioning flow). A domain's own Policies column (06-policies.md)
references these rather than restating them, and adds only what's
genuinely specific to that domain.

Not every candidate universal-looking policy belongs here — a rule stays
domain-specific if its content depends on domain-specific standards (e.g.,
Infrastructure's decommissioning policy cites NIST SP 800-88 media
sanitization, which doesn't generalize to, say, a DNS record).

---

### CCP-1 — Metadata Completeness (Production)
**Rule:** A resource classified as Production cannot be provisioned/
registered unless all fields marked "Required" for its entity type in its
owning domain's Metadata Standards (column 4) are present.
**Applies to:** Production environment, any domain.
**Enforcement:** Hard block.
**Originally drafted as:** Infrastructure POL-1 (2026-09-22); generalized
2026-09-22 when Networking's Policies column needed the identical rule.

### CCP-2 — Cost Attribution Required
**Rule:** A resource cannot be provisioned without a valid Cost Center Tag.
**Applies to:** All environments, any domain.
**Enforcement:** Hard block.
**Originally drafted as:** Infrastructure POL-6 (2026-09-22); generalized 2026-09-22.

### CCP-3 — Production Provisioning Approval
**Rule:** Provisioning a Production resource requires approval prior to
creation. Dev and Staging/QA environments are self-service.
**Applies to:** Differentiated by Environment value, any domain.
**Enforcement:** Approval gate — see CCAR-2/CCAR-3 in
cross-cutting/access-rules.md for who approves.
**Originally drafted as:** Infrastructure POL-5 (2026-09-22); generalized 2026-09-22.

### CCP-4 — Agent Accountability Boundary
**Rule:** The Accountable RACI designation on an Engagement (`eng-participant`, engagements/01-definitions.md) must be held by a human, not an Agent, for any Engagement at High Risk Tier — including vision/direction-setting Engagements drafted by an advisory-role Agent. An Agent may hold Responsible, Consulted, or Informed at any Risk Tier.
**Applies to:** Any Agent (`harness-agent`) named on an Engagement's Participants list, High Risk Tier, any domain.
**Enforcement:** Hard block on Engagement Document approval.
**Rationale:** Generalizes CCAR-1's no-self-approval rule and the Requester/Approver separation (CCAR-2) from Production provisioning to accountability for an Engagement's outcome more broadly — accountability is already a human-only category everywhere else in this framework; this closes the gap an advisory/strategic Agent role would otherwise open.
**Originally drafted as:** engagements/07-planning-and-advisory-agents.md's Accountability Boundary (2026-09-23); generalized here since the rule isn't engagements-specific in principle, only first surfaced there. Whether it should flex below High Risk Tier is open — see engagements/09-open-decisions.md #6.

---

**Open items:**
- (Resolved 2026-09-22) cross-cutting/procedures.md created, extracting
  CCPROC-1/2/3/4 from Infrastructure's PROC-1/2/5/6; Infrastructure's
  procedures retrofitted to extend them.
- Whether Risk Tiers (column 9) concepts should also have a cross-cutting
  registry is an open question — Infrastructure's Risk Tiers (FIPS
  199-aligned Low/Moderate/High) is already fairly generic and a strong
  candidate, but not addressed in this pass.

**Quality bar check (00-framework/quality-bar.md):**
- [x] Simple — 3 policies, each genuinely shared, not force-generalized
- [x] Modular — each domain still owns its domain-specific policies independently
- [x] Easy to update — one edit here updates the rule for every referencing domain
- [x] Easy to maintain — "Originally drafted as" line preserves provenance back to first domain
- [x] Easy to replace — domains reference by ID, not by copied text
