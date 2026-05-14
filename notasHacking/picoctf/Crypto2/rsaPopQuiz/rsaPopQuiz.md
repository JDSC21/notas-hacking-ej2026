# Reto RSA POP QUIZ

## Descripción 
Class, take your seats! It's PRIME-time for a quiz...
nc fickle-tempest.picoctf.net 54266

## Solución

**Forma 2 -  automatizada Python - pwntools**

Script en Python para automatizar el proceso de solución (los valores pueden variar para cada usuario, deberas cambiarlos)
 
Instalar pwntools
`sudo apt install python3-pwntools`

```
##### PRODUCE THE FOLLOWING ####
plaintext
IS THIS POSSIBLE and FEASIBLE? (Y/N):
#### TIME TO SHOW ME WHAT YOU GOT! ###
plaintext: 
[+] Receiving all data: Done (115B)
[*] Closed connection to fickle-tempest.picoctf.net port 57911
Outstanding move!!!


If you convert the last plaintext to a hex number, then ascii, you'll find what you need! ;)

Bytes: b'picoCTF{wA8_th4till3aGal..o288ce54c}'
Flag: picoCTF{wA8_th4till3aGal..o288ce54c}

```

## Notas Adicionales
- El archivo se encuentra en la carptea
- Puede realizarse de forma manual pero es mejor un script que automatice todo
### Referencias

