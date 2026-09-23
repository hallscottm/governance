# Infrastructure Domain — Definitions

Status: Draft — pending review
Ratified: No
Last updated: 2026-09-22
Provenance: see _qa/01-definitions.qa.md
Linking convention: see 00-framework/term-linking-convention.md (ID prefix: `infra`)

Every term below is owned by this domain. Terms owned by other domains but
relevant here will appear in a "Referenced Terms (owned elsewhere)" section
once those domains exist.

---

## Environments & Compute Categories

### Compute Environment {#infra-compute-environment}
A category of physical or virtual location where compute runs. Valid types:
On-Premises, Colocation, Public Cloud, Private Cloud, Hybrid, Edge.
Source: Org convention (generalized)

### Environment (lifecycle) {#infra-environment-lifecycle}
A logically or physically isolated instance of infrastructure used for a
specific stage of the software/data lifecycle. Standard tiers: Development,
Staging/QA, Production.
Source: Common industry practice
Referenced by: Networking, System Architecture, Data/Metadata

### Compute Unit {#infra-compute-unit}
The smallest independently provisionable unit of processing capacity (e.g.,
a VM, container, physical server, or GPU instance).
Source: Common industry practice

## Compute Hardware

### CPU {#infra-cpu}
General-purpose processor executing sequential instructions.
Source: Common industry practice

### GPU {#infra-gpu}
Processor optimized for parallel computation; primary hardware for AI
training/inference.
Source: Common industry practice

### Accelerator (TPU/other) {#infra-accelerator}
Purpose-built processor for a specific workload class (e.g., ML tensor
operations) beyond general GPU use.
Source: Common industry practice

### vCPU {#infra-vcpu}
A virtualized, shareable unit of CPU capacity allocated to a compute unit.
Source: Common cloud provider practice (AWS/Azure/GCP-aligned)

### Core {#infra-core}
A single physical processing unit within a CPU/GPU package.
Source: Common industry practice

### Instance Type/Size Class {#infra-instance-type}
A predefined bundle of compute, memory, and sometimes storage/network
capacity offered as a unit.
Source: Common cloud provider practice

### Bare Metal {#infra-bare-metal}
A physical server provisioned without a hypervisor domain, dedicated to a
single tenant.
Source: Common industry practice

### Virtual Machine (VM) {#infra-vm}
An emulated computer running its own OS, provisioned on shared physical
hardware via a hypervisor.
Source: Common industry practice

### Container {#infra-container}
A lightweight, isolated runtime sharing the host OS kernel, packaging an
application and its dependencies.
Source: OCI (Open Container Initiative)
Referenced by: System Architecture (Container Image)

## AI-Specific Compute

### Inference Workload {#infra-inference-workload}
Compute performing predictions using an already-trained AI model.
Source: Common ML industry practice
Referenced by: System Architecture, Harness (pending — domains not yet built)

### Training Workload {#infra-training-workload}
Compute used to fit/update an AI model's parameters against data.
Source: Common ML industry practice
Referenced by: System Architecture, Harness (pending — domains not yet built)

### GPU Memory (VRAM) {#infra-gpu-memory}
Dedicated high-bandwidth memory on a GPU, a key constraint for model size/
batch size.
Source: Common industry practice
Referenced by: System Architecture, Harness (pending — domains not yet built)

### Model-Serving Node {#infra-model-serving-node}
A compute unit dedicated to hosting a deployed model for inference requests.
Source: Common ML industry practice
Referenced by: System Architecture, Harness (pending — domains not yet built)

## Storage

### Storage Tier — Hot {#infra-storage-tier-hot}
Storage optimized for frequent access and low latency; highest relative
cost.
Source: Common industry practice (AWS/Azure/GCP-aligned)

### Storage Tier — Warm {#infra-storage-tier-warm}
Storage for occasionally accessed data; moderate cost/latency tradeoff.
Source: Common industry practice

### Storage Tier — Cold {#infra-storage-tier-cold}
Storage for rarely accessed data; optimized for cost over speed.
Source: Common industry practice

### Storage Tier — Frozen/Archival {#infra-storage-tier-frozen-archival}
Storage for compliance retention; lowest cost, highest retrieval latency.
Source: Common industry practice

### Block Storage {#infra-block-storage}
Raw storage volumes addressed in fixed-size blocks; typically attached to a
single compute unit.
Source: Common industry practice

### Object Storage {#infra-object-storage}
Storage addressed by unique keys/metadata rather than a file hierarchy;
scales horizontally.
Source: Common industry practice

### File Storage {#infra-file-storage}
Storage organized in a hierarchical directory/file structure, often shared
across compute units.
Source: Common industry practice

### IOPS {#infra-iops}
Input/output operations per second — a storage performance metric.
Source: Common industry practice

### Throughput {#infra-throughput}
Data transfer rate, typically MB/s or GB/s, for a storage or network
resource.
Source: Common industry practice
Referenced by: Networking

### Durability Class {#infra-durability-class}
The statistical likelihood a stored object survives without loss over a
given period.
Source: Common cloud provider practice

### Replication Factor {#infra-replication-factor}
The number of redundant copies of data maintained across storage locations.
Source: Common industry practice

### Snapshot {#infra-snapshot}
A point-in-time, typically incremental, copy of a storage volume's state.
Source: Common industry practice

### Backup {#infra-backup}
A separate, restorable copy of data retained for recovery from loss or
corruption.
Source: Common industry practice

