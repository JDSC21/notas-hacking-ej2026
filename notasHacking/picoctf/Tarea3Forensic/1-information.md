# information

## Descripción

Files can always be changed in a secret way. Can you find the flag? [cat.jpg](https://challenge-files.picoctf.net/c_wily_courier/76e95e3e6ee69b4f82b3cea25051f5a9a5918b57809a1f90b29b06b776c73bc7/cat.jpg)
## Solución

```
┌──(SuperDSanchez㉿kali)-[~/picoCTF/t3forensic/information]
└─$ exiftool cat.jpg 
ExifTool Version Number         : 13.36
File Name                       : cat.jpg
Directory                       : .
File Size                       : 878 kB
File Modification Date/Time     : 2025:12:12 13:21:14-06:00
File Access Date/Time           : 2026:03:26 07:32:40-06:00
File Inode Change Date/Time     : 2026:03:26 07:32:34-06:00
File Permissions                : -rw-rw-r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.02
Resolution Unit                 : None
X Resolution                    : 1
Y Resolution                    : 1
Current IPTC Digest             : 7a78f3d9cfb1ce42ab5a3aa30573d617
Copyright Notice                : PicoCTF
Application Record Version      : 4
XMP Toolkit                     : Image::ExifTool 10.80
License                         : cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9
Rights                          : PicoCTF
Image Width                     : 2560
Image Height                    : 1598
Encoding Process                : Baseline DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 2560x1598
Megapixels                      : 4.1a 

#Cadena en base64 
cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9

#Decodificamos
picoCTF{the_m3tadata_1s_modified}
```

picoCTF{the_m3tadata_1s_modified}
## Notas adicionales

Usamos exiftool para ver los detalles del archivo, donde encontramos la flag codificada en base64.
## Referencias
