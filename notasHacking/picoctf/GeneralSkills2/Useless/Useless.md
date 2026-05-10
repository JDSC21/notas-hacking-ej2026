# Useless

## Description
El reto provee un servidor SSH con un usuario que contiene un script llamado `useless` en su home. El objetivo es analizar el script y su documentación para encontrar la bandera sin ejecutar código peligroso.

Información del reto:
- Hostname: `saturn.picoctf.net`
- Port: `62330`
- Username: `picoplayer`
- Password: `password`

## Solución

1. Conéctate al servidor por SSH usando las credenciales dadas:

```bash
ssh picoplayer@saturn.picoctf.net -p 62330
```

2. Una vez dentro, revisa el directorio y el archivo `useless`:

```bash
pwd
ls -la
file useless
cat useless
```

3. El script `useless` es un script Bash simple que acepta tres argumentos: una operación y dos números. El código relevante es:

```bash
#!/bin/bash
# Basic mathematical operations via command-line arguments

if [ $# != 3 ]
then
  echo "Read the code first"
else
  if [[ "$1" == "add" ]]
  then
    sum=$(( $2 + $3 ))
    echo "The Sum is: $sum"
  elif [[ "$1" == "sub" ]]
  then
    sub=$(( $2 - $3 ))
    echo "The Substract is: $sub"
  elif [[ "$1" == "div" ]]
  then
    div=$(( $2 / $3 ))
    echo "The quotient is: $div"
  elif [[ "$1" == "mul" ]]
  then
    mul=$(( $2 * $3 ))
    echo "The product is: $mul"
  else
    echo "Read the manual"
  fi
fi
```

4. Prueba su funcionamiento con argumentos válidos:

```bash
./useless add 5 3   # -> The Sum is: 8
./useless sub 5 3   # -> The Substract is: 2
./useless mul 2 3   # -> The product is: 6
./useless div 6 3   # -> The quotient is: 2
```

5. Revisa el manual `man useless` y busca la bandera en la salida. En este reto, el manual incluye la bandera al final:

```bash
man useless
```

Dentro de la página de manual aparece la bandera:

`picoCTF{us3l3ss_ch4ll3ng3_3xpl0it3d_8504}`

## Notas

- El script no hace nada peligroso por sí mismo; su utilidad principal es guardar la bandera en el manual.
- Si no quieres ejecutar nada, usa `file` y lee el script con `cat` o `less` antes de interactuar.
- El comando `man useless` es la forma directa de ver la documentación instalada del script.
- Si trabajas con binarios o scripts desconocidos, hazlo en un entorno controlado (máquina virtual o contenedor).

## Referencias

- `man strings`
- `man file`
- `man bash`
