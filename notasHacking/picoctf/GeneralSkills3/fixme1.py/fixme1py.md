# fixme1.py

## Description

Fix the syntax/indentation error in the provided Python script so it prints the flag.

Download the script:

https://artifacts.picoctf.net/c/25/fixme1.py

## Solución

1. Descargar el script:

```bash
wget -q https://artifacts.picoctf.net/c/25/fixme1.py -O fixme1.py
```

2. Ejecutar el script con Python para ver el error y corregir la indentación:

```bash
python3 fixme1.py
# Si aparece un IndentationError, editar con un editor (nano, vim) y corregir la sangría
nano fixme1.py
# corregir la indentación en la línea problemática
python3 fixme1.py
```

3. Salida esperada (flag):

```text
That is correct! Here's your flag: picoCTF{1nd3nt1ty_cr1515_6a476c8f}
```

## Notas

- El error común es una indentación inconsistente (mezcla de tabuladores y espacios o sangría extra).
- Editar el archivo y asegurar que los bloques `if`/`for`/`def` están correctamente indentados con espacios coherentes.
- Si no se desea editar, mostrar el contenido con `sed -n '1,120p' fixme1.py` y corregir la línea indicada.

## Referencias

- Archivo del reto: https://artifacts.picoctf.net/c/25/fixme1.py
- Guía de indentación en Python: https://docs.python.org/3/reference/lexical_analysis.html#indentation
