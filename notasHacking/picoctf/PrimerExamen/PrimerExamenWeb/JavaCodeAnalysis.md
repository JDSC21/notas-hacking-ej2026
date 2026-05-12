# Java Code Analysis!!

## Descripción

BookShelf Pico, my premium online book-reading service.I believe that my website is super secure. I challenge you to prove me wrong by reading the 'Flag' book!Here are the credentials to get you started:

- Username: "user"
- Password: "user"

Source code can be downloaded [here](https://artifacts.picoctf.net/c/483/bookshelf-pico.zip).Website can be accessed [here!]http://saturn.picoctf.net:49230/#/.
## Solución

La vulnerabilidad principal se encuentra en el código fuente de Java, específicamente en cómo se genera el secreto para los JSON Web Tokens (JWT). El servidor utiliza un secreto estático y débil (`"1234"`) si no encuentra un archivo de configuración.

El plan de ataque es:
1. Iniciar sesión como el usuario `user`.
2. Crear un nuevo JWT (token) con el rol (`role`) cambiado a `"Admin"`.
3. Firmar este nuevo token usando el secreto débil `"1234"`.
4. Reemplazar el `AuthToken` en el almacenamiento local del navegador con nuestro token modificado.

A continuación se muestra un ejemplo del *payload* (la información contenida en el token) que se debe usar. Es crucial que las fechas `iat` (emitido el) y `exp` (expiración) sean válidas, de lo contrario el servidor rechazará el token.

```json
{
  "role": "Admin",
  "iss": "bookshelf",
  "exp": 1779180837,
  "iat": 1778576037,
  "userId": 2,
  "email": "admin"
}
```

**Contraseña del cifrado (secreto JWT):** `1234`

Al usar un token con un payload como el anterior, firmado con el secreto correcto, se obtiene acceso de administrador y se puede leer el libro que contiene la bandera.

**Bandera:**
```
picoCTF{w34k_jwt_n0t_g00d_d72df65e}
```

## Notas adicionales

Nos logeamos como `user` y luego forjamos un nuevo JWT para escalar privilegios a `Admin`. La clave fue no solo cambiar el rol, sino también asegurarse de que las marcas de tiempo (`iat` y `exp`) del token fueran válidas en el momento de la solicitud. Un token con fechas futuras o ya expiradas será rechazado por el servidor, resultando en un error al cargar el panel de control.

## Referencias

- Para conseguir la cookie admin
	https://jwt.tplant.com.au/