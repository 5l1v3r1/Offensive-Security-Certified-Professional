# Script Linux


## Jeux du plus ou moins

Le but de ce script et de générer un nombre au hasard puis ensuite de le deviner sans utiliser trop de coups 

Pour le tester j'ai utilisé ./Fauttrouverlenombre.sh et il à ensuite générer un nombre au hasard j'ai du ensuite le trouver en essayant des chiffres et si j'essaie autre chose que des chiffres ça me dit d'aller voir ailleurs


## Sauvegarde 


Pour ce script j'ai utilisé tar et crontab


La commande tar permet de faire une sauvegarde d'un dossier et la commande crontab permet de programmer des actions dans le temps pour ce script j'ai programmé crontab.sh de d'exec save.sh qui avait pôur but de faire une backup en .gz avec la date du jour  ce qui à fonctionné et ensuite je l'ai programmer pour éxec le script de sauvegarde tous les vendredi et j'ai changé la date de mon pc pour le testé ce qui a fonctionné aussi 


## Youtube

Ce script était le plus simple de tous il consistait à demmandé une URL à l'utilisateur pour ensuite la parser avec la commande youtube-dl +x pour télécharger la vidéo j'aurais pu aller plus loin en gérant les petit malin qui ne mettent pas de lien.
