# First Find

## Description

Unzip this archive and find the file named `uber-secret.txt`.

Download the zip file:

https://artifacts.picoctf.net/c/502/files.zip

## Solución

1. Descargar y descomprimir el ZIP:

```bash
wget https://artifacts.picoctf.net/c/502/files.zip -O files.zip
unzip files.zip -d files
```

2. Buscar el fichero `uber-secret.txt` dentro de la jerarquía extraída (ejemplo con `find`):

```bash
find files -name "uber*"
# resultado ejemplo:
# ./files/adequate_books/more_books/.secret/deeper_secrets/deepest_secrets/uber-secret.txt
```

3. Leer el archivo para obtener la flag:

```bash
cat ./files/adequate_books/more_books/.secret/deeper_secrets/deepest_secrets/uber-secret.txt
# picoCTF{f1nd_15_f457_ab443fd1}
```

## Notas

- El fichero objetivo está dentro de directorios ocultos (`.secret`) y en una ruta profunda; `find` es la forma más directa de localizarlo.
- También se puede usar `grep -R "picoCTF" files` para buscar la cadena de la flag en todos los archivos.
- Evitar ejecutar binarios desconocidos; aquí solo es necesario leer ficheros de texto.

## Referencias

- Archivo del reto: https://artifacts.picoctf.net/c/502/files.zip
- `find` manual: https://man7.org/linux/man-pages/man1/find.1.html
- `unzip` manual: https://linux.die.net/man/1/unzip
