# ADR-004: Análisis de Duplicados y Consolidación de Casos

## Estado
✅ Aceptado

## Fecha
12 de diciembre de 2025

## Contexto

Durante el procesamiento masivo de casos de prueba ICARIA, se detectó un alto número de duplicados y casos que requieren revisión manual. Este ADR documenta las decisiones tomadas para el tratamiento de duplicados y la consolidación del dataset.

## Decisión

### Estadísticas del Procesamiento

| Métrica | Valor | Porcentaje |
|---------|-------|------------|
| **Total casos procesados** | 4044 | 100% |
| **Casos únicos** | 1481 | 36.6% |
| **Casos duplicados** | 2521 | 62.3% |
| **Casos para revisar** | 42 | 1.0% |

### Reducción Final

Después del proceso de deduplicación:
- **Antes**: 4044 casos
- **Después**: 1327 casos únicos validados
- **Reducción**: 67.2%

## Filtros KO - Conceptos Sin Modelar

### TOP 20 Conceptos Sin Modelar (Frecuencia de Repetición)

| # | Concepto | Repeticiones | Prioridad |
|---|----------|--------------|-----------|
| 1 | Disponer de un usuario enrolado en BIZUM | 29 | 🔴 Alta |
| 2 | Con cuenta de valores | 18 | 🔴 Alta |
| 3 | Tiene que estar enrolado con un dispositivo | 15 | 🔴 Alta |
| 4 | E intención de compra de activo ETF con doc kid | 13 | 🟡 Media |
| 5 | El dispositivo debe tener la versión anterior instalada | 12 | 🟡 Media |
| 6 | Que disponga de contrato de valores y movimientos | 10 | 🟡 Media |
| 7 | Disponer de cuenta asociada a Bizum | 10 | 🔴 Alta |
| 8 | Que disponga de una cuenta de valores | 10 | 🟡 Media |
| 9 | Permisos de actuar | 10 | 🟡 Media |
| 10 | Destino fuera de ESP dentro de SEPA | 9 | 🟢 Baja |
| 11 | El usuario debe tener contactos asociados a su número | 9 | 🟢 Baja |
| 12 | E intención de compra de activo ETF sin doc kid | 9 | 🟡 Media |
| 13 | Beneficiario dado de alta para transferencias | 8 | 🟡 Media |
| 14 | Usuario con al menos un préstamo | 8 | 🟡 Media |
| 15 | Préstamo preconcedidos con intervinientes | 8 | 🟡 Media |
| 16 | Usuario debe haber entrado en BSO | 7 | 🟢 Baja |
| 17 | Teléfono del cliente destinatario Bizum | 7 | 🔴 Alta |
| 18 | Contrato de avisos y alertas activo | 6 | 🟢 Baja |
| 19 | Tarjeta de crédito con movimientos | 6 | 🟢 Baja |
| 20 | Cuenta sin saldo suficiente | 5 | 🟢 Baja |

### Agrupación por Categoría

| Categoría | Casos KO | % del Total |
|-----------|----------|-------------|
| **BIZUM** | 56 | 4.3% |
| **Valores/ETF** | 50 | 3.8% |
| **Dispositivo/App** | 35 | 2.7% |
| **Transferencias SEPA** | 25 | 1.9% |
| **Préstamos** | 16 | 1.2% |
| **Otros** | 1135 | 86.1% |
| **TOTAL KO** | **1317** | **100%** |

## Códigos ICARIA - Estado Actual

### Códigos Más Utilizados (TOP 10)

| Código | Frecuencia | Descripción |
|--------|------------|-------------|
| ES_PERSONA_FISICA | 1164 | Usuario particular |
| TIENE_BANCA_A_DISTANCIA | 778 | Contrato BD activo |
| TIPO_DE_FIRMA_DIGITAL_BSO | 444 | VTPC1/VTPC2/VTPC3 |
| ES_PERSONA_JURIDICA | 374 | Usuario empresa |
| TIENE_BANCA_A_DISTANCIA_EMPRESA | 334 | BD tipo empresa |
| TIENE_CUENTA_VISTA | 270 | Cuenta a la vista |
| TIENE_TARJETA_PAGO_ACTIVA | 173 | Tarjeta activa |
| TIPO_SALDO_DV_PARAMETRIZADO | 126 | Con saldo |
| TIENE_MOVIMIENTOS_EN_CUENTA | 86 | Movimientos recientes |
| ES_TITULAR_ACTIVO_AVISOS_ALERTAS | 63 | Contrato avisos |

### Códigos Sin Usar (27 de 67)

```
ES_AUTONOMO_TARJ_ENTREGADA_VIGENTE_ACT
ES_PERSONA_FISICA_RESIDENTE
ES_PERSONA_MAYOR_18
ES_PERSONA_VIVA
NO_IDENTIFICACION_DIGITALIZADA
NO_TIENE_CUENTA_CIALP
NO_TIENE_LINEA_EXPANSION_ACTIVA
NO_TIENE_PLAN_DE_PENSIONES
SI_IDENTIFICACION_DIGITALIZADA
SI_TIENE_TELF_INFORMADO_PERSONA
TIENE_BANCA_A_DISTANCIA_PLAN_PENSIONES
TIENE_CONTRATOS_ACTIVOS_CON_TRABAS
TIENE_CUENTA_VISTA_INACTIVA
TIENE_FIRMA_EN_CONTRATO
TIENE_IGUAL_CUENTAS_VISTA_PARAMETRO
TIENE_IGUAL_TARJETAS_PAGO_ACTIVA
TIENE_IGUAL_X_CUENTAS_VISTA_EMPRESA
TIENE_IGUAL_X_LINEAS_EXPANSION
TIENE_MENOS_DE_X_CUENTAS_VISTA_EMPRESA
TIENE_MENOS_DE_X_TARJETAS_PAGO_ACTIVA
TIENE_MOVIMIENTOS_CUENTA_FECHA
TIENE_MOVIMIENTOS_X_DIAS
TIENE_TARJETA_MOVIMIENTO_CONFIRMADO
TIENE_TARJETA_MOVIMIENTO_PENDIENTE
TIENE_TIPO_APLICACION_MOVIL_TARJETA
TIENE_TIPO_MOVIMIENTO_CUENTA
TIPO_DE_IDENTIFICACION
```

## Consecuencias

### Positivas
- ✅ Reducción del 67% en casos a mantener
- ✅ Identificación clara de 1317 conceptos sin modelar
- ✅ Priorización de trabajo futuro (BIZUM, Valores, Dispositivo)
- ✅ Base de conocimiento documentada para RAG

### Negativas
- ⚠️ 42 casos requieren revisión manual
- ⚠️ 27 códigos del catálogo sin uso (posible obsolescencia)
- ⚠️ 23.8% de precondiciones aún sin modelar

## Próximos Pasos

1. **Inmediato**: Crear códigos para BIZUM (56 casos afectados)
2. **Corto plazo**: Modelar cuenta de valores y dispositivos
3. **Medio plazo**: Revisar códigos obsoletos del catálogo
4. **Largo plazo**: Automatizar detección de duplicados en pipeline

## Referencias

- [casos_revisados.txt](../data/entrada/casos_bs/casos_revisados.txt)
- [catalogo_icaria.csv](../data/catalogo_icaria.csv)
- [ADR-003: Eliminación de Duplicados](003-eliminacion-duplicados.md)
