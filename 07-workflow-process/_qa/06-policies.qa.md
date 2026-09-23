# Q&A Log — Policies
# Append-only. Do not edit past entries; add new dated entries instead.

## 2026-09-22 — Q7.7: Domain-specific policies, closing three other domains' forward references

**Bucket:** [Org-decision]/Human-only for enforcement levels; [Standard]/
AI-draftable for rule content.

**Answers:**
- WFPOL-1 (branch protection on default branch): Hard block — the
  mechanism making every other domain's hard-block test/scan policies
  actually enforceable at merge time.
- WFPOL-2 (deployment gate before Production promotion): Hard block —
  the general mechanism System Architecture's SAPOL-4, Data Platform's
  DPPOL-1, and Business Intelligence / Reporting's BIPOL-1 all assumed
  existed; this closes that loop for all three at once.
- WFPOL-3 (IaC apply requires reviewed plan): Hard block.
- WFPOL-4 (post-incident review, scaled by severity): Sev1/Sev2 required,
  Sev3/Sev4 optional — same scaled-by-classification pattern used
  throughout this framework.
- WFPOL-5 (emergency change requires post-hoc review): the first policy
  in this framework whose approval gate runs after the action it gates,
  flagged as a structural departure worth noting rather than treated as
  an ordinary approval gate.

**Status:** Pending explicit review.
