# AnalizadorEstadisticasIcaria.ps1
# Script PowerShell para analizar el archivo resumen_final.txt

param(
    [string]$archivoResumen = "resumen_final.txt"
)

# Configuración
$outputDir = "output_analisis"
$fechaAnalisis = Get-Date -Format "yyyy-MM-dd HH:mm:ss"

# Crear directorio de salida
if (-not (Test-Path $outputDir)) {
    New-Item -ItemType Directory -Path $outputDir | Out-Null
    Write-Host "Directorio de salida creado: $outputDir" -ForegroundColor Green
}

# Función para cargar el contenido del archivo
function Cargar-Contenido {
    param($archivo)
    
    if (-not (Test-Path $archivo)) {
        Write-Host "Error: No se encuentra el archivo '$archivo'" -ForegroundColor Red
        return $null
    }
    
    try {
        $contenido = Get-Content -Path $archivo -Raw -Encoding UTF8
        Write-Host "Archivo cargado exitosamente: $archivo" -ForegroundColor Green
        Write-Host "Tamaño: $($contenido.Length) caracteres" -ForegroundColor Cyan
        return $contenido
    }
    catch {
        Write-Host "Error al cargar el archivo: $_" -ForegroundColor Red
        return $null
    }
}

# Función para extraer estadísticas básicas
function Extraer-EstadisticasBasicas {
    param($contenido)
    
    Write-Host "`nExtrayendo estadisticas basicas..." -ForegroundColor Yellow
    
    $estadisticas = @{}
    
    # Patrones de busqueda
    if ($contenido -match "Total casos procesados:\s*(\d+)") {
        $estadisticas.total_casos = [int]$matches[1]
        Write-Host "  Total casos procesados: $($estadisticas.total_casos)" -ForegroundColor Cyan
    }
    
    if ($contenido -match "Casos completamente modelados:\s*~(\d+)") {
        $estadisticas.casos_completamente_modelados = [int]$matches[1]
        Write-Host "  Casos completamente modelados: $($estadisticas.casos_completamente_modelados)" -ForegroundColor Cyan
    }
    
    if ($contenido -match "Casos parcialmente modelados:\s*~(\d+)") {
        $estadisticas.casos_parcialmente_modelados = [int]$matches[1]
        Write-Host "  Casos parcialmente modelados: $($estadisticas.casos_parcialmente_modelados)" -ForegroundColor Cyan
    }
    
    if ($contenido -match "Cobertura de modelado:\s*~([\d\.]+)%") {
        $estadisticas.porcentaje_modelados = [float]$matches[1]
        Write-Host "  Cobertura de modelado: $($estadisticas.porcentaje_modelados)%" -ForegroundColor Cyan
    }
    
    if ($contenido -match "Fecha de procesamiento:\s*(\d{1,2}/\d{1,2}/\d{4})") {
        $estadisticas.fecha_procesamiento = $matches[1]
        Write-Host "  Fecha de procesamiento: $($estadisticas.fecha_procesamiento)" -ForegroundColor Cyan
    }
    
    return $estadisticas
}

# Función para extraer distribución por tipo de usuario
function Extraer-DistribucionTipos {
    param($contenido)
    
    Write-Host "`nAnalizando distribucion por tipo de usuario..." -ForegroundColor Yellow
    
    $distribucion = @{}
    
    # Buscar la sección
    if ($contenido -match "DISTRIBUCIÓN POR SEGMENTO:.*?ETIQUETAS ICARIA") {
        $seccion = $matches[0]
        
        # Particulares
        if ($seccion -match "Particulares:\s*~(\d+)") {
            $distribucion.Particulares = [int]$matches[1]
            Write-Host "  Particulares: $($distribucion.Particulares) casos" -ForegroundColor Cyan
        }
        
        # Empresas
        if ($seccion -match "Empresas:\s*~(\d+)") {
            $distribucion.Empresas = [int]$matches[1]
            Write-Host "  Empresas: $($distribucion.Empresas) casos" -ForegroundColor Cyan
        }
        
        # Autónomos
        if ($seccion -match "Autónomos:\s*~(\d+)") {
            $distribucion.Autonomos = [int]$matches[1]
            Write-Host "  Autónomos: $($distribucion.Autonomos) casos" -ForegroundColor Cyan
        }
        
        # Calcular total y porcentajes
        $total = $distribucion.Particulares + $distribucion.Empresas + $distribucion.Autonomos
        if ($total -gt 0) {
            $distribucion.Particulares_Porcentaje = [math]::Round(($distribucion.Particulares / $total) * 100, 1)
            $distribucion.Empresas_Porcentaje = [math]::Round(($distribucion.Empresas / $total) * 100, 1)
            $distribucion.Autonomos_Porcentaje = [math]::Round(($distribucion.Autonomos / $total) * 100, 1)
        }
    }
    
    return $distribucion
}

