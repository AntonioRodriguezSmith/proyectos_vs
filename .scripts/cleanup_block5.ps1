$ErrorActionPreference = 'Stop'
$ErrorActionPreference = 'Stop'
$patterns = @('backups_remote/','backups_externos_*.zip','__pycache__/','*.pyc','.pytest_cache/','.venv/','venv/','env/','.ipynb_checkpoints/','.DS_Store','.vscode/','.idea/')
if (-not (Test-Path .gitignore)) { "" | Out-File .gitignore -Encoding utf8 }
foreach ($p in $patterns) {
    $escaped = [regex]::Escape($p)
    if (-not (Select-String -Path .gitignore -Pattern $escaped -Quiet -ErrorAction SilentlyContinue)) {
        Add-Content .gitignore $p
        Write-Host 'Added to .gitignore:' $p
    }
}
# stage and commit
git add .gitignore
git add -A
# commit only if there are staged changes
git diff --cached --quiet
if ($LASTEXITCODE -ne 0) {
    git commit -m 'chore: remove generated files not in conflict and update .gitignore'
    Write-Host 'Committed cleanup.'
} else {
    Write-Host 'No staged changes to commit.'
}
# push main (try normal push, fallback to force-with-lease)
git push origin HEAD:main 2>$null
if ($LASTEXITCODE -ne 0) { git push origin HEAD:main --force-with-lease }
# create/update cleaned branch from main and push
git rev-parse --verify cleaned 2>$null
if ($LASTEXITCODE -ne 0) { git branch cleaned }
git branch -f cleaned
git push -u origin cleaned --force-with-lease
Write-Host 'Block5 done'