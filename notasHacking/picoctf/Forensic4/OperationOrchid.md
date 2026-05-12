# Operation Orchid

## Descripción

Download this disk image and find the flag. Note: if you are using the webshell, download and extract the disk image into `/tmp` not your home directory.

- [Download compressed disk image](https://artifacts.picoctf.net/c/214/disk.flag.img.gz)
## Solución

```
┌──(SuperDSanchez㉿kali)-[~/picoCTF/forensic/operationorchid]
└─$ sudo mkdir -p /tmp/foo
                                                                                                                                                                                                                                           
┌──(SuperDSanchez㉿kali)-[~/picoCTF/forensic/operationorchid]
└─$ sudo mount disk.flag.img /tmp/foo -o offset=$((411648*512))

┌──(SuperDSanchez㉿kali)-[~/picoCTF/forensic/operationorchid]
└─$ cd /tmp/foo       
                                                                                                                                                                                                                                           
┌──(SuperDSanchez㉿kali)-[/tmp/foo]
└─$ sudo su 
┌──(root㉿kali)-[/tmp/foo]
└─# cd root 
                                                                                                                                                                                                                                           
┌──(root㉿kali)-[/tmp/foo/root]
└─# ls -alps
total 4
1 drwx------  2 root root 1024 oct  6  2021 ./
1 drwxr-xr-x 22 root root 1024 oct  6  2021 ../
1 -rw-------  1 root root  202 oct  6  2021 .ash_history
1 -rw-r--r--  1 root root   64 oct  6  2021 flag.txt.enc

┌──(root㉿kali)-[/tmp/foo/root]
└─# cat .ash_history 
touch flag.txt
nano flag.txt 
apk get nano
apk --help
apk add nano
nano flag.txt 
openssl
openssl aes256 -salt -in flag.txt -out flag.txt.enc -k unbreakablepassword1234567
shred -u flag.txt
ls -al
halt

┌──(root㉿kali)-[/tmp/foo/root]
└─# openssl aes256 -d -in flag.txt.enc -out decrypt.txt
enter AES-256-CBC decryption password:
*** WARNING : deprecated key derivation used.
Using -iter or -pbkdf2 would be better.
bad decrypt
4077C665307F0000:error:1C800064:Provider routines:ossl_cipher_unpadblock:bad decrypt:../providers/implementations/ciphers/ciphercommon_block.c:107:

┌──(root㉿kali)-[/tmp/foo/root]
└─# cat decrypt.txt 
picoCTF{h4un71ng_p457_1d02081e} 
```

picoCTF{h4un71ng_p457_1d02081e}
## Notas adicionales

Realizamos una serie de pasos para indagar en el disco y obtener la flag.
## Referencias
