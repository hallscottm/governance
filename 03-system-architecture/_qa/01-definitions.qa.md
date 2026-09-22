# Q&A Log — Definitions (System Architecture)
# Append-only. Do not edit past entries; add new dated entries instead.

## 2026-09-22 — Q1.1: Full-sweep coverage of System Architecture vocabulary

**Context:** Applying the lesson learned from Infrastructure's first pass
(too thin — 11 terms — corrected to a full 10-subdomain, 58-term sweep)
and carried forward proactively into Networking (47 terms, full sweep from
the start). Did the same here: full sweep from the start, no thin-first-
pass.

**Bucket:** [Standard]/AI-draftable — bulk-drafted vocabulary, not an
org-specific decision.

**Drafted:** 64 owned terms across 10 subdomains — Architectural Patterns
& Styles, Application Building Blocks, Interfaces & APIs, Databases &
Storage, Integration & Messaging, State & Caching, Versioning & Release
Management, Application Security, Quality Attributes (ISO/IEC 25010),
Testing & Quality Gates — plus 5 referenced (not owned) terms: Container
and Environment (lifecycle) from Infrastructure; TLS, Encryption in
Transit, and Load Balancer from Networking. Reverse "Referenced by:" tags
added to all 5 source definitions.

**Design note:** Two same-word-different-owner cases handled per
00-framework/term-linking-convention.md, both flagged explicitly in the
file: "API Schema" (this layer) vs. "Database Schema" (this layer, same
layer but distinct entities — disambiguated by full term name, not by
layer prefix, since both belong to System Architecture); and
Infrastructure's "Container" (runtime isolation unit) vs. this layer's new
"Container Image" (the deployable build artifact) — related but distinct
concepts, not a collision, cross-referenced explicitly in the Container
Image entry.

**Status:** Pending explicit review.
