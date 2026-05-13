# CanYouSee

## Descripción

How about some hide and seek? Download this file [here](https://artifacts.picoctf.net/c_titan/128/unknown.zip).
## Solución

```
Usamos `exiftool` para leer los metadatos XMP/EXIF incrustados en la imagen y luego decodificamos el valor en Base64.

Comandos reproducibles:

```bash
# Ver metadatos (muestra el campo "Attribution URL")
exiftool ukn_reality.jpg

# Decodificar la cadena Base64 encontrada en el campo (ejemplo):
echo 'cGljb0NURntNRTc0RDQ3QV9ISUREM05fZGVjYTA2ZmJ9Cg==' | base64 -d
```

Salida (bandera):

```
picoCTF{ME74D47A_HIDD3N_deca06fb}
```
## Notas adicionales

Usamos exiftool para ver detalles de la imagen.
## Referencias
