# Disk, disk, sleuth!

## Descripción

Use `srch_strings` from the sleuthkit and some terminal-fu to find a flag in this disk image. [dds1-alpine.flag.img.gz](https://challenge-files.picoctf.net/c_wily_courier/ae15f331b193f3e33b88ebbd7a054b6d48af0e2d8b79c53805b3eeab7cf2c9e5/dds1-alpine.flag.img.gz)
## Solución

```
┌──(SuperDSanchez㉿kali)-[~/picoCTF/forensic/diskdisksle]
└─$ gzip -d dds1-alpine.flag.img.gz 
                                                                                                                                                                                                                                           
┌──(SuperDSanchez㉿kali)-[~/picoCTF/forensic/diskdisksle]
└─$ ls                              
dds1-alpine.flag.img
                                                                                                                                                                                                                                           
┌──(SuperDSanchez㉿kali)-[~/picoCTF/forensic/diskdisksle]
└─$ strings dds1-alpine.flag.img | grep pico          
ffffffff81399ccf t pirq_pico_get
ffffffff81399cee t pirq_pico_set
ffffffff820adb46 t pico_router_probe
  SAY picoCTF{f0r3ns1c4t0r_n30phyt3_5e56e786}
                                                                                                                                                                                                                                           
┌──(SuperDSanchez㉿kali)-[~/picoCTF/forensic/diskdisksle]
└─$ 

```

picoCTF{f0r3ns1c4t0r_n30phyt3_5e56e786}
## Notas adicionales

Sacamos la flag de manera mas facil con strings y grep. 
## Referencias
