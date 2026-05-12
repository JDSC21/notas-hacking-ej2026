# Local Authority

## Descripción

Can you get the flag?Go to this [website](http://saturn.picoctf.net:59908/) and see what you can discover.
## Solución

```
#Nos vamos al código de la página y vemos como verifica el user y contraseña en login.php

<!DOCTYPE html> <html lang="en"> <head> <meta charset="UTF-8"> <meta name="viewport" content="width=device-width, initial-scale=1.0"> <meta http-equiv="X-UA-Compatible" content="ie=edge"> <link rel="stylesheet" href="[style.css](view-source:http://saturn.picoctf.net:59908/style.css)"> <title>Login Page</title> </head> <body> <script src="[secure.js](view-source:http://saturn.picoctf.net:59908/secure.js)"></script> <p id='msg'></p> <form hidden action="[admin.php](view-source:http://saturn.picoctf.net:59908/admin.php)" method="post" id="hiddenAdminForm"> <input type="text" name="hash" required id="adminFormHash"> </form> <script type="text/javascript"> function filter(string) { filterPassed = true; for (let i =0; i < string.length; i++){ cc = string.charCodeAt(i); if ( (cc >= 48 && cc <= 57) || (cc >= 65 && cc <= 90) || (cc >= 97 && cc <= 122) ) { filterPassed = true; } else { return false; } } return true; } window.username = ""; window.password = ""; usernameFilterPassed = filter(window.username); passwordFilterPassed = filter(window.password); if ( usernameFilterPassed && passwordFilterPassed ) { loggedIn = checkPassword(window.username, window.password); if(loggedIn) { document.getElementById('msg').innerHTML = "Log In Successful"; document.getElementById('adminFormHash').value = "2196812e91c29df34f5e217cfd639881"; document.getElementById('hiddenAdminForm').submit(); } else { document.getElementById('msg').innerHTML = "Log In Failed"; } } else { document.getElementById('msg').innerHTML = "Illegal character in username or password." } </script> </body> </html>

#Podemos encontrar un usuario valido
function checkPassword(username, password)
{
  if( username === 'admin' && password === 'strongPassword098765' )
  {
    return true;
  }
  else
  {
    return false;
  }
}

#Ingresamos con ese usuario y nos da la flag

picoCTF{j5_15_7r4n5p4r3n7_a8788e61}
```

picoCTF{j5_15_7r4n5p4r3n7_a8788e61}
## Notas adicionales

Repaso de archivos php para validar usuarios.
## Referencias
