# Static ain't always noise

## Description

Can you look at the data in this binary? The bash script might help!
static, ltdis.sh

## Solución

El reto propone descargar dos archivos: un binario (`static`) y un script de ayuda (`ltdis.sh`). El script ofrece una forma de disasembler el binario e extraer cadenas interpretables.

1. Descargar los archivos necesarios:

```bash
wget https://challenge-files.picoctf.net/c_wily_courier/418e2775a501eaabeb99a96c5c467a83539369fe9649e8234644250cfb72d717/ltdis.sh
wget https://challenge-files.picoctf.net/c_wily_courier/418e2775a501eaabeb99a96c5c467a83539369fe9649e8234644250cfb72d717/static
```

2. Comprobar el tipo de archivo y la presencia de los elementos:

```bash
file *
```

3. Dar permiso de ejecución al script de ayuda y usarlo con el binario:

```bash
chmod +x ltdis.sh
./ltdis.sh static
```

4. El script de ayuda genera un archivo de salida (`static.ltdis.strings.txt`) con las cadenas encontradas en el binario. Para encontrar la bandera directamente, se puede usar `strings` y buscar el patrón `pico`:

```bash
strings static | grep pico
```

La salida ofrece la bandera:

`picoCTF{d15a5m_t34s3r_20335e41}`

## Notas

- El script `ltdis.sh` intenta disensamblar el binario y extraer cadenas con offsets.
- La herramienta `strings` es útil cuando se buscan banderas en ejecutables porque extrae texto imprimible.
- Si el script falla con un nombre de archivo predeterminado (`a.out`), se debe pasar explícitamente el nombre correcto del binario.
- Se recomienda revisar primero el tipo de archivo antes de ejecutarlo.

## Referencias

- `man file`
- `man strings`
- `man chmod`
