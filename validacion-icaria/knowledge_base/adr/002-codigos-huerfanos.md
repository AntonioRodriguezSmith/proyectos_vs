# ADR-002: Corrección de Códigos Huérfanos

## Estado
Aceptado

## Contexto
Algunas líneas contenían solo el código ICARIA sin texto descriptivo.

**Ejemplo incorrecto:**
```
- que tenga contratadas cuentas a la vista ✅TIENE_CUENTA_VISTA
✅TIPO_SALDO_DV_PARAMETRIZADO
```

## Decisión
Cada código ICARIA debe estar precedido por un texto descriptivo que empiece con `- `.

**Formato correcto:**
```
- que tenga contratadas cuentas a la vista ✅TIENE_CUENTA_VISTA
- Que dispongan de saldo suficiente ✅TIPO_SALDO_DV_PARAMETRIZADO
```

## Mapeos de códigos huérfanos
| Código huérfano | Texto a añadir |
|-----------------|----------------|
| ✅TIPO_SALDO_DV_PARAMETRIZADO | - Que dispongan de saldo suficiente |
| ✅TIENE_TARJETA_PAGO_ACTIVA | - Tenga tarjeta de pago activa |
| ✅TIENE_CUENTA_VISTA_EMPRESA | - Tenga cuenta vista empresa |
| ✅TIENE_BANCA_A_DISTANCIA_EMPRESA | - Tenga banca a distancia empresa |
| ✅TIPO_DE_FIRMA_DIGITAL_BSO | - Con firma digital |
| ✅TIENE_MAS_DE_X_CUENTAS_VISTA_PARAMETRO | - Tenga más de una cuenta vista |
| ✅TIENE_CUENTA_VISTA | - Tenga cuenta vista |
| ✅TIENE_MOVIMIENTOS_EN_CUENTA | - Tenga movimientos en cuenta |
| ✅TIENE_MOVIMIENTO_TARJETA | - Tenga movimientos de tarjeta |
| ✅ES_TITULAR_ACTIVO_AVISOS_ALERTAS | - Titular activo avisos/alertas |

## Consecuencias
- Todas las líneas son legibles y autoexplicativas
- Facilita la revisión manual de precondiciones
