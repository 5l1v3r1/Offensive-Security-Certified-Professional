# Write up : Les années 80 - la suite

Catégorie :

```
Divers
```

Consigne :

```
Votre fils a caché des informations dans une ROM GameBoy. Cependant celle-ci fut endommagée lors du transfert sur votre PC et vous n'avez accès qu'à une petite partie de la NVRAM.

Conseils: https://fms.komkon.org/GameBoy/Tech/Software.html

Le flag trouvé devra être intégré dans MARS{} afin de pouvoir le soumettre.
```

Pièce jointe :

```
challenge_annee80_suite.bin
```

Serveur :

```
CTFd
```

Points attribués :

```
80
```

Flag :

```
MARS{42xoc}  insensible à la casse
```

## Solution


Les données issues de la NVRAM du gameboy contiennent les tuiles pour le background.
Documentation donnée lors du chall : https://fms.komkon.org/GameBoy/Tech/Software.html

La documentation explique comment utiliser les données hexadécimales pour dessiner les tuiles.

Données à exploiter :

````bash
40 10 58 00 10 00 00 00 00 50 08 58 40 78 00 00 00 28 00 20 00 00 00 00 00 28 10 28 00 57 54 05 00 00 00 00 00 24 44 73 00
````

Le code ci-dessous permet la création du code hexa et des tuiles.

````python
# coding: utf-8
# POC pour Mars@Hack
# Alain 2018
listbinaire1 = []
listbinaire2 = []

# Génération de l'hexa à partir d'une tile

tile2 =  ['. 1 . . . . . .',
          '. 2 . 1 . . . .',
          '. 1 2 1 1 . . .',
          '. . . 2 . . . .',
          '. . . 3 . . . .',
          '. . . . . . . .',
          '. . . . . . . .',
          '. . . . . . . .']

tile3 =  ['. 1 2 1 2 . . .',
          '. . . . 1 . . .',
          '. 1 2 1 1 . . .',
          '. 1 . . . . . .',
          '. 1 1 1 1 . . .',
          '. . . . . . . .',
          '. . . . . . . .',
          '. . . . . . . .']

tile4 =  ['. . 1 . 1 . . .',
          '. . . 1 . . . .',
          '. . 1 . 1 . . .',
          '. . . . . . . .',
          '. 1 2 1 . 3 1 1',
          '. 3 . 1 . 3 . .',
          '. 2 2 2 . 1 2 3',
          '. . . . . . . .']

hexa1 = []
hexa2 = []
for t in range(0,8):
    for i in tile3[t]:
        for elem in list(i)[0]:
            if elem == '.':
                hexa1.append(0)
                hexa2.append(0)
            elif elem == '1':
                hexa1.append(1)
                hexa2.append(0)
            elif elem == '2':
                hexa1.append(0)
                hexa2.append(1)
            elif elem == '3':
                hexa1.append(1)
                hexa2.append(1)

    print hex(int(''.join(map(str, hexa1)),2)),
    print hex(int(''.join(map(str, hexa2)),2)),
    print hexa1,
    print hexa2
    hexa1[:] = []
    hexa2[:] = []

print '\n'
# Generation du tile à partir des données hexa

#hexString = bytearray(b'\x40\x10\x58\x00\x10\x00\x00\x00\x00\x40\x20\x10\x10\x00\x00\x00') # 4
#hexString = bytearray(b'\x50\x08\x58\x40\x78\x00\x00\x00\x28\x00\x20\x00\x00\x00\x00\x00') # 2
hexString = bytearray(b'\x28\x10\x28\x00\x57\x54\x05\x00\x00\x00\x00\x00\x24\x44\x73\x00') # XOC


premierBloc =  hexString[0:8]
secondBloc =  hexString[8:]

[x for x in hexString[0:8]]

for i in premierBloc:
    listbinaire1.append(bin(i)[2:].zfill(8))
for i in secondBloc:
    listbinaire2.append(bin(i)[2:].zfill(8))

print listbinaire1
print listbinaire2

for a in range(0,8):
    for i in range(0,8):
        if int(list(listbinaire1[a])[i]) == 0 and int(list(listbinaire2[a])[i]) == 0:
            print ' ',
        elif int(list(listbinaire1[a])[i]) == 0 and  int(list(listbinaire2[a])[i]) == 1:
            print 2,
        elif int(list(listbinaire1[a])[i]) == 1 and  int(list(listbinaire2[a])[i]) == 0:
            print 1,
        elif int(list(listbinaire1[a])[i]) == 1 and int(list(listbinaire2[a])[i]) == 1:
            print 3,
        else:
            print "erreur"
    print '\n'

````

L'épreuve sera un binaire :

````
echo "0000000: 40 10 58 00 10 00 00 00 00 50 08 58 40 78 00 00 00 28 00 20 00 00 00 00 00 28 10 28 00 57 54 05 00 00 00 00 00 24 44 73 00" | xxd -a -r -c 50 > challenge_annee80_suite

hexdump -C challenge_annee80_suite

00000000  40 10 58 00 10 00 00 00  00 40 20 10 10 00 00 00  |@.X......@ .....|
00000010  50 08 58 40 78 00 00 00  28 00 20 00 00 00 00 00  |P.X@x...(. .....|
00000020  28 10 28 00 57 54 05 00  00 00 00 00 24 44 73 00  |(.(.WT......$Ds.|
````

Résultat : 42xoc
