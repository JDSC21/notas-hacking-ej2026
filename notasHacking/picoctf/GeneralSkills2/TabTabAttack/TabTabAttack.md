
# Tab,tab, attack

## Description
Using tabcomplete in the Terminal will add years to your life, esp. when dealing with long rambling directory structures and filenames.
Addadshashanammu.zip

## Solución

- Descargar el archivo del reto:

```bash
wget https://challenge-files.picoctf.net/c_wily_courier/730d9106a6ce1d52c6463b90937ec89f5eb661388954fbd15cfa0c8a2eec012f/Addadshashanammu.zip
```

- Descomprimir el ZIP:

```bash
unzip Addadshashanammu.zip
```

- Usar tab-completion para navegar por la estructura profunda de directorios y localizar el binario, o extraer la flag sin ejecutar el binario usando `strings`:

```bash
# Navegación (ejemplo):
cd Addadshashanammu/<TAB>...

# Ejecutar el binario (si se está en un entorno seguro):
./fang-of-haynekhtnamet

# Extraer la flag sin ejecutar:
strings fang-of-haynekhtnamet | grep pico
```

- Ejemplo de salida (flag encontrada):

```text
*ZAP!* picoCTF{l3v3l_up!_t4k3_4_r35t!_fc588427}
```

## Notas

- El reto se resuelve principalmente usando la autocompletación (`TAB`) para llegar al fichero dentro de una jerarquía muy profunda.
- No ejecutar binarios desconocidos en el equipo local; si no se dispone de un entorno aislado, usar `strings` o analizar en una máquina virtual.
- Tener cuidado con comandos peligrosos como `rm -rf`, que borran todo sin preguntar.

## Referencias

- Archivo del reto: https://challenge-files.picoctf.net/c_wily_courier/730d9106a6ce1d52c6463b90937ec89f5eb661388954fbd15cfa0c8a2eec012f/Addadshashanammu.zip
- `strings` man page: https://man7.org/linux/man-pages/man1/strings.1.html
