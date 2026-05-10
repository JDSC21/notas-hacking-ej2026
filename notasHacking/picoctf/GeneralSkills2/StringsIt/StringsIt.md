Strings it

## Descripción
En este reto recibes un binario descargable pero no debes (y no conviene) ejecutarlo directamente. El objetivo es extraer la bandera sin correr código no confiable.

## Solución

Pasos recomendados para este tipo de retos:

1. Descargar el archivo (ejemplo):

```bash
wget https://challenge-files.picoctf.net/c_fickle_tempest/285538e2710605958a055500d6573657fcafea6308545cecfabb34462199cfd5/strings
```

2. Revisar el tipo de archivo (no ejecutar si es un binario):

```bash
file strings
```

3. NO ejecutar el binario directamente. En el ejemplo se intentó ejecutar y la salida sugiere usar la función "strings" en lugar de correrlo:

```bash
./strings            # => Permission denied (o podría ejecutar código peligroso)
chmod +x strings     # no recomendado salvo que confíes en la fuente
./strings            # esto ejecuta el binario (NO RECOMENDADO)
```

4. Extraer cadenas imprimibles desde el binario con la utilidad `strings` y filtrar la bandera:

```bash
strings strings | grep pico
# Resultado esperado:
# picoCTF{5tRIng5_1T_1067EC4c}
```

5. (Opcional) Verificar metadatos del binario con `ls -la` o `hexdump -C` si quieres analizarlo más en detalle:

```bash
ls -la strings
hexdump -C strings | head
```

**Por qué no ejecutar binarios desconocidos:**
- Ejecutar un binario descargado de una fuente externa puede ejecutar código malicioso en tu sistema. Por eso las técnicas seguras consisten en analizar el archivo (con `file`, `strings`, `hexdump`, `objdump`, etc.) y extraer información sin ejecutarlo.

## Notas Adicionales
- `strings` busca secuencias de bytes imprimibles dentro de un archivo (útil para encontrar mensajes, URLs o banderas). Puedes ajustar el tamaño mínimo de la cadena: `strings -n 6 filename`.
- `file` indica el tipo general del archivo (ELF, ASCII, etc.).
- `hexdump` y `xxd` permiten ver el contenido en hexadecimal si necesitas inspeccionar más profundamente.

## Bandera
`picoCTF{5tRIng5_1T_1067EC4c}`

### Referencias
- `man strings`
- `man file`
- `man hexdump`