"""
Script de estadísticas y análisis de casos ICARIA.
Genera reportes sin modificar archivos.
"""
import re
from pathlib import Path
from collections import Counter

# Verificar VPN al inicio
from utils.vpn_check import verificar_vpn
verificar_vpn()


# ============================================================================
# CONFIGURACIÓN
# ============================================================================
RUTA_CASOS = Path(__file__).parent.parent / 'data' / 'entrada' / 'casos_bs' / 'casos_revisados.txt'
RUTA_CATALOGO = Path(__file__).parent.parent / 'data' / 'catalogo_icaria.csv'
RUTA_SALIDA = Path(__file__).parent.parent / 'output_analisis'


# ============================================================================
# FUNCIONES DE CARGA
# ============================================================================
def leer_archivo(filepath: Path) -> str:
    """Lee archivo con encoding UTF-8."""
    return filepath.read_text(encoding='utf-8')


def cargar_catalogo(catalogo_file: Path) -> set:
    """Carga códigos válidos del catálogo."""
    if not catalogo_file.exists():
        return set()
    text = catalogo_file.read_text(encoding='utf-8')
    lines = text.strip().splitlines()[1:]
    codigos = set()
    for line in lines:
        parts = line.split('\t')
        if len(parts) >= 2:
            codigos.add(parts[1].strip())
    return codigos


# ============================================================================
# FUNCIONES DE ANÁLISIS
# ============================================================================
def analizar_casos(contenido: str) -> dict:
    """Analiza todos los casos y devuelve estadísticas."""
    bloques = contenido.split('---\n')
    
    stats = {
        'total_casos': 0,
        'casos_ok': 0,
        'casos_ko': 0,
        'total_precondiciones': 0,
        'prec_modeladas': 0,
        'prec_sin_modelar': 0,
        'codigos_usados': Counter(),
        'conceptos_sin_modelar': Counter()
    }
    
    for bloque in bloques:
        if not bloque.strip() or 'CASO' not in bloque:
            continue
        
        match_caso = re.search(r'CASO (\d+)', bloque)
        if not match_caso:
            continue
        
        stats['total_casos'] += 1
        
        # Estado del caso
        match_estado = re.search(r'Estado: (✅|❌)', bloque)
        if match_estado:
            if match_estado.group(1) == '✅':
                stats['casos_ok'] += 1
            else:
                stats['casos_ko'] += 1
        
        # Precondiciones
        if 'PRECONDICIONES:' in bloque:
            seccion = bloque.split('PRECONDICIONES:')[1].split('Estado:')[0]
            lineas = [l.strip() for l in seccion.split('\n') if l.strip().startswith('-')]
            
            for linea in lineas:
                stats['total_precondiciones'] += 1
                
                # Códigos modelados
                codigos = re.findall(r'✅([A-Z_]+)', linea)
                for codigo in codigos:
                    stats['prec_modeladas'] += 1
                    stats['codigos_usados'][codigo] += 1
                
                # Sin modelar
                if '❌Sin modelar' in linea:
                    stats['prec_sin_modelar'] += 1
                    # Extraer concepto
                    texto = re.sub(r'[\u2705\u274c].*$', '', linea)
                    texto = re.sub(r'^-\s*', '', texto).strip()
                    if texto:
                        stats['conceptos_sin_modelar'][texto.lower()[:50]] += 1
    
    return stats


def generar_reporte(stats: dict, catalogo: set) -> str:
    """Genera reporte de texto con las estadísticas."""
    lines = []
    lines.append("=" * 60)
    lines.append("ESTADÍSTICAS DE CASOS ICARIA")
    lines.append("=" * 60)
    
    # Resumen general
    lines.append("\n--- RESUMEN GENERAL ---")
    lines.append(f"Total casos: {stats['total_casos']}")
    if stats['total_casos'] > 0:
        pct_ok = stats['casos_ok'] / stats['total_casos'] * 100
        pct_ko = stats['casos_ko'] / stats['total_casos'] * 100
        lines.append(f"  Casos OK: {stats['casos_ok']} ({pct_ok:.1f}%)")
        lines.append(f"  Casos KO: {stats['casos_ko']} ({pct_ko:.1f}%)")
    
    # Precondiciones
    lines.append("\n--- PRECONDICIONES ---")
    lines.append(f"Total precondiciones: {stats['total_precondiciones']}")
    if stats['total_precondiciones'] > 0:
        pct_mod = stats['prec_modeladas'] / stats['total_precondiciones'] * 100
        pct_sin = stats['prec_sin_modelar'] / stats['total_precondiciones'] * 100
        lines.append(f"  Modeladas: {stats['prec_modeladas']} ({pct_mod:.1f}%)")
        lines.append(f"  Sin modelar: {stats['prec_sin_modelar']} ({pct_sin:.1f}%)")
    
    # Catálogo
    lines.append("\n--- CATÁLOGO ---")
    lines.append(f"Códigos en catálogo: {len(catalogo)}")
    codigos_usados = set(stats['codigos_usados'].keys())
    codigos_no_usados = catalogo - codigos_usados
    lines.append(f"Códigos usados: {len(codigos_usados)}")
    lines.append(f"Códigos no usados: {len(codigos_no_usados)}")
    
    # Top códigos más usados
    lines.append("\n--- TOP 15 CÓDIGOS MÁS USADOS ---")
    for codigo, count in stats['codigos_usados'].most_common(15):
        lines.append(f"  {codigo}: {count}")
    
    # Top conceptos sin modelar
    lines.append("\n--- TOP 15 CONCEPTOS SIN MODELAR ---")
    for concepto, count in stats['conceptos_sin_modelar'].most_common(15):
        lines.append(f"  ({count}) {concepto}")
    
    # Códigos no usados
    if codigos_no_usados:
        lines.append("\n--- CÓDIGOS DEL CATÁLOGO NO USADOS ---")
        for codigo in sorted(codigos_no_usados):
            lines.append(f"  {codigo}")
    
    lines.append("\n" + "=" * 60)
    
    return '\n'.join(lines)


# ============================================================================
# FUNCIÓN PRINCIPAL
# ============================================================================
def main():
    # Cargar archivos
    if not RUTA_CASOS.exists():
        print(f"ERROR: No se encuentra {RUTA_CASOS}")
        return
    
    contenido = leer_archivo(RUTA_CASOS)
    catalogo = cargar_catalogo(RUTA_CATALOGO)
    
    # Analizar
    stats = analizar_casos(contenido)
    
    # Generar reporte
    reporte = generar_reporte(stats, catalogo)
    print(reporte)
    
    # Guardar reportes
    RUTA_SALIDA.mkdir(parents=True, exist_ok=True)
    
    # Estadísticas
    (RUTA_SALIDA / 'estadisticas_precondiciones.txt').write_text(reporte, encoding='utf-8')
    
    # Conceptos sin modelar (detallado)
    conceptos_lines = ["CONCEPTOS SIN MODELAR (ordenados por frecuencia)\n" + "=" * 50 + "\n"]
    for concepto, count in stats['conceptos_sin_modelar'].most_common():
        conceptos_lines.append(f"({count}) {concepto}")
    (RUTA_SALIDA / 'conceptos_sin_modelar.txt').write_text('\n'.join(conceptos_lines), encoding='utf-8')
    
    print(f"\nReportes guardados en: {RUTA_SALIDA}")


if __name__ == '__main__':
    main()
