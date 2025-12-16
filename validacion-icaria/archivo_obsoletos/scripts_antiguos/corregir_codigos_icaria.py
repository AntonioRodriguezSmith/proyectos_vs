#!/usr/bin/env python3
"""Corrige códigos Icaria truncados o con errores de caso."""
from pathlib import Path
import re

root = Path(r"c:\Users\rodri\proyectos_vs")
casos_file = root / 'output_analisis' / 'casos_revisados_refinado.txt'
out_file = root / 'output_analisis' / 'casos_revisados_validado.txt'

text = casos_file.read_text(encoding='utf-8')

# Mapa de correcciones: código inválido -> válido
correcciones = {
    'TIENE_BANCA_A_DISTANC': 'TIENE_BANCA_A_DISTANCIA',
    'TIENE_CUENTA_VISTa': 'TIENE_CUENTA_VISTA',
    'TIENE_CUENTA_VIST': 'TIENE_CUENTA_VISTA',
    'TIENE_TARJETA_PAGO_ACT': 'TIENE_TARJETA_PAGO_ACTIVA',
    'TIPO_SALDO_DV_PARAMETRIZado': 'TIPO_SALDO_DV_PARAMETRIZADO',
    'TIPO_SALDO_DV_PARAMETRIZ': 'TIPO_SALDO_DV_PARAMETRIZADO',
}

newtext = text
cambios = 0
for incorrecto, correcto in correcciones.items():
    # Buscar patrones como ✅incorrecto
    pattern = f'✅{re.escape(incorrecto)}'
    matches = re.findall(pattern, newtext)
    if matches:
        newtext = newtext.replace(f'✅{incorrecto}', f'✅{correcto}')
        cambios += len(matches)
        print(f'Corregido {len(matches)} x {incorrecto} -> {correcto}')

out_file.write_text(newtext, encoding='utf-8')
print(f'\nTotal cambios: {cambios}')
print(f'Archivo guardado: {out_file}')
