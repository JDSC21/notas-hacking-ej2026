# runme.py

## Description

Run the `runme.py` script to get the flag. Download the script with your browser or with `wget` in the webshell.

Download the script:

https://artifacts.picoctf.net/c/34/runme.py

## Solución

1. Descargar el script:

```bash
wget https://artifacts.picoctf.net/c/34/runme.py -O runme.py
```

2. Ejecutar el script con Python (siempre en un entorno seguro):

```bash
python3 runme.py
```

3. Salida esperada (flag):

```text
picoCTF{run_s4n1ty_run}
```

## Notas

- Ejecutar scripts desconocidos puede ser peligroso; si no hay un entorno aislado, inspeccionar el contenido primero con `cat runme.py` o ejecutar en una máquina virtual.
- El script de este reto es pequeño y devuelve directamente la flag al ejecutarlo.

## Referencias

- Archivo del reto: https://artifacts.picoctf.net/c/34/runme.py
- `python3` manual: https://docs.python.org/3/using/index.html
