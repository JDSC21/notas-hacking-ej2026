# Repetitions

## Description

Can you make sense of this file?

Download the file here:

https://artifacts.picoctf.net/c/471/enc_flag

## Solución

1. Descargar el archivo del reto:

```bash
wget https://artifacts.picoctf.net/c/471/enc_flag -O enc_flag
```

2. El fichero está codificado en Base64 varias veces. Una forma directa de obtener la flag es decodificar repetidamente:

```bash
# método explícito (6 veces):
cat enc_flag | base64 -d | base64 -d | base64 -d | base64 -d | base64 -d | base64 -d

# o con un bucle (más flexible):
data=$(cat enc_flag)
for i in {1..6}; do
  data=$(echo "$data" | base64 -d)
done
echo "$data"
```

3. Salida esperada (flag):

```text
picoCTF{base64_n3st3d_dic0d!n8_d0wnl04d3d_9b59b35c}
```

## Notas

- El reto consiste en detectar que el contenido es Base64 anidado y aplicarle la decodificación el número adecuado de veces.
- También se puede usar CyberChef para aplicar la operación "From Base64" repetidamente.
- Evitar tratar de ejecutar código no verificado; en este reto solo se necesita decodificar.

## Referencias

- Archivo del reto: https://artifacts.picoctf.net/c/471/enc_flag
- `base64` manual: https://man7.org/linux/man-pages/man1/base64.1.html
- CyberChef: https://gchq.github.io/CyberChef/
