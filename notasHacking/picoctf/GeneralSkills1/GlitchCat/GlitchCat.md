# Glitch Cat

## Descripción 
Our flag printing service has started glitching!
$ nc saturn.picoctf.net 62150


## Solución

Al conectarnos al servidor, en lugar de darnos la bandera limpia, el sistema "falla" y nos arroja una cadena que incluye código escrito en Python.

**Paso 1: Obtener el mensaje del servidor**
Nos conectamos al puerto indicado usando Netcat (`nc`):
```bash
nc saturn.picoctf.net 62150
```
*El servidor nos responde esto:*
`'picoCTF{gl17ch_m3_n07_' + chr(0x39) + chr(0x63) + chr(0x34) + chr(0x32) + chr(0x61) + chr(0x34) + chr(0x35) + chr(0x64) + '}'`

**Paso 2: Procesar la información con Python**
Vemos que el servidor usó la función `chr()` para ofuscar los últimos caracteres usándolos en formato hexadecimal. Para traducirlo fácilmente, simplemente copiamos todo ese texto y dejamos que la herramienta interactiva de Python haga la suma y las conversiones por nosotros:

```python
# Entramos a la consola escribiendo 'python' y pegamos la salida:
>>> 'picoCTF{gl17ch_m3_n07_' + chr(0x39) + chr(0x63) + chr(0x34) + chr(0x32) + chr(0x61) + chr(0x34) + chr(0x35) + chr(0x64) + '}'
```

*Python evaluará la suma de esos caracteres y nos devolverá la bandera armada:*
> `picoCTF{gl17ch_m3_n07_9c42a45d}`

## Notas Adicionales

- La función `chr()` en Python convierte un número entero (ya sea en formato decimal normal o en hexadecimal como `0x39`) a su respectivo carácter textual según la tabla ASCII.


### Referencias