# Función para extraer etiquetas más frecuentes
function Extraer-EtiquetasFrecuentes {
    param($contenido)
    
    Write-Host "`nExtrayendo etiquetas mas frecuentes..." -ForegroundColor Yellow
    
    $etiquetas = @{}
    
    # Buscar las etiquetas (líneas como "1. `TIENE_BANCA_A_DISTANCIA`: ~1170 ocurrencias (~79%)")
    $patron = '(\d+)\.\s*`([^`]+)`\s*:\s*~(\d+)\s*ocurrencias\s*\(~([\d\.]+)%\)'
    $matches = [regex]::Matches($contenido, $patron)
    
    foreach ($match in $matches) {
        $rank = [int]$match.Groups[1].Value
        $etiqueta = $match.Groups[2].Value
        $ocurrencias = [int]$match.Groups[3].Value
        $porcentaje = [float]$match.Groups[4].Value
        
        $etiquetas[$etiqueta] = @{
            rank = $rank
            ocurrencias = $ocurrencias
            porcentaje = $porcentaje
            casos_afectados = [math]::Round(1481 * ($porcentaje / 100))
        }
    }
    
    Write-Host "  Extraidas $($etiquetas.Count) etiquetas frecuentes" -ForegroundColor Cyan
    
    # Mostrar top 5
    $top5 = $etiquetas.GetEnumerator() | Sort-Object { $_.Value.rank } | Select-Object -First 5
    Write-Host "`n  Top 5 etiquetas mas frecuentes:" -ForegroundColor White
    
    foreach ($item in $top5) {
        Write-Host "    $($item.Value.rank). $($item.Key): $($item.Value.ocurrencias) ocurrencias ($($item.Value.porcentaje)%)" -ForegroundColor Gray
    }
    
    return $etiquetas
}

# Función para extraer brechas de cobertura
function Extraer-BrechasCobertura {
    param($contenido)
    
    Write-Host "`nAnalizando brechas de cobertura..." -ForegroundColor Yellow
    
    $brechas = @{}
    
    # Buscar brechas (líneas como "1. Elementos de Bizum/notificaciones Push (266 casos, ~18%)")
    $patron = '(\d+)\.\s*(.+?)\s*\((\d+)\s*casos,\s*~([\d\.]+)%\)'
    $matches = [regex]::Matches($contenido, $patron)
    
    foreach ($match in $matches) {
        $rank = [int]$match.Groups[1].Value
        $elemento = $match.Groups[2].Value.Trim()
        $casos = [int]$match.Groups[3].Value
        $porcentaje = [float]$match.Groups[4].Value
        
        $brechas[$elemento] = @{
            rank = $rank
            casos = $casos
            porcentaje = $porcentaje
        }
    }
    
    Write-Host "  Identificadas $($brechas.Count) brechas de cobertura" -ForegroundColor Cyan
    
    # Mostrar top 3
    $top3 = $brechas.GetEnumerator() | Sort-Object { $_.Value.porcentaje } -Descending | Select-Object -First 3
    Write-Host "`n  Top 3 brechas mas criticas:" -ForegroundColor White
    
    foreach ($item in $top3) {
        Write-Host "    $($item.Value.rank). $($item.Key): $($item.Value.casos) casos ($($item.Value.porcentaje)%)" -ForegroundColor Gray
    }
    
    return $brechas
}

# Función para extraer nuevas etiquetas propuestas
function Extraer-NuevasEtiquetas {
    param($contenido)
    
    Write-Host "`nExtrayendo nuevas etiquetas propuestas..." -ForegroundColor Yellow
    
    $nuevasEtiquetas = @()
    
    # Buscar nuevas etiquetas (líneas como "1. `ES_USUARIO_URQUIJO` → Usuario de Urquijo")
    $patron = '(\d+)\.\s*`([^`]+)`\s*→\s*(.+)'
    $matches = [regex]::Matches($contenido, $patron)
    
    foreach ($match in $matches) {
        $etiqueta = @{
            numero = [int]$match.Groups[1].Value
            etiqueta = $match.Groups[2].Value
            descripcion = $match.Groups[3].Value.Trim()
        }
        $nuevasEtiquetas += $etiqueta
    }
    
    Write-Host "  Extraidas $($nuevasEtiquetas.Count) nuevas etiquetas propuestas" -ForegroundColor Cyan
    
    # Mostrar algunas
    if ($nuevasEtiquetas.Count -gt 0) {
        Write-Host "`n  Ejemplos de nuevas etiquetas:" -ForegroundColor White
        $nuevasEtiquetas | Select-Object -First 3 | ForEach-Object {
            Write-Host "    $($_.numero). $($_.etiqueta): $($_.descripcion)" -ForegroundColor Gray
        }
    }
    
    return $nuevasEtiquetas
}

