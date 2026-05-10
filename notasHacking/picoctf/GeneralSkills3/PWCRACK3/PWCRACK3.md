 # PW CRACK 3
## Descripción

En este reto tienes tres artefactos:
- `level3.py` — script que pide una contraseña y, si su MD5 coincide con el hash almacenado, descifra el fichero cifrado.
- `level3.flag.txt.enc` — fichero cifrado que contiene la flag.
- `level3.hash.bin` — digest MD5 (en binario) de la contraseña correcta.

El script incluye una lista de 7 posibles contraseñas; sólo una de ellas produce el hash correcto. La función `str_xor` se usa para descifrar la flag (XOR con la clave repetida), por lo que una vez conoces la contraseña puedes reproducir la operación localmente.

## Resumen del resultado

- Contraseña correcta: `2295`
- Flag recuperada: `picoCTF{m45h_fl1ng1ng_6f98a49f}`

## Procedimiento recomendado (CLI) — automático y reproducible

1) Coloca los tres archivos en el mismo directorio (o descárgalos):

```bash
wget -q https://artifacts.picoctf.net/c/18/level3.py -O level3.py
wget -q https://artifacts.picoctf.net/c/18/level3.flag.txt.enc -O level3.flag.txt.enc
wget -q https://artifacts.picoctf.net/c/18/level3.hash.bin -O level3.hash.bin
```

2) Verifica que existen y mira el contenido del script (opcional):

```bash
ls -l level3.py level3.flag.txt.enc level3.hash.bin
nl -ba level3.py | sed -n '1,240p'
```

3) Método 1 — comparar MD5 (más limpio): generar el digest binario de cada candidato y compararlo con `level3.hash.bin` usando `cmp`:

```bash
candidates=("8799" "d3ab" "1ea2" "acaf" "2295" "a9de" "6f3d")
for pw in "${candidates[@]}"; do
  # generar digest MD5 binario para la contraseña candidata
  printf "%s" "$pw" | python3 -c "import sys,hashlib; sys.stdout.buffer.write(hashlib.md5(sys.stdin.read().encode()).digest())" > /tmp/pwhash.bin
  if cmp -s /tmp/pwhash.bin level3.hash.bin; then
    echo "MATCH: $pw"
    FOUND_PW="$pw"
    break
  fi
done
echo "Contraseña encontrada: $FOUND_PW"
```

4) Método 2 — ejecutar el checker no interactivo: probar los candidatos alimentando `stdin` (útil si quieres usar el propio script):

```bash
for pw in "${candidates[@]}"; do
  echo "Probando: $pw"
  if printf "%s\n" "$pw" | python3 level3.py |& grep -q "Welcome back"; then
    printf "%s\n" "$pw" | python3 level3.py
    break
  fi
done
```

5) Una vez tienes la contraseña (ej. `2295`), descifra el fichero localmente (evitas re-ejecutar `level3.py`):

```bash
PW=2295
python3 - <<PY
from pathlib import Path
def str_xor(secret, key):
    new_key = key
    i = 0
    while len(new_key) < len(secret):
        new_key = new_key + key[i]
        i = (i + 1) % len(key)
    return ''.join([chr(ord(s) ^ ord(k)) for s,k in zip(secret, new_key)])
enc = Path('level3.flag.txt.enc').read_bytes()
secret = enc.decode('latin-1')
print(str_xor(secret, PW))
PY
```

Esto imprimirá la flag.

## Método alternativo (manual, lo que hiciste en la webshell)

Si prefieres probar manualmente cada candidata, puedes ejecutar `python3 level3.py` y escribir cada contraseña cuando el script pida la entrada. Ejemplo resumido de tu sesión:

```
$ python3 level3.py
Please enter correct password for flag: hola
That password is incorrect
... (probaste varios candidatos)
Please enter correct password for flag: 2295
Welcome back... your flag, user:
picoCTF{m45h_fl1ng1ng_6f98a49f}
```

Otra variante con hash en texto: si quieres comparar en hexadecimal con `md5sum` y `hexdump`:

```bash
# calcular md5 (hex) de la candidata
printf "2295" | md5sum | awk '{print $1}'

# ver el digest binario como hex
hexdump -v -e '1/1 "%02x"' level3.hash.bin

# comparar visualmente (o usar cmp en binario)
```

Notas:
- `level3.hash.bin` está en formato binario (16 bytes). `md5sum` imprime hex; para comparar en binario conviene generar el digest binario con Python y usar `cmp`.
- Usar el método automatizado (MD5 + cmp) es más fiable cuando hay muchas candidatas.

## Explicación breve técnica

- `hash_pw` en el script calcula `md5(password)` y lo compara con `level3.hash.bin`.
- `str_xor` repite la clave hasta la longitud del texto cifrado y XORea byte a byte. Para reproducir la operación en Python, usamos `latin-1` para mapear bytes 1:1 a caracteres sin pérdida.

## Referencias

- Documentación `hashlib` (MD5): https://docs.python.org/3/library/hashlib.html
- `hexdump` / `xxd` para inspeccionar binarios

## Método alternativo (sesión en la webshell)

He añadido aquí tu método manual como alternativa documentada. En tu sesión probaste cada candidato interactivamente con `python level3.py` hasta encontrar el correcto; la transcripción relevante fue:

```
python level3.py
Please enter correct password for flag: hola
That password is incorrect
... (probaste varios candidatos)
Please enter correct password for flag: 2295
Welcome back... your flag, user:
picoCTF{m45h_fl1ng1ng_6f98a49f}
```

También comentaste el uso de `md5sum` para comparar hashes (workflow alternativo):

```bash
# obtener md5 hex del candidato
printf "2295" | md5sum | awk '{print $1}'

# obtener el digest almacenado como hex
hexdump -v -e '1/1 "%02x"' level3.hash.bin

# comparar ambos valores hex para identificar la contraseña correcta
```

Notas prácticas:
- `md5sum` muestra el hash en hexadecimal; `level3.hash.bin` está en binario, por eso usamos `hexdump` para convertirlo a hex legible.
- Para comparar en binario, es más robusto generar el digest binario con Python y usar `cmp` (como muestro en la sección principal).




