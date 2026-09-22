#!/usr/bin/env bash
set -euo pipefail

ROOT="$(pwd)"

LAYERS=(
  "01-infrastructure"
  "02-networking"
  "03-system-architecture"
  "04-data-metadata"
  "05-workflow-process"
  "06-harness"
  "07-interface-human"
)

COLUMNS=(
  "00-standards-alignment|Standards Alignment"
  "01-definitions|Definitions"
  "02-taxonomies|Taxonomies"
  "03-ontologies|Ontologies"
  "04-metadata-standards|Metadata Standards"
  "05-conventions|Conventions"
  "06-policies|Policies"
  "07-access-rules|Access Rules"
  "08-procedures|Procedures"
  "09-risk-tiers|Risk Tiers"
  "10-tooling|Tooling / Implementation"
)

echo "Scaffolding AI Governance Framework in: $ROOT"
echo

write_if_missing() {
  local path="$1"
  local content="$2"
  if [ -f "$path" ]; then
    echo "  skip (exists): $path"
  else
    mkdir -p "$(dirname "$path")"
    printf '%s\n' "$content" > "$path"
    echo "  created: $path"
  fi
}

echo "== 00-framework/ =="

write_if_missing "$ROOT/00-framework/layer-axis-definition.md" "# Layer Axis Definition

Status: Draft
Ratified: No
Last updated: $(date +%Y-%m-%d)

The row axis of the framework matrix. Layers are filled bottom-to-top
(row-major), since each layer's definitions depend on the layer(s) below it.

| # | Layer | Concern |
|---|---|---|
| 1 | Infrastructure | Physical/virtual compute, storage, hardware substrate |
| 2 | Networking | Connectivity, segmentation, routing, network boundaries |
| 3 | System Architecture | Databases, applications, services built on the substrate |
| 4 | Data/Metadata | What the data means — taxonomy, ontology, catalog |
| 5 | Workflow/Process | Git, CI/CD, SOPs, directory conventions |
| 6 | Harness | Role/department-specific AI scaffolding |
| 7 | Interface/Human | Training, change management, human engagement |

Cross-cutting (not rows, expressed through the Policies / Access Rules /
Risk Tiers columns at every layer): Governance, Security.

Activates partway (not from layer 1): Sandbox — becomes relevant starting
at the Workflow/Process layer, once there is something real to test against."

write_if_missing "$ROOT/00-framework/artifact-axis-definition.md" "# Artifact Axis Definition

Status: Draft
Ratified: No
Last updated: $(date +%Y-%m-%d)

The column axis of the framework matrix. Columns are filled left-to-right
within a layer, since each artifact type depends on the one(s) before it.

| Order | Artifact Type | Captures | Depends on |
|---|---|---|---|
| 1 | Definitions | Core vocabulary/glossary | nothing (foundation) |
| 2 | Taxonomies | Classification/hierarchy of defined terms | Definitions |
| 3 | Ontologies | Relationships/rules between classified entities | Taxonomies |
| 4 | Metadata Standards | How real instances get tagged/described | Ontologies |
| 5 | Conventions | Naming, structure, scaffolding, formatting | Definitions + Taxonomy |
| 6 | Policies | Rules — required/allowed/forbidden | Definitions + Ontology |
| 7 | Access Rules | Who/what can see or act | Policies |
| 8 | Procedures (SOPs) | Step-by-step execution of a policy | Policies |
| 9 | Risk Tiers | Risk classification, regulatory mapping | Policies + Taxonomy |
| 10 | Tooling / Implementation | Tools/apps chosen to implement the above | all prior columns (filled last) |

A Standards Alignment reference panel (established external standards
relevant to the layer) is reviewed before column 1 and is not itself
'data' to fill in — it seeds columns 1-2 with existing vocabulary."

write_if_missing "$ROOT/00-framework/quality-bar.md" "# Quality Bar — checked before any cell is marked Ratified

Status: Draft
Ratified: No
Last updated: $(date +%Y-%m-%d)

Every definition, taxonomy, policy, and tooling choice in this framework
must be checked against these before ratification:

- [ ] Simple — no unnecessary complexity for the problem it solves
- [ ] Modular — can be updated or replaced without breaking unrelated cells
- [ ] Easy to update — a future change doesn't require re-deriving context
- [ ] Easy to maintain — ownership and review cadence are clear
- [ ] Easy to replace — not locked to a single vendor/tool without reason"

