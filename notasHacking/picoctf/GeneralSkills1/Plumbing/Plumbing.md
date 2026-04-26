# Plumbing

## Descripción 
Sometimes you need to handle process data outside of a file. Can you find a way to keep the output from this program and search for the flag?
Connect to fickle-tempest.picoctf.net 56629.


## Solución

Este reto nos enseña a redirigir datos y salidas en la terminal de Linux, lo que se conoce como "tuberías" o *pipes*. El servidor envía muchísima información irrelevante de golpe, por lo que tenemos que filtrarla para encontrar la bandera escondida.

**Solución 1: Usando tuberías (Pipes `|`) — Método directo**
Podemos conectar la salida del comando `nc` (Netcat) directamente a la entrada del comando `grep` sin necesidad de guardar nada. El símbolo `|` hace de "tubería" entre ambos comandos:

```bash
nc fickle-tempest.picoctf.net 56629 | grep "picoCTF"
```

**Solución 2: Redirigiendo a un archivo (`>`) — Método alternativo**
Si preferimos guardar todo para analizarlo después, podemos usar el símbolo `>` para arrojar toda la salida del servidor en un archivo de texto llamado `salida` (tienes que presionar `Ctrl + C` después de unos segundos para detener la conexión). Luego, solo analizamos ese archivo combinando `cat` y `grep`:

```bash
nc fickle-tempest.picoctf.net 56629 > salida
cat salida | grep "pico"
```

*Cualquiera de los dos métodos aislará el texto correcto y te entregará la bandera:*
> `picoCTF{digital_plumb3r_8c8f3412}`


## Notas Adicionales

- El símbolo `|` (pipe / tubería) toma lo que un comando imprime y se lo entrega directamente al siguiente comando en la misma línea.
- El símbolo `>` redirige la salida de tu terminal hacia adentro de un archivo nuevo.


### Referencias