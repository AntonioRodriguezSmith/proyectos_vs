# Guía de contribución

Por favor, sigue las normas de estilo y buenas prácticas del proyecto. Toda contribución debe ir acompañada de tests y documentación.

## Requisitos mínimos

- Código en español, claro y documentado.
- Sigue la estructura modular definida en `docs/buenas_practicas_modularidad.md`.
- Usa imports relativos al paquete (no rutas absolutas).
- No dupliques recursos ni lógica entre módulos.
- Añade o actualiza los tests automáticos en la carpeta `tests/`.
- Ejecuta los tests antes de cada commit:

  ```sh
  pytest tests
  ```

- Si añades recursos (JSON, plantillas, etc.), colócalos en la subcarpeta `recursos/` del módulo correspondiente.
- Si añades documentación, usa español y colócala en la subcarpeta `docs/` del módulo o en `docs/` global.

## Ejemplo de estructura

```
modeloJarvis/
├── src/
│   ├── conducta/
│   │   ├── agente.py
│   │   ├── recursos/
│   │   └── docs/
│   ├── agr/
│   │   ├── agente_agr.py
│   │   └── docs/
│   └── jarvis_model.py
├── tests/
│   ├── test_jarvis_model.py
│   └── ...
├── docs/
│   └── buenas_practicas_modularidad.md
└── ...
```

## Troubleshooting

- Si ves errores de importación en VS Code, asegúrate de tener en `.vscode/settings.json`:

  ```json
  {
    "python.analysis.extraPaths": ["./modeloJarvis/src"]
  }
  ```

- Si los tests no se detectan, revisa que los archivos y funciones empiecen por `test_` y ejecuta pytest desde la raíz del proyecto.

¡Gracias por contribuir y mantener la calidad del proyecto!
