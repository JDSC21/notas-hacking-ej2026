
# Client-side-again

## Descripción

Portal de login que valida la contraseña en el cliente mediante JavaScript ofuscado. La URL del reto es:

```
http://fickle-tempest.picoctf.net:50200
```

Pista: "What is obfuscation?" — el JavaScript está ofuscado; desenmascararlo permitirá leer las comprobaciones y reconstruir la contraseña/flag.

## Solución

1. Descargar o abrir la página y localizar el JavaScript embebido (o `md5.js` si está enlazado). En este caso el HTML contiene código JS ofuscado que define una tabla de cadenas y una función `verify()`.

2. Desofuscar mentalmente (o con una herramienta): la tabla `_0x5a46` contiene las cadenas necesarias, y la función rota el array; tras normalizar la rotación las referencias se resuelven a nombres legibles:

```
_0x5a46 after rotation => [
	'getElementById','value','substring','picoCTF{','not_this',
	'daf93}','_again_4','this','Password Verified','Incorrect password'
]
```

3. Sustituir las referencias en la función `verify()` y analizar las comparaciones `substring(start,end)` usadas para validar la contraseña. Las comprobaciones piden que varios rangos del password coincidan con las cadenas de la tabla.

4. Extraer las porciones y concatenarlas en orden (desde el inicio hasta el final):

- substring(0,8) => `picoCTF{`
- substring(8,16) => `not_this`
- substring(16,24) => `_again_4`
- substring(24,32) => `daf93}`

Concatenando:

```
picoCTF{not_this_again_4daf93}
```

## Flag

`picoCTF{not_this_again_4daf93}`

## Notas

- El ofuscador reescribe nombres y rota arrays para dificultar la lectura. Normalmente basta con localizar la tabla de strings y aplicar la rotación (o usar herramientas como `jsnice`/`beautifier`) para recuperar los valores.
- No confíes en validaciones hechas sólo en el cliente; siempre valida en servidor.

## Referencias

- JavaScript obfuscation: https://jscrambler.com/code-integrity
- JavaScript deobfuscation: http://jsnice.org/ , https://beautifier.io/