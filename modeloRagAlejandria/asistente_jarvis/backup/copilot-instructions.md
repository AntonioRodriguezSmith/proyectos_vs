# Instrucciones para agentes de IA y desarrolladores (backup)

## Propósito y arquitectura

-   Este proyecto es un modelo independiente y reutilizable del asistente J.A.R.V.I.S., pensado para integrarse como microservicio, API REST o paquete en sistemas RAG.
-   La lógica principal está en src/jarvis_model.py. La API se expone desde api/main.py usando FastAPI.
-   La documentación y ejemplos están en docs/.

## Convenciones y flujos clave

-   Mantén la modularidad: separa lógica de modelo, API, datos y pruebas.
-   Antes de crear/modificar archivos estructurales, confirma con el usuario si hay dudas.
-   Usa nombres descriptivos y comentarios claros, especialmente en métodos de inferencia y entrenamiento.
-   Los tests deben estar en tests/ y cubrir casos básicos de inferencia.
-   Documenta cualquier cambio relevante en README.md y docs/.

## Ejemplos y buenas prácticas

-   Para exponer nuevas rutas en la API, sigue el patrón de api/main.py.
-   Para ampliar el modelo, hereda o extiende JarvisModel en src/.
-   Usa requirements.txt para dependencias y mantenlo actualizado.

## Archivos clave

-   README.md: Descripción general y objetivos
-   src/jarvis_model.py: Lógica principal del modelo
-   api/main.py: API REST
-   tests/: Pruebas unitarias
-   docs/: Documentación y ejemplos
-   requirements.txt: Dependencias

## Notas finales

-   Mantén la documentación clara y actualizada.
-   Si el modelo evoluciona, considera versionar releases y documentar breaking changes.
-   Si integras con otros sistemas, añade ejemplos en docs/integracion.md.
