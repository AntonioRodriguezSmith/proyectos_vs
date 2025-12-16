"""
Funciones de ayuda para el proyecto
"""

import os
from datetime import datetime

def obtener_ruta_entrada():
    '''Devuelve la ruta absoluta a data/entrada'''
    return os.path.join(os.getcwd(), "data", "entrada")

def obtener_ruta_salida():
    '''Devuelve la ruta absoluta a data/salida'''
    return os.path.join(os.getcwd(), "data", "salida")

def crear_nombre_archivo(base, extension):
    '''
    Crea un nombre de archivo con timestamp
    
    Args:
        base: nombre base del archivo
        extension: extension (.txt, .csv, etc.)
    
    Returns:
        str: nombre con timestamp
    '''
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"{base}_{timestamp}{extension}"

def listar_archivos_entrada(extension=None):
    '''
    Lista archivos en data/entrada
    
    Args:
        extension: filtro de extension (ej: '.txt', '.xlsx')
    
    Returns:
        list: rutas de archivos
    '''
    entrada_dir = obtener_ruta_entrada()
    
    if not os.path.exists(entrada_dir):
        return []
    
    archivos = []
    for archivo in os.listdir(entrada_dir):
        ruta_completa = os.path.join(entrada_dir, archivo)
        if os.path.isfile(ruta_completa):
            if extension:
                if archivo.lower().endswith(extension.lower()):
                    archivos.append(ruta_completa)
            else:
                archivos.append(ruta_completa)
    
    return archivos
