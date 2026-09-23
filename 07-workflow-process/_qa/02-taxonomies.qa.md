# Q&A Log — Taxonomies
# Append-only. Do not edit past entries; add new dated entries instead.

## 2026-09-22 — Q7.3: Classification tree

**Bucket:** [Standard]/AI-draftable — mirrors 01-definitions.md's
subdomain structure exactly, same pattern every prior domain's Taxonomy
column used.

**Answer:** Single-parent tree, six subdomains matching Definitions.
Deployment Gate kept as a taxonomy sibling to Pipeline Stage rather than
nested under it, even though a Deployment Gate is conceptually a
specialized kind of stage — consistent with this framework's established
practice of not modeling "is-a" specialization in the Taxonomy tree
(Taxonomy classifies by subdomain grouping; a genuine is-a relationship,
where one existed, would use the `extends` mechanism at the Definitions
level instead, as Business Intelligence / Reporting's Source-to-Target
Mapping does).

**Status:** Pending explicit review.
