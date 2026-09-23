# Networking Domain — Risk Tiers

Status: Draft — pending review
Ratified: No
Last updated: 2026-09-22
Provenance: see _qa/09-risk-tiers.qa.md
Built on: 02-taxonomies.md, 06-policies.md, cross-cutting/risk-tiers.md

## Risk Scale

**Extends:** cross-cutting/risk-tiers.md (FIPS 199-aligned Low/Moderate/
High scale — not restated here).

## Determining Factors (domain-specific)

A resource's Risk Tier is the **highest** tier triggered by any applicable
factor (cross-cutting averaging rule, per cross-cutting/risk-tiers.md).

| Factor | Low | Moderate | High |
|---|---|---|---|
| Environment (referenced from Infrastructure) | Dev | Staging/QA | Production |
| Network exposure | Internal-only (`net-network-zone` fully internal) | Cross-zone, internal boundary crossing | Publicly internet-facing (triggers NPOL-3) |
| Trust boundary classification | N/A | Inside a defined trust boundary | Crossing or undefined trust boundary (`net-trust-boundary`) |
| Segmentation posture | Micro-segmented (`net-microsegmentation`) | Zone-segmented (`net-network-zone`) | Flat/unsegmented |
| Data sensitivity of traffic carried (referenced from Data/Metadata, `data-sensitivity-level`) | Public or Internal | Confidential | Restricted, or Contains PII = true |

**Note on Network exposure factor:** public internet-facing exposure is
automatically High risk, not just a triggering factor to weigh — this is
consistent with NPOL-3 treating public exposure as categorically
different, deserving its own approval step regardless of other factors.

## Consequences by Tier

**Extends:** cross-cutting/risk-tiers.md's baseline (two-person sign-off
for High risk, via CCAR-3).

**Domain-specific additions beyond the baseline:**

| Tier | Networking-Specific Policy Implication |
|---|---|
| **Low** | NPOL-1 (default-deny) and NPOL-2 (encryption in transit) still apply — these are not risk-tier-scaled, unlike Infrastructure's POL-2/POL-3. |
| **Moderate** | Same as Low. |
| **High** | Same as Low/Moderate, plus: NPOL-3's public-exposure approval (NAR-1) is required whenever Network exposure factor is High, which by definition it always is at this tier. |

---

**Open items:**
- (Resolved 2026-09-22) Confirmed: NPOL-1/NPOL-2 apply uniformly
  regardless of Risk Tier — a default-deny posture and encryption
  requirement are baseline security hygiene, not proportional controls
  that should relax for lower-risk resources.
- (Resolved 2026-09-22) Data sensitivity factor added, sourced from
  Data/Metadata's Sensitivity Level field, now that domain is drafted —
  network exposure/trust boundary factors remain as additional
  network-specific factors, not a substitute for this one.

**Quality bar check (00-framework/quality-bar.md):**
- [x] Simple — 4 determining factors, reusing the cross-cutting scale
- [x] Modular — domain-specific factors independent of Infrastructure's
- [x] Easy to update — cross-cutting scale updates once, applies here automatically
- [x] Easy to maintain — factors derived from existing Definitions terms
- [x] Easy to replace — standard-grounded (FIPS 199, inherited)
