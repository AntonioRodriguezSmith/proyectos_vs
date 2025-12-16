"""
Validadores para casos Icaria.
"""
from typing import List, Dict, Tuple


def validar_estado_caso(precondiciones: List[str], estado_actual: str) -> Tuple[bool, str]:
    """
    Valida si el estado del caso es correcto según sus precondiciones.
    
    Args:
        precondiciones: Lista de strings de precondiciones
        estado_actual: Estado actual del caso ('✅' o '❌')
    
    Returns:
        Tupla (es_valido, estado_correcto)
    """
    ok_count = sum(1 for p in precondiciones if '✅' in p)
    ko_count = sum(1 for p in precondiciones if '❌Sin modelar' in p)
    
    # Determinar estado correcto
    if ko_count > 0:
        estado_correcto = '❌'
    elif ok_count > 0:
        estado_correcto = '✅'
    else:
        return True, estado_actual  # No hay precondiciones, mantener estado
    
    es_valido = (estado_actual == estado_correcto)
    return es_valido, estado_correcto


def validar_codigo_icaria(codigo: str, catalogo: set) -> bool:
    """
    Valida si un código Icaria existe en el catálogo.
    
    Args:
        codigo: Código a validar
        catalogo: Set de códigos válidos
    
    Returns:
        True si el código es válido
    """
    return codigo in catalogo


def detectar_codigos_pegados(linea: str) -> bool:
    """
    Detecta si hay códigos pegados sin espacio (✅CODIGO1✅CODIGO2).
    
    Returns:
        True si detecta códigos pegados
    """
    import re
    # Buscar patrón ✅CODIGO✅CODIGO (sin espacio o separador)
    pattern = r'✅[A-Z_]+✅[A-Z_]+'
    return bool(re.search(pattern, linea))


def detectar_palabras_duplicadas(linea: str) -> List[str]:
    """
    Detecta palabras duplicadas consecutivas (ej: "documentos documentos").
    
    Returns:
        Lista de palabras duplicadas encontradas
    """
    import re
    duplicadas = []
    # Buscar palabras repetidas
    matches = re.finditer(r'\b(\w+)\s+\1\b', linea, re.IGNORECASE)
    for match in matches:
        duplicadas.append(match.group(1))
    return duplicadas


def detectar_errores_mayusculas(codigo: str) -> bool:
    """
    Detecta errores de mayúsculas en códigos (ej: PARAMETRIZado).
    
    Returns:
        True si tiene errores de mayúsculas
    """
    import re
    # Códigos deben ser todo mayúsculas y guiones bajos
    return bool(re.search(r'[a-z]', codigo))
