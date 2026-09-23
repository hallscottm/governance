# Run this from the repo root: .\commit-session.ps1

# 1. Clear the stale lock (safe if no other git process is actually running)
if (Test-Path ".git\index.lock") {
    Write-Host "Removing stale .git\index.lock..."
    Remove-Item ".git\index.lock" -Force
}

# 2. Show what changed since your last commit, before staging anything
Write-Host "=== Last commit ==="
git log -1 --format="%H  %ci  %s"
Write-Host " "
Write-Host "=== Files changed since then (summary) ==="
git diff --stat HEAD | Select-Object -Last 20
Write-Host " "
Write-Host "=== Full file list ==="
git status --short

# 3. Pause for a sanity check before staging/committing
Read-Host "Review the above. Press Enter to stage + commit everything, or Ctrl+C to abort"

# 4. Stage everything
git add -A

# 5. Write the commit message to a temp file, then commit from it
$commitMsg = @'
Add Roles & Departments pillar; restructure axis to Domains; add Data Platform and Business Intelligence/Reporting domains

- Establish Roles and Departments as a third cross-cutting pillar (roles,
  departments, org chart) alongside Governance and Security; retrofit all
  4 completed domains' Access Rules to reference it instead of carrying
  provisional role vocabulary.
- Rename the axis concept "Layer" to "Domain" throughout; add
  00-framework/ea-framework-alignment.md mapping the axis to TOGAF's BDAT
  and the Zachman Framework.
- Insert new Data Platform domain (Database/Table/Transaction/etc.
  migrated out of System Architecture; new Data Lake/Lakehouse/Warehouse/
  Vector DB/Streaming content); insert new Business Intelligence /
  Reporting domain (Report Data Model, Calculated Field, Source-to-Target
  Mapping extending Data/Metadata's lineage concept). Domains renumbered
  1-9 accordingly, all cross-references and directory paths updated.
- Add Data Architect, Data Engineer, and Analytics Engineer roles
  co-owning Data Platform; add Business Intelligence and Analytics
  department (Business Analyst/Report Builder, BI Analyst/Developer)
  owning the new BI/Reporting domain.
- Add data-metric (Data/Metadata) and dp-semantic-layer (Data Platform)
  terms bridging official definitions into the new BI domain.

DevOps/Workflow-Process ownership remains unresolved (flagged
"under revision" throughout); Workflow/Process domain itself and most of
Data Platform/BI-Reporting's later columns (Policies, Access Rules,
Procedures, Risk Tiers, Tooling) are not yet drafted.
'@

$commitMsg | Out-File -FilePath ".git\COMMIT_MSG.tmp" -Encoding utf8

git commit -F ".git\COMMIT_MSG.tmp"

Remove-Item ".git\COMMIT_MSG.tmp"

# 6. Confirm
Write-Host " "
Write-Host "=== Done ==="
git log -1 --format="%H  %ci  %s"
git status --short
