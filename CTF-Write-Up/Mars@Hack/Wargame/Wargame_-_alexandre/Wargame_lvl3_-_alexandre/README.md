# Write up : Wargames

### Level 3 

Consigne :

```
Consignes lvl3 :<br>
Le but de ce challenge est de vous connecter au port 9998, puis de transmettre votre mot de passe de connexion ssh.<br>

Se connecter à l'adresse suivante : <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<FONT COLOR="#ff0000">ssh -p 6666 challenge3@game1.marshack.fr</FONT> <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;password : [flag obtenu dans l'épreuve précédente]
```

Connexion 

```bash
ssh -p 6666 challenge3@game1.marshack.fr
password: MARS{Z0jU71sabjJ9DHzLEVV3nLoVibLS1wC9}
```

Effectuer un netcat localhost sur le port 9998.
Puis envoyer le mot de passe.

```
nc 127.0.0.1 9998
MARS{Z0jU71sabjJ9DHzLEVV3nLoVibLS1wC9} 

Résultat : MARS{4RiNhHV2o6lNuA6vGWkvV6MPuliITzza}
```