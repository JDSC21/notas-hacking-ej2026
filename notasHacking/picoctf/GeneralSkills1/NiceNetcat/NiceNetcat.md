# Nice Net Cat...

## Descripción 
There is a nice program that you can talk to by using this command in a shell:
$ nc wily-courier.picoctf.net 52852, but it doesn't speak English...


## Solución

Al igual que en retos anteriores, utilizaremos `nc` (Netcat) para conectarnos al servidor. Esta vez, el servidor nos enviará una lista de números en lugar de texto legible.

**Paso 1: Conectarnos al servidor**
Ejecutamos el comando que nos proporciona la descripción en nuestra terminal:
```bash
nc wily-courier.picoctf.net 52852
```
*El servidor nos responderá con una larga lista de números en formato decimal (uno por línea), como por ejemplo `112`, `105`, `99`...*

**Paso 2: Decodificar los números**
El servidor "no habla en inglés", pero nos está enviando los caracteres usando su valor numérico en la tabla **ASCII**.

Para traducirlo rápidamente, podemos copiar y pegar toda esa lista de números en la herramienta web **CyberChef** y aplicarle el filtro/receta: **"From Decimal"** (Desde Decimal). 

*CyberChef traducirá los números y nos devolverá la bandera en texto plano:*
> `picoCTF{g00d_k1tty!_n1c3_k1tty!_d5d88}`

## Notas Adicionales

- El formato de codificación **ASCII** le asigna un número específico a cada letra y símbolo. Por ejemplo, el número `112` corresponde a la letra `p`, el `105` a la `i`, `99` a la `c`, `111` a la `o`, formando así la palabra "pico...".
- Puedes acceder a [CyberChef en este enlace](https://gchq.github.io/CyberChef/) (La navaja suiza de la criptografía y ciberseguridad).

### Referencias