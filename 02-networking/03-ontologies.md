# Networking Domain — Ontologies

Status: Draft — pending review
Ratified: No
Last updated: 2026-09-22
Provenance: see _qa/03-ontologies.qa.md
Relation vocabulary: 00-framework/relation-types.md
Built on: 01-definitions.md, 02-taxonomies.md

Relationships may reference anchors owned by other domains (e.g.,
Infrastructure) where a genuine cross-domain relationship exists — this is
distinct from the "Referenced Terms" mechanism in Definitions, which is
about term ownership, not relationships between terms.

---

## Addressing

- `net-subnet` --[contains]--> `net-ip-address`
  Rationale: a subnet is composed of a range of IP addresses.
- `net-subnet` --[measured-by]--> `net-cidr-block`
  Rationale: a subnet's size/range is expressed via CIDR notation.

## Topology & Segmentation

- `net-vpc` --[contains]--> `net-subnet`
  Rationale: a VPC/VNet is subdivided into one or more subnets.
- `net-network-zone` --[contains]--> `net-vlan`
  Rationale: a network zone can group one or more VLANs sharing its trust posture.
- `net-segmentation` --[produces]--> `net-network-zone`
  Rationale: applying segmentation is what creates distinct network zones.
- `net-dmz` --[requires]--> `net-firewall`
  Rationale: a DMZ's boundary is enforced by firewall rules.
- `net-microsegmentation` --[requires]--> `net-zero-trust`
  Rationale: micro-segmentation is a common implementation pattern of zero trust principles.

## Routing

- `net-routing-table` --[contains]--> `net-route`
  Rationale: a routing table is composed of individual route entries.
- `net-gateway` --[requires]--> `net-routing-table`
  Rationale: a gateway makes forwarding decisions by consulting a routing table.
- `net-dynamic-routing` --[produces]--> `net-route`
  Rationale: dynamic routing protocols compute and produce routes automatically, as opposed to static routes being manually entered.

## Connectivity

- `net-vpn` --[requires]--> `net-vpn-tunnel`
  Rationale: a VPN is implemented through an encapsulated tunnel connection.
- `net-vpn` --[requires]--> `net-encryption-in-transit`
  Rationale: VPNs protect data by encrypting it in transit.
- `net-transit-gateway` --[requires]--> `net-vpc`
  Rationale: a transit gateway exists to interconnect multiple VPCs/VNets.
- `net-nat` --[requires]--> `net-gateway`
  Rationale: NAT is commonly performed at a gateway boundary.
- `net-ingress` --[requires]--> `net-firewall`
  Rationale: inbound traffic is filtered according to firewall rules.
- `net-egress` --[requires]--> `net-firewall`
  Rationale: outbound traffic is filtered according to firewall rules.

## Security Boundaries

- `net-firewall` --[requires]--> `net-acl`
  Rationale: firewalls enforce their rules via access control lists.
- `net-security-group` --[constrains]--> `net-vpc`
  Rationale: security groups constrain what traffic is allowed within a VPC/VNet.
- `net-perimeter` --[contains]--> `net-firewall`
  Rationale: perimeter-based security is traditionally implemented via firewalls at the boundary.
- `net-zero-trust` --[requires]--> `net-network-identity`
  Rationale: zero trust access decisions depend on verified identity, not network location.
- `net-zero-trust` --[requires]--> `net-trust-boundary`
  Rationale: zero trust explicitly defines and enforces trust boundaries rather than assuming a single perimeter.
- `net-zero-trust` --[constrains]--> `net-perimeter`
  Rationale: zero trust limits reliance on the traditional perimeter model as the sole security boundary.

## DNS & Service Discovery

- `net-domain-name` --[requires]--> `net-dns`
  Rationale: a domain name is only resolvable to an address through the DNS system.
- `net-service-discovery` --[requires]--> `net-dns`
  Rationale: DNS is a common mechanism by which service discovery is implemented.

## Load Balancing

- `net-load-balancer` --[requires]--> `net-traffic-policy`
  Rationale: a load balancer distributes traffic according to a defined policy.
- `net-reverse-proxy` --[runs-on]--> `infra-compute-unit`
  Rationale: cross-domain — a reverse proxy is software that executes on some compute unit (may be abstracted/managed, but a compute unit exists underneath).
- `net-load-balancer` --[runs-on]--> `infra-compute-unit`
  Rationale: cross-domain — same reasoning as reverse proxy; even a managed load balancer service runs on underlying compute.

## Transport Security

- `net-tls` --[produces]--> `net-encryption-in-transit`
  Rationale: TLS is the primary mechanism producing encryption in transit (not the only one — e.g., IPsec — but the dominant case).

## Performance Metrics (cross-domain)

- `net-bandwidth` --[constrains]--> `infra-throughput`
  Rationale: cross-domain — available bandwidth is the ceiling on achievable throughput; throughput can never exceed bandwidth.

---

## Cross-Domain References (relationships pointing into this domain)

Per 00-framework/relation-types.md's reverse-pointer rule, added once
System Architecture's ontology created a relationship into this domain.

- `net-encryption-in-transit`
  Referenced by (cross-domain relationships):
  - System Architecture: `sysarch-service --[requires]--> net-encryption-in-transit`

---

**Open items:**
- `net-transit-gateway --[requires]--> net-vpc` and `net-private-link`
  overlap conceptually (both connectivity alternatives to peering) but no
  direct relationship was drawn between them — left unconnected rather
  than forcing an artificial comparison relation, consistent with the
  "not every term needs a relationship" scope note.
- (Resolved 2026-09-22) Reverse-pointer rule added to
  00-framework/relation-types.md; Infrastructure's ontology
  (01-infrastructure/03-ontologies.md) updated with reverse pointers for
  infra-compute-unit and infra-throughput.

**Quality bar check (00-framework/quality-bar.md):**
- [x] Simple — ~26 relationships, no forced/artificial edges
- [x] Modular — each relationship stands alone
- [x] Easy to update — anchor-ID based, survives renames
- [x] Easy to maintain — grouped by subdomain, matches Definitions/Taxonomy
- [x] Easy to replace — relation-type vocabulary shared with Infrastructure, no duplication
