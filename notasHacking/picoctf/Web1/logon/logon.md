# logon

## Descripción

La fábrica está ocultando información a sus usuarios. Nos piden iniciar sesión como `Joe` para ver qué ha estado revisando.

URL del reto: `http://fickle-tempest.picoctf.net:56275`

Pista: "Hmm it doesn't seem to check anyone's password, except for Joe's?" — esto sugiere que la autenticación se gestiona de forma inadecuada (por ejemplo, confianza en cookies del cliente o lógica especial para `joe`).

## Solución (explicación paso a paso)

1. Inspecciona la página de login en el navegador (o con `curl`) y observa cómo se gestiona la sesión/identidad: ¿usa cookies, parámetros en la URL, tokens en formularios, etc.? En este reto la aplicación confía en valores del cliente (cookies) para identificar al usuario.

2. Prueba a manipular las cookies. Si la aplicación lee `username`, `password` o una bandera de `admin` desde las cookies sin validarlas en el servidor, basta con inyectar esas cookies en la petición para suplantar a un usuario.

3. Usando `curl` puedes enviar cabeceras `Cookie` directamente. Por ejemplo (comando de ejemplo incluido en el repositorio):

```bash
curl -s http://fickle-tempest.picoctf.net:50359/flag \
	-H "Cookie: password=carlos; username=carlos; admin=True" | grep pico
```

Explicación del comando:
- `-s`: modo silencioso de `curl`.
- La URL `/flag` es el endpoint que devuelve la bandera si la identidad/autorización es correcta.
- La cabecera `Cookie` se establece manualmente con pares `clave=valor` separados por `;`.
- `grep pico` filtra la salida para mostrar la cadena que contiene `picoCTF{...}`.

4. Si la aplicación no verifica las cookies en el servidor (o sólo aplica validación incompleta), el servidor considerará válida la identidad indicada en la cookie y devolverá la bandera.

Por qué esto funciona (resumen técnico):
- La seguridad no debe confiar en valores controlados por el cliente (cookies, parámetros ocultos) para autorizar acciones sensibles. Las cookies deben contener identificadores seguros (session IDs) que el servidor valide contra un almacén de sesiones, o bien deben estar firmadas/encriptadas.
- En este reto la lógica del servidor es débil: lee `username`/`password`/`admin` directamente desde la cookie y decide si devuelve la bandera, permitiendo suplantación.

## Notas

- Siempre valida la sesión y la identidad en el servidor; no confíes en valores del cliente.
- Una mitigación práctica: usar cookies con `HttpOnly`, `Secure`, y sesiones con identificadores almacenados y validados en el servidor.
- Para pruebas locales, `curl -H "Cookie: ..."` es útil para reproducir la petición que haría un navegador con cookies manipuladas.

## Referencias

- HTTP: https://developer.mozilla.org/en-US/docs/Web/HTTP
- HTTP headers: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers
- Request headers: https://developer.mozilla.org/en-US/docs/Glossary/Request_header
- Request methods: https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods
- Response headers: https://developer.mozilla.org/en-US/docs/Glossary/Response_header
- Response codes: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
- Cookies: https://en.wikipedia.org/wiki/HTTP_cookie

