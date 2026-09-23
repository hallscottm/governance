# Networking Domain — Taxonomies

Status: Draft — pending review
Ratified: No
Last updated: 2026-09-22
Provenance: see _qa/02-taxonomies.qa.md
Built on: 01-definitions.md (47 owned terms)

Structure: strict single-parent tree, consistent with the standard set
during Infrastructure's Taxonomy column. Only terms owned by this domain
are classified here — the 3 referenced Infrastructure terms (Throughput,
Redundancy, Failover) are not re-classified in this domain's tree.

---

## Networking
├── Addressing & Core Protocols
│   ├── IP Address (#net-ip-address)
│   ├── IPv4 (#net-ipv4)
│   ├── IPv6 (#net-ipv6)
│   ├── MAC Address (#net-mac-address)
│   ├── Port (#net-port)
│   ├── Protocol (#net-protocol)
│   ├── Subnet (#net-subnet)
│   └── CIDR Block (#net-cidr-block)
│
├── Topology & Segmentation
│   ├── VLAN (#net-vlan)
│   ├── VPC/VNet (#net-vpc)
│   ├── Network Zone (#net-network-zone)
│   ├── DMZ (#net-dmz)
│   ├── Segmentation (#net-segmentation)
│   └── Micro-segmentation (#net-microsegmentation)
│
├── Routing
│   ├── Route (#net-route)
│   ├── Routing Table (#net-routing-table)
│   ├── Gateway (#net-gateway)
│   ├── Default Route (#net-default-route)
│   ├── Static Route (#net-static-route)
│   ├── Dynamic Routing (#net-dynamic-routing)
│   └── BGP (#net-bgp)
│
├── Connectivity
│   ├── VPN (#net-vpn)
│   ├── VPN Tunnel (#net-vpn-tunnel)
│   ├── Peering (#net-peering)
│   ├── Private Link/Direct Connect (#net-private-link)
│   ├── Transit Gateway (#net-transit-gateway)
│   ├── NAT (#net-nat)
│   ├── Ingress (#net-ingress)
│   └── Egress (#net-egress)
│
├── Security Boundaries
│   ├── Firewall (#net-firewall)
│   ├── Security Group (#net-security-group)
│   ├── ACL (#net-acl)
│   ├── Perimeter (#net-perimeter)
│   ├── Zero Trust (#net-zero-trust)
│   ├── Trust Boundary (#net-trust-boundary)
│   └── Network Identity (#net-network-identity)
│
├── DNS & Service Discovery
│   ├── DNS (#net-dns)
│   ├── Domain Name (#net-domain-name)
│   └── Service Discovery (#net-service-discovery)
│
├── Load Balancing & Traffic Management
│   ├── Load Balancer (#net-load-balancer)
│   ├── Reverse Proxy (#net-reverse-proxy)
│   └── Traffic Policy (#net-traffic-policy)
│
├── Transport Security
│   ├── TLS (#net-tls)
│   └── Encryption in Transit (#net-encryption-in-transit)
│
└── Performance Metrics
    ├── Latency (#net-latency)
    ├── Bandwidth (#net-bandwidth)
    ├── Packet Loss (#net-packet-loss)
    └── Jitter (#net-jitter)

---

**Coverage check:** all 47 owned terms from 01-definitions.md are
classified above, one category each. No orphaned terms, no term under
two categories.

**Open items:** none for this pass.

**Quality bar check (00-framework/quality-bar.md):**
- [x] Simple — single-parent tree, consistent with Infrastructure's precedent
- [x] Modular — each branch stands alone
- [x] Easy to update — flat list per category
- [x] Easy to maintain — directly derived from Definitions' subdomain grouping
- [x] Easy to replace — descriptive structure, not load-bearing for any system yet
