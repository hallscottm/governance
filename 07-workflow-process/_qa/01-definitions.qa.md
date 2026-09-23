# Q&A Log — Definitions
# Append-only. Do not edit past entries; add new dated entries instead.

## 2026-09-22 — Q7.2: Domain scope and the six-subdomain structure

**Bucket:** [Org-decision]/Human-only for the workflow-type list itself
(confirmed with the user before drafting — Source Control, CI/CD
Pipelines, Data Pipeline Orchestration, Infrastructure as Code,
Operational SOPs, Release Management); [Standard]/AI-draftable for term
content within that agreed scope.

**Answer:** 29 owned terms across the six subdomains. Key boundary
decision: Code Review stays owned by System Architecture
(`sysarch-code-review`, already anchored there before this domain
existed) — this domain owns the Pull Request mechanism that hosts a
review, not the review practice itself, stated explicitly rather than
left as a silent gap. Pipeline Trigger and Pipeline Run are deliberately
shared vocabulary between the CI/CD and Data Pipeline Orchestration
subdomains rather than duplicated per subdomain, consistent with this
framework's DRY discipline.

**Status:** Pending explicit review.
