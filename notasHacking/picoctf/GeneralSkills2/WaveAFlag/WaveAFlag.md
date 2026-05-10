
# Wave a flag

## Descripción
Este reto muestra un binario que incluye una opción de ayuda. La idea es obtener información útil (la ayuda) sin ejecutar comportamiento no deseado del binario.

## Solución

Pasos recomendados (seguro y reproducible):

1) Descargar el binario (ejemplo):

```bash
wget https://challenge-files.picoctf.net/c_wily_courier/5a478d0b24d6a4f4185e3adb7a78c41cdad626fb02fe80e083dc33bf8b197d3d/warm -O warm
```

2) Inspeccionar el fichero sin ejecutar:

```bash
file warm
strings warm | head
```

3) Buscar si la ayuda o la bandera ya aparecen en texto plano:

```bash
strings warm | grep -i pico
strings warm | grep -Ei "-h|help"
```

4) Si decides obtener la ayuda con `-h`, hazlo con cautela (preferible en una VM/entorno aislado):

```bash
chmod +x warm        # solo si decides permitir ejecución
./warm -h
# Salida de ejemplo (según la instancia):
# Hello user! Pass me a -h to learn what I can do!
# Oh, help? I actually don't do much, but I do have this flag here: picoCTF{b1scu1ts_4nd_gr4vy_ac5832c}
```

La bandera encontrada en este reto es:

`picoCTF{b1scu1ts_4nd_gr4vy_ac5832c}`

## Notas Adicionales

- No ejecutes binarios desconocidos en tu máquina principal; usa una VM o sandbox.
- `strings` extrae secuencias de texto imprimible dentro de binarios y es la forma segura más rápida de buscar banderas.
- `file`, `hexdump`, `objdump` y `readelf` son útiles para análisis estático.
- Ten cuidado con comandos peligrosos (por ejemplo, `rm *` o `sudo rm -rf`) que puedas encontrar en ejemplos o scripts.

### Referencias

- `man strings`
- `man file`
- Prácticas seguras: sandbox / máquina virtual para ejecutar binarios.
