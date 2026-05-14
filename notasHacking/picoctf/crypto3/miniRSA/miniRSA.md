# Reto Mini RSA

## Descripción 
What happens if you have a small exponent? There is a twist though, we padded the plaintext so that (M ** e) is just barely larger than N. Let's decrypt this:
values
## Solución

**Stereotype**
- Como tu exponente e es 3 (muy pequeño), la vulnerabilidad es un ataque de raíz cúbica conocido como: Stereotyped attack o small e attack.
- Este ataque funciona si el mensaje original m fue lo suficientemente pequeño como para que:
    m^3 < n. 
- Si eso ocurrió, el módulo no tuvo efecto, y por lo tanto c = m^3
    c = m ^ e mod n
    c = m ^ 3
- Para revertirlo, solo necesitamos calcular la raíz cúbica de c.
    m = raiz3(c)

    Instalar libreria de python gmpy2
`sudo apt install python3-gmpy2`

**Probar ataque 2 - Ataque de k iterativa**
- Si el ataque anterior falla es porque la suposición  m^3 < n  no se cumple y módulo se aplica.
-  Esto nos lleva al *siguiente ataque más común para e=3: Ataque de k iterativa
- La ecuación real es : c = m^3 mod n
- Por definición de la aritmética modular, esto significa que m^3 es igual a c más algún múltiplo de n.
    m^3 = c + k  * n
- Donde k es un entero desconocido (k=1, k=2, etc) suele ser un numero pequeño

## Notas Adicionales
Archivo está en carpeta
### Referencias

