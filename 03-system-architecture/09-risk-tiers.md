# System Architecture Layer — Risk Tiers

Status: Draft — pending review
Ratified: No
Last updated: 2026-09-22
Provenance: see _qa/09-risk-tiers.qa.md
Built on: 02-taxonomies.md, 04-metadata-standards.md, 06-policies.md, cross-cutting/risk-tiers.md

## Risk Scale

**Extends:** cross-cutting/risk-tiers.md (FIPS 199-aligned Low/Moderate/
High scale — not restated here).

## Determining Factors (layer-specific)

A resource's Risk Tier is the **highest** tier triggered by any applicable
factor (cross-cutting maximum rule, per cross-cutting/risk-tiers.md).

| Factor | Low | Moderate | High |
|---|---|---|---|
| Environment (referenced from Infrastructure) | Dev | Staging/QA | Production |
| Service Tier / Criticality (04-metadata-standards.md) | Non-critical, internal tooling | Business-important, moderate user impact if down | Business-critical, severe impact if down |
| Public exposure | Internal-only (no public Endpoint) | N/A — this factor has no Moderate value | Publicly internet-facing (triggers SAPOL-5, and Networking's NPOL-3) |
| Data handled (referenced from Data/Metadata, `data-sensitivity-level`) | Public or Internal | Confidential | Restricted, or Contains PII = true |

**Note on Public exposure factor:** same treatment as Networking's
identical factor — public internet-facing exposure is automatically High
risk, not just a weighted input, consistent with SAPOL-5 and NPOL-3 both
treating public exposure as categorically different.

**Note on Data handled factor (resolved 2026-09-22):** now sourced from
Data/Metadata's Sensitivity Level field for whatever Dataset(s) this
Service/Database handles — a Service handling Restricted data, or data
flagged Contains PII, is High risk regardless of its own Service
Tier/Criticality or exposure factors, same "highest tier wins" rule.

## Consequences by Tier

**Extends:** cross-cutting/risk-tiers.md's baseline (two-person sign-off
for High risk, via CCAR-3).

**Layer-specific additions beyond the baseline (already defined in full
in 06-policies.md/07-access-rules.md — summarized here for visibility):**

| Tier | System Architecture-Specific Policy Implication |
|---|---|
| **Low** | SAPOL-2 migration review: peer review only. SAPOL-5 (if public-facing): ASVS L1, Owning Team Lead self-attestation. |
| **Moderate** | SAPOL-2: peer review + Owning Team Lead sign-off. SAPOL-5 (if public-facing): ASVS L2, Owning Team Lead attestation + Security/Compliance review. |
| **High** | SAPOL-2: peer review + Owning Team Lead sign-off + documented rollback plan. SAPOL-5 (if public-facing): ASVS L3, mandatory independent Security/Compliance verification. SAPOL-1, SAPOL-3, SAPOL-4 hard blocks apply uniformly at every tier (not scaled), same treatment as Networking's NPOL-1/NPOL-2. |

---

**Open items:**
- (Resolved 2026-09-22) Data handled/sensitivity factor populated,
  sourced from Data/Metadata's Sensitivity Level field — resolved in one
  pass across all three prior layers (Infrastructure, Networking, System
  Architecture) once Data/Metadata was drafted, as anticipated.
- SAPOL-1, SAPOL-3, SAPOL-4 confirmed uniform (not Risk-Tier-scaled) by
  design during Policies drafting — restated here for consistency with
  how Networking's Risk Tiers column documents the same kind of decision.

**Quality bar check (00-framework/quality-bar.md):**
- [x] Simple — 4 determining factors (1 unpopulated placeholder), reusing the cross-cutting scale
- [x] Modular — layer-specific factors independent of Infrastructure's and Networking's
- [x] Easy to update — cross-cutting scale updates once, applies here automatically
- [x] Easy to maintain — factors derived from existing Definitions/Metadata Standards
- [x] Easy to replace — standard-grounded (FIPS 199, inherited)
