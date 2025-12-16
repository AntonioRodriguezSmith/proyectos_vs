"""
Script unificado para procesar casos ICARIA.
Incluye: validación, corrección de errores y eliminación de duplicados.
"""
import re
from pathlib import Path
from collections import defaultdict
from datetime import datetime

# Verificar VPN al inicio
from utils.vpn_check import verificar_vpn
verificar_vpn()


# ============================================================================
# CONFIGURACIÓN
# ============================================================================
RUTA_CASOS = Path(__file__).parent.parent / 'data' / 'entrada' / 'casos_bs' / 'casos_revisados.txt'
RUTA_CATALOGO = Path(__file__).parent.parent / 'data' / 'catalogo_icaria.csv'


# ============================================================================
# FUNCIONES DE LECTURA/ESCRITURA
# ============================================================================
def leer_archivo(filepath: Path) -> str:
    """Lee archivo con encoding UTF-8."""
    return filepath.read_text(encoding='utf-8')


def escribir_archivo(filepath: Path, contenido: str) -> None:
    """Escribe archivo con encoding UTF-8."""
    filepath.write_text(contenido, encoding='utf-8')


def crear_backup(filepath: Path) -> Path:
    """Crea backup con timestamp."""
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_path = filepath.parent / f'{filepath.stem}_backup_{timestamp}{filepath.suffix}'
    backup_path.write_text(filepath.read_text(encoding='utf-8'), encoding='utf-8')
    return backup_path


def cargar_catalogo(catalogo_file: Path) -> set:
    """Carga códigos válidos del catálogo."""
    if not catalogo_file.exists():
        return set()
    text = catalogo_file.read_text(encoding='utf-8')
    lines = text.strip().splitlines()[1:]  # skip header
    codigos = set()
    for line in lines:
        parts = line.split('\t')
        if len(parts) >= 2:
            codigos.add(parts[1].strip())
    return codigos


# ============================================================================
# FUNCIONES DE PARSEO
# ============================================================================
def parsear_casos(contenido: str) -> list:
    """Parsea contenido y devuelve lista de casos estructurados."""
    bloques = contenido.split('---\n')
    casos = []
    
    for bloque in bloques:
        if not bloque.strip() or 'CASO' not in bloque:
            continue
        
        match_caso = re.search(r'CASO (\d+)', bloque)
        if not match_caso:
            continue
        
        numero = match_caso.group(1)
        match_estado = re.search(r'Estado: (✅|❌)', bloque)
        estado = match_estado.group(1) if match_estado else None
        
        precondiciones = []
        if 'PRECONDICIONES:' in bloque:
            seccion = bloque.split('PRECONDICIONES:')[1].split('Estado:')[0]
            lineas = [l.strip() for l in seccion.split('\n') if l.strip().startswith('-')]
            precondiciones = lineas
        
        casos.append({
            'numero': numero,
            'estado': estado,
            'precondiciones': precondiciones,
            'texto_completo': bloque
        })
    
    return casos


def normalizar_precondiciones(precondiciones: list) -> tuple:
    """Normaliza precondiciones para comparación."""
    normalized = []
    for p in precondiciones:
        texto = re.sub(r'[\u2705\u274c].*$', '', p)
        texto = re.sub(r'\s+', ' ', texto.strip().lower())
        if texto:
            normalized.append(texto)
    return tuple(sorted(normalized))


# ============================================================================
# FUNCIONES DE VALIDACIÓN
# ============================================================================
def validar_codigo(codigo: str, catalogo: set) -> bool:
    """Valida si código existe en catálogo."""
    return codigo in catalogo


def detectar_errores(contenido: str, catalogo: set) -> dict:
    """Detecta todos los errores en el archivo."""
    errores = {
        'codigos_invalidos': [],
        'palabras_duplicadas': [],
        'estados_incorrectos': []
    }
    
    bloques = contenido.split('---\n')
    
    for bloque in bloques:
        if not bloque.strip() or 'CASO' not in bloque:
            continue
        
        match_caso = re.search(r'CASO (\d+)', bloque)
        if not match_caso:
            continue
        numero = match_caso.group(1)
        
        # Extraer estado y precondiciones
        match_estado = re.search(r'Estado: (✅|❌)', bloque)
        estado = match_estado.group(1) if match_estado else None
        
        if 'PRECONDICIONES:' in bloque:
            seccion = bloque.split('PRECONDICIONES:')[1].split('Estado:')[0]
            lineas = [l.strip() for l in seccion.split('\n') if l.strip().startswith('-')]
            
            ok_count = sum(1 for p in lineas if '✅' in p and '❌Sin modelar' not in p)
            ko_count = sum(1 for p in lineas if '❌Sin modelar' in p)
            
            # Validar códigos
            for linea in lineas:
                codigos = re.findall(r'✅([A-Z_]+)', linea)
                for codigo in codigos:
                    if not validar_codigo(codigo, catalogo):
                        errores['codigos_invalidos'].append({
                            'caso': numero,
                            'codigo': codigo
                        })
                
                # Palabras duplicadas
                palabras = re.findall(r'\b\w+\b', linea.lower())
                for i, palabra in enumerate(palabras[:-1]):
                    if palabra == palabras[i+1] and len(palabra) > 3:
                        errores['palabras_duplicadas'].append({
                            'caso': numero,
                            'palabra': palabra
                        })
            
            # Validar estado
            if estado == '✅' and ko_count > 0:
                errores['estados_incorrectos'].append({
                    'caso': numero,
                    'estado_actual': '✅',
                    'estado_esperado': '❌'
                })
            elif estado == '❌' and ko_count == 0 and ok_count > 0:
                errores['estados_incorrectos'].append({
                    'caso': numero,
                    'estado_actual': '❌',
                    'estado_esperado': '✅'
                })
    
    return errores


