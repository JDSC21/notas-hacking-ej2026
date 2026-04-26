# Warmed Up

## Descripción 
What is 0x3D (base 16) in decimal (base 10)?

## Solución

Para resolver este reto, necesitamos convertir el número hexadecimal `0x3D` a formato decimal (base 10). El prefijo `0x` solo sirve para indicar que es un número hexadecimal.

**Método Manual (Matemáticas):**
En formato hexadecimal, los números van del 0 al 9, y luego las letras de la A(10) a la F(15). 
- La letra `D` equivale a 13.
- El número `3` está en la posición de los dieciseisavos (16^1).

Cálculo: `(3 * 16) + (13 * 1) = 48 + 13 = 61`

**Método Rápido (Terminal / Python):**
Puedes usar una sola línea en tu terminal para que Python haga la conversión por ti:
```bash
python -c "print(0x3D)"
```
*Salida: `61`*

La bandera final es:
`picoCTF{61}`

## Notas Adicionales

Se resuelve más rápido en python

### Referencias