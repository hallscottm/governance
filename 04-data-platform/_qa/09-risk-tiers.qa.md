# Q&A Log — Risk Tiers
# Append-only. Do not edit past entries; add new dated entries instead.

## 2026-09-22 — Q4.7: Determining factors, sourced from Data/Metadata and System Architecture

**Bucket:** [Standard]/AI-draftable — factors follow the established
cross-domain sourcing pattern (Sensitivity Level/PII from Data/Metadata,
same as Infrastructure/Networking/System Architecture already do).

**Answer:** 4 factors: Environment, Sensitivity Level/PII (sourced from
Data/Metadata), Service Tier/Criticality (sourced from System
Architecture, inherited from the Service a Database backs), Public
exposure (narrower than System Architecture's — flagged as applying
mainly to Vector Database/Streaming Platform, not most Data Platform
resources). No retrofit needed — Data/Metadata's Sensitivity Level
already existed by the time this column was drafted, unlike the first
three domains which needed a later retrofit.

**Status:** Pending explicit review.
