# Q&A Log — Conventions (System Architecture)
# Append-only. Do not edit past entries; add new dated entries instead.

## 2026-09-22 — Q5.1: Should Service/Application names include environment?

**Context:** Infrastructure and Networking both embed `<env>` in the
resource name. Whether that pattern extends to this layer is a real
design decision, not mechanical — a service is conventionally a stable
identity across environments, unlike a VPC or compute instance which is a
distinct resource per environment.

**Bucket:** [Org-decision]/Human-only.

**Options presented:** (a) stable name, environment tracked only via the
Environment metadata field [Recommended]; (b) env-in-name, consistent
with Infrastructure/Networking.

**Answer:** (a) Stable name, env as metadata only.

**Resulting convention:** `<domain>-<function>[-<type>]` for
Services/Applications, no `<env>` segment; Environment is recorded via
04-metadata-standards.md's Environment field instead.

## 2026-09-22 — Q5.2: Database naming and API versioning conventions

**Bucket:** [Standard]/AI-draftable.

**Drafted:** Database naming uses snake_case (`<service_name>_<purpose>`)
as an explicit, engine-driven exception to the kebab-case convention used
elsewhere. API versioning ties the major version segment to Semantic
Version's MAJOR component.

**Status:** Pending explicit review.
