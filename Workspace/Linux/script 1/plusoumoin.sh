
 #!/bin/bash     #1 – Le shibang

 limite=100                     # nbr max possible
 nbr=0                         # nbr joueur
 tentatives=0                       # nbr de tentatives effectuées
 aleatoire=$(( $RANDOM))      # nbr aléatoire, entre 1 et la variable

 while [ "$nbr" -ne $aleatoire ] ; do
  echo -n "Devinez? " ; read nbr
  if [ "$nbr" -lt $aleatoire ] ; then 
    echo " guigol c'est plus grand!"
  elif [ "$nbr" -gt $aleatoire ] ; then
    echo " guignol c'est plus petit!"
  elif [ "nbr" = ]
  fi
  tentatives=$(( $tentatives + 1 ))
 done

 echo " Vous avez deviné $aleatoire en $tentatives coups."

 exit 0