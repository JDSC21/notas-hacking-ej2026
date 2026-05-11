# MatchTheRegex

## Descripción

Reto corto donde la página valida un input con una expresión regular. La pista del patrón está presente en el código cliente; enviando un input que coincida con ese patrón se obtiene la bandera desde la ruta `/flag`.

URL del reto: `http://saturn.picoctf.net:59879`

## Solución

Al inspeccionar el JavaScript de la página (función `send_request`) aparece un comentario que indica el patrón a coincidir:

```js
// ^p.....F!?
```

Interpretación: el input debe comenzar por la letra `p`, seguido de exactamente 5 caracteres cualesquiera, seguido de `F!?` (es decir, la secuencia literal `F!?`). Un ejemplo que cumple el patrón es `pAAAAAF!?`.

La aplicación expone una ruta que devuelve la bandera en formato JSON: `/flag?input=...`. Usando `curl` (con los caracteres especiales URL-encoded) se puede obtener la bandera:

```bash
# ejemplo que funciona
curl -s 'http://saturn.picoctf.net:59879/flag?input=pAAAAAF%21%3F' | jq -r .flag
```

Salida:

```
picoCTF{succ3ssfully_matchtheregex_f89ea585}
```

Nota: `%21` es `!` y `%3F` es `?` en codificación URL; hay que escapar esos caracteres al construir la URL.

## Notas

- Inspeccionar siempre el código cliente (`<script>`) cuando la página parece validar entradas en el navegador: muchas pistas se dejan ahí (comentarios, patrones, etc.).
- Para construir cadenas que cumplan un patrón `^p.....F!?` puede usarse cualquier herramienta o simplemente fabricarla manualmente (ej.: `p12345F!?`, `pHelloF!?`).
- Si necesita depurar rápidamente, abrir la consola del navegador y ejecutar `fetch('/flag?input=TU_INPUT').then(r=>r.json()).then(console.log)`.

## Referencias

- Expresiones regulares interactivas: https://regexr.com/
- `curl` manual: https://curl.se/docs/
