# Business Intelligence / Reporting Domain — Risk Tiers

Status: Draft — pending review
Ratified: No
Last updated: 2026-09-22
Provenance: see _qa/09-risk-tiers.qa.md
Built on: 02-taxonomies.md, 04-metadata-standards.md, 06-policies.md, cross-cutting/risk-tiers.md

## Risk Scale

**Extends:** cross-cutting/risk-tiers.md (FIPS 199-aligned Low/Moderate/
High scale — not restated here).

## Determining Factors

A resource's Risk Tier is the **highest** tier triggered by any applicable
factor (cross-cutting maximum rule, per cross-cutting/risk-tiers.md).

| Factor | Low | Moderate | High |
|---|---|---|---|
| Environment (referenced from Infrastructure) | Dev | Staging/QA, Production | — (Environment alone never reaches High; see note below) |
| Sensitivity Level / Contains PII (referenced from Data/Metadata) | Public or Internal, no PII | Confidential | Restricted, or Contains PII = true |
| Distribution Scope (04-metadata-standards.md) | Internal | Departmental | Organization-wide or External |
| Certification Status (04-metadata-standards.md) | N/A at Internal scope | Draft, at Departmental scope | Draft, if somehow paired with wider scope — should be structurally prevented by BIPOL-1, so this combination flags a policy violation rather than a normal risk state |

**Note on Environment factor (corrected 2026-09-23):** Production alone
caps this factor at Moderate, matching cross-cutting/risk-tiers.md's own
stated interpretation ("Most Production resources... Moderate"). An
earlier version of this table put Production directly in the High
column, which combined with the cross-domain "highest tier wins" rule
meant every Production resource in every domain was automatically High
regardless of any other factor — contradicting cross-cutting's own
description of itself. High still requires Production *plus* another
High-triggering factor from this table (data sensitivity, public
exposure, business-criticality, etc., depending on domain) — Environment
alone is never sufficient.

**Note on Distribution Scope factor:** this is the domain-defining factor
— unlike every prior domain's Risk Tiers, where "who can see this" is
governed by Access Rules rather than Risk Tiers directly, this domain's
entire purpose is about audience reach, so Distribution Scope earns a
place as a first-class Risk Tier factor rather than staying purely an
Access Rules concern.

**Note on Certification Status factor:** included mainly as a
cross-check, not a genuinely independent risk input — BIPOL-1 already
structurally prevents a Draft report from reaching Organization-wide/
External scope, so a resource in that combined state indicates the
policy was bypassed (e.g. via CCPROC-4 break-glass) rather than a normal
risk gradient. Flagged distinctly from every other factor in this
framework for that reason.

## Consequences by Tier

**Extends:** cross-cutting/risk-tiers.md's baseline (two-person sign-off
for High risk, via CCAR-3).

**Domain-specific additions beyond the baseline (already defined in full
in 06-policies.md/07-access-rules.md — summarized here for visibility):**

| Tier | Business Intelligence / Reporting-Specific Policy Implication |
|---|---|
| **Low** | BIPOL-3 (Row-Level Security): not required (Sensitivity Level below Confidential). |
| **Moderate** | BIPOL-3: required, BI Analyst/Developer self-attestation (Confidential tier). BIPOL-1: Certified status required once Distribution Scope reaches Organization-wide/External. |
| **High** | BIPOL-3: required, mandatory independent Security/Compliance verification (Restricted/PII tier). BIPOL-1, BIPOL-2, BIPOL-4 hard blocks apply uniformly at every tier (not scaled), same treatment established across every other domain's uniform hard blocks. |

---

**Open items:**
- (Resolved 2026-09-23) Environment factor corrected: Production alone
  now caps at Moderate, not High — see the note under Determining Factors.
- Distribution Scope as a Risk Tier factor is a genuine departure from
  this framework's established pattern (every prior domain treats "who
  can see this" as an Access Rules concern, not a Risk Tiers one) —
  flagged explicitly as a deliberate domain-specific choice, not an
  inconsistency to reconcile.
- The Certification Status factor's "flags a policy violation" case has
  no defined automated response yet (e.g., should it trigger an alert,
  auto-revert Distribution Scope?) — deferred to Tooling (column 10).

**Quality bar check (00-framework/quality-bar.md):**
- [x] Simple — 4 determining factors, reusing the cross-cutting scale
- [x] Modular — domain-specific factors independent of every other domain's
- [x] Easy to update — cross-cutting scale updates once, applies here automatically
- [x] Easy to maintain — factors derived from existing Definitions/Metadata Standards
- [x] Easy to replace — standard-grounded (FIPS 199, inherited); Distribution Scope factor is this domain's own considered addition, documented as such
