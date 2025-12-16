# Diagrama de flujo de información - Atenas

```mermaid
graph TD;
    Registro[Nomenclatura nueva] -->|Atenas.py| Estructura[Creación de estructura de carpetas y archivos]
    Estructura -->|Actualiza| Datos[Nomenclaturas (json/md)]
    Datos -->|Sincroniza| README[README y documentación]
    Datos -->|Referencia| ADR[ADR y decisiones]
    Estructura -->|Recursos| Recursos[Recursos globales indexados]
    Recursos -->|Indexa| Datos
```

Este diagrama representa el flujo principal de información y automatización gestionado por el script Atenas en el proyecto informes_ejecutivos.