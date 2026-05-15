# Reto interencdec

## Descripción 

Can you get the real meaning from this file.
Download the file here.

## Solución


Decodificar base64
Eliminar caracteres : 'b y '
Decodificar nuevamente en base64
`cat enc_flag | base64 -d | tr -d "'b" | base64 -d`
**Otra Opción más sencilla**
Ir a cyberchef elegir la receta rot13 y rotar 19 posiciones

## Notas Adicionales

### Referencias