### Archive {#infra-archive}
Long-term, infrequently accessed data retention, often for compliance
rather than operational recovery.
Source: Common industry practice
Referenced by: Data/Metadata

## Facility / Physical

### Data Center {#infra-data-center}
A physical facility housing compute, storage, and networking
infrastructure.
Source: TIA-942

### Rack {#infra-rack}
A standardized physical enclosure housing multiple servers/network devices.
Source: TIA-942

### Power Draw (kW) {#infra-power-draw}
The electrical load a piece of infrastructure or facility consumes.
Source: TIA-942

### Cooling {#infra-cooling}
Facility systems maintaining safe operating temperature for hardware.
Source: TIA-942

### PUE (Power Usage Effectiveness) {#infra-pue}
Ratio of total facility power to IT-equipment power; measures data center
efficiency.
Source: Green Grid / Uptime Institute

## Availability

### Availability Tier I {#infra-availability-tier-i}
Basic capacity, no redundancy.
Source: Uptime Institute Tier Classification

### Availability Tier II {#infra-availability-tier-ii}
Redundant capacity components.
Source: Uptime Institute Tier Classification

### Availability Tier III {#infra-availability-tier-iii}
Concurrently maintainable, no downtime for planned maintenance.
Source: Uptime Institute Tier Classification

### Availability Tier IV {#infra-availability-tier-iv}
Fault-tolerant, no downtime for planned or unplanned events.
Source: Uptime Institute Tier Classification

## Virtualization

### Hypervisor {#infra-hypervisor}
Software domain that creates and runs virtual machines on physical
hardware.
Source: Common industry practice

### Container Runtime {#infra-container-runtime}
Software that executes and manages containers on a host (e.g., containerd).
Source: OCI

### Orchestrator {#infra-orchestrator}
System that automates deployment, scaling, and management of containers/
VMs across a cluster.
Source: Common industry practice

## Capacity & Scaling

### Vertical Scaling {#infra-vertical-scaling}
Increasing capacity by adding resources to an existing compute unit.
Source: Common industry practice

### Horizontal Scaling {#infra-horizontal-scaling}
Increasing capacity by adding more compute units.
Source: Common industry practice

### Autoscaling {#infra-autoscaling}
Automated addition/removal of compute capacity based on demand signals.
Source: Common industry practice

### Provisioned Capacity {#infra-provisioned-capacity}
Capacity allocated and reserved in advance of use.
Source: Common industry practice

### On-Demand Capacity {#infra-on-demand-capacity}
Capacity requested and billed as used, without advance reservation.
Source: Common industry practice

### Reserved Capacity {#infra-reserved-capacity}
Capacity committed to in advance, typically at a discount, for a fixed
term.
Source: Common cloud provider practice

## Resource Identity

### Asset Tag {#infra-asset-tag}
A unique identifier attached to a physical or virtual asset for tracking.
Source: ISO/IEC 27001 (Annex A asset management)

### Resource ID {#infra-resource-id}
A unique, system-generated identifier for a provisioned resource.
Source: Common industry practice

## Lifecycle

### Provisioning {#infra-provisioning}
The process of allocating and configuring infrastructure for use.
Source: Common industry practice

### Decommissioning {#infra-decommissioning}
The process of retiring infrastructure and sanitizing/disposing of it
securely.
Source: NIST SP 800-88 (Media Sanitization)

### End-of-Life (EOL) {#infra-eol}
The point at which a hardware/software asset is no longer supported or
maintained.
Source: Common industry practice

### Maintenance Window {#infra-maintenance-window}
A scheduled period during which planned changes/patches occur.
Source: NIST SP 800-53 (CM family)

## Resilience

### Redundancy {#infra-redundancy}
Duplication of critical components to prevent single points of failure.
Source: NIST SP 800-53 (CP family)
Referenced by: Networking

### Failover {#infra-failover}
Automatic switching to a redundant/standby resource upon failure.
Source: Common industry practice
Referenced by: Networking

### Disaster Recovery (DR) Tier {#infra-dr-tier}
A classification of how quickly and completely a system must recover after
a major outage.
Source: NIST SP 800-34

## Cost / FinOps

### Cost Center Tag {#infra-cost-center-tag}
A label associating infrastructure spend with an organizational budget
owner.
Source: FinOps Foundation

### Chargeback Unit {#infra-chargeback-unit}
The unit by which infrastructure cost is attributed back to a consuming
team/department.
Source: FinOps Foundation

---

**Scope decisions made this pass:**
- AI-specific compute terms retained in Infrastructure (owner), tagged
  Referenced by System Architecture and Harness for when those domains are
  built.
- Cost/FinOps terms included now rather than deferred.

**Open items:** none — full subdomain sweep complete for this pass. New
terms may still surface once Networking/System Architecture/Data-Metadata
are drafted and cross-reference back here.

**Quality bar check (00-framework/quality-bar.md):**
- [x] Simple — terms borrowed from established standards, not invented
- [x] Modular — each term stands alone under its own anchor; no
      interdependency within this column
- [x] Easy to update — flat, anchored structure; add/edit one term without
      touching others
- [x] Easy to maintain — sourced to named standards, no ambiguity about
      ownership
- [x] Easy to replace — adopting external standard vocabulary rather than a
      custom scheme; cross-domain references are links, not copies (see
      00-framework/term-linking-convention.md)
