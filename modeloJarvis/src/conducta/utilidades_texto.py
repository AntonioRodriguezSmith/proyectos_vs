"""
Utilidades de procesamiento y comprensión de texto para J.A.R.V.I.S.
Incluye funciones de resumen, análisis y manipulación de cadenas.
"""

def comprimir_texto(texto, max_palabras=50):
    """Devuelve un resumen del texto limitado a max_palabras palabras."""
    palabras = texto.split()
    if len(palabras) <= max_palabras:
        return texto
    return ' '.join(palabras[:max_palabras]) + '...'

# Aquí puedes añadir más funciones relacionadas con el diccionario o análisis de texto.
