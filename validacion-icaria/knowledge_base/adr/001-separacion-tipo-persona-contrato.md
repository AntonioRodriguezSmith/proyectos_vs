# ADR-001: Separación de Tipo de Persona y Tipo de Contrato

## Estado
Aceptado

## Contexto
Las precondiciones de los casos de prueba mezclaban el tipo de persona (Particular, Empresa, Autónomo) con el tipo de contrato (Banca a Distancia) en una sola línea.

**Ejemplo incorrecto:**
```
- Disponer de un usuario con un contrato de banca a distancia particular✅TIENE_BANCA_A_DISTANCIA
```

## Decisión
Separar en dos líneas distintas:
1. **Tipo de Persona**: código `ES_PERSONA_FISICA`, `ES_PERSONA_JURIDICA`, o `ES_AUTONOMO`
2. **Tipo de Contrato**: código `TIENE_BANCA_A_DISTANCIA` o `TIENE_BANCA_A_DISTANCIA_EMPRESA`

**Formato correcto:**
```
- Tipo Particular ✅ES_PERSONA_FISICA
- Disponer de un contrato de banca a distancia ✅TIENE_BANCA_A_DISTANCIA
```

## Consecuencias
- Cada precondición tiene un único código ICARIA
- Facilita el filtrado por tipo de persona o tipo de contrato
- Reduce ambigüedad en la interpretación

## Mapeos aplicados
| Texto original | Código |
|----------------|--------|
| "particular", "tipo Particular" | ES_PERSONA_FISICA |
| "empresa", "tipo Empresa" | ES_PERSONA_JURIDICA |
| "autónomo" | ES_AUTONOMO |
