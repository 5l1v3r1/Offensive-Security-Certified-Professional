# Writeup : LambdaCrackme #

Catégorie :

```
Divers
```

Consigne :  

```
Crackme dans les méandres de la programmation fonctionnelle.
Si vous êtes bloqué, pensez aux classiques.

Le flag trouvé devra être intégré dans MARS{} afin de pouvoir le soumettre.
```

Pieces jointes :

```
crackme
```

Serveur :

```
CTFD
```

Points attribués

```
20
```

Flag :   

```
MARS{Esioc CTF 2018}
```

## Solution

L'idée de ce crackme est le coté "exotique" de la technologie.

**Haskell** est un langage fonctionnel qui est particulièrement compliqué à reverser notamment à cause du fonctionnement du compilateur et du faible nombre d'outils disponibles.



Le code source du fichier crackme :

````haskell
import Data.Char

findice :: IO()
indice = putStrLn "bruteforce kali"

fun :: Char -> Int -> Char
fun a b
    | ord(a) + b < 97 = chr(ord(a) + b + 26 )
    | ord(a) + b > 122 = chr(ord(a) + b - 26 )
    | otherwise = chr(ord(a) + b)

check :: [Char] -> [Char]
check l = map (\(a,b) -> fun a b) $ zip l [1..length l]

-- Mot de passe Final

flag :: [Char] -> [Char]
flag a = map (\x -> chr(ord(x) - 9)) a


main :: IO()
main = do
       putStrLn "Crackme Exotique"
       inpStr <- getLine
       -- indice sur la taille du mdp
       print $ (++) "vous avez saisi: " (take 5 inpStr)
       case check inpStr == "igopt" of
           False -> case inpStr == "help" of
                        False -> putStrLn "Dommage, essaye encore :)"
                        True -> indice
           True -> print $ (++) "Bien joue le flag est: "  (flag "N|rxl)L]O);9:A")
````


La compilation :

````
ghc crack.hs -o crack
````

Il est nécessaire d'avoir l'environnement de développement  pour modifier le programme et le compiler pour l'architecture de destination. Une fois cela fait, le programme s'exécutera sans dépendance.

Sous Ubuntu (site officiel) :

````bash
sudo apt-get update
sudo apt-get install -y software-properties-common
sudo add-apt-repository -y ppa:hvr/ghc
sudo apt-get update
sudo apt-get install -y cabal-install-1.22 ghc-7.10.3
cat >> ~/.bashrc <<EOF
export PATH="\$HOME/.cabal/bin:/opt/cabal/1.22/bin:/opt/ghc/7.10.3/bin:\$PATH"
EOF
export PATH=~/.cabal/bin:/opt/cabal/1.22/bin:/opt/ghc/7.10.3/bin:$PATH
````

Fonctionnement du crackme:

Une valeur est saisie par l'utilisateur. Le script renverra ce qui a été saisi, tronqué à la bonne taille du mot de passe, soit 5 caractères. Ceci est un premier indice.

````
-- La taille est bloquée a 5 : 1er indice
➜  haskell ./crackme
Crackme Exotique
dlkfklmksdlfmkdsml
"vous avez saisi: dlkfk"
Dommage, essaie encore :)

-- Si la personne tape help, 2d indice sur le type d'attaque
➜  haskell ./crackme
Crackme Exotique
help
"vous avez saisi: help"
bruteforce kali

➜  haskell ./crackme
Crackme Exotique
hello
"vous avez saisi: hello"
"Bien joue le flag est: Esioc CTF 2018"
➜  haskell
````

Pour rester dans un timing acceptable, je me suis basé sur l'un des dictionnaires présents sur la distribution Kali à savoir /usr/share/theharvester/wordlists/general/common.txt

```bash
#!/bin/bash
essai()
{ for line in $(cat /usr/share/theharvester/wordlists/general/common.txt | tr -d '\r')
  do 
	echo "$line" | ./crackme | grep "Bien jou" -B1
  done
}
essai
```

Pour ceux qui voudront creuser, la commande `strings` ne donnera que peu d'informations car toutes les chaînes subissent un traitement.

````
strings ./hello | grep "Crackme" -B5
igopt
Dommage, essaie encore :)
N|rxl)L]O);9:A
Bien joue le flag est:q
vous avez saisi:
Crackme Exotique
````
Résultat : MARS{Esioc CTF 2018}