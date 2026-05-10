## Super SSH

## Description

Using a Secure Shell (SSH) is going to be pretty important.
Can you ssh as `ctf-player` to `titan.picoctf.net` at port `55893` to get the flag?
You'll also need the password `83dcefb7`. If asked, accept the fingerprint by answering `yes`.

If your device doesn't have a shell, you can use: https://webshell.picoctf.org
If you're not sure what a shell is, check out the primer: https://primer.picoctf.com/#_the_shell

## Solución

1. Abrir una terminal y conectarse por SSH usando el puerto indicado:

```bash
ssh ctf-player@titan.picoctf.net -p 55893
```

2. Introducir la contraseña cuando se solicite: `83dcefb7`.

3. Si el cliente pregunta si confiar en la clave del host, responder `yes` para añadirla a `~/.ssh/known_hosts`.

4. Una vez conectado, listar y leer los archivos para localizar la flag. Comandos útiles:

```bash
ls -la
cat flag.txt || cat FLAG || find . -type f -maxdepth 4 -print -exec grep -H "picoCTF" {} \; 2>/dev/null
```

5. La salida contendrá la flag con el formato `picoCTF{...}`. 
:

```text
picoCTF{s3cur3_c0nn3ct10n_8969f7d3}
```



## Notas

- Aceptar la huella (`yes`) añade la entrada al fichero `~/.ssh/known_hosts`.
- Si no se quiere usar la máquina local, usar `https://webshell.picoctf.org` y ejecutar los mismos pasos allí.
- Evitar ejecutar binarios desconocidos encontrados en el host; para extraer la flag se suelen usar `cat` o `grep`.

## Referencias

- `ssh` manual: https://linux.die.net/man/1/ssh
- Primer sobre la shell: https://primer.picoctf.com/#_the_shell