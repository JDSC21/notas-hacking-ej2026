
# fixme2.py

## Description

Fix the syntax error in the Python script so it prints the flag.

Download the script:

https://artifacts.picoctf.net/c/6/fixme2.py

## Solución

1. Descargar el script:

```bash
wget -q https://artifacts.picoctf.net/c/6/fixme2.py -O fixme2.py
```

2. Ejecutar el script para reproducir el error, editar y corregir la línea problemática (error típico: usar `=` en la condición en lugar de `==`):

```bash
python3 fixme2.py
# editar con nano/vim y corregir, por ejemplo cambiar `if flag = "":` por `if flag == "":`
nano fixme2.py
python3 fixme2.py
```

3. Salida esperada (flag):

```text
That is correct! Here's your flag: picoCTF{3qu4l1ty_n0t_4551gnm3nt_f6a5aefc}
```

## Notas

- El error mostrado indica una asignación en una condición; Python requiere `==` para comparar o `:=` para asignación con expresión.
- En ejecuciones anteriores también apareció un `NameError` por una variable no definida; asegúrate de que `flag_enc` y demás variables estén declaradas antes de usarlas.
- Siempre revisar el código antes de ejecutar en el sistema si no estás en un entorno aislado.

## Referencias

- Archivo del reto: https://artifacts.picoctf.net/c/6/fixme2.py
- PEP 8 / reglas de indentación y estilo: https://peps.python.org/pep-0008/
