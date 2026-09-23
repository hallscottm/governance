# Data/Metadata Layer — Risk Tiers

Status: Draft — pending review
Ratified: No
Last updated: 2026-09-22
Provenance: see _qa/09-risk-tiers.qa.md
Built on: 02-taxonomies.md, 04-metadata-standards.md, 06-policies.md, cross-cutting/risk-tiers.md

This is the layer that owns the Data-sensitivity factor referenced
provisionally by Infrastructure, Networking, and System Architecture
since it was first flagged. All three have been retrofitted in this same
session to source it from here — see their Risk Tiers columns.

## Risk Scale

**Extends:** cross-cutting/risk-tiers.md (FIPS 199-aligned Low/Moderate/
High scale — not restated here).

## Determining Factors

A resource's Risk Tier is the **highest** tier triggered by any applicable
factor (cross-cutting maximum rule, per cross-cutting/risk-tiers.md).
Unlike the three prior layers, Sensitivity Level here is not just *a*
factor among several — it's the field every other layer's Data-sensitivity
factor points back to, so its definition is authoritative, not a proxy.

| Factor | Low | Moderate | High |
|---|---|---|---|
| Environment (referenced from Infrastructure) | Dev | Staging/QA | Production |
| Sensitivity Level (`data-sensitivity-level`) | Public or Internal | Confidential | Restricted |
| Contains PII (`data-pii`) | False | — (no Moderate value; PII is binary) | True — automatically High regardless of stated Sensitivity Level |
| Data volume / scale (qualitative) | Small, limited blast radius if compromised | Moderate | Large-scale (e.g., full customer population) — raises consequence severity even at a given Sensitivity Level |

**Note on Contains PII factor:** treated as automatically High when true,
the same categorical treatment Networking gave public exposure (NPOL-3)
and System Architecture gave public-facing services (SAPOL-5) — PII
presence is not a weighted input to average against other factors.

**Note on Data volume/scale factor:** intentionally qualitative, not a
hard numeric threshold — a defensible universal row-count/user-count
cutoff would need org-specific input this generalized framework doesn't
have; included as a factor an org should weigh, not a bright line this
framework draws for them.

## Consequences by Tier

**Extends:** cross-cutting/risk-tiers.md's baseline (two-person sign-off
for High risk, via CCAR-3).

**Layer-specific additions beyond the baseline (already defined in full
in 06-policies.md/07-access-rules.md — summarized here for visibility):**

| Tier | Data/Metadata-Specific Policy Implication |
|---|---|
| **Low** | DPOL-2 (retention period) and DPOL-3 (access approval, if Confidential/Restricted — doesn't apply at Low) still apply as written. |
| **Moderate** | DPOL-3 (Data Owner approval) applies — Confidential is the Moderate-tier trigger. |
| **High** | DPOL-1 (encryption/need-to-know) and DPOL-3 both apply, per Restricted/PII triggering. DPOL-4 (Right to Erasure SLA), where Personal Data is in scope, applies regardless of tier — not scaled, since the SLA is a regulatory-adjacent obligation, not a proportional control. |

---

**Open items:**
- Data volume/scale factor is deliberately left qualitative — see note
  above. An org adopting this framework may want to define its own
  numeric thresholds; this framework does not assert one.
- DPOL-1 and DPOL-3's hard-block/approval-gate status already accounts
  for the Sensitivity Level scaling described here — this table doesn't
  introduce new scaling, only cross-references what 06-policies.md
  already established.

**Quality bar check (00-framework/quality-bar.md):**
- [x] Simple — 4 determining factors, reusing the cross-cutting scale
- [x] Modular — this layer's factor is now the authoritative source
      three other layers reference, not a duplicate parallel scale
- [x] Easy to update — cross-cutting scale updates once, applies here automatically
- [x] Easy to maintain — factors derived from existing Definitions/Metadata Standards
- [x] Easy to replace — standard-grounded (FIPS 199, inherited); volume factor left as org-fillable, not hardcoded
