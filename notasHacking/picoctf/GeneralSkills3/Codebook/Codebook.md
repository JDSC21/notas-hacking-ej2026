# Codebook

## Description

Run the Python script `code.py` in the same directory as `codebook.txt`.

Download:

https://artifacts.picoctf.net/c/3/code.py
https://artifacts.picoctf.net/c/3/codebook.txt

## Solución

1. Descargar los ficheros del reto:

```bash
wget -q https://artifacts.picoctf.net/c/3/code.py -O code.py
wget -q https://artifacts.picoctf.net/c/3/codebook.txt -O codebook.txt
```

2. Inspeccionar `codebook.txt` (contiene la clave de sustitución):

```bash
cat codebook.txt
# azbycxdwevfugthsirjqkplomn
```

3. Ejecutar el script Python para obtener la flag (o leer el código para entender la decodificación):

```bash
python3 code.py
# picoCTF{c0d3b00k_455157_197a982c}
```

## Notas

- El script usa un `codebook` (cadena de sustitución) para decodificar la entrada, pero en este reto ejecutar `code.py` devuelve directamente la flag.
- `wget -q` descarga silenciosamente; omitir `-q` si se desea ver el progreso.
- Siempre revisar scripts desconocidos antes de ejecutarlos si no se dispone de un entorno aislado.

## Referencias

- Archivo `code.py`: https://artifacts.picoctf.net/c/3/code.py
- Archivo `codebook.txt`: https://artifacts.picoctf.net/c/3/codebook.txt
