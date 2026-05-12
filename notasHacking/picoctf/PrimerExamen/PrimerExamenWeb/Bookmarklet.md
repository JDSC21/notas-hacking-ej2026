# Bookmarklet

## Descripción

Why search for the flag when I can make a bookmarklet to print it for me? Browse [here](http://titan.picoctf.net:54213/), and find the flag!
## Solución

```
#La pagina nos da un codigo en javascript

        javascript:(function() {
            var encryptedFlag = "àÒÆÞ¦È¬ëÙ£ÖÓÚåÛÑ¢ÕÓÒËÉ§©í";
            var key = "picoctf";
            var decryptedFlag = "";
            for (var i = 0; i < encryptedFlag.length; i++) {
                decryptedFlag += String.fromCharCode((encryptedFlag.charCodeAt(i) - key.charCodeAt(i % key.length) + 256) % 256);
            }
            alert(decryptedFlag);
        })();
    
#Lo corremos y nos da la flag
picoCTF{p@g3_turn3r_e8b2d43b}```

picoCTF{p@g3_turn3r_e8b2d43b}## Notas adicionales

Corremos el código en la misma página inspeccionando en la parte de cosola.
## Referencias
