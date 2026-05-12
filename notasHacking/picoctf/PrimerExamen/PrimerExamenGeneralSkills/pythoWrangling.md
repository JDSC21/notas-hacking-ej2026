# Python Wrangling

## Descripción

Python scripts are invoked kind of like programs in the Terminal... Can you run [ende.py](https://challenge-files.picoctf.net/c_wily_courier/2946b2b767f2d6792cb13dcfc9312c0fd5888dcabaf4196f2d88ae6d46f2a62c/ende.py) using [password.txt](https://challenge-files.picoctf.net/c_wily_courier/2946b2b767f2d6792cb13dcfc9312c0fd5888dcabaf4196f2d88ae6d46f2a62c/password.txt) to get [flag.txt.en](https://challenge-files.picoctf.net/c_wily_courier/2946b2b767f2d6792cb13dcfc9312c0fd5888dcabaf4196f2d88ae6d46f2a62c/flag.txt.en)?
## Solución

```
#Inspeccionamos primero el código

import sys

import base64

from cryptography.fernet import Fernet

  
  
  

usage_msg = "Usage: "+ sys.argv[0] +" (-e/-d) [file]"

help_msg = usage_msg + "\n" +\

"Examples:\n" +\

" To decrypt a file named 'pole.txt', do: " +\

"'$ python "+ sys.argv[0] +" -d pole.txt'\n"

  
  
  

if len(sys.argv) < 2 or len(sys.argv) > 4:

print(usage_msg)

sys.exit(1)

  
  
  

if sys.argv[1] == "-e":

if len(sys.argv) < 4:

sim_sala_bim = input("Please enter the password:")

else:

sim_sala_bim = sys.argv[3]

  

ssb_b64 = base64.b64encode(sim_sala_bim.encode())

c = Fernet(ssb_b64)

  

with open(sys.argv[2], "rb") as f:

data = f.read()

data_c = c.encrypt(data)

sys.stdout.write(data_c.decode())

  
  

elif sys.argv[1] == "-d":

if len(sys.argv) < 4:

sim_sala_bim = input("Please enter the password:")

else:

sim_sala_bim = sys.argv[3]

  

ssb_b64 = base64.b64encode(sim_sala_bim.encode())

c = Fernet(ssb_b64)

  

with open(sys.argv[2], "r") as f:

data = f.read()

data_c = c.decrypt(data.encode())

sys.stdout.buffer.write(data_c)

  
  

elif sys.argv[1] == "-h" or sys.argv[1] == "--help":

print(help_msg)

sys.exit(1)

  
  

else:

print("Unrecognized first argument: "+ sys.argv[1])

print("Please use '-e', '-d', or '-h'.")

#Ya sabiendo como usan las contraseñas corremos el programa


└─$ python3 ende.py -d ./flag.txt.en 
Please enter the password:720b6ad346f84cd483c60c7464dd95d4
picoCTF{4p0110_1n_7h3_h0us3_9c5f9bcf}
```

picoCTF{4p0110_1n_7h3_h0us3_9c5f9bcf}
## Notas adicionales

Inspeccionando el código sabemos que ocupamos mandarle 2 argumentos y posterior usar la contraseña que se nos dio para que nos de la flag.
## Referencias
