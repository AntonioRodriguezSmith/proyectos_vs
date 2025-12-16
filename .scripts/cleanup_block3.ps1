$ErrorActionPreference = 'Stop'
$ts = Get-Date -Format 'yyyyMMdd_HHmmss'
$parent = Split-Path -Parent (Get-Location)
$dest = Join-Path $parent ("backups_externos_$ts")
Write-Host "Destino: $dest"
if (-Not (Test-Path $dest)) { New-Item -ItemType Directory -Path $dest | Out-Null }
if (Test-Path .\backups_remote) {
    Write-Host 'Moviendo backups_remote...'
    Move-Item -Path .\backups_remote -Destination $dest -Force
    $zip = Join-Path $parent ("backups_externos_${ts}.zip")
    if (Test-Path $zip) { Remove-Item $zip -Force }
    Add-Type -AssemblyName System.IO.Compression.FileSystem
    [System.IO.Compression.ZipFile]::CreateFromDirectory($dest, $zip)
    Write-Host 'ZIP creado en:' $zip
    git rm -r --cached --ignore-unmatch 'backups_remote' 2>$null
} else {
    Write-Host 'No se encontró backups_remote'
}
