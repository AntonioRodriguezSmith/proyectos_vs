# ADR-003: Eliminación de Casos Duplicados

## Estado
Aceptado

## Contexto
El archivo de casos contenía múltiples casos con el mismo número de CASO o con precondiciones idénticas.

## Decisión
1. **Duplicados por número**: Mantener solo la primera ocurrencia de cada CASO
2. **Duplicados por contenido**: Cuando varios casos tienen exactamente las mismas precondiciones normalizadas, mantener el de menor número

## Algoritmo de normalización
```python
def normalizar_precondiciones(texto):
    # Extraer solo los códigos ICARIA
    codigos = re.findall(r'[✅❌]([A-Z_]+|Sin modelar)', texto)
    return tuple(sorted(set(codigos)))
```

## Resultados
- Eliminados 165 casos duplicados por número
- Eliminados 81 casos duplicados por contenido
- Total: de 1641 casos a 1390 casos únicos

## Consecuencias
- Cada caso es único
- Se preservan los casos con número más bajo (presumiblemente los originales)
