# convert.py

## Description

Run the Python script and convert the given number from decimal to binary to get the flag.

Download the Python script:

https://artifacts.picoctf.net/c/22/convertme.py

## Solución

1. Descargar el script del reto:

```bash
wget -q https://artifacts.picoctf.net/c/22/convertme.py -O convertme.py
```

2. Ejecutar el script con Python y responder a la pregunta (ejemplo mostrado):

```bash
python3 convertme.py
# Pregunta de ejemplo: If 97 is in decimal base, what is it in binary base?
# Respuesta: 01100001
```

3. Salida esperada (flag):

```text
picoCTF{4ll_y0ur_b4535_762f748e}
```

## Notas

- En Nano se puede navegar por líneas con atajos, y se pueden comentar/editar partes del script si es necesario para pruebas.
- También se puede usar CyberChef: "From Decimal" → "To Binary" para convertir números rápidamente.
- No ejecutar scripts sin revisar si no se dispone de un entorno aislado; en este reto el script solo solicita una conversión.

## Referencias

- Archivo del reto: https://artifacts.picoctf.net/c/22/convertme.py
- `python3` manual: https://docs.python.org/3/using/index.html
