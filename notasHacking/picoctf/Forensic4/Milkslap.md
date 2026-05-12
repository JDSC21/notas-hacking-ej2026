# Milkslap

## Descripción

🥛 http://wily-courier.picoctf.net:49961/
## Solución

```
#La imagen es muy grande asi que la cortamos a una mas chica
┌──(superDsanchez㉿kali)-[~/picoCTF/forensic/Milkslap]
└─$ ffmpeg -i concat_v.png -vf "crop=1280:1000:0:0" parte_superior.png

#la leemos con zsteg
                                                                                                                                                                                                                                           
┌──(superDsanchez㉿kali)-[~/picoCTF/forensic/Milkslap]
└─$ zsteg parte_superior.png 
imagedata           .. text: "\n\n\n\n\n\n\t\t"
chunk:0:IHDR        .. file: Adobe Photoshop Color swatch, version 0, 1280 colors; 1st RGB space (0), w 0x3e8, x 0x802, y 0, z 0; 2nd HSB space (1), w 0, x 0, y 0, z 0
b1,b,lsb,xy         .. text: "picoCTF{imag3_m4n1pul4t10n_sl4p5}\n"
b2,r,lsb,xy         .. text: ["U" repeated 8 times]
b2,r,msb,xy         .. file: VISX image file
b2,g,lsb,xy         .. file: VISX image file
b2,g,msb,xy         .. file: SoftQuad DESC or font file binary - version 15722
b2,b,msb,xy         .. text: "UfUUUU@UUU"
b4,r,lsb,xy         .. text: "\"\"\"\"\"#4D"
b4,r,msb,xy         .. text: "wwww3333"
b4,g,lsb,xy         .. text: "wewwwwvUS"
b4,g,msb,xy         .. text: "\"\"\"\"DDDD"
b4,b,lsb,xy         .. text: "vdUeVwweDFw"
b4,b,msb,xy         .. text: "UUYYUUUUUUUU"

```

picoCTF{imag3_m4n1pul4t10n_sl4p5}
## Notas adicionales

Leemos una imagen con zsteg.
## Referencias
