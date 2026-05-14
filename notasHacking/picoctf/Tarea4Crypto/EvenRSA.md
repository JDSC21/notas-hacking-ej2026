# Even RSA

## Descripción

This service provides you an encrypted flag. Can you decrypt it with just N & e?
Connect to the program with netcat:
```
$ nc verbal-sleep.picoctf.net 56881
```

## Solución

### Conceptos Teóricos

**Introduction to RSA:**
RSA es un sistema criptográfico asimétrico ampliamente utilizado que usa un par de claves: una clave pública para encriptar y una clave privada para desencriptar. La seguridad de RSA depende del módulo N, que es el producto de dos números primos grandes p y q.

**¿Cómo funciona RSA?**
- Un mensaje m se convierte en un entero
- Encriptación: C = m^e mod N
- Desencriptación: m = C^d mod N
- La clave privada d se calcula tal que: e × d ≡ 1 mod φ(N), donde φ(N) = (p-1)(q-1)

### La Vulnerabilidad

El desafío proporciona valores de N que son números pares, lo cual es inusual porque N siempre debería ser impar (producto de dos primos impares). Esta anomalía sugiere que uno de los factores primos podría ser 2 (el único número primo par).

Dividiendo N por 2 se obtiene q = N/2, confirmando que p = 2.

Esto simplifica drasticamente el problema:
- φ(N) = (2–1)(q-1) = q-1
- La clave privada d se calcula como el inverso modular de e módulo φ(N)

### Explotación

```python
from Crypto.Util.number import long_to_bytes

N = <given_even_N>
e = 65537

q = N // 2
phi_N = q - 1
d = pow(e, -1, phi_N)

c = <given_ciphertext>
m = pow(c, d, N)
flag = long_to_bytes(m)
print(flag)
```

## Flag

```
picoCTF{tw0_1$_pr!m378257f39}
```

## Notas Adicionales

La vulnerabilidad en este reto radica en que el módulo N es par, lo que significa que uno de los factores primos es 2. Esto permite factorizar N trivialmente y recuperar la clave privada sin necesidad de métodos sofisticados de factorización.

## Referencias

- https://musthofa-kamaluddin.medium.com/even-rsa-can-be-broken-picoctf-2025-challenge-write-up-891447150064

