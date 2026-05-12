# Secret of the Polyglot

## Descripción

The Network Operations Center (NOC) of your local institution picked up a suspicious file, they're getting conflicting information on what type of file it is. They've brought you in as an external expert to examine the file. Can you extract all the information from this strange file? Download the suspicious file [here](https://artifacts.picoctf.net/c_titan/97/flag2of2-final.pdf).
## Solución

```
┌──(SuperDSanchez㉿kali)-[~/picoCTF/t3forensic/secretofthepolyglot]
└─$ ls
flag2of2-final.pdf
                                                                                                                                                                                                                                           
┌──(SuperDSanchez㉿kali)-[~/picoCTF/t3forensic/secretofthepolyglot]
└─$ open flag2of2-final.pdf 
                                                                                                                                                                                                                                           
┌──(SuperDSanchez㉿kali)-[~/picoCTF/t3forensic/secretofthepolyglot]
└─$ convert flag2of2-final.pdf flag2of2-final.png 
                                                                                                                                                                                                                                           
┌──(SuperDSanchez㉿kali)-[~/picoCTF/t3forensic/secretofthepolyglot]
└─$ open flag2of2-final.png 

#Si abrimos el pdf nos da parte de la flag
1n_pn9_&_pdf_724b1287}

#Si convertimos el pdf a imagen nos da la primera parte de la flag
picoCTF{f1u3n7_
```

picoCTF{f1u3n7_1n_pn9_&_pdf_724b1287}
## Notas adicionales

Un mismo archivo puede tener información diferente cambiando su extensión (pdf o png)
## Referencias
