# Q&A Log — Policies (Data/Metadata)
# Append-only. Do not edit past entries; add new dated entries instead.

## 2026-09-22 — Q6.1: Layer-specific policy set and enforcement levels

**Bucket:** [Org-decision]/Human-only for enforcement levels and DPOL-4's
SLA default; [Standard]/AI-draftable for rule content and rationale.

**Answers:**
- DPOL-1 (PII/Restricted protection): Hard block.
- DPOL-2 (retention period + expiry disposal): Hard block on both halves
  (missing period AND unenforced expiry-disposal).
- DPOL-3 (access approval scaling): Same rule for both Confidential and
  Restricted tiers, no further escalation.
- DPOL-4 (Right to Erasure SLA): 30 days, explicitly conditional on
  Personal Data being in regulatory scope, explicitly adjustable.

**Status:** Pending explicit review.
