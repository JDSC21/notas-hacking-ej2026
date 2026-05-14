# Hash Crack

## Descripción

A company stored a secret message on a server which got breached due to the admin using weakly hashed passwords. Can you gain access to the secret stored within the server?

Connect to the server with:
```
$ nc verbal-sleep.picoctf.net 52434
```

## Solución

### Paso 1: Capturar el hash del servicio

Conectarse con nc al servicio:
```
$ nc verbal-sleep.picoctf.net 52434
```

El servicio imprime un hash que necesitas copiar. Ejemplo (el hash real será diferente):
```
Hash: 5f4dcc3b5aa765d61d8327deb882cf99
```

**Nota:** El hash anterior es md5("password") solo como ejemplo — debes usar el hash exacto que recibas.

### Paso 2: Usar CrackStation para romper el hash

**CrackStation** es una herramienta online que contiene tablas precomputadas de hashes y soporta muchos tipos (MD5, SHA1, etc).

1. Abre https://crackstation.net en tu navegador
2. Pega el hash copiado en el campo de entrada
3. Completa el CAPTCHA y haz clic en "Crack Hashes"
4. CrackStation devuelve la contraseña en texto plano si el hash coincide con sus tablas

### Paso 3: Usar la contraseña descifrada para obtener la flag

Después de que CrackStation devuelva la contraseña en texto plano, úsala para autenticarte en el servicio del desafío.

Reconecta y envía la contraseña cuando se solicite:
```
$ nc verbal-sleep.picoctf.net 52434
[server prompt]
<password>
```

El servidor responderá con la flag:

**Flag obtenida:**
```
picoCTF{UseStr0nG_h@shEs_&PaSswDs!_ccc21957}
```

## Notas adicionales

Este reto demuestra la importancia de usar funciones hash seguras y contraseñas fuertes. Las contraseñas almacenadas con algoritmos débiles como MD5 pueden ser fácilmente descifradas usando tablas arcoíris (rainbow tables) y herramientas online. Es fundamental usar algoritmos modernos como bcrypt, scrypt o Argon2 para almacenar contraseñas, junto con salt criptográfico.

## Referencias

- https://crackstation.net
- https://en.wikipedia.org/wiki/Rainbow_table
- https://en.wikipedia.org/wiki/MD5
