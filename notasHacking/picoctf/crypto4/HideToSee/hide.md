Description

# Reto HidetoSee

## Descripción 
How about some hide and seek heh?
Look at this image here.



## Solución

Podemos usar el webshell de picoCTF luego cyberchef para descifrar el código
Abrimos la imagen, y vemos la palabra abatsh cipher que es el nombre de un algortimo de cifrado
Extraemos el texto dentro de la imagen con steghide y abrimos la imagen
`sudo apt install steghide
steghide --extract -sf atbash.jpg`

mostramos el texto encriptado dentro del archivo de texto que extragimos
`cat encrypted.txt`

Desencriptamos en ciberchef usando el nombre del algoritmo que descubrimos en la. imagen : atbash

## Notas Adicionales

### Referencias