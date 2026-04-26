# Whats a net cat?

## Descripción 
Using netcat (nc) is going to be pretty important. Can you connect to fickle-tempest.picoctf.net at port 54625 to get the flag?

## Solución

El reto nos pide conectarnos a un servidor remoto en un puerto determinado usando la herramienta `nc` (Netcat).

**Paso único: Conectarse al servidor**
En nuestra terminal de Linux/Mac, ejecutamos el comando `nc` seguido de la dirección web del servidor (`fickle-tempest.picoctf.net`) y el número de puerto (`54625`):

```bash
nc fickle-tempest.picoctf.net 54625
```

*Una vez establecida la conexión, el servidor nos responderá directamente con un mensaje de bienvenida devolviendo la bandera del reto:*
> `picoCTF{nEtCat_Mast3ry_5c7cC1a9}`

## Notas Adicionales
nc (netcat) es una herramienta de hacking que permita abrir puertos o conectarse a ellos
### Referencias

https://es.wikipedia.org/wiki/Netcat