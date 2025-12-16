"""
Script para revisar estados de casos después de separaciones
"""
import re
from pathlib import Path

def revisar_estados(filepath):
    """Revisa si los estados de los casos son correctos"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Dividir en casos
    casos = content.split('---\n')
    
    casos_incorrectos = []
    
    for caso in casos:
        if not caso.strip() or 'CASO' not in caso:
            continue
        
        # Extraer número de caso
        match_caso = re.search(r'CASO (\d+)', caso)
        if not match_caso:
            continue
        
        num_caso = match_caso.group(1)
        
        # Buscar el estado
        match_estado = re.search(r'Estado: (✅|❌)', caso)
        if not match_estado:
            continue
        
        estado_actual = match_estado.group(1)
        
        # Contar precondiciones OK y KO
        precondiciones = caso.split('PRECONDICIONES:')[1].split('Estado:')[0] if 'PRECONDICIONES:' in caso else ''
        
        # Contar ✅ y ❌ en las precondiciones (no en el estado)
        ok_count = precondiciones.count('✅')
        ko_count = precondiciones.count('❌Sin modelar')
        
        # Determinar estado correcto
        if ko_count > 0:
            estado_correcto = '❌'
        elif ok_count > 0:
            estado_correcto = '✅'
        else:
            continue
        
        # Verificar si el estado es correcto
        if estado_actual != estado_correcto:
            casos_incorrectos.append({
                'caso': num_caso,
                'estado_actual': estado_actual,
                'estado_correcto': estado_correcto,
                'ok': ok_count,
                'ko': ko_count
            })
    
    return casos_incorrectos

if __name__ == '__main__':
    filepath = Path(__file__).parent.parent / 'data' / 'entrada' / 'casos_bs' / 'casos_revisados.txt'
    
    print("Revisando estados de casos...")
    incorrectos = revisar_estados(filepath)
    
    if incorrectos:
        print(f"\n❌ Encontrados {len(incorrectos)} casos con estado incorrecto:\n")
        for caso in incorrectos:
            print(f"CASO {caso['caso']}: Estado actual {caso['estado_actual']} → Debería ser {caso['estado_correcto']}")
            print(f"  - Precondiciones OK: {caso['ok']}, KO: {caso['ko']}")
    else:
        print("\n✅ Todos los estados son correctos")
