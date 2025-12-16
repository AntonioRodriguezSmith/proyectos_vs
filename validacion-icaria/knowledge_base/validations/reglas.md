# Reglas de Validación de Precondiciones

## Regla 1: Tipo de Persona Obligatorio
Todo caso que tenga `TIENE_BANCA_A_DISTANCIA` debe tener al menos uno de:
- `ES_PERSONA_FISICA`
- `ES_PERSONA_JURIDICA`
- `ES_AUTONOMO`

## Regla 2: Coherencia Tipo Persona - Contrato
| Si tiene... | Debe tener... |
|-------------|---------------|
| TIENE_BANCA_A_DISTANCIA (sin EMPRESA) | ES_PERSONA_FISICA |
| TIENE_BANCA_A_DISTANCIA_EMPRESA | ES_PERSONA_JURIDICA |
| TIENE_BANCA_A_DISTANCIA_AUTONOMO | ES_AUTONOMO |

## Regla 3: No Códigos Huérfanos
Ninguna línea debe empezar con `✅` directamente. 
Debe haber un texto descriptivo antes: `- [texto]✅CODIGO`

## Regla 4: No Mezclar Tipo Persona en Línea de Contrato
La palabra "particular", "empresa" o "autónomo" no debe aparecer en la misma línea que `TIENE_BANCA_A_DISTANCIA`.

## Regla 5: Estado Consistente
Si un caso tiene alguna precondición `❌Sin modelar`, el estado debe ser `❌`.

## Regla 6: Sin Duplicados
No puede haber dos casos con el mismo número de CASO.
