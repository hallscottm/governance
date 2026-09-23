# Q&A Log — Risk Tiers
# Append-only. Do not edit past entries; add new dated entries instead.

## Q9.1 — Risk classification scale
- Type: Judgment (structural) · Required · Human-only
- Options presented: 3-tier FIPS 199-aligned (Low/Moderate/High) / 4-tier
  with Critical / custom
- AI recommendation: 3-tier FIPS 199-aligned — genuine standard, simple
- Human answer: accepted recommended default
- Decision-weight: High (governs risk classification for all future domains)
- Resulting artifact: 09-risk-tiers.md Risk Scale section
- Date answered: 2026-09-22

## Q9.2 — Determining factors, regulatory mapping template, consequences
- Type: Fact/Judgment mix · Bulk-draft-and-veto · AI-draftable
- Drafted: 4 determining factors (Environment, Availability Tier, Data
  sensitivity [provisional], Workload type), a generalized regulatory
  mapping template (not org-specific), and tier-based policy consequences
- Human answer: pending explicit review (drafted, not yet vetted)
- Decision-weight: Medium
- Real inconsistencies surfaced during drafting (not yet resolved):
  1. POL-2/POL-3 are flat "all Production" rules, not Risk-Tier-scaled —
     a High and Moderate resource currently face identical requirements
  2. New two-person sign-off rule for High-tier break-glass overrides
     contradicts AR-2 (07-access-rules.md), which currently says
     Infrastructure Admin alone — AR-2 needs a forward-looking update
- Date answered: 2026-09-22 (drafted; awaiting explicit human review,
  including the two flagged inconsistencies above)

## Q-cc.1 — Retrofit: Risk Scale extracted to cross-cutting registry
- Date: 2026-09-22
- Context: while drafting Networking's Risk Tiers, recognized the FIPS
  199-aligned Risk Scale itself (not the Determining Factors) is fully
  generic. Human confirmed extraction, same pattern as
  Policies/Access Rules/Procedures.
- Resolution: cross-cutting/risk-tiers.md created with the Risk Scale
  table and a baseline Consequences by Tier table; this domain's Risk
  Scale and Consequences by Tier sections updated to "Extends:
  cross-cutting/risk-tiers.md" with only domain-specific additions kept.
- Decision-weight: High (governs Risk Tiers structure for all future domains)
- Date answered: 2026-09-22

## Q-fix.1 — Stale text correction in Consequences by Tier
- Date: 2026-09-22
- Context: while performing the cross-cutting retrofit above, discovered
  the Consequences by Tier table still said "this framework does not
  currently differentiate Moderate from the flat Production rules" — this
  was true when originally written but became stale the moment POL-2/
  POL-3 were updated to scale by Risk Tier earlier the same session. The
  open items section had already been correctly marked resolved; only
  this one table's prose wasn't updated to match.
- Resolution: table corrected to reflect POL-2/POL-3's actual current
  (scaled) requirements per tier, with a note explaining the correction.
- Decision-weight: Low (factual correction, not a new decision)
- Date answered: 2026-09-22

## 2026-09-22 — Retrofit: Data-sensitivity factor resolved

**Context:** Data/Metadata domain (domain 5) drafted; its Sensitivity Level
field (data-sensitivity-level) is now the authoritative source for this
domain's previously provisional/excluded Data-sensitivity Risk Tier
factor.

**Change:** Data-sensitivity factor row now populated with real Low/
Moderate/High values sourced from Data/Metadata, instead of being a
placeholder or an excluded factor. See 05-data-metadata/09-risk-tiers.md
for the authoritative definitions.
