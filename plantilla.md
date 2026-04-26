# Plantilla

# Reto

## Descripción 

## Solución

## Notas Adicionales

### Referencias


## Sintáxis de MarkDown

# Título Principal (H1)
## Subtítulo (H2)
### Sección (H3)
#### Subsección (H4)

## Formato de texto

**Texto en negrita**
*Texto en cursiva* o _Texto en cursiva_
***Negrita y cursiva***
~~Texto tachado~~

## Listas

- Punto número uno
- Punto número dos
    - Subpunto (usando sangría/espacios al inicio)

1. Primer paso
2. Segundo paso
3. Tercer paso

### 4. Código (¡Muy útil para tus notas de hacking!)

Usa el comando `nmap -sV 192.168.1.1` para escanear la red.

Código en una sola línea: Úsalo dentro de un párrafo encerrándolo entre acentos graves (`).

Bloques de código: Usa tres acentos graves (```). Puedes escribir el nombre del lenguaje al lado para que VS Code coloree el código

```python
def resolver_rsa(p, q, e, c):
    n = p * q
    print("El módulo es", n)
```

### 5. Enlaces e Imágenes
**Enlaces:** Primero el texto entre corchetes `[]`, y justo al lado la ruta de tu archivo o URL de internet entre paréntesis `()`.
```markdown
[Ir a mi script de Python](./solve.py)
[Buscar en Google](https://www.google.com)
```

**Imágenes:**
```markdown
![Texto alternativo (por si no carga la imagen)](./captura-de-pantalla.png)
```

### 6. Citas (Blockquotes)
Útil para resaltar una parte importante o citar una salida de la terminal.
> Esto es una cita o un texto resaltado.

7. Tablas
Se crean usando barras verticales | y guiones -.

| Puerto | Servicio | Estado  |
| ------ | -------- | ------- |
| 22     | SSH      | Abierto |
| 80     | HTTP     | Cerrado |

Tip rápido en VS Code:
Para ver cómo va quedando todo esto, abre tu archivo .md y presiona Cmd + Shift + V (en Mac). Verás exactamente cómo este código

se transforma en un documento bonito y bien organizado.
    