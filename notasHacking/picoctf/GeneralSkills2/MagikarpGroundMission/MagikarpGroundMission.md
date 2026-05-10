# Magikarp Ground Mission

## Description

Do you know how to move between directories and read files in the shell? Start the container, ssh to it, and then ls once connected to begin.

Login via ssh as `ctf-player` with the password `8c606eb1` on the host `wily-courier.picoctf.net` and port `55536`.

## Solución

1. Conectar por SSH al host del reto (se pedirá la contraseña `8c606eb1`):

```bash
ssh ctf-player@wily-courier.picoctf.net -p 55536
```

Cuando se pregunte si confiar en la clave del host, responder `yes`.

2. Comandos usados dentro del contenedor para obtener las tres partes de la flag:

```bash
ls
cat 1of3.flag.txt
cat instructions-to-2of3.txt
cd /
ls
cat 2of3.flag.txt
cd ~
ls
cat 3of3.flag.txt
```

3. Resultado esperado (flag ensamblada):

```text
picoCTF{xxsh_0ut_0f_//4t3r_0b24fc4f}
```

## Notas

- El reto practica navegación básica en shell: `ls`, `cd`, `cat`.
- `cd` sin argumentos vuelve al directorio `~` (home).
- Evitar ejecutar binarios desconocidos; si hace falta, usar un entorno aislado.

## Referencias

- SSH manual: https://man.openbsd.org/ssh
- `ls`, `cd`, `cat`: páginas de manual (`man ls`, `man cd`, `man cat`)
