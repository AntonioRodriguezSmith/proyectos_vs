# Proyecto de Validación ICARIA

Herramientas para validar, corregir y analizar casos de prueba ICARIA.

## 📅 Última actualización: 12 de diciembre de 2025

---

## 📊 Resumen del Estado Actual

| Métrica | Valor |
|---------|-------|
| **Total casos** | 1327 |
| ✅ Casos OK | 462 (34.8%) |
| ❌ Casos KO | 865 (65.2%) |
| **Total precondiciones** | 5526 |
| Modeladas | 4210 (76.2%) |
| Sin modelar | 1317 (23.8%) |
| **Códigos en catálogo** | 67 |
| Códigos en uso | 42 |
| Códigos sin usar | 27 |

---

## 📁 Estructura del Proyecto

```text
proyectos_vs/
├── data/
│   ├── catalogo_icaria.csv          # Catálogo de 67 códigos ICARIA
│   ├── entrada/
│   │   ├── casos_bs/
│   │   │   ├── casos_revisados.txt  # Archivo principal (1327 casos)
│   │   │   └── backups/             # Backups automáticos
│   │   └── ejemplo_*.txt/csv
│   └── salida/
│       ├── graficos/
│       ├── reportes/
│       └── resultados/
├── scripts/
│   ├── procesar_casos.py            # Validación, corrección, duplicados
│   ├── estadisticas.py              # Análisis y reportes
│   ├── backup/                      # Backups de scripts
│   └── utils/                       # Módulos auxiliares
├── knowledge_base/                  # Base de conocimiento (RAG)
│   ├── adr/                         # Decisiones arquitectónicas
│   │   ├── 001-separacion-tipo-persona-contrato.md
│   │   ├── 002-codigos-huerfanos.md
│   │   └── 003-eliminacion-duplicados.md
│   ├── mappings/codigos_icaria.md   # Mapeo de códigos
│   ├── patterns/                    # Patrones de corrección
│   │   ├── texto_a_codigo.json
│   │   └── correcciones_linea.json
│   ├── validations/reglas.md        # Reglas de validación
│   └── casos_y_duplicados.md        # Mapeo de duplicados originales
├── output_analisis/                 # Reportes generados
│   ├── estadisticas_precondiciones.txt
│   ├── conceptos_sin_modelar.txt
│   ├── precondiciones_sin_modelar.txt
│   ├── casos_revision_manual.txt
│   └── INFORME_EJECUTIVO.txt
├── notebooks/
│   └── 01_analisis.ipynb
├── archivo_obsoletos/               # Scripts y archivos antiguos
└── requirements.txt
```

---

## 🔧 Uso de Scripts

### Procesar casos (validar, corregir, eliminar duplicados)

```bash
python scripts/procesar_casos.py --validate    # Solo validar
python scripts/procesar_casos.py               # Validar y corregir
```

### Generar estadísticas

```bash
python scripts/estadisticas.py
```

---

## 📈 Códigos más utilizados

| Código | Uso |
|--------|-----|
| ES_PERSONA_FISICA | 1164 |
| TIENE_BANCA_A_DISTANCIA | 778 |
| TIPO_DE_FIRMA_DIGITAL_BSO | 444 |
| ES_PERSONA_JURIDICA | 374 |
| TIENE_BANCA_A_DISTANCIA_EMPRESA | 334 |
| TIENE_CUENTA_VISTA | 270 |
| TIENE_TARJETA_PAGO_ACTIVA | 173 |

---

## 🔄 Historial de correcciones aplicadas

1. **Eliminación de duplicados**: De 1641 → 1327 casos únicos
2. **Separación tipo persona/contrato**: 260 casos EMPRESA, 509 Particular, 30 Autónomo
3. **Códigos huérfanos**: 163 líneas corregidas
4. **Normalización de formato**: Espacios, guiones, emojis estandarizados

---

## Instalación

```bash
pip install -r requirements.txt
```
