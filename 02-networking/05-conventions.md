# Networking Layer — Conventions

Status: Draft — pending review
Ratified: No
Last updated: 2026-09-22
Provenance: see _qa/05-conventions.qa.md
Built on: 01-definitions.md, 04-metadata-standards.md

Scope: naming and tagging conventions for network resources themselves
(VPCs, subnets, security groups, load balancers, DNS zones). Code/repo
layout conventions remain reserved for Workflow/Process
(05-workflow-process/05-conventions.md, not yet drafted), same boundary
established in Infrastructure's Conventions.

---

## Resource Naming Convention

**Pattern:** `<env>-<compute-env>-<resource-type>-<seq>`

Extends Infrastructure's `<env>-<compute-env>-<service>-<seq>` pattern
(05-conventions.md, referenced from
00-framework/term-linking-convention.md's abbreviation registry) with a
`<resource-type>` segment in place of `<service>`, since network
resources are typed (VPC, subnet, security group) rather than tied to a
specific service.

| Segment | Values | Source |
|---|---|---|
| `<env>` | `dev`, `stg`, `prod` | Referenced from Infrastructure's abbreviation registry (01-infrastructure/05-conventions.md) |
| `<compute-env>` | `onprem`, `colo`, `pubcloud`, `privcloud`, `hybrid`, `edge` | Referenced from Infrastructure's abbreviation registry |
| `<resource-type>` | `vpc`, `subnet`, `sg` (security group), `fw` (firewall), `lb` (load balancer), `dns` (DNS zone), `vpn` | This layer's abbreviation registry, below |
| `<seq>` | Zero-padded sequence number, 3 digits minimum | Convention (same rule as Infrastructure) |

**Example:** `prod-pubcloud-vpc-001`, `prod-pubcloud-sg-002`

**Rules:** same as Infrastructure — lowercase, hyphen-separated, `<seq>`
resets per unique `<env>-<compute-env>-<resource-type>` combination.

## Tag Key Naming Convention

Same rule as Infrastructure: kebab-case, matching the Metadata Standards
field registry (04-metadata-standards.md), no free-text tag keys outside
the registry.

## Resource-Type Abbreviation Registry

| Full Term | Abbreviation | Anchor |
|---|---|---|
| VPC/VNet | `vpc` | `net-vpc` |
| Subnet | `subnet` | `net-subnet` |
| Security Group | `sg` | `net-security-group` |
| Firewall | `fw` | `net-firewall` |
| Load Balancer | `lb` | `net-load-balancer` |
| DNS Zone | `dns` | `net-domain-name` |
| VPN Connection | `vpn` | `net-vpn` |

This registry is this layer's addition to the naming pattern; `<env>` and
`<compute-env>` segments continue to draw from Infrastructure's registry
rather than duplicating it.

---

**Open items:**
- `<resource-type>` list covers the entity types already defined in
  04-metadata-standards.md's applicability matrix; if new network
  resource types are added later, this registry needs a matching new row.

**Quality bar check (00-framework/quality-bar.md):**
- [x] Simple — one pattern, one small abbreviation table
- [x] Modular — `<env>`/`<compute-env>` segments inherited from Infrastructure, not duplicated
- [x] Easy to update — add a resource type as a new table row
- [x] Easy to maintain — tag keys locked to Metadata Standards registry
- [x] Easy to replace — pattern is a convention, no tooling dependency yet
