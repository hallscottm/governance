# Infrastructure Layer — Definitions

Status: Draft — pending review
Ratified: No
Last updated: 2026-09-22
Provenance: see _qa/01-definitions.qa.md

| Term | Definition | Source Standard |
|---|---|---|
| **Compute Environment** | A category of physical or virtual location where compute runs. Valid types: On-Premises, Colocation, Public Cloud, Private Cloud, Hybrid, Edge. | Org convention (generalized) |
| **Environment (lifecycle)** | A logically or physically isolated instance of infrastructure used for a specific stage of the software/data lifecycle. Standard tiers: Development, Staging/QA, Production. | Common industry practice |
| **Compute Unit** | The smallest independently provisionable unit of processing capacity (e.g., a VM, container, physical server, or GPU instance). | Common industry practice |
| **Storage Tier — Hot** | Storage optimized for frequent access and low latency; highest relative cost. | Common industry practice (AWS/Azure/GCP-aligned) |
| **Storage Tier — Warm** | Storage for occasionally accessed data; moderate cost/latency tradeoff. | Common industry practice |
| **Storage Tier — Cold** | Storage for rarely accessed data; optimized for cost over speed. | Common industry practice |
| **Storage Tier — Frozen/Archival** | Storage for compliance retention; lowest cost, highest retrieval latency. | Common industry practice |
| **Availability Tier I** | Basic capacity, no redundancy. | Uptime Institute Tier Classification |
| **Availability Tier II** | Redundant capacity components. | Uptime Institute Tier Classification |
| **Availability Tier III** | Concurrently maintainable, no downtime for planned maintenance. | Uptime Institute Tier Classification |
| **Availability Tier IV** | Fault-tolerant, no downtime for planned or unplanned events. | Uptime Institute Tier Classification |

**Glossary callouts:** none needed — all terms defined in place above.

**Open items:** none — all Definitions-column questions answered.

**Quality bar check (00-framework/quality-bar.md):**
- [x] Simple — terms borrowed from established standards, not invented
- [x] Modular — each term stands alone, no interdependency within this column
- [x] Easy to update — flat table, add/edit a row without touching others
- [x] Easy to maintain — sourced to named standards, no ambiguity about ownership
- [x] Easy to replace — adopting external standard vocabulary (Uptime Institute, common practice) rather than a custom scheme
