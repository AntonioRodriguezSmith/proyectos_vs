# Buenas Prácticas de Modularidad e Integración en modeloJarvis

## Estructura recomendada

- Cada módulo (por ejemplo, `conducta`, `agr`) debe ser un paquete Python con su propio `__init__.py` (vacío o solo con docstring descriptivo).
- Los recursos y documentación específica de cada módulo deben estar en subcarpetas internas (`recursos/`, `docs/`).
- Los archivos de recursos (JSON, plantillas, etc.) nunca deben estar duplicados entre módulos.
- La documentación general y de integración debe estar en la carpeta `docs/` raíz del proyecto.
- El punto de entrada (`main_jarvis.py`) debe importar solo las clases públicas de cada módulo.
- Los imports deben ser relativos al paquete, nunca rutas absolutas del sistema.
- No debe haber lógica en los `__init__.py`, solo docstrings o inicialización mínima de paquete.

## Ejemplo de integración modular

```python
# src/main_jarvis.py
from jarvis_model import JarvisModel

if __name__ == "__main__":
    jarvis = JarvisModel()
    print("J.A.R.V.I.S. iniciado. Escribe tu mensaje (Ctrl+C para salir):")
    while True:
        try:
            entrada = input("Usuario: ")
            respuesta = jarvis.inferir(entrada)
            print("JARVIS:", respuesta)
        except KeyboardInterrupt:
            print("\nSaliendo de J.A.R.V.I.S.")
            break
```

```python
# src/jarvis_model.py
from conducta.agente import AgenteConducta
from agr.agente_agr import AgenteAGR

class JarvisModel:
    def __init__(self):
        self.conducta = AgenteConducta()
        self.agr = AgenteAGR()
        self.modo_activo = None
    def entrenar(self, datos):
        self.agr.entrenar(datos)
    def inferir(self, entrada):
        respuesta_conducta, modo = self.conducta.inferir(entrada)
        if modo:
            self.modo_activo = modo
            return respuesta_conducta
        self.modo_activo = None
        return self.agr.inferir(entrada)
```

- Cada módulo puede tener su propia lógica, recursos y documentación, pero la integración siempre se hace a través de clases públicas y rutas relativas.
- Los tests y scripts de utilidad deben estar en carpetas separadas (`tests/`, `scripts/`).

## Resumen de la estructura actual

- `src/conducta/` y `src/agr/` son paquetes autocontenidos.
- `src/conducta/recursos/` y `src/conducta/docs/` contienen los recursos y documentación del módulo de conducta.
- `src/agr/` contiene la lógica y pruebas del módulo AGR.
- No hay duplicados de recursos ni lógica en los `__init__.py`.
- La documentación general está en `docs/` y la específica en cada módulo.

---

Esta estructura garantiza mantenibilidad, escalabilidad y claridad en la integración de nuevos módulos o recursos.

& .venv\Scripts\Activate.ps1
