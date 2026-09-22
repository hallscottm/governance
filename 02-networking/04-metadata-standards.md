# Networking Layer — Metadata Standards

Status: Draft — pending review
Ratified: No
Last updated: 2026-09-22
Provenance: see _qa/04-metadata-standards.qa.md
Built on: 01-definitions.md, 02-taxonomies.md, 03-ontologies.md

Same shape as Infrastructure's Metadata Standards (shared field registry +
entity-type applicability matrix), reused without re-asking since it was
already established as the standard approach for this column.

## Referenced Fields (owned elsewhere)

Metadata Standards fields reference the underlying Definitions term they
draw from (Infrastructure's Metadata Standards table does the same — it
has no separate anchor system of its own; the anchor lives in
Definitions). Links below point to the actual anchored term.

- **Resource ID** — field defined in [01-infrastructure/04-metadata-standards.md](../01-infrastructure/04-metadata-standards.md), drawing from [01-infrastructure/01-definitions.md#infra-resource-id](../01-infrastructure/01-definitions.md#infra-resource-id) — applies to network resources unchanged
- **Cost Center Tag** — field defined in Infrastructure's Metadata Standards, drawing from [01-infrastructure/01-definitions.md#infra-cost-center-tag](../01-infrastructure/01-definitions.md#infra-cost-center-tag) — applies unchanged
- **Compute Environment / Environment (lifecycle)** — fields defined in Infrastructure's Metadata Standards, drawing from [01-infrastructure/01-definitions.md#infra-compute-environment](../01-infrastructure/01-definitions.md#infra-compute-environment) and [#infra-environment-lifecycle](../01-infrastructure/01-definitions.md#infra-environment-lifecycle) — a network resource belongs to an environment the same way a compute resource does

## Field Registry (owned by this layer)

| Field | Definition | Source Term | Required/Optional (default) |
|---|---|---|---|
| **CIDR Block** | The address range assigned to this resource. | `net-cidr-block` | Required for VPC/Subnet; N/A for other entity types |
| **Associated VPC** | Which VPC/VNet this resource belongs to. | `net-vpc` | Required for Subnet, Security Group, Load Balancer |
| **Network Zone** | Which trust/security zone this resource is classified under. | `net-network-zone` | Required for VPC, Subnet |
| **Trust Boundary Classification** | Whether this resource sits inside or outside a defined trust boundary (zero trust model). | `net-trust-boundary` | Optional — recommended for Security Boundaries entity types |
| **DNS Zone Name** | The domain name this resource is associated with, if applicable. | `net-domain-name` | Required for DNS Zone entity type; N/A otherwise |
| **Connectivity Type** | How this resource connects to other networks (VPN, Peering, Transit Gateway, Private Link). | `net-vpn`, `net-peering`, `net-transit-gateway`, `net-private-link` | Required for VPN/Connectivity entity type |

## Entity Types & Field Applicability

| Entity Type | Required Fields | Optional Fields |
|---|---|---|
| **VPC/VNet** | Resource ID, Compute Environment, CIDR Block, Network Zone, Cost Center Tag | Trust Boundary Classification |
| **Subnet** | Resource ID, Associated VPC, CIDR Block, Cost Center Tag | Network Zone (inherited from VPC unless overridden) |
| **Security Boundary (Firewall/Security Group/ACL)** | Resource ID, Associated VPC, Cost Center Tag | Trust Boundary Classification |
| **Load Balancer** | Resource ID, Associated VPC, Cost Center Tag | — |
| **DNS Zone** | Resource ID, DNS Zone Name, Cost Center Tag | — |
| **VPN/Connectivity Resource** | Resource ID, Connectivity Type, Cost Center Tag | — |

---

**Open items:**
- Enforcement (whether these fields are mandatory-blocking vs.
  recommended) is deferred to Policies (column 6), same boundary as
  Infrastructure's Metadata Standards.
- System Architecture-layer metadata (e.g., which application/service
  uses a given network resource) is explicitly out of scope here.
- Metadata Standards tables have no field-level anchors of their own
  (unlike Definitions/Ontology, which anchor every term). This means
  there's no reverse-pointer mechanism yet for "which other layers'
  Metadata Standards reference this field" the way Definitions has
  "Referenced by" and Ontology now has reverse pointers. Flagged as a
  framework-level gap, not fixed here — revisit if it causes real
  confusion once more layers reference Infrastructure's fields.

**Quality bar check (00-framework/quality-bar.md):**
- [x] Simple — one field registry (plus referenced fields), one matrix
- [x] Modular — a field's definition changes once, applies everywhere referenced
- [x] Easy to update — add an entity type as one matrix row
- [x] Easy to maintain — fields reference Definitions terms, cross-layer where genuinely shared
- [x] Easy to replace — tool-agnostic, ISO/IEC 11179-grounded (same standard as Infrastructure)
