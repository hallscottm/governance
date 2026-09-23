# Q&A Log — Risk Tiers (System Architecture)
# Append-only. Do not edit past entries; add new dated entries instead.

## 2026-09-22 — Q9.1: Determining factors for this domain

**Bucket:** [Standard]/AI-draftable, reusing the already-established
cross-cutting scale and the "highest tier wins" rule.

**Drafted:** 3 populated factors (Environment, Service Tier/Criticality,
Public exposure) plus 1 provisional unpopulated factor (Data handled),
consistent with Infrastructure's and Networking's identical placeholder.
Consequences-by-tier table restated (not newly decided) from SAPOL-2/
SAPOL-5's already-confirmed Risk Tier scaling.

**Status:** Pending explicit review.

## 2026-09-22 — Retrofit: Data-sensitivity factor resolved

**Context:** Data/Metadata domain (domain 5) drafted; its Sensitivity Level
field (data-sensitivity-level) is now the authoritative source for this
domain's previously provisional/excluded Data-sensitivity Risk Tier
factor.

**Change:** Data-sensitivity factor row now populated with real Low/
Moderate/High values sourced from Data/Metadata, instead of being a
placeholder or an excluded factor. See 05-data-metadata/09-risk-tiers.md
for the authoritative definitions.
