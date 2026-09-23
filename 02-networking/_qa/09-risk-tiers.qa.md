# Q&A Log — Risk Tiers
# Append-only. Do not edit past entries; add new dated entries instead.

## Process note
- Extends cross-cutting/risk-tiers.md, extracted from Infrastructure's
  Risk Tiers during this session once Networking needed the identical
  scale. See 01-infrastructure/_qa/09-risk-tiers.qa.md Q-cc.1 for that
  retrofit (which also caught and fixed a stale-text bug, Q-fix.1).

## Q9.1 — Determining factors
- Type: Fact/Judgment mix · Bulk-draft-and-veto · AI-draftable
- 4 factors drafted: Environment (referenced), Network exposure, Trust
  boundary classification, Segmentation posture
- Human answer: pending explicit review
- Decision-weight: Medium
- Date answered: 2026-09-22 (drafted; awaiting explicit human review)

## Q9.2 — Should NPOL-1/NPOL-2 scale by Risk Tier?
- Type: Judgment (org-decision) · Required · Human-only
- Options presented: Apply uniformly, no scaling / Scale down for
  Low-risk
- AI recommendation: Apply uniformly — these are baseline hygiene, not
  proportional controls
- Human answer: explicitly selected recommended default
- Decision-weight: Medium
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
