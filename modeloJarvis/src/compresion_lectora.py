"""
Módulo de comprensión lectora para J.A.R.V.I.S.
Permite analizar, resumir y extraer patrones de comunicación de los mensajes del usuario.
"""
def comprimir_texto(texto, max_palabras=50):
    """Devuelve un resumen del texto limitado a max_palabras palabras."""
    palabras = texto.split()
    if len(palabras) <= max_palabras:
        return texto
    return ' '.join(palabras[:max_palabras]) + '...'

if __name__ == "__main__":
    ejemplo = (
        "J.A.R.V.I.S. debe ser capaz de analizar y resumir mensajes largos para extraer la idea principal, "
        "identificar patrones de comunicación y mejorar la interacción con el usuario."
    )
    print(comprimir_texto(ejemplo, max_palabras=20))
