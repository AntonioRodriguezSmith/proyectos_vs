# Proyecto modeloJarvis

Repositorio remoto: <https://github.com/AntonioRodriguezSmith>

Este proyecto contiene el modelo independiente y reutilizable del asistente J.A.R.V.I.S. para integración en sistemas RAG o como microservicio.

## Estructura inicial

- /src: Código fuente del modelo y lógica de inferencia
- /api: Endpoints REST para exponer el modelo
- /data: Datos de entrenamiento y pruebas
- /tests: Pruebas unitarias y de integración
- /docs: Documentación técnica y ejemplos de uso

## Objetivos

- Permitir el entrenamiento, despliegue e integración sencilla del asistente J.A.R.V.I.S.
- Facilitar la reutilización como paquete o microservicio
- Mantener dependencias mínimas y documentación clara

## Próximos pasos

- Implementar lógica base del modelo
- Definir API REST
- Añadir ejemplos de integración

## Modos especiales de respuesta

Jarvis puede activar modos especiales de comportamiento según palabras clave en la entrada del usuario. Por ejemplo:

- **arrebatao**: activa el modo "la jumpa (Arcangel)", donde el asistente responde de forma más enérgica y directa.

El sistema está preparado para añadir más modos y nombres en el futuro. Consulta comportamientos_globales.md para detalles globales.

## Recursos compartidos

- Este asistente puede hacer uso del diccionario de expresiones ubicado en `../../modeloRagAlejandria/asistente_jarvis/diccionario.json` para personalizar respuestas y comportamientos.

## Ejecución universal de J.A.R.V.I.S

Puedes lanzar J.A.R.V.I.S. desde cualquier carpeta principal del monorepo ejecutando el script `run_jarvis.bat` ubicado en la raíz:

```
./run_jarvis.bat
```

Este script cambia automáticamente al directorio correcto y ejecuta el servidor.

---

## Gestión de tareas

- Las tareas propias de modeloJarvis deben guardarse en `tareas_pendientes.md` dentro del propio proyecto.
- El directorio central de tareas (`modeloRagAlejandria/knowledge_base/tareas/`) solo debe contener tareas globales o enlaces a los archivos de tareas locales de cada proyecto.
- Cuando se cree un nuevo proyecto, debe incluirse un archivo de tareas local y, opcionalmente, un README de tareas si el proyecto lo requiere por su complejidad o colaboración.

---

## Ejemplo de uso rápido

### 1. Ejecutar los tests

```bash
pytest tests
```

### 2. Lanzar el modelo como API REST

```bash
cd modeloJarvis
python api/main.py
```

### 3. Realizar una petición de ejemplo (usando curl)

```bash
curl -X POST "http://localhost:8000/infer" -H "Content-Type: application/json" -d '{"input": "Hola Jarvis"}'
```

---

## Automatización y CI

- El proyecto incluye un workflow de GitHub Actions en `.github/workflows/python-app.yml` que ejecuta los tests automáticamente en cada push o pull request.
- Si algún test falla, la integración se detiene y se notifica en GitHub.

---

## Badges de estado

Puedes añadir estos badges al inicio del README:

```
![Tests](https://github.com/AntonioRodriguezSmith/modeloJarvis/actions/workflows/python-app.yml/badge.svg)
```

---

## Troubleshooting

- Si los tests no se detectan, revisa la configuración de `pytest` y la estructura de carpetas.
- Si hay problemas de imports en VS Code, asegúrate de tener `.vscode/settings.json` con `python.analysis.extraPaths` configurado.
- Para errores de dependencias, ejecuta `pip install -r requirements.txt`.
- Consulta `CONTRIBUTING.md` para pautas de contribución y reporte de errores.
