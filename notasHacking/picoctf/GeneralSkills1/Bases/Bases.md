# Bases

## Descripción 
What does this bDNhcm5fdGgzX3IwcDM1 mean? I think it has something to do with bases.

## Solución

El título del reto y la descripción ("bases") nos dan una pista clave. El texto `bDNhcm5fdGgzX3IwcDM1` está codificado en **Base64** (un sistema muy común de codificación que usa letras mayúsculas, minúsculas y números).

Para resolverlo y obtener el texto original, puedes usar la terminal de Linux/Mac con el siguiente comando:

```bash
echo "bDNhcm5fdGgzX3IwcDM1" | base64 -d
```

*Salida resultante:* `l3arn_th3_r0p35`

Otra opción rápida es utilizar herramientas web como *CyberChef* o *base64decode.org*.

Por lo tanto, la bandera completa es:
`picoCTF{l3arn_th3_r0p35}`

## Notas Adicionales

### Referencias