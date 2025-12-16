# 🧠 Contexto Maestro del Sistema: Bayton Dental OS

> **USO:** Copia y pega este documento junto con las "Instrucciones Maestras" para dar a tu IA un conocimiento profundo de las capacidades del software.

---

## 1. ¿QUÉ ES ESTE SOFTWARE?
No es un simple ERP. Es un **Sistema Operativo Clínico (Clinical OS)** basado en procesos guiados.
A diferencia de los programas tradicionales (Gesden, Dentras) que son "bases de datos pasivas", este software es **proactivo**: guía al usuario paso a paso y hace cumplir las reglas del negocio.

### Filosofía Central: "Fractal UI"
El sistema visualiza la clínica como niveles de profundidad (zoom):
*   **Nivel 0 (Clínica):** Visión global, Agenda, Sala de Espera.
*   **Nivel 1 (Paciente):** "Timeline" de visitas.
*   **Nivel 2 (Visita):** "Tablero" de fases (Recepción > Gabinete > Salida).
*   **Nivel 3 (Tarea):** La acción concreta (Firmar, Radiografía).

---

## 2. CAPACIDADES ACTUALES (Módulos)

### 🏥 Módulo Clínico (Process Engine)
*   **Motor de Procesos:** Ejecuta recetas predefinidas (PV-01, Revisión, Cirugía).
*   **Historia Clínica:** No es texto plano. Es una secuencia de eventos estructurados.
*   **Pruebas:** Soporta formularios, checklists, subida de fotos y visores DICOM (RX/CBCT).

### 💰 Módulo Financiero (Billing & Sales)
*   **Presupuestos Inteligentes (EP-01):**
    *   Sabe distinguir Fases: **Salud** (Prioritaria) > **Función** > **Estética**.
    *   Oculta precios futuros en casos complejos (`CaseDifficulty`).
*   **Gestión de Cobro:** Facturación directa vinculada a la finalización de tareas.
*   **Pipeline de Ventas (SG-01):** Tablero Kanban para seguimiento de pacientes indecisos ("Lo Piensa").

### 📅 Módulo Operativo (Agenda & HR)
*   **Agenda:** Vinculada a la duración real de los procesos.
*   **RRHH:** Control de fichaje y permisos por rol (Dr, Aux, Recep).

### 📦 Módulo Logístico (Stocks)
*   **BOM (Bill of Materials):** Vincula servicios con consumo de material (V1).

---

## 3. REGLAS DE ORO DEL SISTEMA (Constraints)

Si vas a diseñar un nuevo proceso, debes respetar estas reglas:

1.  **Principio de Atomicidad:**
    *   Todo lo que ocurre en la clínica DEBE ser parte de un Proceso. No existen "acciones sueltas".
    *   Si quieres cobrar algo, debe haber una tarea "Cobrar" dentro de un proceso.

2.  **Principio de Inmutabilidad Clínica:**
    *   Una vez firmado un consentimiento o cerrada una visita, no se puede editar. Se debe crear un "Proceso de Rectificación".

3.  **Principio de Rol:**
    *   Cada tarea tiene un dueño. Una Recepcionista no puede completar una tarea marcada para `DOCTOR`.

---

## 4. VOCABULARIO (Glosario Técnico)

Usa estos términos con precisión:

*   **Process Template:** La receta teórica (ej. "Protocolo de Implante").
*   **Process Execution:** La realidad de un paciente hoy (ej. "El implante de Juan a las 10:00").
*   **Treatment Plan:** La propuesta económica y clínica. Tiene estados: `DRAFT`, `QUOTED` (Lo Piensa), `APPROVED`.
*   **Conversion Pipeline:** El tablero donde se persigue la venta.

---

## 5. CÓMO DISEÑAR PARA ESTE SISTEMA

Cuando propongas una mejora o proceso, piensa en **Flujos, no en Pantallas**.

*   ❌ **MAL:** "Quiero una pantalla para pedir implantes".
*   ✅ **BIEN:** "Quiero añadir una tarea 'Solicitar Implante' en la Fase de Preparación del proceso de Cirugía".

El sistema se encarga de pintar la pantalla. Tú define el **Proceso**.

