# Metodología y Procesos de Trabajo

Este documento consolida la metodología para la toma de decisiones y el modelado colaborativo dentro de cualquier proyecto.

---
## 1. Taxonomía y Ámbito de las Decisiones

Para mantener el conocimiento organizado y reutilizable, las decisiones del proyecto se clasifican según su **ámbito de aplicación** y su **tipo**.

### 1.1. Ámbito de Aplicación

La primera pregunta al tomar una decisión es: **"¿A quién afecta?"**

- **Ámbito Global:** Afecta a **todos los proyectos** dentro del entorno. Son las "leyes federales" que garantizan la consistencia global.
- **Ámbito de Proyecto Específico:** Afecta **únicamente a un proyecto o subdominio**. Son las "leyes locales" que resuelven problemas concretos de un dominio.

### 1.2. Tipos de Decisión

Cada decisión, independientemente de su ámbito, se clasifica en una de las siguientes categorías:

- **Arquitectura (`ARQ-`):** Decisiones de alto nivel sobre la estructura y comportamiento del sistema.
- **Datos (`DAT-`):** Decisiones relacionadas con el modelo de datos, la estructura de la base de datos y el ciclo de vida de la información.
- **Transversales (`TRN-`):** Estándares y convenciones globales para asegurar la consistencia.
- **Dominio de Negocio (`DOM-`):** Mapeo de un concepto de negocio específico a una entidad del sistema.
- **Metodología (`MET-`):** Reglas sobre nuestra forma de trabajar y gobernar el conocimiento.

### 1.3. Contenido Mínimo y Metadatos

Todo archivo de decisión (`.md`) deberá contener una cabecera de metadatos en formato **YAML Front Matter**. Esta cabecera es esencial para la automatización, la indexación y la auditoría.

El bloque YAML deberá contener, como mínimo, las siguientes claves:

```yaml
---
id: "[TIPO]-[CONTEXTO]-C[XX]-[ID]"
title: "Título Descriptivo de la Decisión"
status: "draft" # Opciones: draft, approved, deprecated
date: "YYYY-MM-DD"
tags: ["etiqueta1", "etiqueta2"]
reference: "Fuente de la decisión (Libro, Artículo, etc.)" # Opcional
impact: "medium" # Opciones: critical, high, medium, low
category: "Categoría de Alto Nivel (ej. Diseño Estratégico)"
---
```
-   **id**: El identificador único del ADR, que debe coincidir con el nombre del archivo (sin la descripción).
-   **title**: El título completo y descriptivo de la decisión.
-   **status**: El estado actual de la decisión en su ciclo de vida.
-   **date**: La fecha de la última modificación significativa.
-   **tags**: Una lista de etiquetas para facilitar la búsqueda.
-   **reference**: El origen o la inspiración de la decisión (opcional).
-   **impact**: El nivel de criticidad o influencia de la decisión.
-   **category**: Una clasificación funcional para agrupar decisiones similares.

### 1.4. Nomenclatura de Archivos

Para asegurar la trazabilidad y la organización, los nombres de los archivos de decisión seguirán un formato estricto:

**`[TIPO]-[CONTEXTO]-C[CAPÍTULO]-[ID]_[Nombre_Descriptivo].md`**

-   **[TIPO]:** `ARQ`, `DAT`, `TRN`, `DOM`, `MET`.
-   **[CONTEXTO]:** El framework o proyecto al que pertenece (ej. `DDD`, `DV`, `IGC`).
-   **[CAPÍTULO]:** El número del capítulo del libro de referencia (`C01`, `C13`). Usar `C00` si la decisión no está vinculada a un capítulo específico.
-   **[ID]:** Un número secuencial de tres dígitos (ej. `001`, `002`).
-   **[Nombre_Descriptivo]:** Un nombre en `Pascal_Case` que resuma la decisión.

### 1.5. Estructura de Almacenamiento

Las decisiones se almacenan en una estructura de carpetas que refleja su ámbito y tipo:

```
/entornos/
└── ENTORNO/
    ├── decisiones_globales/
    │   ├── arquitectura/
    │   ├── transversales/
    │   └── metodologia/
    └── projects/
        └── PROYECTO/
            └── docs/
                └── decisiones/
                    ├── arquitectura/
                    ├── transversales/
                    ├── dominio/
                    └── metodologia/
```

---

## 2. Ciclo de Vida de una Decisión Arquitectónica

Las decisiones no son estáticas; evolucionan con el tiempo y el contexto. Se reconocen los siguientes estados, que deben ser reflejados en el campo `status` de los metadatos YAML:

- **Borrador (`draft`):** La decisión está en proceso de definición y aún no ha sido aprobada para su implementación.
- **Aprobado (`approved`):** La decisión ha sido aceptada y es la guía a seguir.
- **Desaprobado (`deprecated`):** La decisión ha sido reemplazada por una nueva y ya no debe aplicarse.

El proceso de resolución se basará en la consulta de los ADRs con estado `approved`.

---

## 3. Patrón para una Conversación de Modelado Exitosa

Para asegurar que las conversaciones de modelado sean productivas, se sigue un patrón colaborativo:

1.  **Planteamiento del Problema (Usuario):** El usuario describe el reto o la entidad a modelar.
2.  **Análisis Contextual (IA):** La IA hace preguntas clave para entender el contexto.
3.  **Propuesta Múltiple (IA):** La IA presenta 2-3 opciones viables, explicando los pros y contras de cada una.
4.  **Refinamiento y Colaboración (Usuario + IA):** Este es el paso más importante. El usuario aporta su conocimiento del negocio y las realidades técnicas para refinar, corregir o mejorar la propuesta de la IA. Es una construcción iterativa.
5.  **Documentación Final (IA):** Una vez alcanzada la solución óptima, la IA documenta la decisión final, incluyendo el contexto, la justificación y ejemplos.

La clave del éxito es la **colaboración activa**, donde ni el usuario ni la IA imponen su idea inicial, sino que construyen juntos una solución superior. 