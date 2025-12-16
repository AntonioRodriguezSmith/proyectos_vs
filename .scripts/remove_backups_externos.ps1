$ErrorActionPreference = 'Stop'
$cwd = (Get-Location).Path
$src = Join-Path $cwd 'backups_externos.zip'
if (Test-Path $src) {
  $dest = Join-Path (Split-Path -Parent $cwd) ('backups_externos_removed_' + (Get-Date -Format 'yyyyMMdd_HHmmss') + '.zip')
  Move-Item -Path $src -Destination $dest -Force
  Write-Host "Moved to: $dest"
  if (Get-Command git -ErrorAction SilentlyContinue) {
    git rm --cached --ignore-unmatch 'backups_externos.zip'
    git add -A
    git diff --cached --quiet
    if ($LASTEXITCODE -ne 0) { git commit -m 'chore: remove backups_externos.zip from repo' }
    git push origin main
  } else {
    Write-Host 'Git not available; aborting git operations'
  }
} else {
  Write-Host 'No backups_externos.zip found'
}
