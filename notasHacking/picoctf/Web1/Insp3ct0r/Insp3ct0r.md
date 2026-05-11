# Insp3ct0r

## Descripción

Kishor Balan nos alertó que el siguiente código necesita inspección:
http://fickle-tempest.picoctf.net:56152

¿Cómo inspeccionas código web en un navegador? El flag está dividido en 3 partes ubicadas en diferentes recursos de la página.

## Solución

### Paso 1: Acceder a la URL
```
http://fickle-tempest.picoctf.net:56152
```

### Paso 2: Inspeccionar el código fuente HTML

Haz clic derecho en la página y selecciona "Ver código fuente" (o presiona `Ctrl+U`).

Busca comentarios HTML. La primera parte del flag suele estar en un comentario:
```html
<!-- Part 1 of the flag: picoCTF{tru3_d3 -->
```

### Paso 3: Buscar referencias a archivos JS y CSS

En el código fuente identificarás referencias a archivos como:
- `my_awesome_script.js`
- `style.css`

### Paso 4: Abrir archivo JavaScript

Accede a: `http://fickle-tempest.picoctf.net:56152/my_awesome_script.js`

Busca comentarios en el archivo. La segunda parte del flag suele estar aquí:
```javascript
// Part 2 of the flag: t3ct1ve_0r_ju5t
```

### Paso 5: Abrir archivo CSS

Accede a: `http://fickle-tempest.picoctf.net:56152/style.css`

Busca comentarios en el archivo. La tercera parte del flag suele estar aquí:
```css
/* Part 3 of the flag:  _lucky?302945a7}} */
```

### Paso 6: Unir las tres partes

Concatena las tres partes:
```
Part 1: picoCTF{tru3_
Part 2: 0f_s0urc3_
Part 3: ag3nt_5e7e1b7}

Flag final: picoCTF{tru3_d3t3ct1ve_0r_ju5t_lucky?302945a7}
```

## Flag

`picoCTF{tru3_0f_s0urc3_ag3nt_5e7e1b7}`

## Notas

- En retos web, siempre revisa comentarios en el código fuente.
- Inspecciona archivos estáticos (JS, CSS) referenciados en la página.
- Usa las herramientas de desarrollador del navegador (F12) para explorar todos los recursos cargados.
- La pestaña "Red" (Network) permite ver todos los archivos cargados por la página.

## Referencias

- Inspector de elementos del navegador (F12)
- Ver código fuente (Ctrl+U o Cmd+U)
- Concepto de inspección web y análisis de fuentes
