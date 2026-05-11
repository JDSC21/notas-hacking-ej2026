# picobrowser

## Descripción

Sitio que sólo muestra el contenido correcto si el navegador envía un `User-Agent` concreto (`picobrowser`). El objetivo es acceder al endpoint `/flag` con ese User-Agent para obtener el flag.

URL del reto:

```
http://fickle-tempest.picoctf.net:56286
```

## Solución (pasos)

1. El sitio muestra un enlace a `/flag`, pero al acceder normalmente puede no mostrar el contenido correcto. Inspecciona las cabeceras y el HTML para ver si hay condicionantes por `User-Agent`.

2. La forma más rápida es solicitar el recurso con `curl` enviando la cabecera `User-Agent: picobrowser`:

```bash
curl -s http://fickle-tempest.picoctf.net:56286/flag -H "User-Agent: picobrowser" | sed -n '1,200p'
```

3. La respuesta contiene el flag en el HTML cuando se envía el `User-Agent` correcto.

## Flag

`picoCTF{p1c0_s3cr3t_ag3nt_fba5c48f}`

## Notas

- El `User-Agent` es una cabecera HTTP que el servidor puede usar para adaptar la respuesta al cliente. No es fiable como mecanismo de autenticación o control de acceso.
- Para reproducir esto en un navegador puedes usar una extensión que cambie el `User-Agent` (por ejemplo, "User-Agent Switcher and Manager").
- En automatización o pruebas, `curl -H "User-Agent: ..."` permite enviar la cabecera manualmente.

## Referencias

- Cabeceras HTTP: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers
- `curl` manual de uso de cabeceras: https://curl.se/docs/manpage.html