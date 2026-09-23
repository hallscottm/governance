# Workflow/Process Domain — Risk Tiers

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
| Environment (referenced from Infrastructure) | Dev | Staging/QA | Production |
| Service Tier / Criticality (referenced from System Architecture, for the Repository/Pipeline's owning Service) | Non-critical, internal tooling | Business-important | Business-critical |
| Change Request Type (04-metadata-standards.md) | Standard | Normal | Emergency |
| Incident Severity (04-metadata-standards.md), where applicable | Sev4 | Sev3 | Sev1/Sev2 |
| Break-glass/override used (WFPROC-1 override, or CCPROC-4) | Not used | N/A — this factor has no Moderate value | Used — an override is automatically High risk regardless of the underlying change's own tier |

**Note on Change Request Type factor:** an Emergency change is
automatically High risk not because the underlying change is necessarily
riskier than a Normal one, but because it executes *before* the review
that would normally catch a problem — the ordering itself is the risk
factor, distinct from every other domain's risk factors, which score the
resource's inherent properties rather than the process used to change it.

**Note on Break-glass/override factor:** the first Risk Tier factor in
this framework keyed to *process bypass itself* rather than a resource
property — using CCAR-3/WFAR-1's override authority is inherently a
High-risk event regardless of what was overridden, since it means a
designed safeguard didn't run.

## Consequences by Tier

**Extends:** cross-cutting/risk-tiers.md's baseline (two-person sign-off
for High risk, via CCAR-3).

**Domain-specific additions beyond the baseline (already defined in full
in 06-policies.md/07-access-rules.md — summarized here for visibility):**

| Tier | Workflow/Process-Specific Policy Implication |
|---|---|
| **Low** | WFAR-1 override: Owning Team Lead alone. WFPOL-4: Post-Incident Review optional (Sev3/Sev4). |
| **Moderate** | WFAR-2 IaC approval: single applicable role (Infrastructure Admin or Data Engineer). |
| **High** | WFAR-1 override: Owning Team Lead + Security/Compliance. WFAR-2: applicable role + Security/Compliance. WFPOL-4: Post-Incident Review required (Sev1/Sev2). WFPOL-1, WFPOL-2, WFPOL-3 hard blocks apply uniformly at every tier (not scaled), same treatment established across every other domain's uniform hard blocks. |

---

**Open items:**
- Change Request Type and Break-glass/override are both "process, not
  resource" risk factors — a genuine first for this framework's Risk
  Tiers columns, flagged explicitly as a category worth watching for as
  Harness (domain 8) is built, since an AI agent's own actions may
  introduce similar process-level risk factors not yet modeled anywhere.
- Incident Severity's interaction with the other factors (does a Sev1
  Incident automatically elevate every Change Request made during its
  response?) is not fully specified — WFPOL-5's Emergency Change path
  already covers the most common case; a less common combination (a
  Normal-type change made during an active Sev1) is left to the "highest
  tier wins" rule rather than a bespoke interaction rule.

**Quality bar check (00-framework/quality-bar.md):**
- [x] Simple — 5 determining factors, reusing the cross-cutting scale
- [x] Modular — domain-specific factors independent of every other domain's
- [x] Easy to update — cross-cutting scale updates once, applies here automatically
- [x] Easy to maintain — factors derived from existing Definitions/Metadata Standards
- [x] Easy to replace — standard-grounded (FIPS 199, inherited); two factors are this domain's own considered addition, documented as such
