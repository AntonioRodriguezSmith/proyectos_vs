# Perfiles y seguridad en modeloJarvis

Este proyecto soporta diferentes perfiles de entorno:
- DXC (alta seguridad, auditoría, API restringida)
- MTP (seguridad media, API expuesta)
- ASR (seguridad baja, API expuesta)

El perfil activo se define en config.json y puede ser consultado o modificado por los scripts del modelo.

## Ejemplo de uso en Python

```python
from src.perfil import obtener_perfil_activo, restricciones_perfil

perfil = obtener_perfil_activo()
restricciones = restricciones_perfil(perfil)
print(f"Perfil: {perfil}, Restricciones: {restricciones}")
```

## Advertencias
- En DXC, no expongas la API públicamente ni uses datos sensibles sin anonimizar.
- Cambia el perfil solo si tienes autorización y documenta cualquier modificación.
