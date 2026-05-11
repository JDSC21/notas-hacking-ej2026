# Collaborative

## Descripción

Reto sobre gestión de ramas en Git y fusión de código. El equipo ha dividido el flag en tres partes distribuidas en diferentes ramas de Git. El objetivo es localizar cada parte en las ramas `feature/part-1`, `feature/part-2` y `feature/part-3`, y luego combinarlas para obtener el flag completo.

## Datos de acceso

- Archivo: `challenge.zip` (contiene repositorio Git)
- Herramientas: `git`, editor de texto

## Solución

### Paso 1: Descargar y extraer
```bash
unzip challenge.zip
cd drop-in
```

### Paso 2: Explorar las ramas
```bash
git branch -a
```

Devuelve:
- `feature/part-1`
- `feature/part-2`
- `feature/part-3`

### Paso 3: Extraer cada parte del flag

**Rama 1:**
```bash
git checkout feature/part-1
cat flag.py
# Output: print("picoCTF{t3@mw0rk_", end='')
cp flag.py ../flag1.py
```

**Rama 2:**
```bash
git checkout feature/part-2
cat flag.py
# Output: print("m@k3s_th3_dr3@m_", end='')
cp flag.py ../flag2.py
```

**Rama 3:**
```bash
git checkout feature/part-3
cat flag.py
# Output: print("w0rk_e4b79efb}")
cp flag.py ../flag3.py
```

### Paso 4: Combinar y ejecutar
```bash
cd ..
cat flag1.py flag2.py flag3.py > flag.py
python flag.py
```

## Flag

`picoCTF{t3@mw0rk_m@k3s_th3_dr3@m_w0rk_e4b79efb}`

## Notas

- Cada rama contiene una porción del código que imprime una parte del flag.
- Es necesario visitar cada rama y copiar el contenido.
- La combinación correcta de los tres archivos produce el flag final.

## Referencias

- `git branch` - listar ramas disponibles
- `git checkout` - cambiar de rama
- `git log` - revisar historial de commits