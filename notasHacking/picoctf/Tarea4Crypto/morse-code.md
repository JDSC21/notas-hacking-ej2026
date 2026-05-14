# Morse Code

## Descripción

Morse code is well known. Can you decrypt this?

Download the provided morse-code audio file.

**Instrucciones:**
- Wrap your answer with `picoCTF{}`
- Put underscores in place of pauses
- Use all lowercase

## Solución

### Conceptos Teóricos

**Código Morse:**
El código Morse es un método de codificación de caracteres a través de secuencias de puntos (dots) y rayas (dashes), separadas por pausas. Fue desarrollado originalmente para transmisión telegráfica.

**Estructura:**
- Punto (dot/dit): sonido corto (representado como .)
- Raya (dash/dah): sonido largo (representado como -)
- Pausa entre caracteres: espacio pequeño
- Pausa entre palabras: espacio grande (representado como _)

### Proceso de Descodificación

Para resolver este reto, existen varias herramientas disponibles:

1. **Morse Audio Decoder Online:** La opción más rápida
   - Sube el archivo de audio a https://www.morsecode.world/international/decoder/audio-decoder-2.html
   - La herramienta decodifica automáticamente
   - Transcribe el código Morse a texto

2. **Audacity + Inspección Manual:**
   - Abre el archivo en Audacity
   - Analiza visualmente las ondas sonoras
   - Identifica patrones de puntos y rayas
   - Traduce manualmente

3. **Espectrograma:**
   - Usa programas como GIMP o Audacity para ver el espectrograma
   - Identifica visualmente los patrones Morse

### Solución Práctica

```
Pasos:
1. Descargar el archivo morse-code.wav
2. Acceder a Morse Audio Decoder
3. Cargar el archivo de audio
4. Esperar a que se decodifique automáticamente
5. Reemplazar pausas con underscores (_)
6. Convertir a minúsculas
7. Envolver con picoCTF{}
```

**Flag obtenida:**
```
picoCTF{wh47_h47h_90d_w20u9h7}
```

## Notas adicionales

El código Morse es una forma antigua pero efectiva de codificación que fue revolucionaria en su tiempo. Aunque hoy en día no es común, entender cómo funciona es útil para:
- Comprender sistemas de codificación históricos
- Aprender sobre comunicaciones de emergencia (SOS)
- Desarrollar habilidades de análisis de patrones

Las herramientas online modernas hacen que la descodificación sea trivial, pero conocer la estructura subyacente es importante para entender la ciberseguridad.

## Referencias

- https://www.morsecode.world/international/decoder/audio-decoder-2.html
- https://en.wikipedia.org/wiki/Morse_code
- https://morsecode.scphillips.com/morse2.html

