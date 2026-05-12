# shark on wire 2

## Descripción

We found this [packet capture](https://challenge-files.picoctf.net/c_fickle_tempest/ca7e8f9bb6b060dd724f90e3243aa3e36fc0d98c9b421cef0e860d1ff75f9ef0/capture.pcap). Recover the flag.
## Solución

```
from scapy.all import *

# Lee el archivo de captura de red
packets = rdpcap('capture.pcap')

flag = ''

for p in packets:
    # Filtra paquetes UDP con puerto de destino 22
    if UDP in p and p[UDP].dport == 22:
        # Si el puerto de origen es mayor a 5000, resta 5000 
        # y convierte el resultado a un carácter ASCII
        if p[UDP].sport > 5000:
            flag += chr(p[UDP].sport - 5000)

print(flag)

```

picoCTF{p1LLf3r3d_data_v1a_st3g0}
## Notas adicionales

La flag estaba los paquetes del puerto 22 UDP.
## Referencias
