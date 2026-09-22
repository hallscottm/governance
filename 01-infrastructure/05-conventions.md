# Infrastructure Layer — Conventions

Status: Draft — pending review
Ratified: No
Last updated: 2026-09-22
Provenance: see _qa/05-conventions.qa.md
Built on: 01-definitions.md, 04-metadata-standards.md

Scope: naming, tagging, and formatting conventions for infrastructure
*resources themselves* (compute instances, storage volumes, physical
assets). Code/repository layout conventions (Infrastructure-as-Code repo
structure, module organization) belong to the Workflow/Process layer
(05-workflow-process/05-conventions.md, not yet drafted) — kept separate
so this file isn't duplicated or contradicted once that layer exists.

---

## Resource Naming Convention

**Pattern:** `<env>-<compute-env>-<service>-<seq>`

| Segment | Values | Source |
|---|---|---|
| `<env>` | `dev`, `stg`, `prod` (abbreviations of `infra-environment-lifecycle`) | This layer, Definitions |
| `<compute-env>` | `onprem`, `colo`, `pubcloud`, `privcloud`, `hybrid`, `edge` (abbreviations of `infra-compute-environment`) | This layer, Definitions |
| `<service>` | Short, lowercase, hyphenated identifier for the function the resource serves (org-specific vocabulary, not standardized here) | Org-specific |
| `<seq>` | Zero-padded sequence number, 3 digits minimum (`001`, `002`, ...) | Convention |

**Example:** `prod-pubcloud-dataeng-001`

**Rules:**
- All lowercase, hyphen-separated, no underscores or spaces
- Total length should respect the shortest length limit among target
  platforms (e.g., some cloud resource name fields cap at 63 characters)
- `<seq>` resets per unique `<env>-<compute-env>-<service>` combination,
  not globally

## Tag Key Naming Convention

- Tag keys are kebab-case, matching the Metadata Standards field registry
  (04-metadata-standards.md), lowercased: e.g. `cost-center-tag`,
  `availability-tier`, `resource-id`
- Tag *values* follow whatever format that field's Definitions entry
  implies (e.g., `availability-tier` value is one of `tier-i`..`tier-iv`)
- No free-text tag keys outside the registry — a new tag key requires
  adding a new field to the Metadata Standards registry first (keeps tags
  and the field registry from drifting apart)

## Required Tag Set (by entity type)

Not redefined here — see 04-metadata-standards.md's Entity Types & Field
Applicability matrix. This convention only fixes *how* those required
fields are expressed as actual tag keys (kebab-case, per above), not
*which* fields are required (that's Metadata Standards' job).

## Abbreviation Registry

Referenced by: Networking (02-networking/05-conventions.md reuses `<env>`
and `<compute-env>` segments from this registry rather than duplicating
them). Same anchor-granularity gap noted in Infrastructure's Metadata
Standards applies here — no per-row anchors yet, so this is a section-level
reference note rather than a per-term reverse pointer.

| Full Term | Abbreviation | Anchor |
|---|---|---|
| Development | `dev` | `infra-environment-lifecycle` |
| Staging/QA | `stg` | `infra-environment-lifecycle` |
| Production | `prod` | `infra-environment-lifecycle` |
| On-Premises | `onprem` | `infra-compute-environment` |
| Colocation | `colo` | `infra-compute-environment` |
| Public Cloud | `pubcloud` | `infra-compute-environment` |
| Private Cloud | `privcloud` | `infra-compute-environment` |
| Hybrid | `hybrid` | `infra-compute-environment` |
| Edge | `edge` | `infra-compute-environment` |

This registry is the single source of truth for abbreviations used in
resource names — any other document referencing these abbreviations
should link here rather than redefining them (DRY, per
00-framework/term-linking-convention.md).

---

**Open items:**
- `<service>` vocabulary is explicitly left org-specific/undefined here —
  it depends on what services/teams actually exist, which this
  generalized template can't presume. An org adopting this framework
  fills in their own service vocabulary when they apply it.
- Naming convention for the AI-Specific Compute entity type (Model-Serving
  Node, Training Workload instances) not yet distinguished from general
  Compute Unit naming — revisit if a real need for a distinct pattern
  emerges (e.g., encoding model name/version in the resource name).

**Quality bar check (00-framework/quality-bar.md):**
- [x] Simple — one pattern, one abbreviation table, no competing schemes
- [x] Modular — abbreviation registry can be extended without changing the naming pattern itself
- [x] Easy to update — add an abbreviation as a new table row
- [x] Easy to maintain — tag keys locked to the Metadata Standards registry, can't drift independently
- [x] Easy to replace — pattern is a convention, not hard-coded into any tooling yet (tooling choice deferred to column 10)
