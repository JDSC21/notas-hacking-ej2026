# Glory of the Garden

## Descripción

This file contains more than it seems.Get the flag from [garden.jpg](https://challenge-files.picoctf.net/c_fickle_tempest/ae74cbed5077635927f22095db7234ef717013f25d893a6993e4418696e586f0/garden.jpg).
## Solución

```
┌──(superdsanchez@kali)-[~]
└─$ cd picoCTF 
                                                                                                                                                                                                                                           
┌──(superdsanchez@kali)-[~/picoCTF]
└─$ cd forensic
                                                                                                                                                                                                                                           
┌──(superdsanchez@kali)-[~/picoCTF/forensic]
└─$ mkdir gloryofthegarden
                                                                                                                                                                                                                                           
┌──(superdsanchez@kali)-[~/picoCTF/forensic]
└─$ cd gloryofthegarden 
                                                                                                                                                                                                                                           
┌──(superdsanchez@kali)-[~/picoCTF/forensic/gloryofthegarden]
└─$ wget https://challenge-files.picoctf.net/c_fickle_tempest/ae74cbed5077635927f22095db7234ef717013f25d893a6993e4418696e586f0/garden.jpg

┌──(superdsanchez@kali)-[~/picoCTF/forensic/gloryofthegarden]
└─$ ls
garden.jpg
                                                                                                                                                                                                                                           
┌──(superdsanchez@kali)-[~/picoCTF/forensic/gloryofthegarden]
└─$ hexeditor garden.jpg
                                                                                                                                                                                                                                           
┌──(superdsanchez@kali)-[~/picoCTF/forensic/gloryofthegarden]
└─$ hexeditor garden.jpg
                                                                                                                                                                                                                                           
┌──(superdsanchez@kali)-[~/picoCTF/forensic/gloryofthegarden]
└─$ strings -n 13 garden.jpg| grep pico       
Here is a flag: picoCTF{more_than_m33ts_the_3y395e12915}
```

picoCTF{more_than_m33ts_the_3y395e12915}
## Notas adicionales

Vemos el contenido de binarios en una imagen  lcon un editor hexadecimal o filtramos a texto con strings en la consola.
## Referencias

https://en.wikipedia.org/wiki/Hex_editor