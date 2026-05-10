# PW CRACK 2

## Description

This challenge is similar to PW CRACK 1: a small password checker (`level2.py`) and an encrypted flag file (`level2.flag.txt.enc`). The checker compares the entered password against a value assembled with `chr()` calls and, on success, decrypts the flag using the `str_xor` helper.

## Solución

We have the `level2.py` source (provided). Key lines:

```python
if( user_pw == chr(0x33) + chr(0x39) + chr(0x63) + chr(0x65) ):
    # ... decrypt with str_xor(flag_enc.decode(), user_pw)
```

- `chr(0x33)` = `'3'`
- `chr(0x39)` = `'9'`
- `chr(0x63)` = `'c'`
- `chr(0x65)` = `'e'`

Therefore the password literal assembled by the script is: `39ce`.

To obtain the flag, download the encrypted file alongside the checker and run it (it will prompt for the password):

```bash
# use these artifact URLs (corrected)
wget -q https://artifacts.picoctf.net/c/15/level2.py -O level2.py
wget -q https://artifacts.picoctf.net/c/15/level2.flag.txt.enc -O level2.flag.txt.enc
python3 level2.py
# When prompted, enter: 39ce
```

Observed run (webshell) and result:

```bash
printf "39ce\n" | python3 level2.py
Please enter correct password for flag: Welcome back... your flag, user:
picoCTF{tr45h_51ng1ng_502ec42e}
```

Recovered flag:

```
picoCTF{tr45h_51ng1ng_502ec42e}
```



Reproducing the decryption locally (same approach as PWCRACK1):

```python
from pathlib import Path

enc = Path('level2.flag.txt.enc').read_bytes()
key = '39ce'
secret = enc.decode('latin-1')
new_key = key
i = 0
while len(new_key) < len(secret):
    new_key = new_key + key[i]
    i = (i + 1) % len(key)
plain = ''.join([chr(ord(s) ^ ord(k)) for (s,k) in zip(secret, new_key)])
print(plain)
```

Run that after placing `level2.flag.txt.enc` in the same folder to print the cleartext flag.

## Notas

- The password is constructed in the source using `chr()` and hex byte values; converting those bytes to characters reveals the password.
- As in PWCRACK1, the `str_xor` helper repeats the key to match the secret length and XORs characters — use `latin-1` decoding when reconstructing raw bytes as characters.


## Explicación línea por línea (resumen)

- `str_xor(secret, key)`: extiende `key` hasta la longitud de `secret` y devuelve la XOR byte-a-byte entre ambos.
- `flag_enc = open('level2.flag.txt.enc', 'rb').read()`: lee el archivo cifrado en bytes.
- `user_pw = input(...)`: solicita la contraseña.
- `if( user_pw == chr(0x33) + chr(0x39) + chr(0x63) + chr(0x65) ):`: compara con la contraseña `39ce`.
- Si coincide, descifra con `str_xor(flag_enc.decode(), user_pw)` y muestra la flag.

## Referencias

- `chr()` Python built-in: https://docs.python.org/3/library/functions.html#chr
- `hexdump` / `xxd` for file inspection

---

