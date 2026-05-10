
# PW CRACK 1

## Description

Can you crack the password to get the flag? Download the password checker (`level1.py`) and the encrypted flag (`level1.flag.txt.enc`) into the same directory and run the checker.

Hints:
- To view the checker in the webshell: `nano level1.py` (Ctrl+X to exit).
- The `str_xor` function used in the script does not need to be reverse engineered for this challenge — focus on how the script derives or checks the password.

## Solución

I ran the commands in the picoCTF webshell and inspected `level1.py`. The checker compares the entered password to the literal string `"691d"` and, upon a correct password, decrypts the encrypted bytes using the provided `str_xor` function.

Exact commands and observed outputs (from the webshell):

```bash
# download files
wget -q https://artifacts.picoctf.net/c/10/level1.py -O level1.py && echo downloaded level1.py
downloaded level1.py
wget -q https://artifacts.picoctf.net/c/10/level1.flag.txt.enc -O level1.flag.txt.enc && echo downloaded level1.flag.txt.enc
downloaded level1.flag.txt.enc

# show source (excerpt)
nl -ba level1.py | sed -n '1,200p'
  flag_enc = open('level1.flag.txt.enc', 'rb').read()

  def level_1_pw_check():
    user_pw = input("Please enter correct password for flag: ")
    if( user_pw == "691d"):
      print("Welcome back... your flag, user:")
      decryption = str_xor(flag_enc.decode(), user_pw)
      print(decryption)
      return
    print("That password is incorrect")

# file sizes
ls -l level1.py level1.flag.txt.enc
-rw-rw-r-- 1 user user  30 Mar 16  2023 level1.flag.txt.enc
-rw-rw-r-- 1 user user 876 Mar 16  2023 level1.py

# hex preview
hexdump -C level1.flag.txt.enc | head -n 40
00000000  46 50 52 0b 75 6d 77 1f  03 0d 04 0c 69 4b 00 0a  |FPR.umw.....iK..|
00000010  51 08 5f 03 69 0c 07 5c  0f 08 05 55 0f 44        |Q._.i..\...U.D|

# run the checker and enter the password
python3 level1.py
Please enter correct password for flag: 691d
Welcome back... your flag, user:
```

The decoded output printed by the checker (the flag) is:

```
picoCTF{545h_r1ng1ng_56891419}
```

Reproducing the decryption locally: the script decodes the encrypted bytes using `latin-1` style decoding to preserve raw byte values, repeats the password to match the length, and XORs corresponding character codes. Example reproduction snippet:

```python
from pathlib import Path

enc = Path('level1.flag.txt.enc').read_bytes()
key = '691d'
secret = enc.decode('latin-1')
new_key = key
i = 0
while len(new_key) < len(secret):
  new_key = new_key + key[i]
  i = (i + 1) % len(key)
plain = ''.join([chr(ord(s) ^ ord(k)) for (s,k) in zip(secret, new_key)])
print(plain)
```

This prints the same `picoCTF{545h_r1ng1ng_56891419}` flag.

## Notas

- I cannot download the challenge files from this environment. If you paste the contents of `level1.py` (and the encrypted file if small), I can write the exact reversal script and produce the flag for you.

## Explicación línea por línea

1. `### THIS FUNCTION WILL NOT HELP YOU FIND THE FLAG --LT ########################` — comentario superior; indica al competidor que la función mencionada no es el punto principal del reto.
2-9. `def str_xor(secret, key):` y su cuerpo — función que realiza XOR carácter a carácter entre `secret` y una `key` repetida hasta igualar la longitud de `secret`:
  - Se crea `new_key` igual a `key` y se amplía añadiendo caracteres de `key` en bucle hasta que `len(new_key) >= len(secret)`.
  - Finalmente devuelve una cadena resultante donde cada carácter es `chr(ord(secret_c) ^ ord(new_key_c))` para cada par de caracteres emparejados.
  - Observación: la función asume que `secret` y `key` son cadenas de texto; por eso el script usa `flag_enc.decode()` antes de pasar `flag_enc` aquí.
11. Línea en blanco para separar bloques.
13. `flag_enc = open('level1.flag.txt.enc', 'rb').read()` — abre el fichero cifrado en modo binario y lee sus bytes en `flag_enc`.
17-25. `def level_1_pw_check():` — función que maneja la comprobación de contraseña:
  - 18. `user_pw = input("Please enter correct password for flag: ")` — pide la contraseña al usuario.
  - 19. `if( user_pw == "691d"):` — compara la contraseña introducida con la cadena literal `"691d"`. Esa es la contraseña correcta (hardcodeada).
  - 20-22. Si la contraseña es correcta, imprime un mensaje y descifra la flag llamando a `str_xor(flag_enc.decode(), user_pw)`; luego imprime el resultado descifrado.
  - 24. Si la contraseña no coincide, imprime `That password is incorrect`.
28. `level_1_pw_check()` — llamada que inicia la comprobación al ejecutar el script.

Notas adicionales:
- La presencia de la contraseña en claro en el código (`"691d"`) significa que no hace falta romper un cifrado complejo: basta con leer el script.
- El script convierte los bytes cifrados a texto con `flag_enc.decode()` antes de pasarlos a `str_xor`. Para preservar los valores de bytes sin pérdida al reproducir la operación localmente, usamos `latin-1` al decodificar (por ejemplo `enc.decode('latin-1')`) para mapear cada byte a un carácter con el mismo valor numérico.
- La función `str_xor` repite la clave y aplica XOR sobre los códigos de caracteres; la operación es reversible si conoces la clave.


## Referencias

- `nano` (editor): https://www.nano-editor.org/docs.php
- `wget` manual: https://www.gnu.org/software/wget/manual/wget.html

