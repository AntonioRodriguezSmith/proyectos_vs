# Instrucciones de uso y troubleshooting (backup)

## Estructura y automatización

- El modelo principal está en src/jarvis_model.py
- La API REST se expone desde api/main.py (FastAPI)
- Los recursos (modos, patrones, diccionario) están en src/conducta/recursos/
- Los tests automáticos están en tests/ y se ejecutan con pytest
- El workflow de CI está en .github/workflows/python-app.yml

## Ejemplo de uso rápido

1. Ejecutar tests:

   ```bash
   pytest tests
   ```

2. Lanzar API:

   ```bash
   cd modeloJarvis
   python api/main.py
   ```

3. Petición de ejemplo:

   ```bash
   curl -X POST "http://localhost:8000/infer" -H "Content-Type: application/json" -d '{"input": "Hola Jarvis"}'
   ```

## Troubleshooting

- Si los tests no se detectan, revisa pytest y la estructura de carpetas
- Si hay problemas de imports en VS Code, revisa .vscode/settings.json
- Para errores de dependencias, ejecuta pip install -r requirements.txt
