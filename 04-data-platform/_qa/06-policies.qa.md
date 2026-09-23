# Q&A Log — Policies
# Append-only. Do not edit past entries; add new dated entries instead.

## 2026-09-22 — Q4.4: Domain-specific policy set, including a migration and a new governance-motivated policy

**Bucket:** [Org-decision]/Human-only for enforcement levels and Risk
Tier scaling; [Standard]/AI-draftable for rule content and rationale.

**Answers:**
- DPPOL-1 (schema migration review, migrated from SAPOL-2): Scale by Risk
  Tier, approving role updated from Owning Team Lead to Data Engineer/
  Data Architect.
- DPPOL-2 (streaming retention window required): Hard block.
- DPPOL-3 (embedding model reference required): Hard block — justified as
  a data-correctness concern (mixed-model similarity search is silently
  wrong), not just a compliance/metadata-completeness one, a new
  rationale category for this framework's Hard Blocks.
- DPPOL-4 (lakehouse table format declared/changes reviewed): Hard block
  on missing declaration, approval gate on change.
- DPPOL-5 (Semantic Layer as sole source for Certified Metrics): Approval
  gate — this is the direct policy expression of the divergence risk that
  motivated Business Intelligence / Reporting's creation as domain 6;
  drafted without a separate question since the ontology relationship
  (`dp-semantic-layer --[requires]--> data-metric`) already established
  the intent, this policy just makes it enforceable.

**Status:** Pending explicit review.
