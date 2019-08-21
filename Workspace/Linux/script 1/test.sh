#!/bin/bash

nbrmax=1000 
nbr=0
tentative=0
aleatoire=$(($$ % $nbrmax))

while [$nombre -ne $aleatoire] ; do
	echo -n "Devinez "; read nbr
	if [ "$nombre" -lt $aleatoire] ; then
	echo "c'est plus"
	elif [ "$nombre" -gt $aleatoire] ; then
	echo "c'est moins"
	fi
	tentative=$(($nbtentative + 1 ))
done
echo "Bravo ! vous avez deviné $aleatoire en $nbtentative"

exit 0