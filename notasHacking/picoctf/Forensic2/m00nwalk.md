# m00nwalk

## Descripción

Decode this [message](https://challenge-files.picoctf.net/c_fickle_tempest/c9834b19f74a20802d7c53dc42fe1ccd8a69da4cf5c38fa5b6aab8ec472efdd3/message.wav) from the moon.
## Solución

```
#Instalamos un repositorio para transformar de audio a imagen 

┌──(superDsanchez㉿kali)-[~/picoCTF/forensic/moonwalk]
└─$ sstv -d message.wav -o result.png
[sstv] Searching for calibration header... Found!    
[sstv] Detected SSTV mode Scottie 1
[sstv] Decoding image...                                                                                                        [####################################################################################################] 100%
[sstv] Drawing image data...
[sstv] ...Done!
                                                                                                                                                                                                                                           
┌──(superDsanchez㉿kali)-[~/picoCTF/forensic/moonwalk]
└─$ open result.png

Y nos da una imagen con la flag
```

picoCTF{beep_boop_im_in_space}
## Notas adicionales

Aprendemos sobre sstv y la conversión de audio a imagen.
## Referencias

https://github.com/colaclanth/sstv
