Big Zip

Description
## Description

Unzip this archive and find the flag.

Download the zip file. Hint: Can `grep` be instructed to look at every file in a directory and its subdirectories?

## Solución

1. Descargar y descomprimir el ZIP:

```bash
wget <ZIP_URL> -O bigzip.zip
unzip bigzip.zip -d bigzip_contents
```

2. Buscar la flag dentro de todos los archivos recursivamente (usar `-r` o `-R` en `grep`):

```bash
grep -R "pico" bigzip_contents
# o buscar específicamente el patrón 'picoCTF':
grep -R "picoCTF" bigzip_contents
```

3. Leer el archivo que contiene la flag con `cat` o `less`.

## Notas

- `grep -r` recorre directorios y busca en los ficheros regulares; usar `-n` para mostrar números de línea.
- Si los archivos son binarios o comprimidos internamente, puede ser necesario descomprimirlos todos primero.
- Evitar ejecutar binarios desconocidos; solo leer los ficheros de texto para extraer la flag.

## Referencias

- `grep` manual: https://man7.org/linux/man-pages/man1/grep.1.html
- `unzip` manual: https://linux.die.net/man/1/unzip

grep -r pico: Busca en cada directorio pico
