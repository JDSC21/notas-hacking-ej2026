# Lets Warm Up

## Descripción

If I told you a word started with 0x70 in hexadecimal, what would it start with in ASCII?

## Solución

### Solución 1
Usando cyberchef 
https://gchq.github.io/CyberChef/#recipe=From_Hex('0x')&input=MHg3MA

### Solución 2 
Usando Python
```superdsanchez-picoctf@webshell:~$ python
Python 3.10.12 (main, Feb  4 2025, 14:57:36) [GCC 11.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> int(0x70)
112
>>> chr(112)
'p'
>>> ord(‘p’)
112

```

**picoCTF{p}**

## Notas

-Usamos la página 

## Referencias