# Workflow/Process Domain — Definitions

Status: Draft
Ratified: No
Last updated: 2026-09-22

Scope: Git/source control, CI/CD pipelines, data pipeline orchestration,
Infrastructure as Code, operational SOPs, and release management — the
mechanisms that move a change from proposed to running, and the runbooks
that keep a running system operating. Distinct from System Architecture
(domain 3), which owns the *artifacts* this domain moves (Build, Release,
Container Image, Unit Test) — this domain owns *how* they move. Distinct
from Data Platform (domain 4), which owns the Data Pipeline concept
itself (`dp-data-pipeline`) — this domain owns what runs and schedules it.
Built fresh 2026-09-22, after Standards Alignment (00-standards-alignment.md).

Anchor convention: `wf-<term-slug>`.

---

## Referenced Terms (owned elsewhere)

- **Build, Release, Container Image, Semantic Version (SemVer)** — owned by System Architecture →
  [03-system-architecture/01-definitions.md#sysarch-release](../03-system-architecture/01-definitions.md#sysarch-release)
- **Code Review** — owned by System Architecture →
  [03-system-architecture/01-definitions.md#sysarch-code-review](../03-system-architecture/01-definitions.md#sysarch-code-review) —
  this domain owns the Pull Request mechanism that hosts a Code Review,
  not the review practice itself; boundary confirmed explicitly rather
  than left implicit.
- **Unit Test, Integration Test, Test Coverage** — owned by System Architecture →
  [03-system-architecture/01-definitions.md#sysarch-unit-test](../03-system-architecture/01-definitions.md#sysarch-unit-test)
- **Data Pipeline, ETL/ELT, Batch Processing, Stream Processing** — owned by Data Platform →
  [04-data-platform/01-definitions.md#dp-data-pipeline](../04-data-platform/01-definitions.md#dp-data-pipeline)
- **Compute Unit** — owned by Infrastructure →
  [01-infrastructure/01-definitions.md#infra-compute-unit](../01-infrastructure/01-definitions.md#infra-compute-unit)

---

## Source Control

### Repository {#wf-repository}
The version-controlled source tree for a Service, Application, Package,
or other buildable unit (System Architecture's entities) — the thing a
Repository Reference field (03-system-architecture/04-metadata-standards.md)
points to. Source: General software engineering usage (Git and other
version control systems).

### Branch {#wf-branch}
A named, independent line of development within a Repository, allowing
changes to be made without affecting other lines until merged. Source:
General software engineering usage.

### Branching Strategy {#wf-branching-strategy}
The organization-wide policy governing how Branches are created, named,
and merged (e.g., trunk-based development, GitFlow). Stated here as a
concept an organization chooses one of — this framework does not
prescribe which, same posture already used for Business Function
Department groupings and medallion-layer naming. Source: Common industry
practice.

### Pull Request / Merge Request {#wf-pull-request}
A request to merge one Branch into another, serving as the unit at which
a Code Review (`sysarch-code-review`) is attached and approval is
recorded before merge. Source: General software engineering usage (GitHub/
GitLab/Bitbucket-originated terminology, now generic).

### Branch Protection Rule {#wf-branch-protection-rule}
A configured constraint on a Branch (e.g., requiring a passing Pipeline,
a minimum number of Code Review approvals, or a linear history) that
must be satisfied before a Pull Request targeting it can merge. Source:
General software engineering usage.

### Repository Scaffolding {#wf-repository-scaffolding}
The standardized directory structure, starter files, and configuration a
new Repository is created from, so that every Repository of a given type
(e.g., a Service) starts from the same baseline layout rather than an
ad hoc one. See 05-conventions.md (not yet drafted) for this domain's own
scaffolding pattern. Source: Common industry practice (template
repositories, scaffolding generators).

---

## CI/CD Pipelines

### Pipeline {#wf-pipeline}
An automated, ordered sequence of stages that takes a code change from
Repository to a deployed Release (a CI/CD Pipeline) or that runs a Data
Pipeline (`dp-data-pipeline`) on a schedule or trigger — the general
concept this domain owns; CI/CD Pipeline and Data Pipeline Orchestration
are its two primary uses. Source: General software/DevOps engineering
usage.

### Pipeline Stage {#wf-pipeline-stage}
One ordered step within a Pipeline (e.g., build, lint, test, security
scan, package, deploy) — each Pipeline Stage either passes (the Pipeline
continues) or fails (the Pipeline halts, subject to that stage's own
retry/override rules). Source: General software/DevOps engineering usage.

### Pipeline Trigger {#wf-pipeline-trigger}
The event that starts a Pipeline Run: a Pull Request update, a merge to a
protected Branch, a Scheduled Trigger (a cron-like time-based trigger),
or a manual invocation. Applies to both CI/CD Pipelines and Data Pipeline
Orchestration Runs. Source: General software/DevOps engineering usage.

### Pipeline Run {#wf-pipeline-run}
A single execution instance of a Pipeline, with its own start time,
status, and log — the record that a Deployment Gate or Backfill decision
is made against. Source: General software/DevOps engineering usage.

### CI Runner / Agent {#wf-ci-runner}
The Compute Unit (`infra-compute-unit`) that executes a Pipeline Stage's
actual commands. Distinct from Infrastructure's Compute Unit definition
itself — this term is the CI/CD-specific role that compute plays, not a
new resource type. Source: General software/DevOps engineering usage.

### Deployment Gate {#wf-deployment-gate}
A Pipeline Stage that blocks progression to the next stage/environment
until a specific condition is met — the mechanism, owned here, that
enforces several other domains' forward-referenced hard blocks and
approval gates (System Architecture's SAPOL-4 automated test gate,
Data Platform's DPPOL-1 schema migration review, Business Intelligence /
Reporting's BIPOL-1 certification requirement) at the point a change
actually tries to ship. Source: General software/DevOps engineering
usage.

---

## Data Pipeline Orchestration

### Orchestration Engine {#wf-orchestration-engine}
The system that schedules, triggers, and monitors Data Pipeline
(`dp-data-pipeline`) Pipeline Runs, tracking dependencies between
pipeline steps — the mechanism Data Platform's Orchestration Reference
field (04-data-platform/04-metadata-standards.md) points to. Source:
Common industry practice.

### DAG (Directed Acyclic Graph) {#wf-dag}
The dependency structure of a Data Pipeline's steps, expressed so that
each step's inputs are guaranteed to be produced before it runs, with no
circular dependencies. The Workflow Definition an Orchestration Engine
actually executes. Source: Common industry practice (graph theory
applied to pipeline orchestration).

### Backfill {#wf-backfill}
A Pipeline Run (or set of them) executed for a past time window, to
populate or correct data that a regular Scheduled Trigger already should
have produced but didn't (e.g., after a bug fix or a new pipeline step's
addition). Source: Common industry practice.

---

## Infrastructure as Code

### Infrastructure as Code (IaC) {#wf-iac}
Managing and provisioning Infrastructure/Networking/Data Platform
resources through versioned, declarative configuration files rather than
manual/interactive changes — already referenced as a Tooling category in
Infrastructure's and Networking's 10-tooling.md; this domain owns the
workflow (Plan/Apply/review) around using it. Source: Common industry
practice (GitOps principles, 00-standards-alignment.md).

### IaC Plan {#wf-iac-plan}
A preview of the changes an IaC Apply would make to actual
infrastructure, generated without making any change, reviewed before
Apply. Source: Common industry practice.

### IaC Apply {#wf-iac-apply}
The execution of an approved IaC Plan, making the actual infrastructure
match the declared configuration. Source: Common industry practice.

### State File {#wf-state-file}
The record an IaC tool maintains of the infrastructure resources it
manages and their last-known configuration, used to compute an IaC
Plan's diff. Source: Common industry practice.

### Drift Detection {#wf-drift-detection}
The process of comparing actual infrastructure against a State File to
identify resources that were changed outside of IaC Apply (a manual,
out-of-band change) — the mechanism that makes CCP-3's provisioning
approval requirement meaningful on an ongoing basis, not just at initial
creation. Source: Common industry practice.

---

## Operational SOPs

### Runbook {#wf-runbook}
A documented, step-by-step procedure for a specific operational task
(e.g., responding to a specific alert, performing a specific manual
recovery step) — distinct from this framework's own Procedures columns
(which execute that *domain's own Policies*), a Runbook is written for a
human/AI operator responding to a live operational situation, not for
provisioning/approval workflows. Source: ITIL; general operations
practice.

### Incident {#wf-incident}
An unplanned interruption to, or reduction in quality of, a service,
requiring a response distinct from routine operations. Source: ITIL.

### Post-Incident Review (Postmortem) {#wf-postmortem}
A structured review conducted after an Incident is resolved, documenting
timeline, root cause, and follow-up actions — blameless by convention in
most modern practice (a documented, common practice, not asserted as
this framework's own original judgment). Source: General SRE/operations
practice; ITIL's Problem Management process covers the same territory
formally.

### Change Request {#wf-change-request}
The documented artifact behind a provisioning or configuration change —
the concrete record CCP-3 (cross-cutting/policies.md) and CCPROC-1's
Requester submission actually produce, made explicit as its own term here
since every domain's Access Rules/Procedures reference "a request" without
naming what it is as an artifact. Source: ITIL Change Management; NIST SP
800-53 CM family.

### On-Call Rotation {#wf-on-call-rotation}
The scheduled assignment of responsibility for responding to Incidents
during a defined time window, rotating among a team. Source: General SRE/
operations practice.

---

## Release Management

### Release Candidate {#wf-release-candidate}
A Build (`sysarch-build`) proposed for promotion to a Release
(`sysarch-release`), pending whatever Deployment Gates apply — distinct
from a Release itself, which (per System Architecture's definition) has
already been designated for deployment; a Release Candidate hasn't
cleared that bar yet. Source: General software engineering usage.

### Changelog {#wf-changelog}
A versioned, human-readable record of what changed in each Release,
typically generated from Pull Request titles or Conventional Commits
(00-standards-alignment.md). Source: Keep a Changelog convention;
general software engineering usage.

### Rollback {#wf-rollback}
Reverting a running system from a newly deployed Release back to its
prior Release, in response to a failure detected after deployment.
Source: General software/DevOps engineering usage.

### Feature Flag {#wf-feature-flag}
A runtime-configurable toggle that decouples deploying a Release from
releasing a feature to users — code can ship dark (deployed but
disabled) and be enabled later without a new deploy, or rolled back by
toggling rather than a full Rollback. Source: General software
engineering usage.

**Quality bar check (00-framework/quality-bar.md):**
- [x] Simple — one file, six subdomains, no nested taxonomy logic here
- [x] Modular — each term owned once; System Architecture's and Data
      Platform's artifact/process terms referenced, not restated
- [x] Easy to update — a new pipeline/SOP concept adds a term without
      touching existing ones
- [x] Easy to maintain — single owner per term, DRY via reference stubs;
      Code Review boundary with System Architecture stated explicitly
- [x] Easy to replace — no CI/CD, orchestration, or IaC vendor named as
      the definition of a concept (examples only, where given)
