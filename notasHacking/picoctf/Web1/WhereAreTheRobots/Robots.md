# Where Are The Robots

## Descripción

Se proporciona una URL y hay que localizar "los robots" que suelen aparecer en `robots.txt` o en rutas listadas por éste. El objetivo es inspeccionar los recursos públicos del sitio para encontrar la pista o el flag.

URL objetivo:

```
http://fickle-tempest.picoctf.net:64768
```

## Solución

La forma rápida de resolver este reto es revisar el archivo `robots.txt` y seguir las rutas que indique. Haz lo siguiente en la terminal (o en el navegador):

```bash
# Obtener robots.txt
curl -s http://fickle-tempest.picoctf.net:64768/robots.txt

# Si robots.txt enumera rutas (por ejemplo /hidden/), listar su contenido:
curl -s http://fickle-tempest.picoctf.net:64768/hidden/

# También revisar index.html y buscar comentarios o enlaces
curl -s http://fickle-tempest.picoctf.net:64768 | sed -n '1,200p'
```

Ejemplo de flujo típico:

- `robots.txt` contiene una línea `Disallow: /robots/` o `Sitemap: /sitemap.xml`.
- Accede a la ruta listada (por ejemplo `http://.../robots/` o `http://.../sitemap.xml`) y busca pistas dentro de archivos o comentarios.

Si prefieres, pega aquí la salida de `curl -s http://fickle-tempest.picoctf.net:64768/robots.txt` y yo te indico la ruta exacta a seguir y edito el archivo para incluir el flag.

## Flag


El usuario obtuvo acceso a una ruta listada o descubierta inspeccionando el sitio:

```
http://fickle-tempest.picoctf.net:64768//cc6b1.html
```

Puedes abrirla en tu navegador o con `curl`:

```bash
curl -s http://fickle-tempest.picoctf.net:64768//cc6b1.html
```



## Notas

- `robots.txt` suele contener rutas que los administradores indican a los buscadores; en CTF suele esconderse una ruta útil.
- Si `robots.txt` no muestra nada útil, revisa `sitemap.xml`, comentarios en `index.html` o archivos JS/CSS referenciados.

## Referencias

- `robots.txt` — formato: https://www.robotstxt.org/
- Uso de `curl` y `sed` para inspección rápida
- Herramientas del navegador: pestaña "Network" para ver recursos cargados

