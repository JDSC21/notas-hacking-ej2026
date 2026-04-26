# Obedient Cat


## Descripción 
This file has a flag in plain sight (aka "in-the-clear").


## Solución

Este reto sirve para familiarizarnos con los comandos básicos de lectura de archivos en la terminal de Linux.

**Paso 1: Descargar el archivo**
Primero, utilizamos el comando `wget` para descargar el archivo del reto llamado `flag` directamente a nuestra computadora:

```bash
wget https://challenge-files.picoctf.net/c_wily_courier/4acf636990e4540d6fc36684b1256e625c0617d7cb01727e12e3f9606d89fe45/flag
```

**Paso 2: Leer el contenido del archivo**
Como la descripción nos dice que el archivo está en texto claro ("plain sight"), no necesitamos desencriptarlo; solo necesitamos leerlo.

Para ver el contenido de un documento de texto en la consola sin abrir un editor, usamos el comando `cat` (que viene de la palabra concatenar):

```bash
cat flag
```

*Al ejecutar ese comando, la terminal imprime el texto del archivo y nos revela la bandera:*
> `picoCTF{s4n1ty_v3r1f13d_9b8fa0bc}` 




## Notas Adicionales

### Referencias