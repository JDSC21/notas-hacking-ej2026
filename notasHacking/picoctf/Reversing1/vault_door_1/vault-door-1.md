# VaultDoor1


## Descripción

This vault uses some complicated arrays! I hope you can make sense of it, special agent. The source code for this vault is here: VaultDoor1.java
Hint: Look up the charAt() method online


## Solución
En foto está el comando en linux 
cat flag | sort | awk
Examinamos el código fuente en Java que se nos da
De la función checkPassword copiamos a un archivo, las lineas con password.charAt
Agregamos 0s a las cantidades para hacerlas de dos dígitos y poderlas ordenar
Ordenamos
cat flag | sort

Imprimimos 3a columna
cat flag | sort | awk '{print($3)}'

Quitamos comilla que abre y cierra
cat flag | sort | awk '{print($3)}' | tr -d "\'"  

Quitamos saltos de linea
cat flag | sort | awk '{print($3)}' | tr -d "'" | tr -d "\n"