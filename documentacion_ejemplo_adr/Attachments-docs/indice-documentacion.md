# Índice de Documentación

Este documento proporciona un mapa completo de toda la documentación del proyecto, organizada según su propósito y ámbito.

---

## 🗺 Estructura General

### 1. 🚀 **Gobernanza del Conocimiento (`/docs/00_gobernanza_conocimiento`)**

Contiene la metodología y los procesos agnósticos que definen CÓMO trabajamos. Este es el "sistema operativo" de nuestro sistema colaborativo.

- **[Metodología y Procesos](./01_metodologia_decisiones.md):** El documento central que define nuestro flujo de conversación, el ciclo de vida de las decisiones y la taxonomía de las mismas.

### 2. 🧠 **Framework Data Vault 2.0 (`/docs/01_frameworks_tecnicos/datavault_2.0`)**

El conocimiento específico de Data Vault y su implementación:

- **[Estándares Data Vault](../01_frameworks_tecnicos/datavault_2.0/estandares_datavault.md):** Guías y estándares específicos del framework.
- **Decisiones (`../01_frameworks_tecnicos/datavault_2.0/conocimiento_base/decisiones/`):** El núcleo de la base de conocimiento.
- **[Decisiones del Libro Oficial](../01_frameworks_tecnicos/datavault_2.0/conocimiento_base/decisiones_libro_oficial/):** El "canon" basado en los estándares de Dan Linstedt.
- **[Casos de Estudio](../01_frameworks_tecnicos/datavault_2.0/conocimiento_base/casos-de-estudio/):** Análisis detallados de problemas de modelado específicos.
- **[Conversaciones de Ejemplo](../01_frameworks_tecnicos/datavault_2.0/conocimiento_base/conversaciones-ejemplo/):** Transcripciones de flujos de trabajo de modelado que sirven como material de aprendizaje.

### 3. 🛠 **Frameworks de Desarrollo (`/docs/01_frameworks_tecnicos`)**

Documentación técnica de las tecnologías base:

- **[DDD (Domain-Driven Design)](../01_frameworks_tecnicos/ddd/indice_maestro.md):** Índice maestro de patrones y decisiones DDD.
- **[Vaadin Flow](../01_frameworks_tecnicos/vaadin_flow/README.md):** Guías de UI, componentes y arquitectura Frontend.
  - **[Arquitectura Clean Vaadin](../01_frameworks_tecnicos/vaadin/ARQ-GLOBAL-VAADIN-001_Arquitectura_Clean_Vaadin.md):** Reglas arquitectónicas y patrones de implementación.

### 4. 🎯 **Entornos y Proyectos (`/docs/02_entornos`)**

La implementación práctica en entornos específicos:

#### EDW Global

- **[Decisiones Globales](../02_entornos/EDW_Global/decisiones_globales/):** Decisiones que afectan a todo el EDW.
  - Arquitectura
  - Transversales
  - Metodología

#### Proyecto IGC

- **[Documentación](../02_entornos/EDW_Global/projects/IGC/docs/):** Documentación específica del proyecto.
  - Decisiones de Dominio
  - Decisiones de Arquitectura
- **[Implementación](../02_entornos/EDW_Global/projects/IGC/):** Código y artefactos.
  - Modelos
  - Scripts
  - Datos

## 📚 Documentos Clave

1. [**Punto de Partida**](../00_PUNTO_DE_PARTIDA.md): Visión general del proyecto
2. [**Documentación Unificada**](./documentacion-unificada.md): La guía maestra
3. [**Base de Conocimiento**](./base-conocimiento-integracion.md): Cómo gestionamos el conocimiento
4. [**Requerimientos**](./requerimientos-datavault-ia.md): Especificaciones funcionales
5. [**Plan de Pruebas**](./plan-pruebas-detallado.md): Validación y calidad 