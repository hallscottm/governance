# Q&A Log — Policies (System Architecture)
# Append-only. Do not edit past entries; add new dated entries instead.

## 2026-09-22 — Q6.1: Domain-specific policy set and enforcement levels

**Bucket:** [Org-decision]/Human-only for enforcement levels and Risk
Tier scaling; [Standard]/AI-draftable for rule content and rationale.

**Answers:**
- SAPOL-1 (backward compatibility, Production APIs): Hard block.
- SAPOL-2 (schema migration review): Scale by Risk Tier
  (Low: peer review / Moderate: + lead sign-off / High: + rollback plan).
- SAPOL-3 (managed secret storage): Hard block.
- SAPOL-5 (public-facing security baseline): Scale by Risk Tier
  (Low: ASVS L1 / Moderate: ASVS L2 / High: ASVS L3).

**Also drafted without a separate question (bucketed AI-draftable,
consistent with prior sessions' pattern of only asking where genuine
judgment was needed):**
- SAPOL-4 (automated tests must pass before Production deploy) — hard
  block, no specific coverage threshold set (left to Workflow/Process or
  Owning Team, no defensible universal number).

**Design note:** Unlike Infrastructure (which scaled POL-2/POL-3 by Risk
Tier only after Risk Tiers was drafted, requiring a retrofit), Risk Tiers
already existed as a cross-cutting concept by the time this column was
reached — SAPOL-2 and SAPOL-5 scale by tier from the start, no retrofit
needed.

**Status:** Pending explicit review.
