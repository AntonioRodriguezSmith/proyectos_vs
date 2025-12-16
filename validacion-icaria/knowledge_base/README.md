# Knowledge Base - ICARIA Precondiciones

Base de conocimiento para el procesamiento de casos de prueba ICARIA.

## 📊 Estado Actual

| Métrica | Valor |
|---------|-------|
| Casos procesados | 4,044 |
| Casos únicos | 1,481 (36.6%) |
| Duplicados eliminados | 2,521 (62.3%) |
| Casos finales | 1,327 |
| Precondiciones OK | 76.2% |
| Precondiciones KO | 23.8% |

## Estructura

```text
knowledge_base/
├── adr/                    # Architecture Decision Records
│   ├── 001-separacion-tipo-persona-contrato.md
│   ├── 002-codigos-huerfanos.md
│   ├── 003-eliminacion-duplicados.md
│   └── 004-analisis-duplicados-consolidacion.md  # NUEVO
├── patterns/               # Patrones de corrección aprendidos
│   ├── texto_a_codigo.json
│   └── correcciones_linea.json
├── mappings/               # Mapeos de texto a códigos ICARIA
│   └── codigos_icaria.md
├── validations/            # Reglas de validación
│   └── reglas.md
└── casos_y_duplicados.md   # Mapeo original → duplicados
```

## ADRs (Architecture Decision Records)

| ADR | Título | Estado |
|-----|--------|--------|
| 001 | Separación tipo persona/contrato | ✅ Aceptado |
| 002 | Códigos huérfanos | ✅ Aceptado |
| 003 | Eliminación de duplicados | ✅ Aceptado |
| 004 | Análisis duplicados y consolidación | ✅ Aceptado |

## Uso

Esta base de conocimiento sirve como contexto para un modelo RAG que:

1. Detecta patrones incorrectos en precondiciones
2. Sugiere correcciones basadas en decisiones previas
3. Aplica mapeos consistentes de texto a códigos ICARIA
4. Identifica duplicados automáticamente
5. Prioriza conceptos sin modelar por frecuencia

## Prioridades de Modelado

### 🔴 Alta (>15 repeticiones)

- BIZUM (56 casos)
- Cuenta de valores (50 casos)
- Dispositivo enrolado (35 casos)

### 🟡 Media (5-15 repeticiones)

- ETF/Valores (22 casos)
- Transferencias SEPA (25 casos)

### 🟢 Baja (<5 repeticiones)

- Otros conceptos (1135 casos)
