# Run this from the repo root: .\commit-session.ps1

if (Test-Path ".git\index.lock") {
    Write-Host "Removing stale .git\index.lock..."
    Remove-Item -Force ".git\index.lock"
}

Write-Host "`n--- Last commit ---"
git --no-pager log -1
Write-Host "`n--- Diff stat (last 20 lines) ---"
git diff --stat HEAD | Select-Object -Last 20
Write-Host "`n--- Status ---"
git status --short

Read-Host "`nReview the above. Press Enter to stage and commit, or Ctrl+C to abort"

git add -A

@'
Fill Business Intelligence / Reporting's remaining 8 columns (Standards Alignment through Tooling)

Standards Alignment: WCAG 2.1/2.2 (first accessibility citation in this
framework -- the first domain whose artifacts a broad human audience
consumes directly), XMLA, ISO 8000, NIST SP 800-53 AC family, plus the
dbt Semantic Layer/MetricFlow spec and TDWI BI governance practice
flagged as community-originated, not formal standards bodies.

Metadata Standards: field registry for Report, Dashboard, and Report
Data Model entities, including Certification Status and Source-to-Target
Mapping Reference fields that directly operationalize the Draft/Certified
lifecycle from 01-definitions.md.

Conventions: Report/Dashboard naming with a [CERTIFIED] title prefix,
Calculated Field naming tied to matching Metric names where one exists.

Policies: BIPOL-1 is the policy this domain was created to write --
Certified status is required before a Report/Dashboard can reach
Organization-wide or External distribution. BIPOL-2 makes the ontology's
Source-to-Target Mapping requirement enforceable. BIPOL-3 scales Row-
Level Security by inherited sensitivity, mirroring System Architecture's
SAPOL-5 escalation pattern. BIPOL-4 requires a refresh schedule on any
Data Extract.

Access Rules: BIAR-1 (certification authority, BI Analyst/Developer only,
no self-certification) and BIAR-2 (Row-Level Security configuration
authority, scaled by sensitivity).

Procedures: BIPROC-1/2/3 execute the above, with BIPROC-2 nested inside
BIPROC-1's certification review flow.

Risk Tiers: introduces Distribution Scope as a first-class Risk Tier
factor -- a deliberate, flagged departure from this framework's usual
pattern of treating "who can see this" as purely an Access Rules concern,
justified because audience reach is this domain's defining risk.

Tooling: 5 capability categories, including Accessibility Testing (new)
and a Data Catalog / Metadata Management Platform explicitly shared with
Data Platform's and Data/Metadata's own Tooling columns rather than
independently selected -- resolves the reconciliation flagged as an open
item in Data Platform's Tooling column (updated to record the resolution).

All 11 columns of Business Intelligence / Reporting (domain 6) are now
drafted.
'@ | Out-File -Encoding utf8 ".git\COMMIT_MSG.tmp"

git commit -F ".git\COMMIT_MSG.tmp"
Remove-Item ".git\COMMIT_MSG.tmp"

Write-Host "`n--- New commit ---"
git --no-pager log -1
Write-Host "`n--- Status after commit ---"
git status --short

Write-Host "`nDone. Run 'git push' separately to push to GitHub."