# Función para generar reporte ejecutivo
function Generar-ReporteEjecutivo {
    param(
        $estadisticas,
        $distribucion,
        $etiquetas,
        $brechas,
        $nuevasEtiquetas
    )
    
    $reporte = @"
============================================================
RESUMEN EJECUTIVO - ANALISIS ICARIA (1481 CASOS)
============================================================

ESTADISTICAS GENERALES:
- Total de casos procesados: $($estadisticas.total_casos)
- Casos completamente modelados: $($estadisticas.casos_completamente_modelados) ($($estadisticas.porcentaje_modelados)%)
- Casos con brechas de cobertura: $($estadisticas.total_casos - $estadisticas.casos_completamente_modelados) ($(100 - $estadisticas.porcentaje_modelados)%)
- Fecha de analisis: $fechaAnalisis

DISTRIBUCION POR TIPO DE USUARIO:
- Particulares: $($distribucion.Particulares) casos ($($distribucion.Particulares_Porcentaje)%)
- Empresas: $($distribucion.Empresas) casos ($($distribucion.Empresas_Porcentaje)%)
- Autonomos: $($distribucion.Autonomos) casos ($($distribucion.Autonomos_Porcentaje)%)

ETIQUETAS MAS UTILIZADAS (Top 3):
"@
    
    # Agregar top 3 etiquetas
    $top3Etiquetas = $etiquetas.GetEnumerator() | Sort-Object { $_.Value.rank } | Select-Object -First 3
    foreach ($item in $top3Etiquetas) {
        $reporte += "`n- $($item.Key): $($item.Value.ocurrencias) ocurrencias ($($item.Value.porcentaje)%)"
    }
    
    $reporte += @"

PRINCIPALES BRECHAS IDENTIFICADAS (Top 3):
"@
    
    # Agregar top 3 brechas
    $top3Brechas = $brechas.GetEnumerator() | Sort-Object { $_.Value.porcentaje } -Descending | Select-Object -First 3
    foreach ($item in $top3Brechas) {
        $reporte += "`n- $($item.Key): $($item.Value.casos) casos ($($item.Value.porcentaje)%)"
    }
    
    $reporte += @"

NUEVAS ETIQUETAS PROPUESTAS:
- Total identificadas: $($nuevasEtiquetas.Count)
- Cobertura potencial estimada: $( [math]::Round($estadisticas.porcentaje_modelados + 27.5, 1) )%

RECOMENDACIONES:
1. Priorizar desarrollo de etiquetas para Onboarding
2. Implementar cobertura para Bizum/Notificaciones
3. Desarrollar etiquetas para Valores/Inversion

============================================================
"@
    
    return $reporte
}

# Función para guardar reportes
function Guardar-Reportes {
    param(
        $reporteEjecutivo,
        $estadisticas,
        $distribucion,
        $etiquetas,
        $brechas,
        $nuevasEtiquetas
    )
    
    Write-Host "`nGenerando reportes..." -ForegroundColor Yellow
    
    # 1. Reporte ejecutivo en TXT
    $reporteEjecutivo | Out-File -FilePath "$outputDir/resumen_ejecutivo.txt" -Encoding UTF8
    Write-Host "  Reporte ejecutivo guardado: $outputDir/resumen_ejecutivo.txt" -ForegroundColor Green
    
    # 2. Estadísticas en CSV
    $csvLineas = @()
    $csvLineas += "Metrica,Valor"
    foreach ($key in $estadisticas.Keys) {
        $csvLineas += "$key,$($estadisticas[$key])"
    }
    $csvLineas | Out-File -FilePath "$outputDir/estadisticas.csv" -Encoding UTF8
    Write-Host "  Estadisticas guardadas: $outputDir/estadisticas.csv" -ForegroundColor Green
    
    # 3. Distribución en CSV
    $csvDist = @()
    $csvDist += "Tipo,Casos,Porcentaje"
    $csvDist += "Particulares,$($distribucion.Particulares),$($distribucion.Particulares_Porcentaje)"
    $csvDist += "Empresas,$($distribucion.Empresas),$($distribucion.Empresas_Porcentaje)"
    $csvDist += "Autonomos,$($distribucion.Autonomos),$($distribucion.Autonomos_Porcentaje)"
    $csvDist | Out-File -FilePath "$outputDir/distribucion.csv" -Encoding UTF8
    Write-Host "  Distribucion guardada: $outputDir/distribucion.csv" -ForegroundColor Green
    
    # 4. Nuevas etiquetas en CSV
    if ($nuevasEtiquetas.Count -gt 0) {
        $csvEtiquetas = @()
        $csvEtiquetas += "Numero,Etiqueta,Descripcion"
        foreach ($etiqueta in $nuevasEtiquetas) {
            $csvEtiquetas += "$($etiqueta.numero),$($etiqueta.etiqueta),$($etiqueta.descripcion)"
        }
        $csvEtiquetas | Out-File -FilePath "$outputDir/nuevas_etiquetas.csv" -Encoding UTF8
        Write-Host "  Nuevas etiquetas guardadas: $outputDir/nuevas_etiquetas.csv" -ForegroundColor Green
    }
    
    # 5. Reporte JSON completo
    $reporteCompleto = @{
        metadata = @{
            fecha_analisis = $fechaAnalisis
            archivo_origen = $archivoResumen
            total_casos = $estadisticas.total_casos
        }
        estadisticas_basicas = $estadisticas
        distribucion_tipos_usuario = $distribucion
        etiquetas_frecuentes = $etiquetas
        brechas_cobertura = $brechas
        nuevas_etiquetas = $nuevasEtiquetas
    }
    
    $reporteCompleto | ConvertTo-Json -Depth 10 | Out-File -FilePath "$outputDir/reporte_completo.json" -Encoding UTF8
    Write-Host "  Reporte JSON completo: $outputDir/reporte_completo.json" -ForegroundColor Green
}

