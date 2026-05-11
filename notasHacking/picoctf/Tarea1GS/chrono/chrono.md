# Chrono

## Descripción

Reto sobre automatización de tareas periódicas en Linux. Te conectas con SSH a un servidor y debes localizar dónde está configurada la tarea programada que contiene la flag.

Datos de acceso:
- Servidor: `saturn.picoctf.net`
- Puerto: `55072`
- Usuario: `picoplayer`
- Contraseña: `kZx-HVJKu8`

## Solución

En este servidor la flag está en el archivo del cron del sistema, no en un cron de usuario ni en un timer de `systemd` de usuario. El archivo correcto es:

```bash
sudo cat /etc/crontab
```

Si quieres localizarla de forma directa, busca la cadena `picoCTF` o `flag` dentro de ese archivo:

```bash
grep -n -E 'picoCTF|flag' /etc/crontab
```

El reto se resuelve leyendo `/etc/crontab`, donde el mensaje contiene la flag.

```text
picoCTF{Sch3DUL7NG_T45K3_L1NUX_5b7059d0}
```

## Explicación

Aunque en el servidor también hay timers de `systemd`, el archivo con la información relevante era el cron del sistema. Esto es válido porque `cron` puede almacenar comandos y datos en `/etc/crontab`, y en este reto el contenido de ese archivo incluye la flag.

La clave fue comprobar que el archivo existe y leerlo con `cat`, luego filtrar por la cadena de la flag con `grep`.

## Notas

- En algunas sesiones anteriores el archivo `/etc/crontab` no estaba visible, por lo que parecía que no existía. En la sesión final sí estuvo disponible.
- Si la flag no aparece en `/etc/crontab`, prueba también con `find / -name 'crontab'` y `grep -RIn 'picoCTF' /etc /var /home`.
- Los timers de `systemd` (`*.timer`) son otra forma común de programar tareas periódicas, pero aquí el reto estaba en el cron clásico del sistema.

## Referencias

- `man crontab`
- `man 5 crontab`
- `grep` para buscar cadenas dentro de archivos