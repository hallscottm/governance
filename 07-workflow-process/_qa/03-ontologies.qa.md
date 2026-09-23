# Q&A Log — Ontologies
# Append-only. Do not edit past entries; add new dated entries instead.

## 2026-09-22 — Q7.4: Relationships, including retroactive edges into three already-built domains plus Cross-Cutting Roles & Departments

**Bucket:** [Standard]/AI-draftable — relationship content and rationale;
cross-domain edges follow the established reverse-pointer discipline.

**Answer:** 26 relationships within this domain, plus 7 cross-domain
edges: 3 outbound into System Architecture's `sysarch-release` (Deployment
Gate, Release Candidate, Rollback), 1 outbound into Data Platform's
`dp-data-pipeline` (DAG), 1 outbound into Infrastructure's
`infra-compute-unit` (IaC), 1 outbound into Cross-Cutting Roles &
Departments' `ccrole-approver` (Change Request), and 1 inbound from
System Architecture (`sysarch-service --[requires]--> wf-repository`,
added directly to System Architecture's own ontology file since that's
the natural owning domain for the relationship's source term — same
retroactive-edge pattern Business Intelligence / Reporting used when it
added edges into Data Platform's `dp-semantic-layer` after that domain
was already built). All four target files (System Architecture, Data
Platform, Infrastructure, Cross-Cutting Roles & Departments) updated with
matching reverse pointers in the same pass.

**Status:** Pending explicit review.
