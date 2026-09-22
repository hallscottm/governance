# Infrastructure Layer — Taxonomies

Status: Draft — pending review
Ratified: No
Last updated: 2026-09-22
Provenance: see _qa/02-taxonomies.qa.md
Built on: 01-definitions.md (58 terms)

Structure: strict single-parent tree. Each term is classified under
exactly one category. Cross-domain relevance (e.g., a term mattering to
another layer, or two terms being related without one containing the
other) is handled separately via the Referenced-by/extends mechanism in
00-framework/term-linking-convention.md — not by taxonomy placement.

---

## Infrastructure
├── Environments & Compute Categories
│   ├── Compute Environment (#infra-compute-environment)
│   ├── Environment / lifecycle (#infra-environment-lifecycle)
│   └── Compute Unit (#infra-compute-unit)
│
├── Compute Hardware
│   ├── CPU (#infra-cpu)
│   ├── GPU (#infra-gpu)
│   ├── Accelerator / TPU (#infra-accelerator)
│   ├── vCPU (#infra-vcpu)
│   ├── Core (#infra-core)
│   ├── Instance Type/Size Class (#infra-instance-type)
│   ├── Bare Metal (#infra-bare-metal)
│   ├── Virtual Machine (#infra-vm)
│   └── Container (#infra-container)
│
├── AI-Specific Compute
│   ├── Inference Workload (#infra-inference-workload)
│   ├── Training Workload (#infra-training-workload)
│   ├── GPU Memory / VRAM (#infra-gpu-memory)
│   └── Model-Serving Node (#infra-model-serving-node)
│
├── Storage
│   ├── Storage Tier — Hot (#infra-storage-tier-hot)
│   ├── Storage Tier — Warm (#infra-storage-tier-warm)
│   ├── Storage Tier — Cold (#infra-storage-tier-cold)
│   ├── Storage Tier — Frozen/Archival (#infra-storage-tier-frozen-archival)
│   ├── Block Storage (#infra-block-storage)
│   ├── Object Storage (#infra-object-storage)
│   ├── File Storage (#infra-file-storage)
│   ├── IOPS (#infra-iops)
│   ├── Throughput (#infra-throughput)
│   ├── Durability Class (#infra-durability-class)
│   ├── Replication Factor (#infra-replication-factor)
│   ├── Snapshot (#infra-snapshot)
│   ├── Backup (#infra-backup)
│   └── Archive (#infra-archive)
│
├── Facility / Physical
│   ├── Data Center (#infra-data-center)
│   ├── Rack (#infra-rack)
│   ├── Power Draw (#infra-power-draw)
│   ├── Cooling (#infra-cooling)
│   └── PUE (#infra-pue)
│
├── Availability
│   ├── Availability Tier I (#infra-availability-tier-i)
│   ├── Availability Tier II (#infra-availability-tier-ii)
│   ├── Availability Tier III (#infra-availability-tier-iii)
│   └── Availability Tier IV (#infra-availability-tier-iv)
│
├── Virtualization
│   ├── Hypervisor (#infra-hypervisor)
│   ├── Container Runtime (#infra-container-runtime)
│   └── Orchestrator (#infra-orchestrator)
│
├── Capacity & Scaling
│   ├── Vertical Scaling (#infra-vertical-scaling)
│   ├── Horizontal Scaling (#infra-horizontal-scaling)
│   ├── Autoscaling (#infra-autoscaling)
│   ├── Provisioned Capacity (#infra-provisioned-capacity)
│   ├── On-Demand Capacity (#infra-on-demand-capacity)
│   └── Reserved Capacity (#infra-reserved-capacity)
│
├── Resource Identity
│   ├── Asset Tag (#infra-asset-tag)
│   └── Resource ID (#infra-resource-id)
│
├── Lifecycle
│   ├── Provisioning (#infra-provisioning)
│   ├── Decommissioning (#infra-decommissioning)
│   ├── End-of-Life / EOL (#infra-eol)
│   └── Maintenance Window (#infra-maintenance-window)
│
├── Resilience
│   ├── Redundancy (#infra-redundancy)
│   ├── Failover (#infra-failover)
│   └── Disaster Recovery Tier (#infra-dr-tier)
│
└── Cost / FinOps
    ├── Cost Center Tag (#infra-cost-center-tag)
    └── Chargeback Unit (#infra-chargeback-unit)

---

**Coverage check:** all 58 terms from 01-definitions.md are classified
above, one category each. No orphaned terms, no term under two categories.

**Note on category ownership:** the 11 top-level categories are themselves
now stable identifiers for this layer's structure. If a future term is
added to Definitions, it must be placed under one of these 11 categories,
or — if it genuinely doesn't fit any of them — that's a signal the
taxonomy itself needs a new top-level category, not that the term should
be force-fit somewhere close enough.

**Open items:** none for this pass.

**Quality bar check (00-framework/quality-bar.md):**
- [x] Simple — single-parent tree, no cross-links cluttering the structure
- [x] Modular — each branch stands alone; adding a term to one branch
      doesn't touch others
- [x] Easy to update — flat list per category, easy to insert/remove
- [x] Easy to maintain — directly derived from Definitions' existing
      subdomain grouping, no separate classification scheme to keep in sync
- [x] Easy to replace — tree structure is descriptive, not load-bearing for
      any downstream system yet
