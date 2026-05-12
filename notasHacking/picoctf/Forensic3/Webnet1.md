# Webnet1

## Descripción

We found this [packet capture](https://challenge-files.picoctf.net/c_fickle_tempest/d1e9add4e31989553f239ebf71ba5972f9bed7bd4932f931e14bfba80d75f815/capture.pcap) and [key](https://challenge-files.picoctf.net/c_fickle_tempest/d1e9add4e31989553f239ebf71ba5972f9bed7bd4932f931e14bfba80d75f815/picopico.key). Recover the flag.
## Solución

- Usando wireshark
```
Se desencriptan los paquetes y la llave esta escondida dentro de una imagen en los detalles (en su encabezad)
picoCTF{honey.roasted.peanuts}
```

picoCTF{honey.roasted.peanuts}
## Notas adicionales

Al igual que el reto anterior solo es hacer uso de wireshark y desencriptar los paquetes con la llave solo que en este caso la flag esta mas escondida.
## Referencias
