# Run this from the repo root: .\commit-session.ps1

# 1. Clear the stale lock (safe if no other git process is actually running)
if (Test-Path ".git\index.lock") {
    Write-Host "Removing stale .git\index.lock..."
    Remove-Item -Force ".git\index.lock"
}

# 2. Show context before committing
Write-Host "`n--- Last commit ---"
git --no-pager log -1
Write-Host "`n--- Diff stat (last 20 lines) ---"
git diff --stat HEAD | Select-Object -Last 20
Write-Host "`n--- Status ---"
git status --short

Read-Host "`nReview the above. Press Enter to stage and commit, or Ctrl+C to abort"

# 3. Stage everything
git add -A

# 4. Write commit message to a temp file (avoids PowerShell quoting issues)
@'
Fill Data Platform's remaining 8 columns (Standards Alignment through Tooling)

Standards Alignment: ANSI/ISO SQL, ISO/IEC 27040, NIST SP 800-53/800-88,
CIS Benchmarks, and the Iceberg/Delta Lake/Hudi and Kafka open-source
specs (flagged distinct in authority from formal standards bodies).

Metadata Standards: field registry + entity-type matrix for Database,
Warehouse/Lakehouse, Data Lake, Vector Database, Stream/Topic, and Data
Pipeline entities.

Conventions: Database naming convention migrated verbatim from System
Architecture (5-conventions.md), alongside new warehouse/lakehouse layer,
streaming topic, table, and embedding-model-reference naming patterns.

Policies/Access Rules/Procedures: migrated System Architecture's schema
migration review governance (SAPOL-2/SAAR-1/SAPROC-2) to this domain as
DPPOL-1/DPPAR-1/DPPROC-1, updating approving roles from Owning Team Lead
to Data Architect/Data Engineer. Added new policies for streaming
retention, vector embedding model versioning, lakehouse table format
changes, and -- most notably -- DPPOL-5, requiring Certified Metrics to
route through the Semantic Layer rather than being recomputed ad hoc by
a downstream report. DPPAR-3 is this framework's first Access Rule to
route a change through a Business Function Department's Data Owner.

Risk Tiers: Environment, Sensitivity Level/PII (from Data/Metadata),
Service Tier/Criticality (from System Architecture), and Public exposure
factors.

Tooling: 7 capability categories, including a Data Catalog / Metadata
Management Platform category connecting to the OpenMetadata-class
tooling discussed for BI/Reporting's lineage and certification needs.

System Architecture's Conventions/Policies/Access Rules/Procedures/Risk
Tiers/Tooling columns updated with reference stubs and reconciled
cross-references wherever schema-migration content moved out.

All 11 columns of Data Platform (domain 4) are now drafted.
'@ | Out-File -Encoding utf8 ".git\COMMIT_MSG.tmp"

git commit -F ".git\COMMIT_MSG.tmp"
Remove-Item ".git\COMMIT_MSG.tmp"

# 5. Confirm
Write-Host "`n--- New commit ---"
git --no-pager log -1
Write-Host "`n--- Status after commit ---"
git status --short

Write-Host "`nDone. Run 'git push' separately to push to GitHub."
