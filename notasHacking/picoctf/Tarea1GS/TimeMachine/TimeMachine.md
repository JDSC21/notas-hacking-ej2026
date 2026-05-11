superdsanchez-academy@webshell:~/drop-in$ ls
superdsanchez-academy@webshell:~/drop-in$ ls
## TimeMachine

## Descripción

Reto sobre el uso de mensajes de commit en Git para recuperar información importante. El flag está oculto en el mensaje de un commit anterior, no en el contenido de los archivos.

## Datos de acceso

- Archivo: `challenge.zip` (contiene un repositorio Git en `drop-in/`)
- Herramientas: `git`, `git log`

## Solución

1. Descargar y extraer los archivos:
```bash
wget https://artifacts.picoctf.net/c_titan/66/challenge.zip
unzip challenge.zip
cd drop-in
```

2. Revisar el historial de commits:
```bash
git log
```

3. Buscar el flag en los mensajes de commit. El flag aparece en el mensaje de uno de los commits:

```
picoCTF{t1m3m@ch1n3_d3161c0f}
```

## Flag

`picoCTF{t1m3m@ch1n3_d3161c0f}`

## Notas

- El flag no está en los archivos, sino en el mensaje de commit.
- Usar `git log` para revisar todos los mensajes históricos.
- Si hay muchos commits, puedes usar `git log --oneline` o buscar con `git log | grep picoCTF`.

## Referencias

- `git log` - ver historial de commits
- Mensajes de commit en Git
- Documentación Git: https://git-scm.com/docs