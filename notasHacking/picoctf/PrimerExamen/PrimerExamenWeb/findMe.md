# findme

## Descripción

Help us test the form by submiting the username as `test` and password as `test!` The website running [here](http://saturn.picoctf.net:54611/).
## Solución
Identificar el problema con la contraseña: Descubrimos que el servidor rechazaba la autenticación con un código 200 OK plano porque la contraseña requería un signo de exclamación (test!).Evitar la interpretación de la terminal: Corregimos el comando usando comillas simples (') en el parámetro del password. Esto evitó que la terminal de tu Mac rompiera el signo ! por ser un carácter especial del historial.Capturar el primer fragmento: Enviamos la solicitud de inicio de sesión por POST al puerto activo. El servidor respondió con una redirección 302 hacia /next-page/id=, exponiendo la primera mitad de la flag en Base64: cGljb0NURntwcm94aWVzX2Fs.Corregir la ruta de navegación: Solucionamos un error de sintaxis de doble barra diagonal (//) en la URL para consultar correctamente la página intermedia.Capturar el segundo fragmento: Al consultar la ruta intermedia con el formato limpio, el servidor generó una nueva redirección que contenía la segunda mitad de la flag en Base64: bF90aGVfd2F5X2EwZmUwNzRmfQ==.Decodificar la Flag: Unimos ambas cadenas de texto en una sola línea continua y usamos el comando base64 --decode nativo de macOS para obtener la bandera limpia: picoCTF{proxies_all_the_way_a0fe074f}.
```
#Decodificamos la flag

cGljb0NURntwcm94aWVzX2FsbF90aGVfd2F5XzAxZTc0OGRifQ==

picoCTF{proxies_all_the_way_01e748db}

echo "cGljb0NURntwcm94aWVzX2FsbF90aGVfd2F5X2EwZmUwNzRmfQ==" | base64 --decode

```

picoCTF{proxies_all_the_way_a0fe074f}
## Notas adicionales

Al interceptar la solicitud a la página, encontramos 2 cadenas base64 en 2 páginas sin contenido en su url, las decodificamos y encontramos la flag
## Referencias