write_if_missing "$ROOT/00-framework/traversal-order.md" "# Traversal Order

Status: Draft
Ratified: No
Last updated: $(date +%Y-%m-%d)

## Row-major, with a reconciliation safeguard

Fill order: complete all columns for Layer 1 (Infrastructure) before
starting Layer 2 (Networking), and so on, bottom-to-top per the layer
axis definition.

After each layer's Definitions column (column 1) is completed, run a
terminology reconciliation pass: compare the new layer's Definitions
against all previously completed layers' Definitions, flag collisions
or near-duplicate terms.

## Q&A provenance rule

Each cell's '_qa/<column>.qa.md' record is append-only: once a question
is answered, that record is not edited in place. A later change in
understanding is logged as a new, dated entry rather than overwriting
the original — the output document (e.g. '01-definitions.md') is what
gets updated/versioned normally; the Q&A file is the historical record
of how it got there.

## Open items (future phases, not yet designed)

- State/history management for ratified content that changes later
  (correction vs. evolution, versioning scheme, dependent-layer
  re-validation flags)
- Migration path from file-based source of truth to a queryable
  structured store (e.g. for harness runtime consumption)"

write_if_missing "$ROOT/00-framework/glossary-master.md" "# Unified Glossary (GENERATED)

Status: Not yet generated
Last updated: —

This file is derived from every layer's 01-definitions.md. Do not edit
directly — regenerate from source layer files once a generation script
exists."

for layer in "${LAYERS[@]}"; do
  echo
  echo "== $layer/ =="

  for col in "${COLUMNS[@]}"; do
    fname="${col%%|*}"
    title="${col##*|}"
    write_if_missing "$ROOT/$layer/$fname.md" "# ${title}

Status: Not started
Ratified: No
Last updated: —

(Content pending — see corresponding file in _qa/ once work begins.)"

    write_if_missing "$ROOT/$layer/_qa/$fname.qa.md" "# Q&A Log — ${title}
# Append-only. Do not edit past entries; add new dated entries instead.

(No questions answered yet.)"
  done

  write_if_missing "$ROOT/$layer/_status.yaml" "# Machine-readable status roll-up for this layer.
# Values: not-started | draft | ratified | deprecated | superseded
layer: \"$layer\"
columns:
  00-standards-alignment: not-started
  01-definitions: not-started
  02-taxonomies: not-started
  03-ontologies: not-started
  04-metadata-standards: not-started
  05-conventions: not-started
  06-policies: not-started
  07-access-rules: not-started
  08-procedures: not-started
  09-risk-tiers: not-started
  10-tooling: not-started"
done

echo
echo "== cross-cutting/ =="

write_if_missing "$ROOT/cross-cutting/governance-and-security-index.md" "# Governance & Security Index (GENERATED)

Status: Not yet generated
Last updated: —

This file is derived from every layer's 06-policies.md, 07-access-rules.md,
and 09-risk-tiers.md files. Governance and Security are not rows in this
framework — they are cross-cutting concerns expressed through those columns
at every layer. Do not edit this file directly."

write_if_missing "$ROOT/cross-cutting/sandbox-activation.md" "# Sandbox Activation

Status: Draft
Ratified: No
Last updated: $(date +%Y-%m-%d)

Sandbox is not a layer — it is a constrained, safe-to-experiment copy of
the stack. It is not needed to begin this project (there is no
institutional knowledge yet to protect), and becomes relevant starting at
the Workflow/Process layer, once there is something real (pipelines,
harness behavior) to test against production-adjacent systems.

Definition, scope, and provisioning details: TBD when Layer 5
(Workflow/Process) work begins."

echo
echo "== roadmap/ =="

write_if_missing "$ROOT/roadmap/roadmap.md" "# Roadmap (GENERATED)

Status: Not yet generated
Last updated: —

Derived from every layer's _status.yaml, in traversal order (see
00-framework/traversal-order.md). Shows sequencing, ownership, and
maturity across the whole framework. Do not edit directly."

write_if_missing "$ROOT/roadmap/buy-in-narrative.md" "# Buy-In Narrative

Status: Not started
Last updated: —

Leadership-facing version of the roadmap: same phase structure as
roadmap.md, reframed around risk reduction and pace-of-adoption rather
than definitional detail."

echo
echo "Done. Review with: git status"
