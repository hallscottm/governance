# Domain Axis Definition

Status: Draft
Ratified: No
Last updated: 2026-09-22

The row axis of the framework matrix. Originally called "Layers"; renamed
to **Domains** on 2026-09-22 because the axis had grown beyond a strict
dependency stack — see 00-framework/ea-framework-alignment.md. Domains are
filled bottom-to-top (row-major) in ascending # order, since each domain's
definitions depend on the domain(s) below it.

| # | Domain | Concern |
|---|---|---|
| 1 | Infrastructure | Physical/virtual compute, storage, hardware substrate |
| 2 | Networking | Connectivity, segmentation, routing, network boundaries |
| 3 | System Architecture | Applications, services, APIs built on the substrate |
| 4 | Data Platform | Databases, data lakes/lakehouses/warehouses, vector stores, streaming — where data physically lives and runs |
| 5 | Data/Metadata | What the data means — taxonomy, ontology, catalog, governance |
| 6 | Business Intelligence / Reporting | Reports, dashboards, self-service report-level models, metrics as consumed — where data becomes a decision-facing artifact |
| 7 | Workflow/Process | Git, CI/CD, SOPs, directory conventions |
| 8 | Harness | Role/department-specific AI scaffolding |

Renumbering history:
- 2026-09-22: Data Platform inserted as #4 (split out of System
  Architecture's Database/Database Schema terms); Data/Metadata shifted
  4→5, Workflow/Process 5→6, Harness 6→7, Interface/Human 7→8.
- 2026-09-22 (same day, second insertion): Business Intelligence /
  Reporting inserted as #6 — Data Platform and Data/Metadata model the
  official, intended data flow; this domain exists because that flow is
  not 1:1 once report builders start creating their own embedded models
  (calculated fields, extracts) that can diverge from the official
  Semantic Layer/Metric definitions. Workflow/Process shifted 6→7,
  Harness 7→8, Interface/Human 8→9.
- 2026-09-22 (same day, third change — a removal, not an insertion):
  Interface/Human (was #9) folded into the Roles & Departments
  cross-cutting pillar rather than kept as a domain — training/
  change-management requirements didn't have artifacts of their own
  (no Definitions/Taxonomy/Ontology distinct from the Role or Department
  they train) once tested against the "noun-oriented artifact domain"
  test applied to every domain this session. Replaced by a Training
  Requirement mechanism (`ccorg-training-requirement`) attached directly
  to Roles/Departments and referenced from each domain's Access Rules
  column — see cross-cutting/roles-and-departments/00-qa.md Q11. No
  renumbering needed (it was the last domain); Harness (8) is now the
  last domain on the axis.

See 00-framework/ea-framework-alignment.md for why each of these changes
was made — the two insertions kept as their own domain, the one removal
folded into an existing cross-cutting pillar instead.

Cross-cutting (not rows, expressed through the Policies / Access Rules /
Risk Tiers columns at every domain): Governance, Security, Roles &
Departments (added 2026-09-22 — see cross-cutting/roles-and-departments/;
Access Rules is this pillar's primary point of contact, though a role can
be referenced from any column that needs to name who acts). Roles &
Departments also now carries training/change-management requirements
(the Training Requirement mechanism, `ccorg-training-requirement`) after
Interface/Human was folded in — see the renumbering history above and
00-qa.md Q11.

## Areas outside the domain axis

Not every top-level directory is a domain or a cross-cutting pillar. `00-framework/` (meta: conventions, generators), `cross-cutting/` (pillars threaded through every domain's own columns), and `roadmap/` (generated status rollup) sit outside this axis by construction. `engagements/` (added 2026-09-23) is the newest of these — the unit-of-work planning layer (Engagement Documents, Vetting Agent, Engagement Planning Agent) that consumes this axis's content plus Harness's Agent machinery, rather than adding a ninth technology-layer row. It failed the same "noun-oriented artifact domain" test Interface/Human failed above, for a different reason: it isn't tech-layer-shaped at all, it's a process layer above every layer. See engagements/01-definitions.md.

Activates partway (not from domain 1): Sandbox — becomes relevant starting
at the Workflow/Process domain, once there is something real to test
against.
