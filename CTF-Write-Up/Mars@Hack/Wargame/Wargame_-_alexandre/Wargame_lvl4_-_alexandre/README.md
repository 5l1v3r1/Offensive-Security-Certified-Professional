# Write up : Wargames

### Level 4

Consigne  :

```
Consignes lvl4 :<br>
Trouver la seule ligne qui est unique dans le fichier data.txt.<br>
Le résultat est le flag de l'épreuve.<br>

Pour vous connecter à cette épreuve :<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<FONT COLOR="#ff0000">ssh -p 6666 challenge4@game1.marshack.fr</FONT> <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;password : [flag obtenu dans l'épreuve précédente]
```

Connexion 

```bash
ssh -p 6666 challenge4@game1.marshack.fr
password: MARS{4RiNhHV2o6lNuA6vGWkvV6MPuliITzza}
```

Contenu du répertoire :

```bash
challenge4@fb0a879ee360:~$ ls -al

drwxr-x--- 1 root challenge4  4096 Jan 31 14:09 .
drwxr-xr-x 1 root root        4096 Jan 31 14:09 ..
-rw-r----- 1 root challenge4 39039 Oct 30 17:31 data.txt

```

Un petit tricks unix permet de nettoyer le fichier.

Pour valider l'épreuve, il vous suffit de trouver la seule ligne qui est unique dans le fichier data.txt.

```
cat data.txt | sort | uniq -u

   -u : affiche les lignes qui n'apparaissent qu'une seule fois  

Résultat : MARS{UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR}
```