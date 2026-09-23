# Workflow/Process Domain — Taxonomies

Status: Draft
Ratified: No
Last updated: 2026-09-22
Provenance: see _qa/02-taxonomies.qa.md
Built on: 01-definitions.md (29 owned terms)

Structure: strict single-parent tree, consistent with every domain's
Taxonomy column. Only terms owned by this domain are classified here —
the 5 referenced terms (Build/Release/Container Image/SemVer/Code
Review/Unit Test/Integration Test/Test Coverage from System Architecture,
Data Pipeline/ETL-ELT/Batch/Stream Processing from Data Platform, Compute
Unit from Infrastructure) are not re-classified in this domain's tree.

---

## Workflow/Process
├── Source Control
│   ├── Repository (#wf-repository)
│   ├── Branch (#wf-branch)
│   ├── Branching Strategy (#wf-branching-strategy)
│   ├── Pull Request / Merge Request (#wf-pull-request)
│   ├── Branch Protection Rule (#wf-branch-protection-rule)
│   └── Repository Scaffolding (#wf-repository-scaffolding)
│
├── CI/CD Pipelines
│   ├── Pipeline (#wf-pipeline)
│   ├── Pipeline Stage (#wf-pipeline-stage)
│   ├── Pipeline Trigger (#wf-pipeline-trigger)
│   ├── Pipeline Run (#wf-pipeline-run)
│   ├── CI Runner / Agent (#wf-ci-runner)
│   └── Deployment Gate (#wf-deployment-gate)
│
├── Data Pipeline Orchestration
│   ├── Orchestration Engine (#wf-orchestration-engine)
│   ├── DAG (Directed Acyclic Graph) (#wf-dag)
│   └── Backfill (#wf-backfill)
│
├── Infrastructure as Code
│   ├── Infrastructure as Code (IaC) (#wf-iac)
│   ├── IaC Plan (#wf-iac-plan)
│   ├── IaC Apply (#wf-iac-apply)
│   ├── State File (#wf-state-file)
│   └── Drift Detection (#wf-drift-detection)
│
├── Operational SOPs
│   ├── Runbook (#wf-runbook)
│   ├── Incident (#wf-incident)
│   ├── Post-Incident Review (Postmortem) (#wf-postmortem)
│   ├── Change Request (#wf-change-request)
│   └── On-Call Rotation (#wf-on-call-rotation)
│
└── Release Management
    ├── Release Candidate (#wf-release-candidate)
    ├── Changelog (#wf-changelog)
    ├── Rollback (#wf-rollback)
    └── Feature Flag (#wf-feature-flag)

**Quality bar check (00-framework/quality-bar.md):**
- [x] Simple — one tree, six subdomains, matches Definitions' grouping
- [x] Modular — subdomains classify independently
- [x] Easy to update — a new pipeline/SOP concept adds a leaf
- [x] Easy to maintain — mirrors 01-definitions.md's subdomain headings
      exactly, no separate structure to keep in sync by hand
- [x] Easy to replace — pure classification, no tooling/vendor lock-in
