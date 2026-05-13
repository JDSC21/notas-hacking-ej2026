# Ph4nt0m 1ntrud3r

## Descripción

A digital ghost has breached my defenses, and my sensitive data has been stolen! 😱💻 Your mission is to uncover how this phantom intruder infiltrated my system and retrieve the hidden flag. To solve this challenge, you'll need to analyze the provided PCAP file and track down the attack method. The attacker has cleverly concealed his moves in well timely manner. Dive into the network traffic, apply the right filters and show off your forensic prowess and unmask the digital intruder! Find the PCAP file here [Network Traffic PCAP file](https://challenge-files.picoctf.net/c_verbal_sleep/3fe089c41615b9413666bedca922e07bf6ad8894a3dabd2737735143ad2396cf/myNetworkTraffic.pcap) and try to get the flag.
## Solución

```
#Usamos wireshark para ir consiguiendo la flag 

──(SuperDSanchez㉿kali)-[~/picoCTF/t3forensic/phantomintruder]
└─$ echo "cGljb0NURnsxdF93NHNudF90aDR0XzM0c3lfdGJoXzRyXzk2NmQwYmZiZfQ=" | base64 -d
picoCTF{1t_w4snt_th4t_34sy_tbh_4r_966d0bfb}
```

picoCTF{1t_w4snt_th4t_34sy_tbh_4r_966d0bfb}
## Notas adicionales

Usamos wireshark para encontrar las cadenas base64 y decodificarlas para que nos de la flag
## Referencias