# Función para mostrar estadísticas en consola
function Mostrar-EstadisticasConsola {
    param(
        $estadisticas,
        $distribucion,
        $etiquetas,
        $brechas,
        $nuevasEtiquetas
    )
    
    Write-Host "`n" + ("="*60) -ForegroundColor Magenta
    Write-Host "RESUMEN DEL ANALISIS" -ForegroundColor White -BackgroundColor DarkMagenta
    Write-Host ""="*60 -ForegroundColor Magenta
    
    Write-Host "`nESTADISTICAS CLAVE:" -ForegroundColor Yellow
    Write-Host "-------------------" -ForegroundColor Gray
    Write-Host "Total de casos: $($estadisticas.total_casos)" -ForegroundColor White
    Write-Host "Casos modelados completamente: $($estadisticas.casos_completamente_modelados) ($($estadisticas.porcentaje_modelados)%)" -ForegroundColor White
    Write-Host "Casos con brechas: $($estadisticas.casos_parcialmente_modelados) ($(100 - $estadisticas.porcentaje_modelados)%)" -ForegroundColor White
    
    Write-Host "`nDISTRIBUCION:" -ForegroundColor Yellow
    Write-Host "-------------" -ForegroundColor Gray
    Write-Host "Particulares: $($distribucion.Particulares) ($($distribucion.Particulares_Porcentaje)%)" -ForegroundColor White
    Write-Host "Empresas: $($distribucion.Empresas) ($($distribucion.Empresas_Porcentaje)%)" -ForegroundColor White
    Write-Host "Autonomos: $($distribucion.Autonomos) ($($distribucion.Autonomos_Porcentaje)%)" -ForegroundColor White
    
    Write-Host "`nBRECHAS MAS GRAVES:" -ForegroundColor Yellow
    Write-Host "-------------------" -ForegroundColor Gray
    $topBrechas = $brechas.GetEnumerator() | Sort-Object { $_.Value.porcentaje } -Descending | Select-Object -First 3
    foreach ($brecha in $topBrechas) {
        Write-Host "$($brecha.Value.rank). $($brecha.Key): $($brecha.Value.casos) casos" -ForegroundColor White
    }
    
    Write-Host "`nNUEVAS ETIQUETAS IDENTIFICADAS:" -ForegroundColor Yellow
    Write-Host "--------------------------------" -ForegroundColor Gray
    Write-Host "Total: $($nuevasEtiquetas.Count)" -ForegroundColor White
    
    Write-Host "`n" + ("="*60) -ForegroundColor Magenta
}

# Función principal
function Main {
    Write-Host "============================================================" -ForegroundColor Green
    Write-Host "ANALISIS ESTADISTICO DE CASOS ICARIA - BANCO SABADELL" -ForegroundColor White -BackgroundColor DarkGreen
    Write-Host "============================================================" -ForegroundColor Green
    
    # Cargar contenido
    $contenido = Cargar-Contenido -archivo $archivoResumen
    if (-not $contenido) {
        return
    }
    
    # Extraer todas las estadísticas
    $estadisticas = Extraer-EstadisticasBasicas -contenido $contenido
    $distribucion = Extraer-DistribucionTipos -contenido $contenido
    $etiquetas = Extraer-EtiquetasFrecuentes -contenido $contenido
    $brechas = Extraer-BrechasCobertura -contenido $contenido
    $nuevasEtiquetas = Extraer-NuevasEtiquetas -contenido $contenido
    
    # Generar reporte ejecutivo
    $reporteEjecutivo = Generar-ReporteEjecutivo -estadisticas $estadisticas -distribucion $distribucion -etiquetas $etiquetas -brechas $brechas -nuevasEtiquetas $nuevasEtiquetas
    
    # Guardar reportes
    Guardar-Reportes -reporteEjecutivo $reporteEjecutivo -estadisticas $estadisticas -distribucion $distribucion -etiquetas $etiquetas -brechas $brechas -nuevasEtiquetas $nuevasEtiquetas
    
    # Mostrar en consola
    Mostrar-EstadisticasConsola -estadisticas $estadisticas -distribucion $distribucion -etiquetas $etiquetas -brechas $brechas -nuevasEtiquetas $nuevasEtiquetas
    
    # Mostrar ubicación de resultados
    Write-Host "`nARCHIVOS GENERADOS:" -ForegroundColor Yellow
    Write-Host "-------------------" -ForegroundColor Gray
    Get-ChildItem $outputDir | ForEach-Object {
        Write-Host "  $($_.Name) ($([math]::Round($_.Length/1KB, 2)) KB)" -ForegroundColor Cyan
    }
    
    Write-Host "`nUbicacion completa: $(Resolve-Path $outputDir)" -ForegroundColor Green
    
    Write-Host "`n============================================================" -ForegroundColor Green
    Write-Host "ANALISIS COMPLETADO EXITOSAMENTE" -ForegroundColor White -BackgroundColor DarkGreen
    Write-Host "============================================================" -ForegroundColor Green
}

