# WebNet0

## Descripción

We found this [packet capture](https://challenge-files.picoctf.net/c_fickle_tempest/66113619363fca174ef6bf56587007af1626f99c44fc5cf92333f9fd8876ce9a/capture.pcap) and [key](https://challenge-files.picoctf.net/c_fickle_tempest/66113619363fca174ef6bf56587007af1626f99c44fc5cf92333f9fd8876ce9a/picopico.key). Recover the flag.
## Solución

- Usando wireshark 
```
#Seguimos el archivo de paquetes y usamos la llave para desencriptarlos.

picoCTF{nongshim.shrimp.crackers}
```

picoCTF{nongshim.shrimp.crackers}
## Notas adicionales

Utilizamos wireshark para abrir un archivo de paquetes y una llave para desencriptarlos, ya solo seguimos el protocolo tls y  encontramos la llave
## Referencias

https://en.wikipedia.org/wiki/Transport_Layer_Security