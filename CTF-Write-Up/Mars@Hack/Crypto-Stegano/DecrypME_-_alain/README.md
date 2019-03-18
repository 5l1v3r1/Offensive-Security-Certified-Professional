# Write-up : DecryptME

Catégorie :

```
Crypto-Stegano
```

Consigne :

```
Vous êtes en possession de deux informations :

MEUwDQYJKoZIhvcNAQEBBQADNAAwMQIqAsj
<br>VmvR8gas3JbRyvkF+O/erhUOa9ybtPf32ZI<br>
nRVdwLdxx6UO98Xlj7AgMBAAE=<br>

Ainsi qu'un fichier chall chiffré.
```

Pièce jointe :

```
chall
```

Serveur :

```
CTFD
```

Points attribués :

```
20
```

Flag :

```
MARS{RsaWeakPq}
```



## Création des clés ##

Le code ci-dessous permet de générer la clé publique et la clé privée.
**p** et **q** correspondent au rsa-100 qui a déjà été traité (https://fr.wikipedia.org/wiki/Nombre_RSA)

````python
from Crypto.PublicKey import RSA

#37975227936943673922808872755445627854565536638199
#40094690950920881030683735292761468389214899724061

N = 1522605027922533360535618378132637429718068114961380688657908494580122963258952897654000350692006139L
e = 65537L
d = 1435319569480661473883310243084583371347212233430112391255270984679722445287591616684593449660400673L
publique = [N,e]
prive = [N,e,d]
clepu = RSA.construct(publique)
print clepu.exportKey('PEM')
clepriv = RSA.construct(prive)
print clepriv.exportKey('PEM')

​`````

La clé d a été crée avec le script rsatool.py disponible sur internet.

​````python
python rsatool.py -f PEM -o key.der -p 37975227936943673922808872755445627854565536638199 -q 40094690950920881030683735292761468389214899724061
Using (p, q) to initialise RSA instance

n = 2c8d59af47c81ab3725b472be417e3bf7ab85439af726ed3dfdf66489d155dc0b771c7a50ef7c5e58fb

e = 65537 (0x10001)

d = 29ff85cfea470484ad04c6eee532700b8d503e75af7ce9a98f65c7b98eeb6fc9abcdf8f312a89914421

p = 19fbd41d69aa3d86009a967db3379c63cd501f24f7

q = 1b6f141f98eeb619bc0360220160a5f75ea07cdf1d
````

````bash
-----BEGIN PUBLIC KEY-----
MEUwDQYJKoZIhvcNAQEBBQADNAAwMQIqAsjVmvR8gas3JbRyvkF+O/erhUOa9ybt
Pf32ZInRVdwLdxx6UO98Xlj7AgMBAAE=
-----END PUBLIC KEY-----
-----BEGIN RSA PRIVATE KEY-----
MIHTAgEAAioCyNWa9HyBqzcltHK+QX4796uFQ5r3Ju09/fZkidFV3At3HHpQ73xe
WPsCAwEAAQIqAp/4XP6kcEhK0Exu7lMnALjVA+da986amPZce5jutvyavN+PMSqJ
kUQhAhUbbxQfmO62GbwDYCIBYKX3XqB83x0CFRn71B1pqj2GAJqWfbM3nGPNUB8k
9wIVB9iJwcukIZJUkgaRUyGH9aorbesFAhUZqBfikxuOdGrUOhUUiazavziGCDEC
FRAsTXSkNkXG1OH7nDgUSNv3W7VX6Q==
-----END RSA PRIVATE KEY-----

Le code à déchiffrer a été réalisé via : 

echo "MARS{RsaWeakPq}" | openssl rsautl -encrypt -inkey pubkey.pem -pubin -out encrypt

````

## Enoncé du challenge ##

```
MEUwDQYJKoZIhvcNAQEBBQADNAAwMQIqAsjVmvR8gas3JbRyvkF+O/erhUOa9ybtPf32ZInRVdwLdxx6UO98Xlj7AgMBAAE=

fichier encrypt
```

## Obtenir des informations ##

Copier l'énoncé dans un format "clé publique" puis lancer la commande suivante :

````bash
openssl rsa -pubin -inform PEM -text -noout < pubkey.pem 
Public-Key: (330 bit)
Modulus:
    02:c8:d5:9a:f4:7c:81:ab:37:25:b4:72:be:41:7e:
    3b:f7:ab:85:43:9a:f7:26:ed:3d:fd:f6:64:89:d1:
    55:dc:0b:77:1c:7a:50:ef:7c:5e:58:fb
Exponent: 65537 (0x10001)

````
Nous avons donc **e** et **n** (clé publique). L'idée étant de trouver **d** afin de déchiffrer le message :
 - Internet en copier collant **n** (rsa-100 est connu)
 - Via le site *factordb*

Une fois **p** et **q** obtenus, rsatool permet de trouver **d**.
Il faut alors générer la clé privée puis déchiffrer le code.

````python
[..]
clepriv = RSA.construct(prive)
print clepriv.exportKey('PEM')
````

Puis déchiffrer le message :

````
openssl rsautl -decrypt -inkey privkey.pem -out key.bin -in encrypt

more key.bin 
MARS{RsaWeakPq}

````

Résultat : MARS{RsaWeakPq}
