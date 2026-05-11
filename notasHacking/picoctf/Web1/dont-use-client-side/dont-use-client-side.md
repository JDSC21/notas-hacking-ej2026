# dont-use-client-side
## Descripción
Portal de login que parecer ser "super seguro" pero que realiza validaciones de contraseña en el cliente (JavaScript). La URL del reto es:

```
http://fickle-tempest.picoctf.net:58045
```

Pista incluida: "Never trust the client" — esto indica que la validación se hace en el navegador y que podemos inspeccionar/leer el código JS para reconstruir la contraseña correcta.

## Solución

1. Abrir la página en el navegador o descargarla con `curl`:

```bash
curl -s http://fickle-tempest.picoctf.net:58045 | sed -n '1,200p'
```

2. En el código fuente verás una función `verify()` que comprueba porciones (substrings) de la contraseña con un valor `split = 4`.

Fragmento relevante (resumido):

```javascript
split = 4;
if (checkpass.substring(0, split) == 'pico') {
	if (checkpass.substring(split*6, split*7) == 'eb02') {
		if (checkpass.substring(split, split*2) == 'CTF{') {
			if (checkpass.substring(split*4, split*5) == 'ts_p') {
				if (checkpass.substring(split*3, split*4) == 'lien') {
					if (checkpass.substring(split*5, split*6) == 'lz_2') {
						if (checkpass.substring(split*2, split*3) == 'no_c') {
							if (checkpass.substring(split*7, split*8) == 'b45}') {
								alert("Password Verified")
							}
						}
					}
				}
			}
		}
	}
}
```

3. Reconstruir la contraseña correcta concatenando las partes en el orden de sus rangos (desde `substring(0, split)` hasta `substring(split*7, split*8)`). Las partes encontradas son (por índice de bloque):

- 0: `pico`
- 1: `CTF{`
- 2: `no_c`
- 3: `lien`
- 4: `ts_p`
- 5: `lz_2`
- 6: `eb02`
- 7: `b45}`

Concatenando en ese orden:

```
picoCTF{no_clients_plz_2eb02b45}
```

4. Validación rápida (ejemplo en Python si quieres reconstruirlo desde el código):

```python
parts = ['pico','CTF{','no_c','lien','ts_p','lz_2','eb02','b45}']
flag = ''.join(parts)
print(flag)
# -> picoCTF{no_clients_plz_2eb02b45}
```

## Flag

`picoCTF{no_clients_plz_2eb02b45}`

## Notas

- Nunca confíes en validaciones hechas únicamente en el cliente: todo el código y datos del cliente son visibles y manipulables.
- Las aplicaciones deben validar credenciales en el servidor y no depender de valores enviados desde el cliente para decisiones sensibles.
- Para investigar estos retos puedes usar `curl`, `wget` o las herramientas de desarrollador del navegador (F12) para revisar JavaScript y comentarios.

## Referencias

- Cliente vs servidor: https://www.educative.io/answers/client-side-vs-server-side
- Firefox debugger: https://firefox-source-docs.mozilla.org/devtools-user/debugger/index.html
