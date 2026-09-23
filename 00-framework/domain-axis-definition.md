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
| 9 | Interface/Human | Training, change management, human engagement |

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

See 00-framework/ea-framework-alignment.md for why each of these two
insertions was kept as its own domain rather than folded into an
existing one.

Cross-cutting (not rows, expressed through the Policies / Access Rules /
Risk Tiers columns at every domain): Governance, Security, Roles &
Departments (added 2026-09-22 — see cross-cutting/roles-and-departments/;
Access Rules is this pillar's primary point of contact, though a role can
be referenced from any column that needs to name who acts).

Activates partway (not from domain 1): Sandbox — becomes relevant starting
at the Workflow/Process domain, once there is something real to test
against.
