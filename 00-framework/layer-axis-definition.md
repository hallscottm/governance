# Layer Axis Definition

Status: Draft
Ratified: No
Last updated: 2026-09-22

The row axis of the framework matrix. Layers are filled bottom-to-top
(row-major), since each layer's definitions depend on the layer(s) below it.

| # | Layer | Concern |
|---|---|---|
| 1 | Infrastructure | Physical/virtual compute, storage, hardware substrate |
| 2 | Networking | Connectivity, segmentation, routing, network boundaries |
| 3 | System Architecture | Databases, applications, services built on the substrate |
| 4 | Data/Metadata | What the data means — taxonomy, ontology, catalog |
| 5 | Workflow/Process | Git, CI/CD, SOPs, directory conventions |
| 6 | Harness | Role/department-specific AI scaffolding |
| 7 | Interface/Human | Training, change management, human engagement |

Cross-cutting (not rows, expressed through the Policies / Access Rules /
Risk Tiers columns at every layer): Governance, Security.

Activates partway (not from layer 1): Sandbox — becomes relevant starting
at the Workflow/Process layer, once there is something real to test against.
