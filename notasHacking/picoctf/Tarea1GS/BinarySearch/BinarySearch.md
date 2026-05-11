# Binary Search

## Descripción

Reto sobre el algoritmo de búsqueda binaria. El objetivo es encontrar un número secreto entre 0 y 1000 usando solo 10 intentos. El servidor elige un número aleatorio y proporciona pistas ("más alto" o "más bajo") para guiar la búsqueda. Este reto enseña cómo aplicar el algoritmo de búsqueda binaria en un contexto práctico de ciberseguridad.

**Concepto:** La búsqueda binaria es eficiente porque cada intento elimina aproximadamente la mitad de las posibilidades restantes. Con 10 intentos es posible buscar entre $2^{10} = 1024$ valores.

## Datos de acceso

- Servidor: `atlas.picoctf.net`
- Puerto: `50394`
- Usuario: `ctf-player`
- Contraseña: `83dcefb7`
- Comando: `ssh -p 50394 ctf-player@atlas.picoctf.net`

## Solución

### Paso 1: Conectar al servidor
```bash
ssh -p 50394 ctf-player@atlas.picoctf.net
# Contraseña: 83dcefb7
# Aceptar fingerprint con: yes
```

### Paso 2: Ejecutar el programa
```bash
ls
# Buscar y ejecutar el programa del desafío
./guesser
```

### Paso 3: Aplicar búsqueda binaria

El algoritmo de búsqueda binaria funciona de la siguiente manera:

1. **Inicio:** Rango [0, 1000]
2. **Primer intento:** ~500 (punto medio)
3. **Según la respuesta:** Ajustar el rango
   - Si "mayor": nuevo rango [500, 1000]
   - Si "menor": nuevo rango [0, 500]
4. **Repetir:** Calcular nuevo punto medio y continuar

**Ejemplo de secuencia de intentos:**
- Intento 1: 500
- Intento 2: 250 o 750 (según respuesta anterior)
- Intento 3: 125, 375, 625 o 875
- Y así sucesivamente...

Con este método se garantiza encontrar el número en máximo 10 intentos.

## Flag

`picoCTF{g00d_gu355_ee8225d0}`

## Notas

- El servidor elige un número aleatorio cada conexión, por lo que cada intento requiere empezar desde cero.
- La importancia de comenzar desde 500 es que es el punto medio exacto del rango [0, 1000].
- La búsqueda binaria es fundamental en ciberseguridad para optimizar búsquedas en grandes volúmenes de datos (logs, reportes de vulnerabilidades, análisis forense).
- Cada intento fallido reduce el espacio de búsqueda a aproximadamente la mitad.
- Con $n$ intentos, se pueden búscar entre $2^n$ valores.

## Referencias

- Algoritmo de búsqueda binaria
- Logaritmos: $\log_2(1000) \approx 10$ (razón de 10 intentos para 1000 valores)
- Aplicaciones en ciberseguridad
- Eficiencia algorítmica: $O(\log n)$ vs búsqueda lineal $O(n)$