# Ejecutar análisis
Main
# AnalizadorEstadisticasIcaria.ps1
# Script PowerShell para analizar el archivo resumen_final.txt

param(
    [string]$archivoResumen = "resumen_final.txt"
)

# Configuración
$outputDir = "output_analisis"
$fechaAnalisis = Get-Date -Format "yyyy-MM-dd HH:mm:ss"

# Crear directorio de salida
if (-not (Test-Path $outputDir)) {
    New-Item -ItemType Directory -Path $outputDir | Out-Null
    Write-Host "Directorio de salida creado: $outputDir" -ForegroundColor Green
}

# Función para cargar el contenido del archivo
function Cargar-Contenido {
    param($archivo)
    
    if (-not (Test-Path $archivo)) {
        Write-Host "Error: No se encuentra el archivo '$archivo'" -ForegroundColor Red
        return $null
    }
    
    try {
        $contenido = Get-Content -Path $archivo -Raw -Encoding UTF8
        Write-Host "Archivo cargado exitosamente: $archivo" -ForegroundColor Green
        Write-Host "Tamaño: $($contenido.Length) caracteres" -ForegroundColor Cyan
        return $contenido
    }
    catch {
        Write-Host "Error al cargar el archivo: $_" -ForegroundColor Red
        return $null
    }
}

# Función para extraer estadísticas básicas
function Extraer-EstadisticasBasicas {
    param($contenido)
    
    Write-Host "`nExtrayendo estadisticas basicas..." -ForegroundColor Yellow
    
    $estadisticas = @{}
    
    # Patrones de busqueda
    if ($contenido -match "Total casos procesados:\s*(\d+)") {
        $estadisticas.total_casos = [int]$matches[1]
        Write-Host "  Total casos procesados: $($estadisticas.total_casos)" -ForegroundColor Cyan
    }
    
    if ($contenido -match "Casos completamente modelados:\s*~(\d+)") {
        $estadisticas.casos_completamente_modelados = [int]$matches[1]
        Write-Host "  Casos completamente modelados: $($estadisticas.casos_completamente_modelados)" -ForegroundColor Cyan
    }
    
    if ($contenido -match "Casos parcialmente modelados:\s*~(\d+)") {
        $estadisticas.casos_parcialmente_modelados = [int]$matches[1]
        Write-Host "  Casos parcialmente modelados: $($estadisticas.casos_parcialmente_modelados)" -ForegroundColor Cyan
    }
    
    if ($contenido -match "Cobertura de modelado:\s*~([\d\.]+)%") {
        $estadisticas.porcentaje_modelados = [float]$matches[1]
        Write-Host "  Cobertura de modelado: $($estadisticas.porcentaje_modelados)%" -ForegroundColor Cyan
    }
    
    if ($contenido -match "Fecha de procesamiento:\s*(\d{1,2}/\d{1,2}/\d{4})") {
        $estadisticas.fecha_procesamiento = $matches[1]
        Write-Host "  Fecha de procesamiento: $($estadisticas.fecha_procesamiento)" -ForegroundColor Cyan
    }
    
    return $estadisticas
}

# Función para extraer distribución por tipo de usuario
function Extraer-DistribucionTipos {
    param($contenido)
    
    Write-Host "`nAnalizando distribucion por tipo de usuario..." -ForegroundColor Yellow
    
    $distribucion = @{}
    
    # Buscar la sección
    if ($contenido -match "DISTRIBUCIÓN POR SEGMENTO:.*?ETIQUETAS ICARIA") {
        $seccion = $matches[0]
        
        # Particulares
        if ($seccion -match "Particulares:\s*~(\d+)") {
            $distribucion.Particulares = [int]$matches[1]
            Write-Host "  Particulares: $($distribucion.Particulares) casos" -ForegroundColor Cyan
        }
        
        # Empresas
        if ($seccion -match "Empresas:\s*~(\d+)") {
            $distribucion.Empresas = [int]$matches[1]
            Write-Host "  Empresas: $($distribucion.Empresas) casos" -ForegroundColor Cyan
        }
        
        # Autónomos
        if ($seccion -match "Autónomos:\s*~(\d+)") {
            $distribucion.Autonomos = [int]$matches[1]
            Write-Host "  Autónomos: $($distribucion.Autonomos) casos" -ForegroundColor Cyan
        }
        
        # Calcular total y porcentajes
        $total = $distribucion.Particulares + $distribucion.Empresas + $distribucion.Autonomos
        if ($total -gt 0) {
            $distribucion.Particulares_Porcentaje = [math]::Round(($distribucion.Particulares / $total) * 100, 1)
            $distribucion.Empresas_Porcentaje = [math]::Round(($distribucion.Empresas / $total) * 100, 1)
            $distribucion.Autonomos_Porcentaje = [math]::Round(($distribucion.Autonomos / $total) * 100, 1)
        }
    }
    
    return $distribucion
}

