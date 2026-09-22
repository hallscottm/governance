# Ontology Relation Types

Status: Draft
Ratified: No
Last updated: 2026-09-22

The standard vocabulary of relationships used in every layer's Ontology
column (03-ontologies.md). Kept deliberately small — 9 types — to match
the quality bar (simple, modular). Taxonomy (column 2) already handles
hierarchical classification ("what category is this in"); Ontology
relations describe how classified terms interact, not where they sit in
the tree, so no "is-a" type is needed here.

| Relation | Meaning | Example |
|---|---|---|
| **runs-on** | A executes/operates on top of B | Virtual Machine runs-on Hypervisor |
| **contains** | A is composed of B (B is part of A) | CPU contains Core |
| **located-in** | A is physically or logically placed within B | Rack located-in Data Center |
| **requires** | A cannot function/exist without B | Autoscaling requires Horizontal Scaling |
| **constrains** | A limits or governs the behavior/scope of B | Availability Tier constrains Redundancy |
| **measured-by** | A's quality/performance is quantified by metric B | Block Storage measured-by IOPS |
| **consumes / produces** | A uses up B (consumes) or generates B (produces) | Training Workload consumes GPU Memory |
| **scales-via** | A's capacity changes through mechanism B | Compute Unit scales-via Horizontal Scaling |
| **has-lifecycle-state** | A can be in state B at a point in time | Compute Unit has-lifecycle-state Decommissioning |

## Format for relationship entries

```
Term A --[relation]--> Term B
Rationale: one short line
```

Relationships reference terms by their anchor ID (e.g., `infra-cpu`), not
display text, so they stay valid if a term's wording changes later.

## Scope note

Not every term needs to appear in a relationship. Ontology captures
*meaningful* connections, not an exhaustive graph — a term with no
natural relationship to others in its layer is left unconnected rather
than forced into an artificial one.
