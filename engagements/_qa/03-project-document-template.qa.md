# Q&A Log — 03-project-document-template
# Append-only. Do not edit past entries; add new dated entries instead.

## 2026-09-23 — Q9.1: Translated from reviewed Claude Docs design pass

**Bucket:** [Judgment]/User-confirmed — content was drafted and
iterated with the user in a standalone Claude Docs artifact
("Engagement Document Framework") across several review rounds before
being written here, per the user's explicit "review before it's set in
stone in the project folder" instruction. The user then said to make it
part of the main project and make all necessary updates.

**Answer:** 03-project-document-template.md written following this framework's existing
anchor/reference-stub/quality-bar conventions. engagements/ established
as a new top-level area (not a domain — see
00-framework/domain-axis-definition.md's "Areas outside the domain
axis" note and 00-framework/term-linking-convention.md's `eng` prefix
addition). Cross-references verified against real anchors already in
the repo (Harness's Agent schema, Roles & Departments' ccrole/ccdept
registries) rather than assumed.

**Applied to:** engagements/03-project-document-template.md.

**Status:** Pending explicit review.

## 2026-09-23 — Q9.2: Cross-domain projects and workflow pattern documentation

**Bucket:** [Judgment]/User-confirmed — user asked two follow-up
questions after the Engagement Document review: (1) how a project
spanning multiple technical domains and a requesting department (e.g. a
marketing report touching Marketing, BI/Reporting, Data/Metadata) gets
vetted and documented, and (2) whether the workflow/orchestration
pattern used by a Project's Agents is captured anywhere in planning.

**Answer:** (1) Confirmed the existing schema already separates
`owning_department` (org-chart, who) from `applicable_domains`
(technical axis, which governance applies) — added a short clarifying
note rather than new machinery, since the mechanism (Governance
Mapping's full Anchor-layer read access, per-domain Task decomposition)
already handles the multi-domain case; the existing `dq-metrics-
dashboard` worked example (08-worked-example.md) already demonstrates
the same shape (3 domains), so a second worked example was judged
redundant and not added. (2) Was a real gap: added `workflow_pattern`
to the Project Document front matter (single-agent | sequential |
parallel | orchestrator-workers | evaluator-optimizer), naming the
patterns already cited from Anthropic's "Building Effective AI Agents"
in 00-standards-alignment.md — previously only implicit in each Task's
own `dependencies` list, which captures ordering but not the
coordination shape.

**Applied to:** engagements/03-project-document-template.md.

**Status:** Pending explicit review.

## 2026-09-23 — Q9.4: Source control, CI/CD, and IaC clarified as a distinct concern from workflow_pattern

**Bucket:** [Judgment]/User-confirmed — user clarified that "workflow"
in Q9.2 meant Workflow/Process domain concepts (CI/CD, IaC, source
control), not the orchestration-pattern field added there (which the
user separately confirmed was wanted). Real gap: the Project Document
only had thin `repository`/`scaffolding_template` fields with no
connection to Workflow/Process's already-rich vocabulary (Branching
Strategy, Pipeline, Deployment Gate, IaC Plan/Apply, State File).

**Answer:** Added a `source_control_and_delivery` block (repository
detail, ci_cd, iac) replacing the thin fields, referencing existing
Workflow/Process terms rather than restating them. Explicitly scoped as
required only when `applicable_domains` includes a domain whose
deliverable is code/config/infrastructure, optional otherwise (avoids
forcing CI/CD/IaC fields onto e.g. a pure report Engagement). Noted
explicitly that this is a planning-time record — once a Service/
Application entity exists, its own Repository Reference field
(03-system-architecture/04-metadata-standards.md) is the ongoing
source of truth, not duplicated here, per this framework's DRY/
anti-drift convention.

**Applied to:** engagements/03-project-document-template.md.

**Status:** Pending explicit review.
