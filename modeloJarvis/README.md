# Proyecto modeloJarvis

Repositorio remoto: https://github.com/AntonioRodriguezSmith

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

## Ejecución universal de J.A.R.V.I.S.

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
