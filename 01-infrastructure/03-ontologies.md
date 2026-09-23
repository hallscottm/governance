# Infrastructure Layer — Ontologies

Status: Draft — pending review
Ratified: No
Last updated: 2026-09-22
Provenance: see _qa/03-ontologies.qa.md
Relation vocabulary: 00-framework/relation-types.md
Built on: 01-definitions.md, 02-taxonomies.md

Not every term appears below — only terms with a meaningful relationship
to another term in this layer. See scope note in relation-types.md.

---

## Virtualization & Compute Stack

- `infra-vm` --[runs-on]--> `infra-hypervisor`
  Rationale: a VM is emulated and managed by a hypervisor.
- `infra-hypervisor` --[runs-on]--> `infra-bare-metal`
  Rationale: hypervisors run directly on physical hardware.
- `infra-container` --[runs-on]--> `infra-container-runtime`
  Rationale: containers are executed by a runtime (e.g., containerd).
- `infra-container-runtime` --[runs-on]--> `infra-compute-unit`
  Rationale: the runtime itself executes on some compute unit (VM or bare metal).
- `infra-orchestrator` --[requires]--> `infra-container-runtime`
  Rationale: orchestration (e.g., scheduling containers across a cluster) depends on a runtime being present on each node.

## Compute Hardware Composition

- `infra-cpu` --[contains]--> `infra-core`
  Rationale: a CPU package is composed of one or more cores.
- `infra-gpu` --[contains]--> `infra-gpu-memory`
  Rationale: VRAM is physically part of the GPU.
- `infra-compute-unit` --[consumes]--> `infra-vcpu`
  Rationale: a compute unit is allocated a share of CPU capacity as vCPUs.
- `infra-instance-type` --[constrains]--> `infra-compute-unit`
  Rationale: the chosen instance type defines the resource envelope (CPU/memory/etc.) available to the compute unit.

## AI-Specific Compute

- `infra-training-workload` --[runs-on]--> `infra-gpu`
  Rationale: training is typically GPU-bound.
- `infra-training-workload` --[consumes]--> `infra-gpu-memory`
  Rationale: model size and batch size are bounded by available VRAM.
- `infra-inference-workload` --[runs-on]--> `infra-model-serving-node`
  Rationale: inference requests are served by dedicated serving nodes.
- `infra-model-serving-node` --[runs-on]--> `infra-compute-unit`
  Rationale: a model-serving node is itself hosted on some compute unit.
- `infra-model-serving-node` --[consumes]--> `infra-gpu-memory`
  Rationale: serving nodes typically require GPU memory to hold the model.

## Placement / Facility

- `infra-compute-unit` --[located-in]--> `infra-compute-environment`
  Rationale: every compute unit exists within one of the six defined environment categories.
- `infra-rack` --[located-in]--> `infra-data-center`
  Rationale: racks are housed within a data center facility.
- `infra-compute-unit` --[located-in]--> `infra-rack`
  Rationale: applies for on-prem/colocation/private-cloud bare-metal deployments; not applicable for public-cloud abstracted compute (see open items below).
- `infra-data-center` --[requires]--> `infra-cooling`
  Rationale: facility operation depends on maintaining safe operating temperature.
- `infra-data-center` --[requires]--> `infra-power-draw`
  Rationale: facility operation depends on power supply matching equipment load.
- `infra-data-center` --[measured-by]--> `infra-pue`
  Rationale: PUE is the standard efficiency metric for a data center.

## Capacity & Scaling

- `infra-compute-unit` --[scales-via]--> `infra-vertical-scaling`
  Rationale: one scaling mechanism available to a compute unit.
- `infra-compute-unit` --[scales-via]--> `infra-horizontal-scaling`
  Rationale: the other scaling mechanism available to a compute unit.
- `infra-autoscaling` --[requires]--> `infra-horizontal-scaling`
  Rationale: autoscaling in common practice automates the addition/removal of compute units, i.e., horizontal scaling.
- `infra-compute-unit` --[consumes]--> `infra-provisioned-capacity`
  Rationale: one of three capacity-acquisition models a compute unit can draw on.
- `infra-compute-unit` --[consumes]--> `infra-on-demand-capacity`
  Rationale: second capacity-acquisition model.
- `infra-compute-unit` --[consumes]--> `infra-reserved-capacity`
  Rationale: third capacity-acquisition model.

## Storage Relationships

- `infra-block-storage` --[measured-by]--> `infra-iops`
  Rationale: IOPS is a primary performance metric for block storage.
- `infra-block-storage` --[measured-by]--> `infra-throughput`
  Rationale: throughput is a primary performance metric for block storage.
- `infra-object-storage` --[measured-by]--> `infra-durability-class`
  Rationale: object storage services are typically rated by durability class.
- `infra-object-storage` --[measured-by]--> `infra-replication-factor`
  Rationale: durability in object storage is commonly achieved through replication.
- `infra-backup` --[consumes]--> `infra-snapshot`
  Rationale: backups are commonly built from point-in-time snapshots.
