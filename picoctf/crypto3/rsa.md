## RSA
```
RSA   
-----------------------------------------------------------
m   - mensaje original o mensaje en texto plano (plaintext)
c   - mensaje cifrado (ciphertext)
p,q - son dos numeros primos distintos y muy grandes
n   - es el modulo (lo comparten la llave publica y privada)
tn  - totient n (funcion de euler)
e   - llave publica - (exponente)  2 ^ 16 + 1 = 65537
d   - llave privada

Calculos
--------------------------------------------------
n  = p * q
tn = (p -1) * (q-1)
d = e ^ -1 (mod tn)	- pow(e, -1, tn)

Cifrar  
--------------------------------------------------
c = m ^ e (mod n)	- pow(m, e, n)

Decifrar
--------------------------------------------------
m = c ^ d (mod n)	- pow(c, d, n)
```

## Mini RSA 
### Probar ataque 1 : Stereotyped 
```
- Como tu exponente e es 3 (muy pequeño), la vulnerabilidad es un ataque de raíz cúbica conocido como: Stereotyped attack o small e attack.
- Este ataque funciona si el mensaje original m fue lo suficientemente pequeño como para que:
    m^3 < n. 
- Si eso ocurrió, el módulo no tuvo efecto, y por lo tanto c = m^3
    c = m ^ e mod n
    c = m ^ 3
- Para revertirlo, solo necesitamos calcular la raíz cúbica de c.
    m = raiz3(c)
```

## Mind your Ps and Qs 
```
- Dado que n es muy corta, se puede factorizar y obtener los valores de p y q
- Para factorizar usamos > https://factordb.com/
```
 
### b00tl3gRSA2 
```
- Los valores de e y d fueron invertidos al encriptar
- Solo se revierten al desencriptar, se usa el valor por defecto de e, y se usa e para desencriptar en lugar de d
```
 
### b00tl3gRSA3 
```
- El valor de n es pequeño, por lo que se puede factorizar, pero no de manera simple, sera multiple
- Encontramos factores multiples y totien con :  https://www.alpertron.com.ar/ECM.HTM
- Se decodifica c y se obtiene m que es la flag
```
 