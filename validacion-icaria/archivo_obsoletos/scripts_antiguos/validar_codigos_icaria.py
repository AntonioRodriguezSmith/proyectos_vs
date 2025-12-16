#!/usr/bin/env python3
"""Valida los códigos Icaria en casos_revisados.txt contra el catálogo."""
from pathlib import Path
import re

root = Path(r"c:\Users\rodri\proyectos_vs")
casos_file = root / 'data' / 'entrada' / 'casos_bs' / 'casos_revisados.txt'
catalogo_file = root / 'data' / 'catalogo_icaria.csv'
output_file = root / 'output_analisis' / 'validacion_codigos_icaria.txt'

# Leer catálogo
cat_text = catalogo_file.read_text(encoding='utf-8')
cat_lines = cat_text.strip().splitlines()[1:]  # skip header
valid_codes = set()
for line in cat_lines:
    parts = line.split('\t')
    if len(parts) >= 2:
        valid_codes.add(parts[1].strip())

print(f'Catálogo cargado: {len(valid_codes)} códigos válidos')

# Leer casos y extraer todos los códigos
casos_text = casos_file.read_text(encoding='utf-8')
found_codes = {}  # code -> count
invalid_codes = {}  # code -> [ejemplos de líneas]

for line in casos_text.splitlines():
    # buscar patrones como ✅CODIGO
    matches = re.findall(r'✅([A-Z_]+)', line)
    for code in matches:
        if code not in found_codes:
            found_codes[code] = 0
        found_codes[code] += 1
        
        if code not in valid_codes:
            if code not in invalid_codes:
                invalid_codes[code] = []
            invalid_codes[code].append(line.strip()[:80])

# Generar reporte
report = []
report.append('VALIDACIÓN DE CÓDIGOS ICARIA')
report.append('=' * 80)
report.append(f'\nCatálogo: {len(valid_codes)} códigos válidos')
report.append(f'Encontrados en casos: {len(found_codes)} códigos diferentes')
report.append(f'Total de referencias: {sum(found_codes.values())} usos')
report.append(f'Códigos inválidos o no documentados: {len(invalid_codes)}')

if invalid_codes:
    report.append('\n' + '=' * 80)
    report.append('CÓDIGOS INVÁLIDOS O NO DOCUMENTADOS:')
    report.append('=' * 80)
    for code in sorted(invalid_codes.keys()):
        count = found_codes.get(code, 0)
        report.append(f'\n❌ {code} (aparece {count} veces)')
        for ejemplo in invalid_codes[code][:3]:
            report.append(f'   Ejemplo: {ejemplo}')
        if len(invalid_codes[code]) > 3:
            report.append(f'   ... y {len(invalid_codes[code]) - 3} más')

report.append('\n' + '=' * 80)
report.append('TOP 10 CÓDIGOS MÁS USADOS:')
report.append('=' * 80)
sorted_codes = sorted(found_codes.items(), key=lambda x: x[1], reverse=True)[:10]
for i, (code, count) in enumerate(sorted_codes, 1):
    status = '✅' if code in valid_codes else '❌'
    report.append(f'{i:2}. {status} {code:45} {count:4} usos')

# Guardar reporte
out_text = '\n'.join(report)
output_file.write_text(out_text, encoding='utf-8')
print(out_text)
print(f'\nReporte guardado en: {output_file}')
