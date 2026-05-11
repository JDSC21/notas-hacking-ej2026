# getAhead

## Descripción

Reto para localizar un recurso protegido en un servidor web. El objetivo consiste en encontrar la ruta que devuelve el flag y obtenerla modificando el comportamiento de las solicitudes HTTP.

URL del reto:

```
http://wily-courier.picoctf.net:49872/
```

## Explicación de la resolución 

Se solucionó el reto mediante la inspección y manipulación de las solicitudes HTTP que el navegador envía al servidor. El equipo que resolvió el reto siguió un flujo típico de pruebas web: primero exploraron el servidor con herramientas de línea de comandos para verificar la respuesta a distintos métodos HTTP; después usaron un proxy HTTP (por ejemplo, Burp Suite) para interceptar y modificar las peticiones en tiempo real.

Al interceptar las solicitudes, cambiaron el método HTTP y observaron cómo variaba la respuesta del servidor; una de esas variaciones permitió acceder al recurso que contenía la pista/flag. Para confirmar el comportamiento replicaron la petición modificada desde la consola (por ejemplo usando `curl`) y así automatizaron la obtención del recurso.

En resumen, la resolución combinó:

- Reconocimiento de la aplicación y pruebas con distintos métodos HTTP (GET, HEAD, PUT, etc.).
- Uso de un proxy (Burp) para interceptar y editar la solicitud antes de que llegara al servidor.
- Verificación y reproducción por consola para documentar el hallazgo.

La explicación evita detallar la petición exacta que devolvió el flag, centrándose en la metodología usada para encontrarla.

## Notas

- Herramientas comunes empleadas: `curl` para pruebas rápidas, Burp Suite (proxy) para interceptación y modificación de requests, y extensiones de navegador (p. ej. FoxyProxy) para redirigir tráfico al proxy.
- Al usar Burp con navegadores, es necesario instalar y confiar en el certificado que Burp genera para poder interceptar tráfico HTTPS.
- Cambiar el método HTTP puede exponer rutas o comportamientos distintos en servidores mal configurados; siempre documentar y validar cualquier cambio antes de automatizarlo.

## Referencias

- Métodos HTTP: https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods
- Proxies y herramientas de pentesting: https://portswigger.net/burp
- Guía rápida de `curl`: https://curl.se/docs/

## Capturas de terminal (ejemplos)

Los siguientes comandos y salidas muestran cómo se inspeccionó el servidor durante la resolución:

1) Petición GET (respuesta completa HTML):

```bash
curl -s -i http://wily-courier.picoctf.net:49872 | sed -n '1,200p'
```

Salida (recortada):

```
HTTP/1.1 200 OK
Date: Mon, 11 May 2026 21:17:45 GMT
Server: Apache/2.4.38 (Debian)
X-Powered-By: PHP/7.2.34
Vary: Accept-Encoding
Content-Length: 1064
Content-Type: text/html; charset=UTF-8

<!doctype html>
<html>
<head>
	<title>Red</title>
	...
</html>
```

2) Petición HEAD (solo cabeceras) — en este caso el servidor devolvió una cabecera personalizada `flag` con la bandera:

```bash
curl -s -I http://wily-courier.picoctf.net:49872 | sed -n '1,200p'
```

Salida:

```
HTTP/1.1 200 OK
Date: Mon, 11 May 2026 21:17:45 GMT
Server: Apache/2.4.38 (Debian)
X-Powered-By: PHP/7.2.34
flag: picoCTF{r3j3ct_th3_du4l1ty_8b13f07}
Content-Type: text/html; charset=UTF-8
```

3) Petición PUT (ejemplo de modificación del método):

```bash
curl -s -X PUT http://wily-courier.picoctf.net:49872 -i | sed -n '1,200p'
```

Salida (recortada):

```
HTTP/1.1 200 OK
Date: Mon, 11 May 2026 21:17:45 GMT
Server: Apache/2.4.38 (Debian)
X-Powered-By: PHP/7.2.34
Vary: Accept-Encoding
Content-Length: 1060
Content-Type: text/html; charset=UTF-8

<!doctype html>
<html>
<head>
	<title>?</title>
	...
</html>
```

Estas salidas fueron usadas como evidencia durante la investigación y se añadieron al registro para documentar la metodología. Si desea que guarde capturas de pantalla reales (imágenes), indíquelo y las generaré (necesitaré permiso para crear archivos de imagen en el workspace y usar una herramienta para renderizar la página).