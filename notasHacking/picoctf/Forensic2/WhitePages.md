# WhitePages

## Descripción

I stopped using YellowPages and moved onto WhitePages... but [the page they gave me](https://challenge-files.picoctf.net/c_fickle_tempest/a8c97e66798b74645b536e392d4374d015529f1e9a812f5a68ed943dc4719e09/whitepages.txt) is all blank!
## Solución

```
from pwn import *

file = open('whitepages.txt','rb') 
data = bytearray(file.read())
data = data.replace(b'\xe2\x80\x83',b'0')
data = data.replace(b'\x20',b'1')
data = data.decode('ascii') 

data = unbits(data)
print(data)

┌──(superDsanchez㉿kali)-[~/picoCTF/forensic/whitepages]
└─$ python3 exp.py
b'\npicoCTF\n\nSEE PUBLIC RECORDS & BACKGROUND REPORT\n5000 Forbes Ave, Pittsburgh, PA 15213\npicoCTF{not_all_spaces_are_created_equal_57203502a1f295faf0d8cf42a1d4c769}\n'
```

picoCTF{not_all_spaces_are_created_equal_57203502a1f295faf0d8cf42a1d4c769}
## Notas adicionales

Convertimos los espacios a caracteres ASCII
## Referencias

https://en-wikipedia-org.translate.goog/wiki/Unicode?_x_tr_sl=en&_x_tr_tl=es&_x_tr_hl=es&_x_tr_pto=tc

https://en.wikipedia.org/wiki/UTF-8