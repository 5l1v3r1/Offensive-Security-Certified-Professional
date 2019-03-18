# Write up : Client Side is Bad

Catégorie :

```
Web
```

Consigne :

```
Le contrôle Javascript, c'est la vie !

<FONT COLOR="#ff0000">Accès au site :<br>   <a href="http://game2.marshack.fr:8089" target="new">http://game2.marshack.fr:8089</a></FONT> <p>
```

Pièce jointe :

```
Aucune
```

Serveur : 

```
game2
```

Points attribués :

```
10
```

Flag

```
MARS{client_side_is_bad_haha}
```



## Solution

En arrivant sur la page, on voit un champ de saisie et un bouton Log in.
En regardant le code source de la page, on peut clairement voir une fonction **`verify`** qui contrôle la valeur soumise dans le formulaire.

``` javascript
<script type="text/javascript">
  function verify() {
    checkpass = document.getElementById("pass").value; # récupération de la valeur saisie
    split = 4;
	
	# Contrôles
    if (checkpass.substring(split*7, split*8) == '}') {
      if (checkpass.substring(split*6, split*7) == 'haha') {
        if (checkpass.substring(split*5, split*6) == 'bad_') {
         if (checkpass.substring(split*4, split*5) == '_is_') {
          if (checkpass.substring(split*3, split*4) == 'side') {
            if (checkpass.substring(split*2, split*3) == 'ent_') {
              # 4 suivantes et ainsi de suite ...
              if (checkpass.substring(split, split*2) == '{cli') {
                # 4 première lettre
                if (checkpass.substring(0,split) == 'MARS') {
                  alert("You got the flag!")
                  }
                }
              }
      
            }
          }
        }
      }
    }
    else {
      alert("Incorrect password");
    }
  }
</script>
```

On peut voir une valeur *split=4* qui est utilisée en paramètre d'une fonction `substring` qui permet de découper une chaîne de caractères selon les critères donnés.



Analysons la ligne checkpass.substring(0,split) :

La variable *split* étant égale à 4, cela veut dire que l'on compare les 4 premiers caractères de la chaîne saisie avec les 4 premiers caractères du flag attendu et ainsi de suite.

On peut ainsi recomposer le flag .

MARS
{cli
ent_
side
_is_
bad_
haha
}

Ce qui donne une fois recomposé MARS{client_side_is_bad_haha}



Résultat : MARS{client_side_is_bad_haha}