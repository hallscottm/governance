# Q&A Log — Risk Tiers
# Append-only. Do not edit past entries; add new dated entries instead.

## Q9.1 — Risk classification scale
- Type: Judgment (structural) · Required · Human-only
- Options presented: 3-tier FIPS 199-aligned (Low/Moderate/High) / 4-tier
  with Critical / custom
- AI recommendation: 3-tier FIPS 199-aligned — genuine standard, simple
- Human answer: accepted recommended default
- Decision-weight: High (governs risk classification for all future layers)
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
