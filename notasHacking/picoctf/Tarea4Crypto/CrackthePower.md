# Crack the Power

## Descripción

We received an encrypted message. The modulus is built from primes large enough that factoring them isn't an option, at least not today. See if you can make sense of the numbers and reveal the flag.

Download the message with the RSA parameters provided.

## Solución

### Conceptos Teóricos

**Ataque de Exponente Pequeño (Low Public Exponent Attack):**

El ataque de Coppersmith ocurre cuando ciertos valores en la configuración de encriptación RSA son más pequeños de lo usual, lo que abre atajos inesperados para recuperar el texto plano.

**Escenarios donde puede ocurrir este ataque:**
- RSA se usó con un exponente pequeño (e bajo)
- El mensaje encriptado m es muy pequeño
- El mismo mensaje pequeño se envía a múltiples personas con el mismo exponente pequeño
- No hay padding

### La Vulnerabilidad

En este reto, el exponente es `e = 20`, que es muy pequeño (normalmente es 65537).

Si tenemos:
- Un mensaje m
- e = 20 (pequeño)
- Un módulo n muy grande

**La clave:** Si m^e < n, entonces:
```
c = m^e mod n = m^e
```

Esto significa que el cifrado no realiza verdaderamente la operación módulo, ¡solo calcula m^e!

Por lo tanto, para recuperar m solo necesitamos:
```
m = c^(1/e) = c^(1/20)
```

Y luego convertir el resultado a bytes.

### Explotación

```python
from Crypto.Util.number import long_to_bytes
import math

# Leer los parámetros RSA del archivo
n = <given_n>
e = 20  # exponente pequeño
c = <given_ciphertext>

# Como m^e < n, el ciphertext es simplemente c = m^e
# Calculamos la raíz e-ésima de c
m = int(c ** (1/e))

# Ajuste fino en caso de errores de precisión de punto flotante
for i in range(max(0, m - 2), m + 3):
    if pow(i, e, n) == c:
        m = i
        break

# Convertir el mensaje a bytes
flag = long_to_bytes(m)
print(flag)
```

**Flag obtenida:**
```
picoCTF{XXXXXXXXXXXXXXX}
```

## Notas adicionales

Este reto demuestra la importancia de elegir parámetros RSA seguros:
- El exponente público e no debe ser muy pequeño (típicamente es 65537)
- Es crucial agregar padding (como OAEP) para evitar que mensajes pequeños se cifren sin la operación módulo
- Un módulo n suficientemente grande es esencial para que la operación módulo tenga efecto

La vulnerabilidad en este caso es que con e tan pequeño y sin padding, si el mensaje original es pequeño, se puede recuperar fácilmente tomando la raíz e-ésima del ciphertext.

## Referencias

- https://en.wikipedia.org/wiki/Coppersmith%27s_attack
- https://en.wikipedia.org/wiki/RSA_%28cryptosystem%29
- https://crypto.stackexchange.com/questions/33609/rsa-problem-when-exponent-e-is-small
