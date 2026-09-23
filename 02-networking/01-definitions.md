# Networking Domain — Definitions

Status: Draft — pending review
Ratified: No
Last updated: 2026-09-22
Provenance: see _qa/01-definitions.qa.md
Linking convention: see 00-framework/term-linking-convention.md (ID prefix: `net`)

---

## Referenced Terms (owned elsewhere)

- **Throughput** — owned by Infrastructure → [01-infrastructure/01-definitions.md#infra-throughput](../01-infrastructure/01-definitions.md#infra-throughput) (its original definition already covers "storage or network resource" — not redefined here)
- **Redundancy** — owned by Infrastructure → [01-infrastructure/01-definitions.md#infra-redundancy](../01-infrastructure/01-definitions.md#infra-redundancy) (applies equally to redundant links/routers, not network-specific)
- **Failover** — owned by Infrastructure → [01-infrastructure/01-definitions.md#infra-failover](../01-infrastructure/01-definitions.md#infra-failover)

---

## Addressing & Core Protocols

### IP Address {#net-ip-address}
A numerical label assigned to a device on a network for identification and location addressing.
Source: IETF RFC 791 (IPv4) / RFC 8200 (IPv6)

### IPv4 {#net-ipv4}
The fourth version of the Internet Protocol, using 32-bit addresses.
Source: IETF RFC 791

### IPv6 {#net-ipv6}
The sixth version of the Internet Protocol, using 128-bit addresses, designed to succeed IPv4.
Source: IETF RFC 8200

### MAC Address {#net-mac-address}
A hardware identifier assigned to a network interface at the link domain.
Source: IEEE 802.3

### Port {#net-port}
A numbered logical endpoint on a device distinguishing multiple simultaneous network connections/services.
Source: IANA/IETF

### Protocol {#net-protocol}
A defined set of rules governing how data is formatted and exchanged between devices.
Source: Common industry practice

### Subnet {#net-subnet}
A logically visible subdivision of an IP network.
Source: IETF RFC 950 / common practice

### CIDR Block {#net-cidr-block}
A notation (address/prefix-length) expressing a range of IP addresses without fixed class boundaries.
Source: IETF RFC 4632

## Topology & Segmentation

### VLAN {#net-vlan}
A logically segmented broadcast domain created within a physical network, independent of physical location.
Source: IEEE 802.1Q

### VPC/VNet {#net-vpc}
An isolated virtual network within a cloud provider's infrastructure, logically separated from other tenants.
Source: Common cloud provider practice

### Network Zone {#net-network-zone}
A logically grouped segment of a network sharing a common trust/security posture.
Source: NIST SP 800-207 (zero trust zoning concept)

### DMZ {#net-dmz}
A network segment that sits between an internal network and an untrusted external network, hosting externally-facing services.
Source: NIST SP 800-41 / common practice

### Segmentation {#net-segmentation}
The practice of dividing a network into smaller, isolated segments to limit the blast radius of a breach and control traffic flow.
Source: ISO/IEC 27033 / NIST SP 800-207

### Micro-segmentation {#net-microsegmentation}
Fine-grained segmentation applied at the individual workload level rather than at the network-zone level.
Source: NIST SP 800-207

## Routing

### Route {#net-route}
A defined path that network traffic follows from source to destination.
Source: Common industry practice

### Routing Table {#net-routing-table}
A data structure listing routes to particular network destinations.
Source: Common industry practice

### Gateway {#net-gateway}
A node that serves as an access point to another network, often translating between routing domains.
Source: Common industry practice

### Default Route {#net-default-route}
The route used to forward traffic when no more specific route matches.
Source: Common industry practice

### Static Route {#net-static-route}
A manually configured route that does not change unless explicitly updated.
Source: Common industry practice

### Dynamic Routing {#net-dynamic-routing}
Automated route computation and adjustment based on real-time network topology/state.
Source: Common industry practice

### BGP {#net-bgp}
Border Gateway Protocol — the standard protocol for exchanging routing information between autonomous systems on the internet.
Source: IETF RFC 4271

## Connectivity

### VPN {#net-vpn}
A Virtual Private Network — an encrypted connection extending a private network across a public network.
Source: IETF RFC 4301 (IPsec) / common practice

### VPN Tunnel {#net-vpn-tunnel}
The encapsulated, encrypted logical connection established by a VPN between two endpoints.
Source: Common industry practice

### Peering {#net-peering}
A direct interconnection between two networks to exchange traffic without transiting a third party.
Source: Common industry practice

### Private Link / Direct Connect {#net-private-link}
A dedicated, private connectivity path between an organization's network and a cloud provider, bypassing the public internet.
Source: Common cloud provider practice

### Transit Gateway {#net-transit-gateway}
A network hub that connects multiple virtual networks and on-premises networks through a single point.
Source: Common cloud provider practice

### NAT {#net-nat}
Network Address Translation — remapping IP addresses between address spaces, typically to allow private addresses to communicate externally.
Source: IETF RFC 3022

### Ingress {#net-ingress}
Traffic entering a network or network segment from outside it.
Source: Common industry practice

### Egress {#net-egress}
Traffic leaving a network or network segment to a destination outside it.
Source: Common industry practice

## Security Boundaries

### Firewall {#net-firewall}
A system that monitors and controls incoming/outgoing network traffic based on defined security rules.
Source: NIST SP 800-41

### Security Group {#net-security-group}
A virtual, stateful firewall applied at the resource level in cloud environments, controlling allowed traffic.
Source: Common cloud provider practice

### ACL (Access Control List) {#net-acl}
An ordered set of rules that permit or deny traffic based on defined criteria (source, destination, port, protocol).
Source: Common industry practice

### Perimeter {#net-perimeter}
The traditional network security boundary separating trusted internal networks from untrusted external ones.
Source: Common industry practice (traditional network security model)

### Zero Trust {#net-zero-trust}
A security model that assumes no implicit trust based on network location; every access request is verified regardless of origin.
Source: NIST SP 800-207

### Trust Boundary {#net-trust-boundary}
A defined line across which data or requests are treated as requiring verification, per zero trust principles.
Source: NIST SP 800-207

### Network Identity {#net-network-identity}
An authenticated identity (device, workload, or user) used to make access decisions independent of network location.
Source: NIST SP 800-207

## DNS & Service Discovery

### DNS {#net-dns}
The Domain Name System — a hierarchical, distributed naming system translating human-readable domain names to IP addresses.
Source: IETF RFC 1035

### Domain Name {#net-domain-name}
A human-readable label identifying a network resource, resolved via DNS.
Source: IETF RFC 1035

### Service Discovery {#net-service-discovery}
The automated process by which services locate each other on a network without hardcoded addresses.
Source: Common industry practice

## Load Balancing & Traffic Management

### Load Balancer {#net-load-balancer}
A system that distributes incoming traffic across multiple backend resources to optimize utilization and availability.
Source: Common industry practice
Referenced by: System Architecture

### Reverse Proxy {#net-reverse-proxy}
A server that sits in front of backend services, forwarding client requests to them and returning responses.
Source: Common industry practice

### Traffic Policy {#net-traffic-policy}
A defined rule set governing how traffic is routed, prioritized, or shaped.
Source: Common industry practice

## Transport Security

### TLS {#net-tls}
Transport Layer Security — the standard protocol for encrypting data in transit between networked systems.
Source: IETF RFC 8446 (TLS 1.3)
Referenced by: System Architecture

### Encryption in Transit {#net-encryption-in-transit}
The practice of encrypting data while it moves across a network, as distinct from encryption at rest.
Source: NIST SP 800-53 (SC family) / common practice
Referenced by: System Architecture

## Performance Metrics

### Latency {#net-latency}
The time delay between a request being sent and a response being received across a network.
Source: Common industry practice

### Bandwidth {#net-bandwidth}
The maximum data transfer capacity of a network link, typically measured in bits per second.
Source: Common industry practice

### Packet Loss {#net-packet-loss}
The percentage of data packets that fail to reach their destination.
Source: Common industry practice

### Jitter {#net-jitter}
Variability in packet arrival times, relevant to latency-sensitive traffic (e.g., voice/video).
Source: Common industry practice

---

**Open items:** none — full subdomain sweep complete for this pass (per
the lesson from Infrastructure's initial thin pass). New terms may still
surface once System Architecture or Data/Metadata are drafted and
cross-reference back here.

**Quality bar check (00-framework/quality-bar.md):**
- [x] Simple — terms borrowed from established standards, not invented
- [x] Modular — each term stands alone under its own anchor
- [x] Easy to update — flat, anchored structure
- [x] Easy to maintain — sourced to named standards
- [x] Easy to replace — no duplication of Infrastructure's already-generic
      terms (Throughput, Redundancy, Failover referenced, not redefined)