# Función para extraer etiquetas más frecuentes
function Extraer-EtiquetasFrecuentes {
    param($contenido)
    
    Write-Host "`nExtrayendo etiquetas mas frecuentes..." -ForegroundColor Yellow
    
    $etiquetas = @{}
    
    # Buscar las etiquetas (líneas como "1. `TIENE_BANCA_A_DISTANCIA`: ~1170 ocurrencias (~79%)")
    $patron = '(\d+)\.\s*`([^`]+)`\s*:\s*~(\d+)\s*ocurrencias\s*\(~([\d\.]+)%\)'
    $matches = [regex]::Matches($contenido, $patron)
    
    foreach ($match in $matches) {
        $rank = [int]$match.Groups[1].Value
        $etiqueta = $match.Groups[2].Value
        $ocurrencias = [int]$match.Groups[3].Value
        $porcentaje = [float]$match.Groups[4].Value
        
        $etiquetas[$etiqueta] = @{
            rank = $rank
            ocurrencias = $ocurrencias
            porcentaje = $porcentaje
            casos_afectados = [math]::Round(1481 * ($porcentaje / 100))
        }
    }
    
    Write-Host "  Extraidas $($etiquetas.Count) etiquetas frecuentes" -ForegroundColor Cyan
    
    # Mostrar top 5
    $top5 = $etiquetas.GetEnumerator() | Sort-Object { $_.Value.rank } | Select-Object -First 5
    Write-Host "`n  Top 5 etiquetas mas frecuentes:" -ForegroundColor White
    
    foreach ($item in $top5) {
        Write-Host "    $($item.Value.rank). $($item.Key): $($item.Value.ocurrencias) ocurrencias ($($item.Value.porcentaje)%)" -ForegroundColor Gray
    }
    
    return $etiquetas
}

# Función para extraer brechas de cobertura
function Extraer-BrechasCobertura {
    param($contenido)
    
    Write-Host "`nAnalizando brechas de cobertura..." -ForegroundColor Yellow
    
    $brechas = @{}
    
    # Buscar brechas (líneas como "1. Elementos de Bizum/notificaciones Push (266 casos, ~18%)")
    $patron = '(\d+)\.\s*(.+?)\s*\((\d+)\s*casos,\s*~([\d\.]+)%\)'
    $matches = [regex]::Matches($contenido, $patron)
    
    foreach ($match in $matches) {
        $rank = [int]$match.Groups[1].Value
        $elemento = $match.Groups[2].Value.Trim()
        $casos = [int]$match.Groups[3].Value
        $porcentaje = [float]$match.Groups[4].Value
        
        $brechas[$elemento] = @{
            rank = $rank
            casos = $casos
            porcentaje = $porcentaje
        }
    }
    
    Write-Host "  Identificadas $($brechas.Count) brechas de cobertura" -ForegroundColor Cyan
    
    # Mostrar top 3
    $top3 = $brechas.GetEnumerator() | Sort-Object { $_.Value.porcentaje } -Descending | Select-Object -First 3
    Write-Host "`n  Top 3 brechas mas criticas:" -ForegroundColor White
    
    foreach ($item in $top3) {
        Write-Host "    $($item.Value.rank). $($item.Key): $($item.Value.casos) casos ($($item.Value.porcentaje)%)" -ForegroundColor Gray
    }
    
    return $brechas
}

# Función para extraer nuevas etiquetas propuestas
function Extraer-NuevasEtiquetas {
    param($contenido)
    
    Write-Host "`nExtrayendo nuevas etiquetas propuestas..." -ForegroundColor Yellow
    
    $nuevasEtiquetas = @()
    
    # Buscar nuevas etiquetas (líneas como "1. `ES_USUARIO_URQUIJO` → Usuario de Urquijo")
    $patron = '(\d+)\.\s*`([^`]+)`\s*→\s*(.+)'
    $matches = [regex]::Matches($contenido, $patron)
    
    foreach ($match in $matches) {
        $etiqueta = @{
            numero = [int]$match.Groups[1].Value
            etiqueta = $match.Groups[2].Value
            descripcion = $match.Groups[3].Value.Trim()
        }
        $nuevasEtiquetas += $etiqueta
    }
    
    Write-Host "  Extraidas $($nuevasEtiquetas.Count) nuevas etiquetas propuestas" -ForegroundColor Cyan
    
    # Mostrar algunas
    if ($nuevasEtiquetas.Count -gt 0) {
        Write-Host "`n  Ejemplos de nuevas etiquetas:" -ForegroundColor White
        $nuevasEtiquetas | Select-Object -First 3 | ForEach-Object {
            Write-Host "    $($_.numero). $($_.etiqueta): $($_.descripcion)" -ForegroundColor Gray
        }
    }
    
    return $nuevasEtiquetas
}

