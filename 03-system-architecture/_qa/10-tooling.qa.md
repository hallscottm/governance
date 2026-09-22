# Q&A Log — Tooling (System Architecture)
# Append-only. Do not edit past entries; add new dated entries instead.

## 2026-09-22 — Q10.1: Tooling posture

**Bucket:** [Org-decision]/Human-only.
**Answer:** Yes, same posture as Infrastructure and Networking — defer
entirely, categories only.

## 2026-09-22 — Q10.2: Category structure

**Bucket:** [Standard]/AI-draftable.

**Drafted:** 6 categories — API Gateway/Management, Database Platform &
Migration Tooling, Secrets Management, Application Security Testing,
Container Image Registry & Build Artifact Repository, Automated Test
Execution & Gating — each tied to a specific SAPOL-/SAPROC- item, plus
cross-category dependency notes (API Gateway likely shares a tool family
with Networking's Load Balancer/Reverse Proxy; Container Image Registry
constrained by Infrastructure's Container Runtime choice; Secrets
Management likely org-wide, not per-layer).

**Status:** Pending explicit review.
