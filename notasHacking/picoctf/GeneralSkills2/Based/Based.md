# Based

## Descripción
El reto prueba tu habilidad para reconocer y convertir datos en distintas bases (binario, octal, hexadecimal). Debes conectarte a un servicio remoto que te dará valores codificados y responder con la palabra correcta antes de que se acabe el tiempo.

Conéctate con (el puerto puede cambiar):
```bash
nc fickle-tempest.picoctf.net <PUERTO>
```

## Solución
El servidor va pidiendo palabras representadas en diferentes bases. Aquí están los pasos y ejemplos para convertir cada tipo.

### 1) Binario (ejemplo)
Prompt que puede aparecer:
```
01110011 01110101 01100010 01101101 01100001 01110010 01101001 01101110 01100101
```
Cada bloque de 8 bits corresponde a un carácter ASCII. Para convertirlo con Python (pega la línea completa entre comillas):
```bash
python3 - <<'PY'
s = "01110011 01110101 01100010 01101101 01100001 01110010 01101001 01101110 01100101"
print(''.join(chr(int(b, 2)) for b in s.split()))
PY
```

### 2) Octal (ejemplo)
Prompt que puede aparecer (nota la `o` antes de cada número):
```
o157 o166 o145 o156
```
Quita la `o` y convierte desde base 8:
```bash
python3 - <<'PY'
s = "o157 o166 o145 o156"
nums = [x.lstrip('o') for x in s.split()]
print(''.join(chr(int(n, 8)) for n in nums))
PY
```

### 3) Hexadecimal (ejemplo)
Prompt que puede aparecer (sin separadores):
```
736c75646765
```
Convierte hex a bytes y decodifica:
```bash
python3 - <<'PY'
h = "736c75646765"
print(bytes.fromhex(h).decode())
PY
```

Si aplicas estas conversiones en cada paso del servicio, al final obtendrás la bandera:

`picoCTF{learning_about_converting_values_aa2bA794}`

## Notas Adicionales
- `nc` (netcat) te permite conectarte a servicios TCP y ver las preguntas en vivo.
- En este reto normalmente aparecen varias bases: binario (0/1), octal (base 8) y hexadecimal (base 16).
- Si usas CyberChef: usa **From Binary** para binario; para octal puedes eliminar la `o` con **Find / Replace** y luego usar **From Octal**; para hex usa **From Hex**.

### Referencias
- https://gchq.github.io/CyberChef/