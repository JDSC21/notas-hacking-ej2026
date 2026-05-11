# CommitmentIssues
## Descripción
Reto sobre recuperación de contenido eliminado usando control de versiones. El autor eliminó una línea con el flag, pero el historial de Git permite recuperar la versión anterior donde la bandera todavía estaba presente.

## Datos de acceso
- Archivo: `challenge.zip` (contiene un repositorio Git en `drop-in/`)
- Herramientas: `git`, `git log`, `git checkout`, `git blame`

## Solución

### Paso 1: Descargar y extraer los ficheros
```bash
wget https://artifacts.picoctf.net/c_titan/77/challenge.zip
unzip challenge.zip
cd drop-in
```

### Paso 2: Revisar el historial de commits
```bash
git log
```

Si `git log` no muestra claramente el contenido, podemos listar objetos o cambiar a un commit específico para ver el árbol histórico.

### Paso 3: Cambiar a la commit donde se creó el flag
```bash
# Usando el hash observado en los objetos: 3d5ec8a26ee7b092a1760fea18f384c35e435139
git checkout 3d5ec8a26ee7b092a1760fea18f384c35e435139
# Ahora estamos en 'detached HEAD' pero podemos inspeccionar los archivos
cat message.txt
```

Salida esperada:

```
picoCTF{s@n1t1z3_30e86d36}
```

## Flag

`picoCTF{s@n1t1z3_30e86d36}`

## Notas

- Estar en `detached HEAD` está bien para inspeccionar versiones antiguas; no hagas commits allí si no quieres afectar ramas.
- `git checkout <commit>` permite ver el árbol de ese commit específico.
- También se puede usar `git show <commit>:<ruta>` para mostrar un archivo en un commit sin cambiar el HEAD.

## Referencias

- `git log` - ver historial de commits
- `git checkout <commit>` - cambiar al estado de un commit concreto
- `git show <commit>:<file>` - ver contenido de un archivo en un commit
- Documentación Git: https://git-scm.com/docs

I accidentally wrote the flag down. Good thing I deleted it!
You download the challenge files here:
challenge.zip

Version control can help you recover files if you change or lose them!
ead the chapter on Git from the picoPrimer here: https://primer.picoctf.org/#_git_version_control
You can 'checkout' commits to see the files inside them


Solution


superdsanchez-academy@webshell:~$ wget https://artifacts.picoctf.net/c_titan/77/challenge.zip
--2026-05-10 06:39:17--  https://artifacts.picoctf.net/c_titan/77/challenge.zip
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.170.131.72, 3.170.131.77, 3.170.131.18, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.170.131.72|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 19199 (19K) [application/octet-stream]
Saving to: 'challenge.zip'

challenge.zip          100%[===========================>]  18.75K  --.-KB/s    in 0.004s  

2026-05-10 06:39:18 (4.75 MB/s) - 'challenge.zip' saved [19199/19199]

