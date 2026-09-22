# Q&A Log — Metadata Standards (System Architecture)
# Append-only. Do not edit past entries; add new dated entries instead.

## 2026-09-22 — Q4.1: Field registry shape and content

**Context:** Same shape already established (shared field registry +
entity-type applicability matrix) and reused without re-asking, per the
pattern Networking followed from Infrastructure.

**Bucket:** [Standard]/AI-draftable, with two fields flagged as
forward/org references rather than fully resolved.

**Drafted:** 3 referenced fields (Resource ID, Cost Center Tag,
Environment) from Infrastructure; 9 new fields owned by this layer
(Service Name, Owning Team, Semantic Version, API Contract Reference,
Database Engine, Repository Reference, Service Tier/Criticality, Health
Check Endpoint, Dependency List); 4 entity types (Service, Application,
API, Database).

**Flagged, not resolved here:**
- Owning Team has no owning Definitions term (organizational, not
  system-architecture) — same boundary hit at Infrastructure/Networking.
- Repository Reference forward-references Workflow/Process (layer 5),
  not yet built.
- Data Classification explicitly excluded — owned by Data/Metadata
  (layer 4), not yet built.

**Status:** Pending explicit review.
