# IntroToBurp

## Descripción

Try [here](http://titan.picoctf.net:53414/) to find the flag
## Solución

- Usando BurpSuit
```
Si vemos la página nos pide datos y un codigo de autentificación

Realmentente no valida este código por lo que si interceptamos la solicitud y borramos este codigo de la petición accedemos a la página.

Welcome, sdsdsd you sucessfully bypassed the OTP request. Your Flag: picoCTF{#0TP_Bypvss_SuCc3$S_6bffad21}
```

picoCTF{#0TP_Bypvss_SuCc3$S_6bffad21}
## Notas adicionales

Un repaso de BurpSuit.
## Referencias
