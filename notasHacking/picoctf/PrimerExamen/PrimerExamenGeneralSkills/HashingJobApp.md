# HashingJobApp

## Descripción

If you want to hash with the best, beat this test!
`nc saturn.picoctf.net 57201`
## Solución

- Usando generador de texto en hash: https://www.md5hashgenerator.com/

```

└─$ nc saturn.picoctf.net 57201
Please md5 hash the text between quotes, excluding the quotes: 'hangnails'
Answer: 
7e3193d5ef5d764bfd8874dda4b5253a
7e3193d5ef5d764bfd8874dda4b5253a
Correct.
Please md5 hash the text between quotes, excluding the quotes: 'a haunted house'
Answer: 
ede833ae0b697454d64168e0e84cc730
ede833ae0b697454d64168e0e84cc730
Correct.
Please md5 hash the text between quotes, excluding the quotes: 'chimpanzees'
Answer: 
e5ab2ced9d181b61fec5d2c5c20a9de0
e5ab2ced9d181b61fec5d2c5c20a9de0
Correct.
picoCTF{4ppl1c4710n_r3c31v3d_3eb82b73}
```

## Notas adicionales

Usamos una página para convertir texto a md5 hash.
## Referencias

https://en.wikipedia.org/wiki/MD5