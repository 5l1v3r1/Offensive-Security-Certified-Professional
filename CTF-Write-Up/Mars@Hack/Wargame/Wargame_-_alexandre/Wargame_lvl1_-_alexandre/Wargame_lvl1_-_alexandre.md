# Write up : Wargames

### Level 1 

Consigne :

```
<b>Consignes générales :</b> <br>
Les challenges doivent être résolus dans l'ordre :<br>
lvl 01, lvl 02, lvl 03 ... lvl 10. <br>
Un flag obtenu sert de password pour accéder au challenge suivant.<br>
Les flags sont généralement stockés dans /etc/wargames_pass/levelX/levelX_password où X correspond au niveau suivant sauf si l'énoncé précise autre chose.
<p>

Consignes lvl1 :<br>
Le but de ce challenge est de lire le fichier qui se trouve à la racine du homedir. <p>

Se connecter à l'adresse suivante :<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<FONT COLOR="#ff0000">ssh -p 6666 challenge1@game1.marshack.fr</FONT><br>
      password : challenge1pass

```

Connexion 

```bash
ssh -p 6666 challenge1@game1.marshack.fr
password: challenge1pass
```

Contenu du répertoire /home/challenge1/

```bash
challenge1@b36757fe226e:~$ ls -al
-rw-r----- 1 root challenge1   39 Oct 30 17:07 -.passwd
drwxr-x--- 1 root challenge1 4096 Jan 30 10:24 .
drwxr-xr-x 1 root root       4096 Jan 30 10:23 ..
```

```
challenge1@b36757fe226e:~$ cat -.passwd

cat: invalid option -- '.'
Try 'cat --help' for more information.
```

A cause du "-",  la commande `cat` échoue.

On ne pense pas forcément à préfixer par "./".

La solution est la suivante : utiliser un chemin absolu. 

```bash
challenge1@b36757fe226e:~$ cd /home/challenge1
challenge1@b36757fe226e:~$ cat ./-.passwd

MARS{hloiO6JJKCRcDPL8YHsBkENGxxRtESQ3}
```


Résultat : MARS{hloiO6JJKCRcDPL8YHsBkENGxxRtESQ3}