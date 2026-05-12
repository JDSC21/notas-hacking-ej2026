# shark on wire 1

## Descripción

We found this [packet capture](https://challenge-files.picoctf.net/c_fickle_tempest/134d2a2cf6ec5b7e757effc9b32977af7cc324b8e99a5ddb64737794a14dc18d/capture.pcap). Recover the flag.
## Solución

- Usando Wireshark

```
Seguimos las transmisiones hasta encontrar la bandera  6

Stream 6 UDP
picoCTF{StaT31355_636f6e6e}
```

picoCTF{StaT31355_636f6e6e}
## Notas adicionales

Pequeña introducción a wireshark y los paquetes de red.
## Referencias

https://pythoninstitute.org/pcap