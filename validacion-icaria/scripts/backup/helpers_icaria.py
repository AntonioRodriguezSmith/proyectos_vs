"""
Funciones auxiliares extendidas para procesar casos Icaria.
"""
import re
from pathlib import Path
from typing import List, Dict, Tuple


def leer_casos(filepath: Path) -> str:
    """Lee el archivo de casos con encoding UTF-8."""
    return filepath.read_text(encoding='utf-8')


def escribir_casos(filepath: Path, contenido: str) -> None:
    """Escribe el contenido al archivo con encoding UTF-8."""
    filepath.write_text(contenido, encoding='utf-8')


def parsear_casos(contenido: str) -> List[Dict]:
    """
    Parsea el contenido y devuelve lista de casos estructurados.
    
    Returns:
        Lista de diccionarios con: numero, precondiciones, estado, texto_completo
    """
    bloques = contenido.split('---\n')
    casos = []
    
    for bloque in bloques:
        if not bloque.strip() or 'CASO' not in bloque:
            continue
        
        # Extraer número de caso
        match_caso = re.search(r'CASO (\d+)', bloque)
        if not match_caso:
            continue
        
        numero = match_caso.group(1)
        
        # Extraer estado
        match_estado = re.search(r'Estado: (✅|❌)', bloque)
        estado = match_estado.group(1) if match_estado else None
        
        # Extraer precondiciones
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


def contar_estados(precondiciones: List[str]) -> Tuple[int, int]:
    """
    Cuenta precondiciones OK (✅) y KO (❌Sin modelar).
    
    Returns:
        Tupla (ok_count, ko_count)
    """
    ok_count = sum(1 for p in precondiciones if '✅' in p)
    ko_count = sum(1 for p in precondiciones if '❌Sin modelar' in p)
    return ok_count, ko_count


def extraer_codigos(linea: str) -> List[str]:
    """Extrae todos los códigos Icaria (✅CODIGO) de una línea."""
    return re.findall(r'✅([A-Z_]+)', linea)


def cargar_catalogo(catalogo_file: Path) -> set:
    """Carga el catálogo de códigos Icaria válidos."""
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


def crear_backup(filepath: Path) -> Path:
    """Crea un backup del archivo con timestamp."""
    from datetime import datetime
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_path = filepath.parent / f'{filepath.stem}_backup_{timestamp}{filepath.suffix}'
    backup_path.write_text(filepath.read_text(encoding='utf-8'), encoding='utf-8')
    return backup_path
