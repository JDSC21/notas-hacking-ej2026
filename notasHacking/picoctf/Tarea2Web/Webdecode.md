# WebDecode

## Descripción

Do you know how to use the web inspector?Start searching [here](http://titan.picoctf.net:56554/) to find the flag
## Solución

```
#Navegamos por la página en busca de la flag, nos dice que puede estar en el codigo fuente del apartado "about", inspeccionando el código fuente

<!DOCTYPE html> <html lang="en"> <head> <meta charset="utf-8"/> <meta content="IE=edge" http-equiv="X-UA-Compatible"/> <meta content="width=device-width, initial-scale=1.0" name="viewport"/> <link href="[style.css](view-source:http://titan.picoctf.net:56554/style.css)" rel="stylesheet"/> <link href="[img/favicon.png](view-source:http://titan.picoctf.net:56554/img/favicon.png)" rel="shortcut icon" type="image/x-icon"/> <!-- font (google) --> <link href="[https://fonts.googleapis.com/css2?family=Lato:ital,wght@0,400;0,700;1,400&amp;display=swap](view-source:https://fonts.googleapis.com/css2?family=Lato:ital,wght@0,400;0,700;1,400&display=swap)" rel="stylesheet"/> <title> About me </title> </head> <body> <header> <nav> <div class="logo-container"> <a href="[index.html](view-source:http://titan.picoctf.net:56554/index.html)"> <img alt="logo" src="[img/binding_dark.gif](view-source:http://titan.picoctf.net:56554/img/binding_dark.gif)"/> </a> </div> <div class="navigation-container"> <ul> <li> <a href="[index.html](view-source:http://titan.picoctf.net:56554/index.html)"> Home </a> </li> <li> <a href="[about.html](view-source:http://titan.picoctf.net:56554/about.html)"> About </a> </li> <li> <a href="[contact.html](view-source:http://titan.picoctf.net:56554/contact.html)"> Contact </a> </li> </ul> </div> </nav> </header> <section class="about" notify_true="cGljb0NURnt3ZWJfc3VjYzNzc2Z1bGx5X2QzYzBkZWRfMDdiOTFjNzl9"> <h1> Try inspecting the page!! You might find it there </h1> <!-- .about-container --> </section> <!-- .about --> <section class="why"> <footer> <div class="bottombar"> Copyright © 2023 Your_Name. All rights reserved. </div> </footer> </section> </body> </html>

#Encontramos esta parte algo rara

<section class="about" notify_true="cGljb0NURnt3ZWJfc3VjYzNzc2Z1bGx5X2QzYzBkZWRfMDdiOTFjNzl9">

#Esta en base64 por lo que la decodificamos

picoCTF{web_succ3ssfully_d3c0ded_07b91c79}
```

picoCTF{web_succ3ssfully_d3c0ded_07b91c79}
## Notas adicionales

Repaso de paginas web.
## Referencias
