# Secrets

## Descripción

We have several pages hidden. Can you find the one with the flag?The website is running [here](http://saturn.picoctf.net:62688/).
## Solución

```
#Vemos el codigo de la página y buscamos entre las paginas ocultas

view-source:http://saturn.picoctf.net:52816/secret/hidden/superhidden

#Encontramos la flag

<!DOCTYPE html> <html> <head> <title></title> <link rel="stylesheet" href="[mycss.css](view-source:http://saturn.picoctf.net:52816/secret/hidden/superhidden/mycss.css)" /> </head> <body> <h1>Finally. You found me. But can you see me</h1> <h3 class="flag">picoCTF{succ3ss_@h3n1c@10n_51b260fe}</h3> </body> </html>
```

picoCTF{succ3ss_@h3n1c@10n_51b260fe}
## Notas adicionales

Repaso de páginas web con extensiones que no directamente estan en la página original pero si en el codigo fuente.
## Referencias
