# Networking Layer — Standards Alignment

Status: Draft — pending review
Ratified: No
Last updated: 2026-09-22

Reference panel for this layer, consulted before drafting Definitions.
Scope per 00-framework/layer-axis-definition.md: connectivity,
segmentation, routing, network boundaries — explicitly not compute
substrate (Infrastructure) or applications/databases (System Architecture).

| Standard | Body | Covers |
|---|---|---|
| **NIST SP 800-207** | NIST | Zero Trust Architecture — identity-centric access, never-trust-always-verify network design |
| **NIST SP 800-41** | NIST | Firewalls and firewall policy |
| **ISO/IEC 27033 (multi-part)** | ISO | Network security design, architecture, and controls |
| **ISO/IEC 27001 Annex A (A.13)** | ISO | Communications security (overlaps with Infrastructure's Annex A citation, different control family — A.13 specifically) |
| **IETF RFC series (core protocols)** | IETF | Foundational protocol definitions: RFC 791 (IPv4), RFC 8200 (IPv6), RFC 793/9293 (TCP), RFC 768 (UDP), RFC 1035 (DNS), RFC 8446 (TLS 1.3), RFC 4271 (BGP) |
| **IEEE 802 series** | IEEE | Link-layer standards: 802.3 (Ethernet), 802.11 (Wi-Fi), 802.1Q (VLAN tagging) |
| **CIS Benchmarks (network devices)** | Center for Internet Security | Configuration hardening baselines for routers, switches, firewalls |

**Not yet consulted, candidate for future passes:**
- **PCI-DSS network segmentation requirements** — relevant if/when this
  framework's Risk Tiers column (9) surfaces payment-card-data scope;
  deferred until that's a real determination, not assumed here
- **DAMA-DMBOK** — not applicable to this layer (data governance, not
  networking)

**Note on citation confidence:** IETF RFCs, IEEE 802 standards, and NIST
SP publications are stable and well-established — citations here are from
general knowledge and reliable without re-verification. ISO/IEC 27033 is
periodically revised; if this becomes load-bearing for a compliance
context, verify against the current published edition before ratifying.

**Quality bar check (00-framework/quality-bar.md):**
- [x] Simple — one table, scoped to what this layer actually covers
- [x] Modular — independent of Infrastructure's standards panel, no forced overlap beyond the genuine ISO 27001 connection
- [x] Easy to update — new standard cited later just adds a row
- [x] Easy to maintain — will be reconciled against actual Definitions citations once column 1 is drafted (same check performed retroactively for Infrastructure)
- [x] Easy to replace — no single standard is load-bearing for the whole layer