# Función para generar reporte ejecutivo
function Generar-ReporteEjecutivo {
    param(
        $estadisticas,
        $distribucion,
        $etiquetas,
        $brechas,
        $nuevasEtiquetas
    )
    
    $reporte = @"
============================================================
RESUMEN EJECUTIVO - ANALISIS ICARIA (1481 CASOS)
============================================================

ESTADISTICAS GENERALES:
- Total de casos procesados: $($estadisticas.total_casos)
- Casos completamente modelados: $($estadisticas.casos_completamente_modelados) ($($estadisticas.porcentaje_modelados)%)
- Casos con brechas de cobertura: $($estadisticas.total_casos - $estadisticas.casos_completamente_modelados) ($(100 - $estadisticas.porcentaje_modelados)%)
- Fecha de analisis: $fechaAnalisis

DISTRIBUCION POR TIPO DE USUARIO:
- Particulares: $($distribucion.Particulares) casos ($($distribucion.Particulares_Porcentaje)%)
- Empresas: $($distribucion.Empresas) casos ($($distribucion.Empresas_Porcentaje)%)
- Autonomos: $($distribucion.Autonomos) casos ($($distribucion.Autonomos_Porcentaje)%)

ETIQUETAS MAS UTILIZADAS (Top 3):
"@
    
    # Agregar top 3 etiquetas
    $top3Etiquetas = $etiquetas.GetEnumerator() | Sort-Object { $_.Value.rank } | Select-Object -First 3
    foreach ($item in $top3Etiquetas) {
        $reporte += "`n- $($item.Key): $($item.Value.ocurrencias) ocurrencias ($($item.Value.porcentaje)%)"
    }
    
    $reporte += @"

PRINCIPALES BRECHAS IDENTIFICADAS (Top 3):
"@
    
    # Agregar top 3 brechas
    $top3Brechas = $brechas.GetEnumerator() | Sort-Object { $_.Value.porcentaje } -Descending | Select-Object -First 3
    foreach ($item in $top3Brechas) {
        $reporte += "`n- $($item.Key): $($item.Value.casos) casos ($($item.Value.porcentaje)%)"
    }
    
    $reporte += @"

NUEVAS ETIQUETAS PROPUESTAS:
- Total identificadas: $($nuevasEtiquetas.Count)
- Cobertura potencial estimada: $( [math]::Round($estadisticas.porcentaje_modelados + 27.5, 1) )%

RECOMENDACIONES:
1. Priorizar desarrollo de etiquetas para Onboarding
2. Implementar cobertura para Bizum/Notificaciones
3. Desarrollar etiquetas para Valores/Inversion

============================================================
"@
    
    return $reporte
}

# Función para guardar reportes
function Guardar-Reportes {
    param(
        $reporteEjecutivo,
        $estadisticas,
        $distribucion,
        $etiquetas,
        $brechas,
        $nuevasEtiquetas
    )
    
    Write-Host "`nGenerando reportes..." -ForegroundColor Yellow
    
    # 1. Reporte ejecutivo en TXT
    $reporteEjecutivo | Out-File -FilePath "$outputDir/resumen_ejecutivo.txt" -Encoding UTF8
    Write-Host "  Reporte ejecutivo guardado: $outputDir/resumen_ejecutivo.txt" -ForegroundColor Green
    
    # 2. Estadísticas en CSV
    $csvLineas = @()
    $csvLineas += "Metrica,Valor"
    foreach ($key in $estadisticas.Keys) {
        $csvLineas += "$key,$($estadisticas[$key])"
    }
    $csvLineas | Out-File -FilePath "$outputDir/estadisticas.csv" -Encoding UTF8
    Write-Host "  Estadisticas guardadas: $outputDir/estadisticas.csv" -ForegroundColor Green
    
    # 3. Distribución en CSV
    $csvDist = @()
    $csvDist += "Tipo,Casos,Porcentaje"
    $csvDist += "Particulares,$($distribucion.Particulares),$($distribucion.Particulares_Porcentaje)"
    $csvDist += "Empresas,$($distribucion.Empresas),$($distribucion.Empresas_Porcentaje)"
    $csvDist += "Autonomos,$($distribucion.Autonomos),$($distribucion.Autonomos_Porcentaje)"
    $csvDist | Out-File -FilePath "$outputDir/distribucion.csv" -Encoding UTF8
    Write-Host "  Distribucion guardada: $outputDir/distribucion.csv" -ForegroundColor Green
    
    # 4. Nuevas etiquetas en CSV
    if ($nuevasEtiquetas.Count -gt 0) {
        $csvEtiquetas = @()
        $csvEtiquetas += "Numero,Etiqueta,Descripcion"
        foreach ($etiqueta in $nuevasEtiquetas) {
            $csvEtiquetas += "$($etiqueta.numero),$($etiqueta.etiqueta),$($etiqueta.descripcion)"
        }
        $csvEtiquetas | Out-File -FilePath "$outputDir/nuevas_etiquetas.csv" -Encoding UTF8
        Write-Host "  Nuevas etiquetas guardadas: $outputDir/nuevas_etiquetas.csv" -ForegroundColor Green
    }
    
    # 5. Reporte JSON completo
    $reporteCompleto = @{
        metadata = @{
            fecha_analisis = $fechaAnalisis
            archivo_origen = $archivoResumen
            total_casos = $estadisticas.total_casos
        }
        estadisticas_basicas = $estadisticas
        distribucion_tipos_usuario = $distribucion
        etiquetas_frecuentes = $etiquetas
        brechas_cobertura = $brechas
        nuevas_etiquetas = $nuevasEtiquetas
    }
    
    $reporteCompleto | ConvertTo-Json -Depth 10 | Out-File -FilePath "$outputDir/reporte_completo.json" -Encoding UTF8
    Write-Host "  Reporte JSON completo: $outputDir/reporte_completo.json" -ForegroundColor Green
}

