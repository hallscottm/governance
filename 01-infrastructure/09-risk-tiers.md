# Infrastructure Layer — Risk Tiers

Status: Draft — pending review
Ratified: No
Last updated: 2026-09-22
Provenance: see _qa/09-risk-tiers.qa.md
Built on: 02-taxonomies.md, 06-policies.md
Standard: NIST FIPS 199 (Standards for Security Categorization of Federal
Information and Information Systems)

---

## Risk Scale

**Extends:** cross-cutting/risk-tiers.md (see that file for the FIPS
199-aligned Low/Moderate/High scale and its general interpretation — not
restated here as of 2026-09-22).

## Determining Factors

A resource's Risk Tier is the **highest** tier triggered by any applicable
factor below (risk tier is not averaged — one high-risk factor is enough
to elevate the whole resource).

| Factor | Low | Moderate | High |
|---|---|---|---|
| Environment (`infra-environment-lifecycle`) | Dev | Staging/QA | Production |
| Availability Tier (`infra-availability-tier-*`) | Tier I–II | Tier III | Tier IV |
| Data sensitivity (`data-sensitivity-level`) | Public or Internal | Confidential | Restricted, or Contains PII = true regardless of stated classification |
| Workload type | General compute | — | AI Training/Inference on regulated data (`infra-training-workload`, `infra-inference-workload`) |

**Data sensitivity note (resolved 2026-09-22):** this factor is now
sourced from Data/Metadata's Sensitivity Level field
(04-data-metadata/04-metadata-standards.md), the layer that actually owns
data classification. A resource holding data classified Restricted, or
flagged Contains PII, is High risk regardless of its own layer-specific
factors — same "highest tier wins" rule applied across layers.

## Regulatory Mapping (generalized — org fills in applicable regimes)

This framework is generalized and doesn't presume any org's specific
regulatory exposure. The table below is a placeholder structure — an org
adopting this framework fills in which regimes apply to which Risk Tier.

| Regime (example, not exhaustive) | Typical trigger | Applies at Risk Tier |
|---|---|---|
| HIPAA | Protected health information present | High (typically) |
| PCI-DSS | Payment card data present | High (typically) |
| GDPR / state privacy law | EU or covered-state personal data present | Moderate–High depending on data volume/sensitivity |
| SOX | Financial reporting systems | Moderate–High depending on materiality |
| (org-specific / none) | — | — |

## Consequences by Tier

**Extends:** cross-cutting/risk-tiers.md's baseline Consequences by Tier
(the two-person sign-off rule for High risk lives there now, via CCAR-3 —
not restated here).

**Layer-specific additions beyond the baseline:**

| Tier | Infrastructure-Specific Policy Implication |
|---|---|
| **Low** | POL-2 requires Availability Tier II minimum; POL-3 recommends (does not require) a DR Tier. |
| **Moderate** | POL-2 requires Availability Tier III minimum; POL-3 requires a DR Tier. (Corrected 2026-09-22 — an earlier version of this table said Moderate wasn't differentiated from flat Production rules; that was resolved when POL-2/POL-3 were updated to scale by Risk Tier, but this table wasn't updated to match until now.) |
| **High** | POL-2 requires Availability Tier IV minimum; POL-3 requires a DR Tier. |

---

**Open items:**
- (Resolved 2026-09-22) POL-2/POL-3 updated in 06-policies.md to scale
  with Risk Tier instead of applying flatly to all Production.
- (Resolved 2026-09-22) AR-2 in 07-access-rules.md updated to require
  two-person sign-off (Infrastructure Admin + Security/Compliance) for
  High-risk break-glass overrides.
- (Resolved 2026-09-22) Data sensitivity factor now sourced from Data/Metadata's Sensitivity Level field, once that layer was drafted.
- Regulatory mapping table is intentionally a template, not filled with
  real determinations — an org applying this framework completes it for
  their actual regulatory exposure.

**Quality bar check (00-framework/quality-bar.md):**
- [x] Simple — 3-tier scale, one determining-factor table, one consequence table
- [x] Modular — regulatory mapping is a fill-in template, doesn't hardcode assumptions
- [x] Easy to update — new determining factors are new table rows
- [x] Easy to maintain — tier is derived from existing terms (Environment,
      Availability Tier), not a new parallel classification
- [x] Easy to replace — standard-grounded (FIPS 199), not a custom scale
