# Workflow/Process Domain — Ontologies

Status: Draft
Ratified: No
Last updated: 2026-09-22
Relation vocabulary: 00-framework/relation-types.md
Built on: 01-definitions.md, 02-taxonomies.md

Relationships may reference anchors owned by other domains (System
Architecture, Data Platform, Infrastructure, Cross-Cutting Roles &
Departments) where a genuine cross-domain relationship exists. Per the
reverse-pointer rule in 00-framework/relation-types.md, every cross-domain
relationship below has a matching reverse pointer added to the target
domain's Ontology file.

## Source Control

- `wf-repository` --[contains]--> `wf-branch`
  Rationale: a repository's branches exist within it.
- `wf-branching-strategy` --[constrains]--> `wf-branch`
  Rationale: the branching strategy governs how branches are created, named, and merged.
- `wf-pull-request` --[requires]--> `wf-branch`
  Rationale: a pull request exists to merge one branch into another.
- `wf-branch-protection-rule` --[constrains]--> `wf-pull-request`
  Rationale: a protection rule on the target branch constrains whether a pull request can merge.
- `wf-repository-scaffolding` --[produces]--> `wf-repository`
  Rationale: a new repository is created from a scaffolding template.

## CI/CD Pipelines

- `wf-pipeline` --[contains]--> `wf-pipeline-stage`
  Rationale: a pipeline is composed of its ordered stages.
- `wf-pipeline` --[produces]--> `wf-pipeline-run`
  Rationale: each execution of a pipeline produces a pipeline run record.
- `wf-pipeline-run` --[requires]--> `wf-pipeline-trigger`
  Rationale: a pipeline run is caused by a specific trigger event.
- `wf-pipeline-run` --[runs-on]--> `wf-ci-runner`
  Rationale: a pipeline run executes on compute allocated as a CI runner.
- `wf-deployment-gate` --[constrains]--> `sysarch-release`
  Rationale: cross-domain — a deployment gate is the mechanism that
  blocks a Release Candidate from becoming a Release until its condition
  is satisfied.

## Data Pipeline Orchestration

- `wf-orchestration-engine` --[requires]--> `wf-dag`
  Rationale: an orchestration engine executes a DAG's dependency structure.
- `wf-orchestration-engine` --[produces]--> `wf-pipeline-run`
  Rationale: reuses the same Pipeline Run concept as CI/CD — a data pipeline execution is a pipeline run like any other.
- `wf-dag` --[requires]--> `dp-data-pipeline`
  Rationale: cross-domain — a DAG is the dependency structure of a
  specific Data Pipeline's steps; it has nothing to structure without one.
- `wf-backfill` --[produces]--> `wf-pipeline-run`
  Rationale: a backfill executes as one or more pipeline runs targeting a past time window.

## Infrastructure as Code

- `wf-iac` --[produces]--> `infra-compute-unit`
  Rationale: cross-domain — Infrastructure as Code is a primary mechanism
  by which Infrastructure's resources actually get created.
- `wf-iac-plan` --[requires]--> `wf-state-file`
  Rationale: a plan is computed as a diff against the last-known state.
- `wf-iac-apply` --[requires]--> `wf-iac-plan`
  Rationale: apply executes an already-generated, reviewed plan.
- `wf-iac-apply` --[produces]--> `wf-state-file`
  Rationale: applying a plan updates the state file to reflect the new actual state.
- `wf-drift-detection` --[requires]--> `wf-state-file`
  Rationale: drift is detected by comparing actual infrastructure against the recorded state file.

## Operational SOPs

- `wf-incident` --[consumes]--> `wf-runbook`
  Rationale: responding to an incident consumes an existing runbook where one applies, rather than the incident requiring a runbook to exist at all.
- `wf-incident` --[produces]--> `wf-postmortem`
  Rationale: a resolved incident produces a structured post-incident review.
- `wf-postmortem` --[produces]--> `wf-change-request`
  Rationale: a postmortem's follow-up actions are typically tracked as change requests.
- `wf-change-request` --[requires]--> `ccrole-approver`
  Rationale: cross-domain — a change request needs a designated approver, the same Requester/Approver separation-of-duties concept cross-cutting/access-rules.md already establishes (CCAR-2).

## Release Management

- `wf-release-candidate` --[requires]--> `wf-deployment-gate`
  Rationale: a release candidate must clear its applicable deployment gates before promotion.
- `wf-release-candidate` --[produces]--> `sysarch-release`
  Rationale: cross-domain — once a release candidate clears its gates, it becomes a Release (System Architecture's term for a Build designated for deployment).
- `wf-changelog` --[requires]--> `wf-pull-request`
  Rationale: changelog entries are typically generated from merged pull request titles or their Conventional Commits.
- `wf-rollback` --[requires]--> `sysarch-release`
  Rationale: cross-domain — a rollback reverts a running system to a prior Release; it has nothing to revert to without one.

## Cross-Domain References (relationships pointing into this domain)

Per 00-framework/relation-types.md's reverse-pointer rule.

- `wf-repository`
  Referenced by (cross-domain relationships):
  - System Architecture: `sysarch-service --[requires]--> wf-repository` (added to 03-system-architecture/03-ontologies.md 2026-09-22, retroactively — same pattern Business Intelligence / Reporting used when it added edges into Data Platform's `dp-semantic-layer` after that domain was already built)

---

**Open items:**
- `wf-feature-flag` was considered for a `constrains sysarch-release`
  relationship (a feature flag decouples what a release does for users
  from the release itself) but left unconnected per the "not every term
  needs a relationship" scope note — the connection is real but not as
  load-bearing as the others drawn here; revisit if this framework later
  needs to reason about feature-flag-driven rollout risk specifically.
- `wf-on-call-rotation` has no drawn relationship to `wf-incident` — the
  connection (on-call exists to respond to incidents) felt more like
  organizational context than a structural dependency; same judgment
  call already made for Infrastructure's Database Replica/Replication
  Factor pair.
- Conventional Commits (00-standards-alignment.md) is referenced in
  `wf-changelog`'s rationale but has no anchored Definitions term of its
  own — treated as a convention (05-conventions.md territory, not yet
  drafted), same treatment SemVer received before this domain existed.

**Quality bar check (00-framework/quality-bar.md):**
- [x] Simple — 26 relationships, grouped by subdomain
- [x] Modular — cross-domain edges (7 total: into System Architecture x3, Data Platform x1, Infrastructure x1, Cross-Cutting Roles & Departments x1, plus 1 inbound from System Architecture) clearly marked, reverse-pointed
- [x] Easy to update — anchor-ID based, survives renames
- [x] Easy to maintain — grouped by subdomain, matches Definitions/Taxonomy
- [x] Easy to replace — relation-type vocabulary shared across all domains
