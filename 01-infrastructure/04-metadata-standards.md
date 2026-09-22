# Infrastructure Layer — Metadata Standards

Status: Draft — pending review
Ratified: No
Last updated: 2026-09-22
Provenance: see _qa/04-metadata-standards.qa.md
Built on: 01-definitions.md, 02-taxonomies.md, 03-ontologies.md

Defines how real infrastructure instances (an actual server, VM, storage
volume, etc.) get tagged/described so AI tooling and metadata catalogs
(e.g., OpenMetadata — tool selection deferred to column 10) can reliably
interpret them. Field definitions reference terms already defined in this
layer rather than restating them (DRY, per
00-framework/term-linking-convention.md).

Standards grounding: ISO/IEC 11179 (Metadata Registries), DAMA-DMBOK
(metadata management discipline, though DAMA is primarily the Data/
Metadata layer's standard — cited here for the general metadata
governance practice it establishes).

---

## Field Registry

Every field below is defined once. Entity types (below) reference fields
by name; they do not redefine them.

| Field | Definition | Source Term | Required/Optional (default) |
|---|---|---|---|
| **Resource ID** | Unique system-generated identifier for the instance. | `infra-resource-id` | Required — always |
| **Asset Tag** | Identifier linking the instance to organizational asset tracking. | `infra-asset-tag` | Required for physical assets; optional for ephemeral virtual resources |
| **Compute Environment** | Which of the six environment categories this instance runs in. | `infra-compute-environment` | Required — always |
| **Environment (lifecycle)** | Dev/Staging-QA/Production classification. | `infra-environment-lifecycle` | Required — always |
| **Instance Type/Size Class** | The resource envelope (CPU/memory/etc.) assigned. | `infra-instance-type` | Required for compute instances; N/A for pure storage |
| **Storage Tier** | Hot/Warm/Cold/Frozen classification. | `infra-storage-tier-hot` (and siblings) | Required for storage instances; N/A for compute |
| **Availability Tier** | Uptime Institute Tier I–IV commitment for this instance. | `infra-availability-tier-i` (and siblings) | Required for production; optional for dev/staging |
| **Cost Center Tag** | Budget owner attribution. | `infra-cost-center-tag` | Required — always |
| **Provisioned Date** | Timestamp the instance was provisioned. | `infra-provisioning` | Required — always |
| **Decommission Date** | Timestamp the instance was or is scheduled to be retired. | `infra-decommissioning` | Optional — filled at EOL, null until then |
| **Redundancy Level** | Whether/how this instance is duplicated. | `infra-redundancy` | Optional — recommended for production |
| **DR Tier** | Disaster recovery classification. | `infra-dr-tier` | Optional — recommended for production |
| **GPU-Backed** | Whether the instance has GPU/accelerator hardware. | `infra-gpu`, `infra-accelerator` | Required for AI-specific compute; N/A otherwise |
| **Workload Class** | Inference / Training / General-purpose. | `infra-inference-workload`, `infra-training-workload` | Required for AI-specific compute; N/A otherwise |

## Entity Types & Field Applicability

| Entity Type | Required Fields | Optional Fields |
|---|---|---|
| **Compute Unit (general)** | Resource ID, Compute Environment, Environment (lifecycle), Instance Type, Cost Center Tag, Provisioned Date | Availability Tier, Redundancy Level, DR Tier, Decommission Date, Asset Tag |
| **AI-Specific Compute (training/inference/model-serving)** | All of Compute Unit (general), plus: GPU-Backed, Workload Class | Same optional set as Compute Unit (general) |
| **Storage Instance (volume/object/bucket)** | Resource ID, Compute Environment, Storage Tier, Cost Center Tag, Provisioned Date | Availability Tier, Redundancy Level, DR Tier, Decommission Date |
| **Physical Asset (server, rack-mounted hardware)** | Resource ID, Asset Tag, Compute Environment, Cost Center Tag, Provisioned Date | Decommission Date |

---

**Open items:**
- Networking-layer metadata (e.g., IP allocation, VLAN tagging) is
  explicitly out of scope here — belongs to the Networking layer once
  drafted, not duplicated into this registry.
- Whether these fields should be *enforced* (rejected if missing) vs.
  *recommended* is a Policy-column decision (column 6), not a Metadata
  Standards decision — this column defines what the fields mean and where
  they apply, not the enforcement mechanism.

**Quality bar check (00-framework/quality-bar.md):**
- [x] Simple — one field registry, one applicability matrix, no repeated schemas
- [x] Modular — a field's definition changes once, applies everywhere it's referenced
- [x] Easy to update — add a new entity type by adding one matrix row, not a new schema
- [x] Easy to maintain — fields reference existing Definitions-column terms, no parallel vocabulary
- [x] Easy to replace — schema is standards-grounded (ISO/IEC 11179) and tool-agnostic; implementation tool chosen separately in column 10
