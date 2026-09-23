# Implementation — Naming Conventions

Status: Draft — pilot, not ratified
Ratified: No
Last updated: 2026-09-23

**Why this file exists.** Every governance domain in this repo
(`01-infrastructure/` through `08-harness/`) has its own
`05-conventions.md` — naming is treated as a spec'd, checkable thing
everywhere except here. That gap let `implementation/`'s own folder
names drift out of sync with the front-matter fields they were supposed
to reflect: `skill-pilot-2`'s Task Document has always correctly said
`parent_project: dq-metrics-dashboard`, but its folder sat as a bare
sibling of `skill-pilot-1` (`parent_project: null`), so two folders
with different relationships to a Pilot looked identical in a
directory listing. The fix is this file: naming stops being a
free choice made per-run and starts being **derived mechanically from
fields that already exist**, the same way every other domain's naming
is derived from its own entities rather than assigned by feel.

## The two kinds of thing under `implementation/`, and where each lives

**A Pilot** is an end-to-end test of the framework against one real (or
realistic) request: Vetting Agent → Planning Agent → Project Document →
Task Documents, run for real. There is exactly one root cause for a new
Pilot folder to exist: a new Intake Brief that actually went through
Vetting.

- Location: `implementation/pilots/<project-slug>/`
- `<project-slug>` **is** the Project Document's own identity — not
  assigned separately. If the Project Document has no explicit slug
  field yet, use the `intake-brief.yaml`'s subject, kebab-cased.
- A Pilot folder never gets a sequence number. There is one Pilot per
  distinct real request, and its name says what it's for.

**A Factory Run** is a single test of the Factory Agent producing one
candidate Skill or Agent Template. It always has a Task Document with a
`parent_project` field — that field is not new; it already exists in
every Factory Run Task Document written so far
(`task-factory-run-csv-summary.md`, `task-factory-run-dq-dummy-data.md`,
etc.). The field's value, not a folder-naming decision made separately,
determines everything about where and how it's filed:

- `parent_project: null` → **standalone**: proving the Factory
  mechanism itself, not in service of any Pilot's Task.
- `parent_project: <slug>` → **serves that Pilot**: exists because one
  of that Pilot's own Task Documents (via its `dependencies` field)
  needs this Skill/Agent Template before it can run.

Either way:

- Location: `implementation/factory-runs/<what-it-builds>/`, one flat
  directory for all Factory Runs regardless of standalone vs.
  serves-a-project — the `parent_project` field is what distinguishes
  them, not a different location or a number.
- `<what-it-builds>` is the candidate's own id (the `skill-lib/...` or
  `agent-lib/...` name it registers under, minus the version suffix) —
  never a sequence number. `factory-run-csv-summary` becomes
  `csv-to-markdown-summary`; `factory-run-dq-dummy-data` becomes
  `dq-metrics-dummy-data-generator`. This means the folder name and the
  eventual Library entry name are always the same string with a
  predictable transform, so you can find one from the other without a
  lookup table.
- **Never number Factory Runs** (`skill-pilot-1`, `skill-pilot-2`,
  `factory-run-3`, ...). A sequence number encodes only "which order I
  did these in," which is exactly the information that made two
  differently-related folders look like a matched pair. What actually
  matters (what it builds, what it's for) is already named by the two
  rules above.
- A Pilot whose Task depends on a Factory Run **references it by id**
  in that Task's own `dependencies` field (already how
  `dq-dash-t2-build-report` does it) — the Factory Run is not nested
  inside the Pilot's folder. This keeps a Factory Run reusable: if a
  second, unrelated Pilot later needs the same Skill, it's the same
  folder and the same Library entry, referenced from two places, not
  duplicated.

## Everything else already follows a derivable rule (stated once, here, for completeness)

- **Task Document ids** (`task_id`): already consistently
  `<parent-slug>-t<n>-<short-verb-phrase>` for a Pilot's own Tasks
  (`dq-dash-t1-define-metrics`) and `factory-run-<what-it-builds>` for
  Factory Run Tasks. No change needed — recorded here so it's written
  down rather than only inferred from examples.
- **Agent definition files** (`implementation/agents/*.md`): the
  role's own slug, matching the `agent-lib/` id it compiles from minus
  version suffix (`vetting-agent.md`, `factory-agent.md`). No change
  needed.
- **Skill definition folders** (`implementation/skills/*/`): the exact
  `skill-lib/` id, version suffix included, because a Skill's version
  is part of its identity (`csv-to-markdown-summary-v1/`,
  `dq-metrics-dummy-data-generator-v1/`). No change needed — this one
  was already right, which is why it wasn't the source of the
  confusion.

## What this doesn't cover yet

This file governs `implementation/`'s own scaffolding (pilots, Factory
Runs, agent/skill definitions). It does not replace or duplicate the
domain-level `05-conventions.md` files, which govern the naming of the
actual entities those domains define (a Report's name, a Table's name,
etc.) — those apply to what gets *produced*, this applies to how the
runtime that produces it is organized.