# ============================================================================
# FUNCIONES DE CORRECCIÓN
# ============================================================================
def eliminar_duplicados(contenido: str) -> tuple:
    """Elimina casos con precondiciones duplicadas. Retorna (nuevo_contenido, eliminados)."""
    bloques = contenido.split('---\n')
    
    # Parsear casos
    casos_info = {}
    for bloque in bloques:
        if not bloque.strip() or 'CASO' not in bloque:
            continue
        match_caso = re.search(r'CASO (\d+)', bloque)
        if not match_caso:
            continue
        numero = match_caso.group(1)
        
        if 'PRECONDICIONES:' in bloque:
            seccion = bloque.split('PRECONDICIONES:')[1].split('Estado:')[0]
            lineas = [l.strip() for l in seccion.split('\n') if l.strip().startswith('-')]
            precs_normalized = normalizar_precondiciones(lineas)
            casos_info[numero] = precs_normalized
    
    # Agrupar por precondiciones
    duplicados = defaultdict(list)
    for numero, precs in casos_info.items():
        if precs:
            duplicados[precs].append(numero)
    
    # Identificar casos a eliminar (mantener número más bajo)
    casos_a_eliminar = set()
    for precs, numeros in duplicados.items():
        if len(numeros) > 1:
            numeros_sorted = sorted(numeros, key=int)
            casos_a_eliminar.update(numeros_sorted[1:])
    
    # Reconstruir sin duplicados
    nuevos_bloques = []
    for bloque in bloques:
        if not bloque.strip():
            continue
        match_caso = re.search(r'CASO (\d+)', bloque)
        if match_caso and match_caso.group(1) in casos_a_eliminar:
            continue
        nuevos_bloques.append(bloque)
    
    nuevo_contenido = '---\n'.join(nuevos_bloques)
    if not nuevo_contenido.endswith('\n'):
        nuevo_contenido += '\n'
    
    return nuevo_contenido, len(casos_a_eliminar)


# ============================================================================
# FUNCIÓN PRINCIPAL
# ============================================================================
def main():
    print("=" * 60)
    print("PROCESAMIENTO DE CASOS ICARIA")
    print("=" * 60)
    
    # Cargar archivos
    if not RUTA_CASOS.exists():
        print(f"ERROR: No se encuentra {RUTA_CASOS}")
        return
    
    contenido = leer_archivo(RUTA_CASOS)
    catalogo = cargar_catalogo(RUTA_CATALOGO)
    
    casos = parsear_casos(contenido)
    print(f"\nCasos cargados: {len(casos)}")
    print(f"Codigos en catalogo: {len(catalogo)}")
    
    # Detectar errores
    print("\n" + "-" * 40)
    print("VALIDACION")
    print("-" * 40)
    
    errores = detectar_errores(contenido, catalogo)
    
    print(f"Codigos invalidos: {len(errores['codigos_invalidos'])}")
    for err in errores['codigos_invalidos'][:5]:
        print(f"  CASO {err['caso']}: {err['codigo']}")
    
    print(f"Palabras duplicadas: {len(errores['palabras_duplicadas'])}")
    for err in errores['palabras_duplicadas'][:5]:
        print(f"  CASO {err['caso']}: '{err['palabra']}'")
    
    print(f"Estados incorrectos: {len(errores['estados_incorrectos'])}")
    for err in errores['estados_incorrectos'][:5]:
        print(f"  CASO {err['caso']}: {err['estado_actual']} -> {err['estado_esperado']}")
    
    # Buscar duplicados
    print("\n" + "-" * 40)
    print("DUPLICADOS")
    print("-" * 40)
    
    _, num_duplicados = eliminar_duplicados(contenido)
    print(f"Casos duplicados detectados: {num_duplicados}")
    
    total_errores = (len(errores['codigos_invalidos']) + 
                     len(errores['palabras_duplicadas']) + 
                     len(errores['estados_incorrectos']) +
                     num_duplicados)
    
    print("\n" + "=" * 60)
    print(f"TOTAL ERRORES/DUPLICADOS: {total_errores}")
    print("=" * 60)
    
    if total_errores > 0:
        respuesta = input("\n¿Corregir duplicados? (s/n): ").strip().lower()
        if respuesta == 's':
            backup_path = crear_backup(RUTA_CASOS)
            print(f"Backup creado: {backup_path.name}")
            
            nuevo_contenido, eliminados = eliminar_duplicados(contenido)
            escribir_archivo(RUTA_CASOS, nuevo_contenido)
            
            casos_finales = len(parsear_casos(nuevo_contenido))
            print(f"Duplicados eliminados: {eliminados}")
            print(f"Casos finales: {casos_finales}")


if __name__ == '__main__':
    main()
