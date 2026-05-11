Someone's commits seems to be preventing the program from working. Who is it?
You can download the challenge files here:
challenge.zip
# BlameGame

## Descripción

Reto para identificar al autor que introdujo cambios problemáticos usando herramientas de control de versiones. El ejercicio pide inspeccionar el historial del repositorio para encontrar quién realizó el commit que rompe el programa.

## Datos de acceso

- Archivo: `challenge.zip` (contiene un repositorio Git)
- Herramientas: `git`, `git log`, `git blame`, editor de texto

## Solución

### Paso 1: Descargar y extraer
```bash
wget https://artifacts.picoctf.net/c_titan/157/challenge.zip
unzip challenge.zip
cd drop-in
```

### Paso 2: Inspeccionar el historial
```bash
git log
```

El comando `git log` muestra los commits recientes; usar `git blame <file>` permite ver línea por línea quién y cuándo se modificó un archivo.

### Resultado observado

Al inspeccionar el historial y los autores de los cambios se encuentra el flag (impreso en la salida del `git log` del reto):

```
picoCTF{@sk_th3_1nt3rn_cfca95b2}
```

## Flag

`picoCTF{@sk_th3_1nt3rn_cfca95b2}`

## Notas

- `git log` muestra el historial de commits y mensajes asociados.
- `git blame <file>` asigna cada línea de un archivo a un commit/autor específico, útil para identificar quién introdujo un cambio.
- En proyectos colaborativos, revisar el historial es clave para entender cuándo y por qué se introdujeron bugs.

## Referencias

- `git log` - ver historial de commits
- `git blame` - ver autoría línea a línea
- Documentación Git: https://git-scm.com/docs