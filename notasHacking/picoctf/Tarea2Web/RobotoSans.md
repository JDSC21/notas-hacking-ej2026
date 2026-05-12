# Roboto Sans

## Descripción

The flag is somewhere on this web application not necessarily on the website. Find it.Check [this](http://saturn.picoctf.net:65531/) out.
## Solución

```
# Me meto al archivo robots de la página 

User-agent *
Disallow: /cgi-bin/
Think you have seen your flag or want to keep looking.

ZmxhZzEudHh0;anMvbXlmaW
anMvbXlmaWxlLnR4dA==
svssshjweuiwl;oiho.bsvdaslejg
Disallow: /wp-admin/

#Decodifico ese texto de base64 y me dan 2 posibles rutas pruebo las 2 hasta 
#encontrar la correcta

┌──(flavio㉿kali)-[~]
└─$ echo anMvbXlmaWxlLnR4dA== | base64 -d
js/myfile.txt

picoCTF{Who_D03sN7_L1k5_90B0T5_22ce1f22}
```

picoCTF{Who_D03sN7_L1k5_90B0T5_22ce1f22}
## Notas adicionales

Repaso de el archivo robots.txt de una página web y base64
## Referencias
