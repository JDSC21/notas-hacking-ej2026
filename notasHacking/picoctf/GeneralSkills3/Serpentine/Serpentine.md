Serpentine
Serpentine

## Descripción

Reto sencillo: te dan un script en Python (`serpentine.py`) que presenta un menú con tres opciones: mostrar ánimo, mostrar la flag y salir. El objetivo es obtener la flag.

## Solución (procedimiento reproducible en CLI)

1) Abrir / descargar el script al directorio de trabajo y comprobar su contenido:

```bash
# si hace falta descargarlo (opcional):
# wget -q <URL_del_script> -O serpentine.py

# listar y revisar el script con numeración de líneas
ls -l serpentine.py
nl -ba serpentine.py | sed -n '1,240p'
```

2) Ejecutar el script e interactuar con el menú:

```bash
# ejecutar y seleccionar la opción para mostrar la flag
printf "b\n" | python3 serpentine.py
```

Con `printf "b\n" | python3 serpentine.py` enviamos la opción `b` por stdin (no hace falta teclearla manualmente). Si el script está correcto la salida mostrará la flag, por ejemplo:

```
Welcome to the serpentine encourager!

a) Print encouragement
b) Print flag
c) Quit

What would you like to do? (a/b/c) b
picoCTF{7h3_r04d_l355_7r4v3l3d_ae0b80bd}
```

3) Si el script no imprime la flag porque la función `print_flag` está “perdida” o no se llama, hay dos alternativas:

- Opción A — ejecutar la función desde Python directamente (si el script define `print_flag`):

```bash
# importar el módulo y llamar la función (evita ejecutar el menú)
python3 - <<PY
import serpentine
# si la función está definida como def print_flag():
serpentine.print_flag()
PY
```

- Opción B — parchear el script para forzar la impresión de la flag (edición rápida con `sed` o `nano`):

```bash
# editar con nano y añadir una llamada a print_flag() en el punto apropiado
nano serpentine.py
# o insertar la llamada con sed (ejemplo hipotético):
# sed -i "$ a\nprint_flag()" serpentine.py
```

Después de parchear, ejecutar de nuevo `python3 serpentine.py` o simplemente ejecutar `python3 -c "import serpentine; serpentine.print_flag()"`.

## Explicación técnica

- El script muestra un menú y espera la entrada del usuario (`input(...)`). La opción `b` debe llamar a la función que imprime la flag. Si el autor del reto dejó la función definida pero no enlazada al menú, basta con invocarla directamente o corregir el menú para que la llame.
- Si la flag no aparece en texto claro dentro del archivo, normalmente se genera dinámicamente (o está cifrada). En este reto la flag se imprime claramente cuando se ejecuta la función correcta.

## Notas

- Usar `printf "b\n" | python3 serpentine.py` es útil para automatizar la interacción.
- Importar el módulo (`import serpentine`) y llamar a `serpentine.print_flag()` evita ejecutar la parte interactiva si solo te interesa la flag.
- No ejecutes código desconocido en un equipo no seguro; usa la webshell de picoCTF o una VM aislada.

## Referencias

- `nl`, `sed`, `printf` para inspección y automatización en CLI
- `nano` / `vim` para editar el script
