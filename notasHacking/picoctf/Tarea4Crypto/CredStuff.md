# Cred Stuff

## Descripción

We found a leak of a blackmarket website's login credentials. Can you find the password of the user `cultiris` and successfully decrypt it?

Download the leak here.

**Nota:** El primer usuario en `usernames.txt` corresponde a la primera contraseña en `passwords.txt`. El segundo usuario corresponde a la segunda contraseña, y así sucesivamente.

## Solución

### Paso 1: Encontrar la posición de 'cultiris'

Necesitamos escribir un programa Python que encuentre la contraseña correspondiente para el usuario 'cultiris'. La clave es encontrar la posición (línea) del usuario en `usernames.txt` y luego usar ese mismo número de línea en `passwords.txt`.

```python
#!/usr/bin/env python3

username = "cultiris"
username_file = "leak/usernames.txt"
password_file = "leak/passwords.txt"

# Encontrar la posición de cultiris en leak/usernames.txt
def search_string_in_file(file_name, string_to_search):
    """Busca una cadena en el archivo y retorna las líneas que la contienen,
    junto con los números de línea"""
    line_number = 0
    list_of_results = []
    
    with open(file_name, 'r') as read_obj:
        for line in read_obj:
            line_number += 1
            if string_to_search in line:
                list_of_results.append((line_number, line.rstrip()))
    
    return list_of_results

# Encontrar cultiris
result = search_string_in_file(username_file, username)
print(result)  # Ejemplo: [(378, 'cultiris')]

# Extraer el número de línea
line_number = result[0][0]  # 378
```

**Resultado:** El usuario 'cultiris' se encuentra en la línea 378.

### Paso 2: Extraer la contraseña

Ahora extraemos la contraseña de la misma posición (línea 378) del archivo `passwords.txt`:

```python
# Leer todas las líneas de passwords.txt
lines = []
with open('leak/passwords.txt', 'rt') as psswd_file:
    for line in psswd_file:
        lines.append(line.rstrip())

# Obtener la contraseña en el índice 377 (line_number - 1)
encrypted_password = lines[377]
print(encrypted_password)  # cvpbPGS{P7e1S_54I35_71Z3}
```

**Resultado:** La contraseña encriptada es `cvpbPGS{P7e1S_54I35_71Z3}`

### Paso 3: Descifrar usando ROT13

La contraseña parece estar encriptada. Si buscamos 'pico' en el archivo de contraseñas, encontramos:
```
pICo7rYpiCoU51N6PicOr0t13
```

Esto sugiere usar **ROT13** para desencriptar:

```python
import codecs

encrypted_password = "cvpbPGS{P7e1S_54I35_71Z3}"

# Aplicar ROT13
decrypted_password = codecs.encode(encrypted_password, 'rot_13')
print(decrypted_password)
```

**Flag obtenida:**
```
picoCTF{C7r1F_54V35_71M3}
```

## Notas adicionales

Este reto enseña varios conceptos importantes:
- **Búsqueda en archivos:** Cómo encontrar datos específicos en archivos de texto grandes
- **Correspondencia de índices:** Entender cómo los datos correlacionados están posicionados
- **Cifrado ROT13:** Un cifrado simple por sustitución donde cada letra se rota 13 posiciones
- **Hints implícitos:** El texto "Picor0t13" en el archivo es una pista para usar ROT13

ROT13 es un método de encriptación muy simple y fácil de descifrar, pero es útil para ofuscación básica.

## Referencias

- https://en.wikipedia.org/wiki/ROT13
- https://rot13.com/
