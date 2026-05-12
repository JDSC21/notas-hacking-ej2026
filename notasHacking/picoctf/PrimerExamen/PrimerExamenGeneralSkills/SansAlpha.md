# SansAlpha

## Descripción

The Multiverse is within your grasp! Unfortunately, the server that contains the secrets of the multiverse is in a universe where keyboards only have numbers and (most) symbols. `ssh -p 55092 ctf-player@mimas.picoctf.net` Use password: `1db87a14`
## Solución

``` 
#Nos dan una cadena base64 después de indagar 

SansAlpha$ /*/???[!_-]64 */????.*
cmV0dXJuIDAgcGljb0NURns3aDE1X211MTcxdjNyNTNfMTVfbTRkbjM1NV80OTQ1NjMwYX0=

#La decodeamos con cyberchef 

return 0 picoCTF{7h15_mu171v3r53_15_m4dn355_145256ec}
```

picoCTF{7h15_mu171v3r53_15_m4dn355_145256ec}
## Notas adicionales

Hacemos uso de wildcarts en lugar de letras del alfabeto para navegar por el sistema
## Referencias

https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/x11655.htmos 