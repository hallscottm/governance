# Business Intelligence / Reporting Domain — Conventions

Status: Draft — pending review
Ratified: No
Last updated: 2026-09-22
Provenance: see _qa/05-conventions.qa.md
Built on: 01-definitions.md, 04-metadata-standards.md

Scope: naming conventions for Reports, Dashboards, and Calculated Fields.

---

## Report / Dashboard Naming Convention

**Pattern:** `[<status>] <Domain> - <Subject> (<audience/scope>)`

| Segment | Values | Notes |
|---|---|---|
| `[<status>]` | `[CERTIFIED]` prefix, or omitted for Draft | Makes Certification Status (04-metadata-standards.md) visible in the report's own title, not just its metadata — a deliberate redundancy so a viewer doesn't need to check metadata to know what they're looking at. |
| `<Domain>` | Free text (e.g. `Sales`, `Marketing`, `Finance`) — aligns with the Business Function Department's Data Domain where one exists (cross-cutting/roles-and-departments/01-definitions.md) | Not tied to Report Owner — an owner can build reports across domains. |
| `<Subject>` | Free text | What the report is about. |
| `(<audience/scope>)` | Matches Distribution Scope's values (Internal/Departmental/Org-wide/External) | Optional if Distribution Scope is already obvious from context (e.g., a personal exploratory report). |

**Examples:** `[CERTIFIED] Finance - Monthly Revenue (Org-wide)`,
`Sales - Pipeline Exploration (Internal)`

## Calculated Field Naming Convention

**Pattern:** `<verb/aggregation>_<subject>` (snake_case or the reporting
tool's native casing convention — deliberately not over-specified, since
BI tools vary widely in what casing their formula editors expect).

**Rule:** if a Calculated Field represents the same business concept as
an existing Metric (`data-metric`), its name should match the Metric's
name exactly — a naming mismatch for the same concept is itself a signal
worth a Source-to-Target Mapping entry explaining the relationship
(BIPOL-2, 06-policies.md).

**Example:** `sum_revenue`, `avg_order_value`

## Certification Badge Convention

Certification Status changes are recorded, not just toggled silently —
see BIPROC-1 (08-procedures.md) for the review record this produces. No
separate naming pattern beyond the `[CERTIFIED]` title prefix above.

---

**Open items:**
- `<Domain>` vocabulary is intentionally free-text, same open item
  System Architecture flagged for its own `<domain>` segment — a
  controlled list would need organizational input this framework doesn't
  have.
- Calculated Field casing is deliberately left to the reporting tool's
  own convention rather than a single cross-tool rule — flagged as a
  looser convention than most others in this framework, justified by
  genuine tool variance rather than an oversight.

**Quality bar check (00-framework/quality-bar.md):**
- [x] Simple — two small patterns, one review-record note
- [x] Modular — Report/Dashboard naming and Calculated Field naming stand alone
- [x] Easy to update — add a new `<audience/scope>` value as Distribution Scope's own values change
- [x] Easy to maintain — `[CERTIFIED]` prefix keeps status visible without a metadata lookup
- [x] Easy to replace — no tooling dependency; Calculated Field casing explicitly deferred to the tool in use