# Función para mostrar estadísticas en consola
function Mostrar-EstadisticasConsola {
    param(
        $estadisticas,
        $distribucion,
        $etiquetas,
        $brechas,
        $nuevasEtiquetas
    )
    
    Write-Host "`n" + ("="*60) -ForegroundColor Magenta
    Write-Host "RESUMEN DEL ANALISIS" -ForegroundColor White -BackgroundColor DarkMagenta
    Write-Host "="*60 -ForegroundColor Magenta
    
    Write-Host "`nESTADISTICAS CLAVE:" -ForegroundColor Yellow
    Write-Host "-------------------" -ForegroundColor Gray
    Write-Host "Total de casos: $($estadisticas.total_casos)" -ForegroundColor White
    Write-Host "Casos modelados completamente: $($estadisticas.casos_completamente_modelados) ($($estadisticas.porcentaje_modelados)%)" -ForegroundColor White
    Write-Host "Casos con brechas: $($estadisticas.casos_parcialmente_modelados) ($(100 - $estadisticas.porcentaje_modelados)%)" -ForegroundColor White
    
    Write-Host "`nDISTRIBUCION:" -ForegroundColor Yellow
    Write-Host "-------------" -ForegroundColor Gray
    Write-Host "Particulares: $($distribucion.Particulares) ($($distribucion.Particulares_Porcentaje)%)" -ForegroundColor White
    Write-Host "Empresas: $($distribucion.Empresas) ($($distribucion.Empresas_Porcentaje)%)" -ForegroundColor White
    Write-Host "Autonomos: $($distribucion.Autonomos) ($($distribucion.Autonomos_Porcentaje)%)" -ForegroundColor White
    
    Write-Host "`nBRECHAS MAS GRAVES:" -ForegroundColor Yellow
    Write-Host "-------------------" -ForegroundColor Gray
    $topBrechas = $brechas.GetEnumerator() | Sort-Object { $_.Value.porcentaje } -Descending | Select-Object -First 3
    foreach ($brecha in $topBrechas) {
        Write-Host "$($brecha.Value.rank). $($brecha.Key): $($brecha.Value.casos) casos" -ForegroundColor White
    }
    
    Write-Host "`nNUEVAS ETIQUETAS IDENTIFICADAS:" -ForegroundColor Yellow
    Write-Host "--------------------------------" -ForegroundColor Gray
    Write-Host "Total: $($nuevasEtiquetas.Count)" -ForegroundColor White
    
    Write-Host "`n" + ("="*60) -ForegroundColor Magenta
}

# Función principal
function Main {
    Write-Host "============================================================" -ForegroundColor Green
    Write-Host "ANALISIS ESTADISTICO DE CASOS ICARIA - BANCO SABADELL" -ForegroundColor White -BackgroundColor DarkGreen
    Write-Host "============================================================" -ForegroundColor Green
    
    # Cargar contenido
    $contenido = Cargar-Contenido -archivo $archivoResumen
    if (-not $contenido) {
        return
    }
    
    # Extraer todas las estadísticas
    $estadisticas = Extraer-EstadisticasBasicas -contenido $contenido
    $distribucion = Extraer-DistribucionTipos -contenido $contenido
    $etiquetas = Extraer-EtiquetasFrecuentes -contenido $contenido
    $brechas = Extraer-BrechasCobertura -contenido $contenido
    $nuevasEtiquetas = Extraer-NuevasEtiquetas -contenido $contenido
    
    # Generar reporte ejecutivo
    $reporteEjecutivo = Generar-ReporteEjecutivo -estadisticas $estadisticas -distribucion $distribucion -etiquetas $etiquetas -brechas $brechas -nuevasEtiquetas $nuevasEtiquetas
    
    # Guardar reportes
    Guardar-Reportes -reporteEjecutivo $reporteEjecutivo -estadisticas $estadisticas -distribucion $distribucion -etiquetas $etiquetas -brechas $brechas -nuevasEtiquetas $nuevasEtiquetas
    
    # Mostrar en consola
    Mostrar-EstadisticasConsola -estadisticas $estadisticas -distribucion $distribucion -etiquetas $etiquetas -brechas $brechas -nuevasEtiquetas $nuevasEtiquetas
    
    # Mostrar ubicación de resultados
    Write-Host "`nARCHIVOS GENERADOS:" -ForegroundColor Yellow
    Write-Host "-------------------" -ForegroundColor Gray
    Get-ChildItem $outputDir | ForEach-Object {
        Write-Host "  $($_.Name) ($([math]::Round($_.Length/1KB, 2)) KB)" -ForegroundColor Cyan
    }
    
    Write-Host "`nUbicacion completa: $(Resolve-Path $outputDir)" -ForegroundColor Green
    
    Write-Host "`n============================================================" -ForegroundColor Green
    Write-Host "ANALISIS COMPLETADO EXITOSAMENTE" -ForegroundColor White -BackgroundColor DarkGreen
    Write-Host "============================================================" -ForegroundColor Green
}

# Ejecutar análisis
Main