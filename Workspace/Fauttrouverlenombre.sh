#!/bin/bash
randnumber=$(($RANDOM % 1000 + 1))
nombre=0
compteur=0
while [ "$randnumber" -ne "$nombre" ]
do echo 'Entrez un nombre'
    read nombre
    if [ "$nombre" -eq "$nombre" 2>/dev/null ]
    then
        if [ "$nombre" -lt "$randnumber" ]
        then
            echo -e 'Le nombre à trouver est plus grand\n'           
            compteur=$(($count + 1))
        elif [ "$nombre" -gt "$randnumber" ]
        then
            echo -e 'Le nombre à trouver est plus petit\n'
            compteur=$(($count+  1))
        else
            echo 'Vous avez trouver en $count essais !'
        fi
    else
        echo -e 'Mec tu crois vraiment que je te vois pas en train de faire nimporte quoi' 
        nombre=0
        compteur=$(($count + 1))
    fi
done




