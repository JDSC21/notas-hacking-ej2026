# SQL Direct

## Descripción

Connect to this PostgreSQL server and find the flag! `psql -h saturn.picoctf.net -p 55452 -U postgres pico` Password is `postgres`
## Solución

```
pico-# \d
        Listado de relaciones
 Esquema | Nombre | Tipo  |  Dueño   
---------+--------+-------+----------
 public  | flags  | tabla | postgres
(1 fila)

pico=# select * from flags;
 id | firstname | lastname  |                address                 
----+-----------+-----------+----------------------------------------
  1 | Luke      | Skywalker | picoCTF{L3arN_S0m3_5qL_t0d4Y_31fd14c0}
  2 | Leia      | Organa    | Alderaan
  3 | Han       | Solo      | Corellia
(3 filas)

```

picoCTF{L3arN_S0m3_5qL_t0d4Y_31fd14c0}
## Notas adicionales

Un poco de sintaxis SQL Direct
## Referencias
