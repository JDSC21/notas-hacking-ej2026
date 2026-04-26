# First Grep

## Descripción 
Can you find the flag in the file? This would be really tedious to look through manually, something tells me there is a better way.
The flag is in this file.
## Solución

Este reto nos enseña a usar comandos de la terminal en Linux para buscar información específica dentro de un documento lleno de texto sin tener que leerlo a mano.

**Paso 1: Descargar el archivo**
Usamos el comando `wget` para descargar el archivo de texto a nuestra máquina (en tu caso, lo guardó como `file.2` de forma automática porque ya tenías otras descargas):

```bash
wget https://challenge-files.picoctf.net/c_fickle_tempest/2e9bfa4e1d90ac25a999fefdfb4feb8a2ff4eb73e4c61af4889a3762687ada01/file
```

**Paso 2: Buscar la bandera usando `grep`**
En lugar de abrir el archivo línea por línea en un editor, usamos la herramienta `grep`. Esta herramienta "filtra" y extrae únicamente las líneas de texto que coincidan con la palabra que le pasemos. 

Como sabemos que el formato de las respuestas siempre es "picoCTF{", le decimos a `grep` que busque eso dentro del archivo:

```bash
grep "picoCTF{" file.2
```

*La terminal nos devolverá únicamente la línea donde se oculta la respuesta:*
> `picoCTF{grep_is_good_to_find_things_29f42460}`

## Notas Adicionales

### Referencias