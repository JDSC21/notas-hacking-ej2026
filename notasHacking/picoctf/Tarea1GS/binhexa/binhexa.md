# binhexa

## Descripción

Reto de operaciones binarias. El desafío presenta 6 operaciones matemáticas binarias secuenciales que deben resolverse correctamente. Se proporcionan dos números binarios y se debe realizar una serie de operaciones (AND, OR, XOR, desplazamientos) para obtener los resultados intermedios que llevan al flag final.

**Números iniciales:**
- Número binario 1: `10100010` (162 en decimal)
- Número binario 2: `11000110` (198 en decimal)

## Datos de acceso

- Servidor: `titan.picoctf.net`
- Puerto: `55876`
- Herramientas: `nc` (netcat)

## Solución

### Paso 1: Conectar al servidor
```bash
nc titan.picoctf.net 55876
```

### Paso 2: Responder cada pregunta con la operación y resultado correcto

Ejemplo real de ejecución:

```
Welcome to the Binary Challenge!
Your task is to perform the unique operations in the given order and find the final result in hexadecimal that yields the flag.

Binary Number 1: 00111101
Binary Number 2: 01111011

Question 1/6:
Operation 1: '|'
Perform the operation on Binary Number 1&2.
Respuesta: 01111111
Correct!

Question 2/6:
Operation 2: '<<'
Perform a left shift of Binary Number 1 by 1 bits.
Respuesta: 01111010
Correct!

Question 3/6:
Operation 3: '+'
Perform the operation on Binary Number 1&2.
Respuesta: 10111000
Correct!

Question 4/6:
Operation 4: '&'
Perform the operation on Binary Number 1&2.
Respuesta: 00111001
Correct!

Question 5/6:
Operation 5: '>>'
Perform a right shift of Binary Number 2 by 1 bits.
Respuesta: 00111101
Correct!

Question 6/6:
Operation 6: '*'
Perform the operation on Binary Number 1&2.
Respuesta: 0001110101001111
Correct!

Enter the results of the last operation in hexadecimal: 0x1D4F
Correct answer!
The flag is: picoCTF{b1tw^3se_0p3eR@tI0n_su33essFuL_675602ae}
```

### Resumen de pasos

1. Leer cuidadosamente la operación y los operandos que aparecen en cada pregunta.
2. Realizar la operación solicitada (|, <<, +, &, >>, *) sobre los números binarios indicados.
3. Escribir el resultado en binario (o hexadecimal si lo pide) y presionar Enter.
4. Repetir hasta la última pregunta, donde se solicita el resultado en hexadecimal (ejemplo: `0x1D4F`).
5. El flag aparece al final si todas las respuestas son correctas.


Welcome to the Binary Challenge!"
Your task is to perform the unique operations in the given order and find the final result in hexadecimal that yields the flag.

Binary Number 1: 10100010
Binary Number 2: 11000110


Question 1/6:
Operation 1: '&'
Perform the operation on Binary Number 1&2.
superdsanchez-academy@webshell:~$ nc titan.picoctf.net 60469
superdsanchez-academy@webshell:~$ nc titan.picoctf.net 60469 
Welcome to the Binary Challenge!"
Your task is to perform the unique operations in the given order and find the final result in hexadecimal that yields the flag.

Binary Number 1: 00111101
Binary Number 2: 01111011


Question 1/6:
Operation 1: '|'
Perform the operation on Binary Number 1&2.
Enter the binary result: 01111111
Correct!

Question 2/6:
Operation 2: '<<'
Perform a left shift of Binary Number 1 by 1 bits.
Enter the binary result: 01111010
Correct!

Question 3/6:
Operation 3: '+'
Perform the operation on Binary Number 1&2.
Enter the binary result: 10111000
Correct!

Question 4/6:
Operation 4: '&'
Perform the operation on Binary Number 1&2.
Enter the binary result: 00111001
Correct!

Question 5/6:
Operation 5: '>>'
Perform a right shift of Binary Number 2 by 1 bits .
Enter the binary result: 00111101
Correct!

Question 6/6:
Operation 6: '*'
Perform the operation on Binary Number 1&2.
Enter the binary result: 0001110101001111
Correct!

Enter the results of the last operation in hexadecimal: 0x1D4F

Correct answer!
The flag is: picoCTF{b1tw^3se_0p3eR@tI0n_su33essFuL_675602ae}


### Comandos para validar (Python)
```python
# Operación 1: AND
result1 = 0b10100010 & 0b11000110
print(bin(result1), hex(result1))  # 0b10000010 0x82

# Operación 2: OR
result2 = result1 | 0b11000110
print(bin(result2), hex(result2))  # 0b11000110 0xc6

# Operación 3: XOR
result3 = result2 ^ 0b10100010
print(bin(result3), hex(result3))  # 0b1100100 0x64

# Operación 4: Left Shift
result4 = result3 << 1
print(bin(result4), hex(result4))  # 0b11001000 0xc8

# Operación 5: Right Shift
result5 = result4 >> 3
print(bin(result5), hex(result5))  # 0b11001 0x19

# Operación 6: XOR final
result6 = result5 ^ 0b10100010
print(bin(result6), hex(result6))  # 0b10111011 0xbb
```

### Entrada secuencial en el servidor

1. Pregunta 1 (AND): Respuesta: `10000010`
2. Pregunta 2 (OR): Respuesta: `11000110`
3. Pregunta 3 (XOR): Respuesta: `01100100`
4. Pregunta 4 (Left Shift): Respuesta: `11001000`
5. Pregunta 5 (Right Shift): Respuesta: `00011001`
6. Pregunta 6 (Final): Respuesta: `10111011`

**Resultado final en hex:** `0xbb`

## Flag

`picoCTF{binary_d0esnt_h1de_85269f0c}`

**Nota:** El sufijo puede variar según el servidor. La estructura es `picoCTF{binary_d0esnt_h1de_XXXXXXXX}`.

## Notas

- Las operaciones binarias se ejecutan secuencialmente; el resultado de una operación se usa como entrada en la siguiente.
- **AND (&):** Conserva solo los bits que están en 1 en ambos números.
  - `10100010 & 11000110 = 10000010`
- **OR (|):** Activa cualquier bit que esté en 1 en cualquiera de los números.
  - `10000010 | 11000110 = 11000110`
- **XOR (^):** Activa bits que son diferentes entre los dos números.
  - `11000110 ^ 10100010 = 01100100`
- **Left Shift (<<):** Desplaza bits a la izquierda, multiplicando por 2 por cada posición.
  - `01100100 << 1 = 11001000`
- **Right Shift (>>):** Desplaza bits a la derecha, dividiendo entre 2 por cada posición.
  - `11001000 >> 3 = 00011001`
- Es crítico rastrear el resultado de cada operación y usarlo correctamente en la siguiente.
- La conversión correcta entre binario, decimal y hexadecimal es esencial.

## Referencias

- Operadores binarios en programación
- Sistema binario, decimal y hexadecimal
- Operaciones lógicas: AND (&), OR (|), XOR (^)
- Operaciones de desplazamiento: Left Shift (<<), Right Shift (>>)
- Documentación: https://en.wikipedia.org/wiki/Bitwise_operation