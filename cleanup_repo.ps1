# cleanup_repo.ps1
# Ejecutar desde la raíz del repo: C:\Users\arodriguezsm\proyectos_vs
if (-not $PSScriptRoot) { $PSScriptRoot = (Get-Location).Path }
Set-Location $PSScriptRoot

$ErrorActionPreference = 'Stop'
Write-Host "Iniciando limpieza segura del repositorio..." -ForegroundColor Cyan

# 1) Crear carpeta de backups_externos
$backupDir = Join-Path $PSScriptRoot "backups_externos"
if (-not (Test-Path $backupDir)) {
  New-Item -ItemType Directory -Path $backupDir | Out-Null
  Write-Host "Creada carpeta:" $backupDir
} else {
  Write-Host "Carpeta de backup ya existe:" $backupDir
}

# 2) Mover items seguros (si existen)
$moveItems = @(
  "modeloRagAlejandria\asistente_jarvis\jarvis.db",
  "validacion-icaria\archivo_obsoletos",
  "backups",
  "output_analisis"
)

foreach ($srcRel in $moveItems) {
  $srcPath = Join-Path $PSScriptRoot $srcRel
  if (Test-Path $srcPath) {
    $destPath = Join-Path $backupDir (Split-Path $srcRel -Leaf)
    if (-not (Test-Path (Split-Path $destPath -Parent))) { New-Item -ItemType Directory -Path (Split-Path $destPath -Parent) -Force | Out-Null }
    Move-Item -Path $srcPath -Destination $destPath -Force
    Write-Host "Movido: $srcRel -> $(Split-Path $destPath -Leaf)"
  } else {
    Write-Host "No existe: $srcRel" -ForegroundColor DarkGray
  }
}

# 2b) Opcional: comprimir backups_externos
$zipPath = Join-Path $PSScriptRoot "backups_externos.zip"
if (-not (Test-Path $zipPath)) {
  try {
    Compress-Archive -Path (Join-Path $backupDir "*") -DestinationPath $zipPath -Force
    if (Test-Path $zipPath) { Write-Host "Creado ZIP: $zipPath" }
  } catch {
    Write-Host "Advertencia: no se pudo crear ZIP (posible tamaños grandes o permisos)." -ForegroundColor Yellow
  }
} else {
  Write-Host "ZIP de backup ya existe: $zipPath" -ForegroundColor DarkGray
}

# 3) Añadir bloque a .gitignore si no existe
$gitignore = Join-Path $PSScriptRoot ".gitignore"
$marker = "# Añadidos por limpieza de monorepo"
$block = @"
$marker
.venv/
venv/
env/
__pycache__/
*.py[cod]
*.pyo
*.pyd
*.db
*.sqlite3
backups/
backups_externos/
output_analisis/
.env
.env.*
.vscode/
*.log
*.tmp
*.bak
*.swp
.DS_Store
Thumbs.db
*.ipynb_checkpoints/
"@

if (-not (Test-Path $gitignore)) {
  New-Item -Path $gitignore -ItemType File | Out-Null
  Add-Content -Path $gitignore -Value $block
  Write-Host ".gitignore creado y bloque recomendado añadido."
} else {
  $exists = Select-String -Path $gitignore -Pattern ([regex]::Escape($marker)) -Quiet
  if (-not $exists) {
    Add-Content -Path $gitignore -Value "`n$block"
    Write-Host "Bloque recomendado añadido a .gitignore."
  } else {
    Write-Host "El bloque recomendado ya está presente en .gitignore." -ForegroundColor DarkGray
  }
}

# 4) Inicializar git y commits (si .git no existe)
if (-not (Test-Path (Join-Path $PSScriptRoot ".git"))) {
  if (Get-Command git -ErrorAction SilentlyContinue) {
    git init
    git branch -M main
    git add .gitignore
    git commit -m "Update .gitignore" --no-verify
    Write-Host "Repositorio inicializado y .gitignore commiteado."
  } else {
    Write-Host "Git no está disponible en PATH; omitiendo inicialización." -ForegroundColor Yellow
  }
} else {
  Write-Host "Ya existe carpeta .git - omitiendo git init." -ForegroundColor DarkGray
}

# 4b) Añadir todo y commit limpio
if (Get-Command git -ErrorAction SilentlyContinue) {
  git add .
  git commit -m "Initial clean commit" -q --allow-empty
  Write-Host "Commit inicial realizado."
} else {
  Write-Host "Git no disponible: no se realizó commit inicial." -ForegroundColor Yellow
}

# 4c) Quitar del índice artefactos regenerables si necesitases (no borra archivos locales)
$toUntrack = @("__pycache__", ".venv", ".vscode", "backups", "output_analisis")
if (Get-Command git -ErrorAction SilentlyContinue) {
  foreach ($p in $toUntrack) {
    if (Test-Path (Join-Path $PSScriptRoot $p)) {
      git rm -r --cached $p -q 2>$null
    }
  }
  git commit -m "Remove generated artifacts from index" -q --allow-empty
} else {
  Write-Host "Git no disponible: no se pudo desindexar artefactos." -ForegroundColor Yellow
}

Write-Host "Limpieza local completada. Revisa backups_externos antes de borrar archivos." -ForegroundColor Green

Write-Host ""
Write-Host "Siguientes pasos (ejecutar manualmente):" -ForegroundColor Cyan
Write-Host "1) Crea el repositorio vacío en GitHub (sin README)."
Write-Host "2) Enlaza remoto y hace push:"
Write-Host "   git remote add origin https://github.com/tu_usuario/tu_repositorio.git"
Write-Host "   git push -u origin main"
