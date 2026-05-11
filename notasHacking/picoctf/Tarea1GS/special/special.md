# special

## Descripción

Reto sobre una shell personalizada llamada "Special" que corrige ortografía y capitaliza comandos automáticamente. El objetivo es encontrar el flag navegando el sistema de archivos, lidiando con la sintaxis modificada de la shell.

## Datos de acceso

- Servidor: `saturn.picoctf.net`
- Puerto: `59081`
- Usuario: `ctf-player`
- Contraseña: `483e80d4`
- Comando: `ssh -p 59081 ctf-player@saturn.picoctf.net`

## Solución

1. Conectarse al servidor:
```bash
ssh -p 59081 ctf-player@saturn.picoctf.net
# Contraseña: 483e80d4
```

2. Explorar el sistema de archivos usando la shell "Special":
```bash
Special$ Clear & find
# Ignorar el error de "Clear" y buscar archivos
.
./blargh
./blargh/flag.txt
./.cache
./.cache/motd.legal-displayed
```

3. Leer el flag:
```bash
Special$ Clear & cat ./blargh/flag.txt
# Ignorar el error de "Clear"
picoCTF{5p311ch3ck_15_7h3_w0r57_b741d1b1}Special$ 
```

## Flag

`picoCTF{5p311ch3ck_15_7h3_w0r57_b741d1b1}`

## Notas

- La shell "Special" capitaliza comandos, lo que puede causar errores si el comando no existe en mayúsculas.
- Para ejecutar comandos correctamente, úsalos en minúsculas después del operador `&`.
- El flag se encuentra en `./blargh/flag.txt`.

## Referencias

- Uso de shells personalizadas
- Operador `&` en shell