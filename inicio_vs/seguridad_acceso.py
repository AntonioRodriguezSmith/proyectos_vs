"""
Políticas básicas de acceso y cifrado para datos sensibles.
Este módulo puede ampliarse según necesidades de seguridad.
"""
def cifrar_dato(dato):
    # Ejemplo simple (no seguro para producción)
    return ''.join(chr(ord(c)+1) for c in dato)

def descifrar_dato(dato):
    return ''.join(chr(ord(c)-1) for c in dato)
