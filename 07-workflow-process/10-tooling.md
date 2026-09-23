# Workflow/Process Domain — Tooling / Implementation

Status: Draft — pending review
Ratified: No
Last updated: 2026-09-22
Provenance: see _qa/10-tooling.qa.md
Built on: all prior columns (00-09)

Same posture as every prior domain: capability categories only, no
specific product/vendor recommendations. This domain's Tooling column
resolves several forward references other domains left pointing here —
see the Cross-Category Dependency Notes below.

## Capability Categories

### SCM (Source Control Management) Platform
Hosts Repositories, enforces WFPOL-1's Branch Protection requirement, and
hosts Pull Requests/Code Review. The platform this framework's own
repository (this governance framework itself) runs on is an instance of
this category.

### CI/CD Pipeline Platform
Runs Pipelines and Pipeline Stages, evaluates Deployment Gates
(WFPOL-2/WFPROC-2), and provides CI Runners/Agents. **This is where
System Architecture's Automated Test Execution & Gating category
(SAPOL-4/SAPROC-4) and Data Platform's DPPROC-5 detection mechanism
actually run** — both were explicitly flagged in those domains' Tooling
columns as forward references to this domain; this category is the
resolution.

### Data Pipeline Orchestration Engine
Implements the Orchestration Engine (`wf-orchestration-engine`) that
runs Data Pipelines against their DAGs, on Pipeline Triggers, supporting
Backfill. **This is where Data Platform's Orchestration Reference field
(04-data-platform/04-metadata-standards.md) actually resolves** — that
field was an explicit forward reference to this domain, not yet built at
the time.

### Infrastructure as Code Platform
Runs IaC Plan/Apply and maintains the State File, enforcing WFPOL-3's
plan-review-before-apply requirement and supporting Drift Detection.
**This is the single, shared selection Infrastructure's and Networking's
Tooling columns each already flagged as "likely one shared tool, not
independently selected" when neither had a domain to point to yet** —
this category is that shared tool's home.

### Incident Management / On-Call Platform
Tracks Incidents through their lifecycle (05-conventions.md's Incident
Lifecycle diagram), manages On-Call Rotation, and supports Post-Incident
Review documentation (WFPOL-4).

### Changelog / Release Automation
Generates Changelog entries from Pull Request titles or Conventional
Commits (00-standards-alignment.md), and manages Release Candidate →
Release promotion tagging in coordination with the CI/CD Pipeline
Platform.

### Data Catalog / Metadata Management Platform (shared, not separately selected)
The same OpenMetadata-class platform already selected by Data Platform,
Data/Metadata, and Business Intelligence / Reporting
(04-data-platform/10-tooling.md, 05-data-metadata/10-tooling.md,
06-bi-reporting/10-tooling.md) — this domain's Pipelines and Data Pipeline
Orchestration Runs are exactly the execution layer such a catalog scans
to auto-derive lineage and Source-to-Target Mapping. Listed here to keep
the shared-tool reconciliation complete across all four domains that now
reference it, not to assert a fifth independent selection.

---

**Cross-category dependency notes (resolving other domains' forward references):**
- CI/CD Pipeline Platform resolves System Architecture's SAPOL-4/SAPROC-4
  ("pipeline mechanism is a forward reference to Workflow/Process") and
  Data Platform's DPPROC-5 ("detection mechanism... forward reference to
  Tooling column, this domain").
- Data Pipeline Orchestration Engine resolves Data Platform's
  Orchestration Reference field ("forward reference, Workflow/Process not
  yet built").
- Infrastructure as Code Platform resolves Infrastructure's and
  Networking's IaC tooling flags (both domains noted their own IaC
  category was "likely the same tool," without yet having a domain to
  point that shared selection to).
- Data Catalog / Metadata Management Platform is explicitly the same
  selection already made by three other domains — not reselected here.

**Open items:**
- SCM Platform and CI/CD Pipeline Platform are very often the same
  product/vendor in practice (e.g., a platform offering both repository
  hosting and pipeline execution) — noted, not asserted as universal,
  same caveat System Architecture used for its own likely-bundled
  categories.

**Quality bar check (00-framework/quality-bar.md):**
- [x] Simple — 6 capability categories, no product lock-in
- [x] Modular — each category maps to a specific Policy/Procedure it implements
- [x] Easy to update — a category can be filled in with a specific product later without touching this structure
- [x] Easy to maintain — cross-category dependency notes explicitly resolve every other domain's forward reference into this one, none left dangling
- [x] Easy to replace — no product named, so no migration cost baked into the framework itself