- `infra-archive` --[located-in]--> `infra-storage-tier-frozen-archival`
  Rationale: archival data is placed in the frozen/archival storage tier by definition.

## Resilience & Availability

- `infra-failover` --[requires]--> `infra-redundancy`
  Rationale: failing over to a standby resource requires that a redundant resource exists.
- `infra-dr-tier` --[requires]--> `infra-failover`
  Rationale: a disaster recovery classification presumes some failover capability.
- `infra-dr-tier` --[requires]--> `infra-backup`
  Rationale: recovery from a major outage presumes restorable backups exist.
- `infra-availability-tier-i` --[constrains]--> `infra-redundancy`
  Rationale: (and similarly for Tiers II–IV) — the availability tier chosen dictates the minimum redundancy required. Shown once here; applies to all four tiers.

## Lifecycle

- `infra-compute-unit` --[has-lifecycle-state]--> `infra-provisioning`
- `infra-compute-unit` --[has-lifecycle-state]--> `infra-maintenance-window`
- `infra-compute-unit` --[has-lifecycle-state]--> `infra-decommissioning`
- `infra-compute-unit` --[has-lifecycle-state]--> `infra-eol`
  Rationale (all four): these are the states a compute unit can be in
  over its lifetime, in typical (though not strictly linear) sequence:
  Provisioning → (operating, subject to Maintenance Windows) → EOL →
  Decommissioning.
- `infra-provisioning` --[produces]--> `infra-resource-id`
  Rationale: a resource ID is assigned at provisioning time.
- `infra-provisioning` --[produces]--> `infra-asset-tag`
  Rationale: an asset tag is typically assigned when a resource is provisioned/tracked.

## Cost / FinOps

- `infra-chargeback-unit` --[requires]--> `infra-cost-center-tag`
  Rationale: attributing cost back to a team requires the resource to carry a cost center tag.

---

**Open items:**
- `infra-compute-unit --[located-in]--> infra-rack` is conditionally true
  (on-prem/colo/private-cloud/bare-metal) but not universally true (public
  cloud abstracts physical placement away from the tenant). Flagged rather
  than silently generalized — revisit if this ambiguity causes confusion
  downstream (e.g., when Networking or System Architecture references it).
- Availability Tier II and III --[constrains]--> Redundancy relationships
  were not written out individually (noted once under Tier I to avoid
  four near-identical lines) — acceptable for a first pass per the
  "simple" quality bar, but flag if a future consumer needs each tier's
  relationship as a distinct, separately-queryable row.

**Quality bar check (00-framework/quality-bar.md):**
- [x] Simple — 9-type vocabulary, ~35 relationships, no forced/artificial edges
- [x] Modular — each relationship stands alone; removing one doesn't break others
- [x] Easy to update — anchor-ID based, survives display-text renames
- [x] Easy to maintain — grouped by subdomain, matches Definitions/Taxonomy structure
- [x] Easy to replace — relation-type vocabulary is a shared framework asset, not layer-specific, so a change there is made once

## Cross-Layer References (relationships pointing into this layer)

Per 00-framework/relation-types.md's reverse-pointer rule, added
retroactively once Networking's ontology created relationships into this
layer.

- `infra-compute-unit`
  Referenced by (cross-layer relationships):
  - Networking: `net-load-balancer --[runs-on]--> infra-compute-unit`
  - Networking: `net-reverse-proxy --[runs-on]--> infra-compute-unit`
  - System Architecture: `sysarch-serverless-architecture --[runs-on]--> infra-compute-unit`
  - System Architecture: `sysarch-database --[runs-on]--> infra-compute-unit`
- `infra-throughput`
  Referenced by (cross-layer relationships):
  - Networking: `net-bandwidth --[constrains]--> infra-throughput`
- `infra-container`
  Referenced by (cross-layer relationships):
  - System Architecture: `sysarch-service --[runs-on]--> infra-container`
  - System Architecture: `sysarch-container-image --[produces]--> infra-container`
- `infra-block-storage`
  Referenced by (cross-layer relationships):
  - System Architecture: `sysarch-database --[requires]--> infra-block-storage`
- `infra-horizontal-scaling`
  Referenced by (cross-layer relationships):
  - System Architecture: `sysarch-stateless-service --[scales-via]--> infra-horizontal-scaling`
  - System Architecture: `sysarch-scalability --[scales-via]--> infra-horizontal-scaling`
- `infra-environment-lifecycle`
  Referenced by (cross-layer relationships):
  - System Architecture: `sysarch-release --[has-lifecycle-state]--> infra-environment-lifecycle`
- `infra-redundancy`
  Referenced by (cross-layer relationships):
  - System Architecture: `sysarch-resilience --[requires]--> infra-redundancy`
- `infra-availability-tier`
  Note: this anchor is the SOURCE (not target) of one cross-layer
  relationship — `infra-availability-tier --[constrains]--> sysarch-availability`
  — recorded in full in 03-system-architecture/03-ontologies.md. Listed
  here for discoverability since the relationship touches this term.
- `infra-archive`
  Referenced by (cross-layer relationships):
  - Data/Metadata: `data-archival --[requires]--> infra-archive`