superdsanchez-academy@webshell:~$ unzip challenge.zip
Archive:  challenge.zip
   creating: drop-in/
   creating: drop-in/.git/
   creating: drop-in/.git/branches/
  inflating: drop-in/.git/description  
   creating: drop-in/.git/hooks/
  inflating: drop-in/.git/hooks/applypatch-msg.sample  
  inflating: drop-in/.git/hooks/commit-msg.sample  
  inflating: drop-in/.git/hooks/fsmonitor-watchman.sample  
  inflating: drop-in/.git/hooks/post-update.sample  
  inflating: drop-in/.git/hooks/pre-applypatch.sample  
  inflating: drop-in/.git/hooks/pre-commit.sample  
  inflating: drop-in/.git/hooks/pre-merge-commit.sample  
  inflating: drop-in/.git/hooks/pre-push.sample  
  inflating: drop-in/.git/hooks/pre-rebase.sample  
  inflating: drop-in/.git/hooks/pre-receive.sample  
  inflating: drop-in/.git/hooks/prepare-commit-msg.sample  
  inflating: drop-in/.git/hooks/update.sample  
   creating: drop-in/.git/info/
  inflating: drop-in/.git/info/exclude  
   creating: drop-in/.git/refs/
   creating: drop-in/.git/refs/heads/
 extracting: drop-in/.git/refs/heads/master  
   creating: drop-in/.git/refs/tags/
 extracting: drop-in/.git/HEAD       
  inflating: drop-in/.git/config     
   creating: drop-in/.git/objects/
   creating: drop-in/.git/objects/pack/
   creating: drop-in/.git/objects/info/
   creating: drop-in/.git/objects/96/
 extracting: drop-in/.git/objects/96/f7309de67d785ec0b93b8766ff2882bef5c3ef  
   creating: drop-in/.git/objects/8c/
 extracting: drop-in/.git/objects/8c/1d254e2da6713e33acd6d622fc1dae357ec3c6  
   creating: drop-in/.git/objects/3d/
 extracting: drop-in/.git/objects/3d/5ec8a26ee7b092a1760fea18f384c35e435139  
   creating: drop-in/.git/objects/d5/
 extracting: drop-in/.git/objects/d5/52d1ecd2d83fa2e65b6724d1ff73b45a7d59b7  
   creating: drop-in/.git/objects/0c/
 extracting: drop-in/.git/objects/0c/1ab266b7a3a1cd099bb509f82b7a2d03aecd03  
   creating: drop-in/.git/objects/e1/
 extracting: drop-in/.git/objects/e1/237df82d2e69f62dd53279abc1c8aeb66f6d64  
  inflating: drop-in/.git/index      
 extracting: drop-in/.git/COMMIT_EDITMSG  
   creating: drop-in/.git/logs/
  inflating: drop-in/.git/logs/HEAD  
   creating: drop-in/.git/logs/refs/
   creating: drop-in/.git/logs/refs/heads/
  inflating: drop-in/.git/logs/refs/heads/master  
 extracting: drop-in/message.txt     
superdsanchez-academy@webshell:~$ ls
README.txt  challenge.zip        level1.py            operation-orchid
apprentice  drop-in              level2.flag.txt.enc  serpentine.py
challenge   level1.flag.txt.enc  level2.py
superdsanchez-academy@webshell:~$ cd drop-in
superdsanchez-academy@webshell:~/drop-in$ git status
On branch master
nothing to commit, working tree clean
superdsanchez-academy@webshell:~/drop-in$ ls       
message.txt
superdsanchez-academy@webshell:~/drop-in$ cat message.txt
TOP SECRET
superdsanchez-academy@webshell:~/drop-in$ git log

superdsanchez-academy@webshell:~/drop-in$ git checkout 3d5ec8a26ee7b092a1760fea18f384c35e435139
Note: switching to '3d5ec8a26ee7b092a1760fea18f384c35e435139'.

You are in 'detached HEAD' state. You can look around, make experimental
changes and commit them, and you can discard any commits you make in this
state without impacting any branches by switching back to a branch.

If you want to create a new branch to retain commits you create, you may
do so (now or later) by using -c with the switch command. Example:

  git switch -c <new-branch-name>

Or undo this operation with:

  git switch -

Turn off this advice by setting config variable advice.detachedHead to false

HEAD is now at 3d5ec8a create flag
superdsanchez-academy@webshell:~/drop-in$ ls -al
total 12
drwxr-xr-x 3 superdsanchez-academy superdsanchez-academy   49 May 10 06:45 .
drwxr-xr-x 8 superdsanchez-academy superdsanchez-academy 4096 May 10 06:44 ..
drwxr-xr-x 8 superdsanchez-academy superdsanchez-academy 4096 May 10 06:45 .git
-rw-rw-r-- 1 superdsanchez-academy superdsanchez-academy   27 May 10 06:45 message.txt
superdsanchez-academy@webshell:~/drop-in$ cat message.txt
picoCTF{s@n1t1z3_30e86d36}

Notas: obtuvimos la version donde se creó la bandera con version control con git log y git checkout