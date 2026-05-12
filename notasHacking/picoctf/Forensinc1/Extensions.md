# extensions

## Descripción

This is a really weird text file. Can you find the flag?Get the flag from [TXT](https://challenge-files.picoctf.net/c_fickle_tempest/31fe772e6a4c71e867af0b2a93818e06d8f8ebf8af2a9615495d00356ff576da/flag.txt).
## Solución

```

└─$ mkdir extensions  
                                                                                                                                                                                                                                           

└─$ cd extensions 
                                                                                                                                                                                                                                           

└─$ wget https://challenge-files.picoctf.net/c_fickle_tempest/31fe772e6a4c71e867af0b2a93818e06d8f8ebf8af2a9615495d00356ff576da/flag.txt


└─$ file flag.txt
flag.txt: PNG image data, 1697 x 608, 8-bit/color RGB, non-interlaced


└─$ mv flag.txt flag.png
                                                                                                                                                                                                                                           

└─$ open flag.png
```

picoCTF{now_you_know_about_extensions}
## Notas adicionales

Cambiamos la extension correcta para abrir el archivo.
## Referencias

https://en-wikipedia-org.translate.goog/wiki/File_format?_x_tr_sl=en&_x_tr_tl=es&_x_tr_hl=es&_x_tr_pto=tc