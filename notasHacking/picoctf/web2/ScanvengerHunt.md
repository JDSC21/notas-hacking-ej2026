# Scavenger hunt

## Descripción

Reto de "scavenger hunt" web: la bandera está escondida en varios recursos del sitio (HTML, hojas de estilo, archivos de configuración o archivos ocultos como `.DS_Store`). La URL base se indica en la descripción del reto.

## Solución (resumen)

La bandera ya fue encontrada inspeccionando recursos accesibles desde la web y ficheros expuestos. A continuación se documentan las distintas opciones y técnicas utilizadas para localizarla.

## Opciones de solución

- **Inspector del navegador**: Abrir las DevTools (F12), revisar el árbol DOM, recursos cargados (`Network` / `Sources`) y buscar rutas interesantes en los enlaces, comentarios o referencias a hojas de estilo y scripts.

- **Revisar `robots.txt`, `.htaccess` y hojas de estilo**: acceder a rutas típicas directamente con el navegador o `curl`:

```bash
curl -s http://wily-courier.picoctf.net:59379/robots.txt
curl -s http://wily-courier.picoctf.net:59379/.htaccess
curl -s http://wily-courier.picoctf.net:59379/style.css
```

- **Buscar archivos ocultos y metadatos (`.DS_Store`)**: algunos servidores exponen `.DS_Store`, que puede contener nombres de archivos sensibles. Descargar y analizarlo localmente:

```bash
curl -s -o .DS_Store http://wily-courier.picoctf.net:59379/.DS_Store
strings .DS_Store | grep -i pico
```

Si `strings` no muestra el resultado directamente, abrir el fichero con un visor hex (`xxd .DS_Store | less`) o usar utilidades específicas para `.DS_Store`.

- **Enumeración de directorios (gobuster/dirb/ffuf)**: lanzar un barrido con un wordlist para encontrar rutas no enlazadas.

```bash
# Ejemplo con gobuster (ajustar wordlist y extensiones)
gobuster dir -u http://wily-courier.picoctf.net:59379 -w /usr/share/wordlists/dirb/common.txt -x .txt,html,php
```

- **`curl` + grep (barrido simple con shell)**: iterar sobre una lista de posibles nombres y filtrar por la cadena `picoCTF`.

```bash
for p in index hidden admin robots.txt .htaccess .DS_Store; do
	curl -s "http://wily-courier.picoctf.net:59379/$p" | grep -i pico || true
done
```

- **Burp Suite**: interceptar peticiones, revisar recursos, y usar Repeater para comprobar rutas sospechosas; Intruder puede automatizar pruebas de nombres/paths.

- **Script Python para comprobaciones masivas**: ejemplo que descarga una lista de rutas y busca la bandera.

```python
import requests, re

host = 'http://wily-courier.picoctf.net:59379'
paths = ['robots.txt', '.htaccess', '.DS_Store', 'index.html', 'hidden.html']
for p in paths:
		r = requests.get(f"{host}/{p}")
		if 'picoCTF{' in r.text:
				print(re.search(r"picoCTF\{.*?\}", r.text).group(0))
				break
```

## Notas

- En este reto la bandera apareció tras inspeccionar recursos expuestos y archivos del servidor (por ejemplo `.DS_Store`), por lo que es recomendable combinar inspección manual con herramientas automáticas.
- Algunos hosts usan diferentes puertos; asegúrese de usar el puerto indicado en la URL del reto.

## Referencias

- `.DS_Store` info: https://en.wikipedia.org/wiki/.DS_Store
- `.htaccess` Apache: https://httpd.apache.org/docs/2.4/howto/htaccess.html
- Herramientas de enumeración: `gobuster`, `ffuf`, `dirb`

## Ejemplos de rutas encontradas

- `http://wily-courier.picoctf.net:56026/`
- `http://wily-courier.picoctf.net:61853/.htaccess`
- `http://wily-courier.picoctf.net:61853/robots.txt`
- `http://wily-courier.picoctf.net:61853/.DS_Store`

La bandera encontrada fue: `picoCTF{th4ts_4_l0t_0f_pl4c3s_2_lO0k_9588550}`