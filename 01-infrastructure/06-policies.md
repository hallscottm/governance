# Infrastructure Layer — Policies

Status: Draft — pending review
Ratified: No
Last updated: 2026-09-22
Provenance: see _qa/06-policies.qa.md
Built on: 01-definitions.md, 04-metadata-standards.md

Unlike prior columns, these are genuine organizational decisions, not
standards lookups — each was answered as a real question, not bulk-
drafted. See _qa/06-policies.qa.md for the full reasoning trail.

---

### POL-1 — Metadata Completeness (Production)
**Extends:** CCP-1 (cross-cutting/policies.md)
**Rule:** As CCP-1, applied to this layer's entity types per
04-metadata-standards.md.
**Applies to:** Production environment only (per `infra-environment-lifecycle`).
**Enforcement:** Hard block.
**Rationale:** Guarantees AI/tooling consuming this metadata can trust
completeness for the environment where it matters most.
**Revision note:** originally fully restated here; converted to extend
CCP-1 on 2026-09-22 once Networking needed the identical rule — this is
the first application of a cross-cutting policy, and CCP-1's "Originally
drafted as" note traces back to this entry.

### POL-2 — Minimum Availability Tier (Production, scaled by Risk Tier)
**Rule:** Production resources must meet a minimum Availability Tier
based on their Risk Tier classification (09-risk-tiers.md):
- Low risk: Tier II (`infra-availability-tier-ii`) minimum
- Moderate risk: Tier III (`infra-availability-tier-iii`) minimum
- High risk: Tier IV (`infra-availability-tier-iv`) minimum
**Applies to:** Production environment only; threshold varies by Risk Tier.
**Enforcement:** Hard block (implied — same enforcement posture as POL-1;
explicit mechanism to be detailed in Procedures, column 8).
**Rationale:** Originally a flat Tier III minimum; revised 2026-09-22
after drafting Risk Tiers (column 9) surfaced that a flat rule doesn't
differentiate a High-risk resource from a Moderate-risk one. Scaling by
Risk Tier keeps the Availability requirement proportionate to actual
consequence of failure, per Uptime Institute Tier Classification.

### POL-3 — Disaster Recovery Tier (Production, scaled by Risk Tier)
**Rule:** Every Production resource must have a defined DR Tier
(`infra-dr-tier`), with requirement strength based on Risk Tier
(09-risk-tiers.md):
- Low risk: Recommended, not required
- Moderate risk: Required
- High risk: Required
**Applies to:** Production environment only; requirement strength varies
by Risk Tier.
**Enforcement:** Required field for Moderate/High; recommended-only for
Low. Enforcement mechanism TBD in Procedures (column 8).
**Rationale:** Originally a flat "required for all Production" rule;
revised 2026-09-22 once Risk Tiers (column 9) existed to differentiate
against, avoiding the earlier problem of needing an undefined
"criticality" concept — Risk Tier now serves that role.

### POL-4 — Decommissioning Sanitization
**Rule:** Storage sanitization prior to disposal or reuse must comply with
NIST SP 800-88 (Media Sanitization).
**Applies to:** All environments (sanitization applies regardless of
environment tier — data exposure risk doesn't scale down with environment).
**Enforcement:** Procedural (detailed in column 8); this policy establishes
the required standard.
**Rationale:** Recommended default accepted — consistent with the standard
already cited for `infra-decommissioning` in Definitions; defensible for
audits.

### POL-5 — Provisioning Approval
**Extends:** CCP-3 (cross-cutting/policies.md)
**Rule:** As CCP-3, applied to this layer's resources.
**Applies to:** Differentiated by `infra-environment-lifecycle` value.
**Enforcement:** Approval gate (who approves: deferred to Access Rules,
column 7 — see CCAR-1/CCAR-2 in cross-cutting/access-rules.md; how
approval is requested/granted: deferred to Procedures, column 8).
**Rationale:** Explicitly chosen — balances safety where it matters
(Production) against not adding friction to dev/staging experimentation,
consistent with the project's original anti-burnout goal.
**Revision note:** converted to extend CCP-3 on 2026-09-22, same
retrofit as POL-1.

### POL-6 — Cost Center Tag Enforcement
**Extends:** CCP-2 (cross-cutting/policies.md)
**Rule:** As CCP-2, applied to this layer's resources.
**Applies to:** All environments (Cost Center Tag is "Required — always"
in Metadata Standards; this policy makes that enforceable rather than
aspirational).
**Enforcement:** Hard block.
**Rationale:** Explicitly chosen — keeps the Policies column consistent
with Metadata Standards' existing "Required" designation rather than
letting a required field go unenforced.
**Revision note:** converted to extend CCP-2 on 2026-09-22, same
retrofit as POL-1/POL-5.

---

**Cross-references:**
- POL-1, POL-6 directly enforce fields already marked Required in
  04-metadata-standards.md — this policy column is what makes those
  requirements real rather than descriptive.
- POL-2, POL-3 apply only to Production; Dev/Staging are intentionally
  left unconstrained on these two policies (not stated as a gap — a
  deliberate choice to avoid slowing down non-production work).
- POL-5's "who approves" and "how" are explicitly deferred to Access
  Rules (column 7) and Procedures (column 8) — this is intentional
  column separation, not an omission.

**Open items:**
- Enforcement *mechanism* (how a hard block is technically implemented —
  e.g., an IaC policy-as-code gate, a CI check) is deferred to Procedures
  (column 8) and/or Tooling (column 10).
- No policy yet defined for Dev/Staging Availability Tier or DR Tier —
  deliberate scope limit for this pass, revisit if a real need surfaces.

**Quality bar check (00-framework/quality-bar.md):**
- [x] Simple — 6 policies, each one rule, no compound/nested conditions
- [x] Modular — each policy stands alone; changing POL-2 doesn't affect POL-3
- [x] Easy to update — policies are independently versionable statements
- [x] Easy to maintain — each policy traces to a specific term/field, not free-floating
- [x] Easy to replace — enforcement mechanism intentionally deferred, so policy intent survives a future tooling change
