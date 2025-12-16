$ErrorActionPreference = 'Continue'
$dirs = '__pycache__','.pytest_cache','.venv','venv','env','.ipynb_checkpoints','.vscode','.idea'
$cwd = (Get-Location).Path
foreach ($d in $dirs) {
    $found = Get-ChildItem -Path . -Recurse -Directory -Force -ErrorAction SilentlyContinue | Where-Object { $_.Name -ieq $d }
    foreach ($item in $found) {
        $rel = $item.FullName.Substring($cwd.Length+1)
        Write-Host 'Untracking and removing:' $rel
        git rm -r --cached --ignore-unmatch "$rel" 2>$null
        Remove-Item -Recurse -Force $item.FullName -ErrorAction SilentlyContinue
    }
}
# remove .pyc files
$pyc = Get-ChildItem -Path . -Recurse -Include '*.pyc' -File -ErrorAction SilentlyContinue
foreach ($f in $pyc) {
    $rel = $f.FullName.Substring($cwd.Length+1)
    Write-Host 'Removing pyc:' $rel
    git rm --cached --ignore-unmatch "$rel" 2>$null
    Remove-Item -Force $f.FullName -ErrorAction SilentlyContinue
}
# also try to remove __pycache__ empty remnants
Get-ChildItem -Path . -Recurse -Directory -Force | Where-Object { $_.Name -ieq '__pycache__' } | ForEach-Object { if ((Get-ChildItem $_.FullName -Recurse -Force -ErrorAction SilentlyContinue).Count -eq 0) { Remove-Item -Recurse -Force $_.FullName -ErrorAction SilentlyContinue } }
Write-Host 'Block4 done'