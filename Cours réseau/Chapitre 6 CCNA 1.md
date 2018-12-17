CHAPITRE 6 : COUCHE RESEAU
========


La couche réseau (couche 3 modèle OSI) fournit des services permettant aux périphériques finaux d'échanger des données sur le réseau pour cela elle utilise 4 processus de base :

-
  - L&#39;adressage des périphériques finaux
  - L&#39;encapsulation (ajout d&#39;information d&#39;en-tête IP (Adresse IP source Adresse IP destinataire
  - Le routage : c&#39;est un services qui permet de diriger les paquet vers un hôte  de destination à travers différent réseaux et tronçon (routeur que le paquet traverse pour atteindre son hote de destination)
  - La désencapsulassions (vérif de l&#39;en-tête IP et suppression de l&#39;en-tête IP après vérification puis forward vers couche 4)

Il existe 2 protocoles de couche réseau IPV4 et IPV6

Le protocole IP comporte de nombreuses caractéristiques :

-
  - Sans connexion  : Aucune connexion avec la destination n&#39;est établie avant l&#39;envoi des paquets de données
  - Acheminement au mieux : IP n&#39;est pas fiable par nature, car la livraison des paquets n&#39;est pas garantie
  - Indépendant du support : le fonctionnement est indépendant du support (cuivre, fibre optique , sans fil) qui transporte les données



![img](https://github.com/StevenDias33/-Offensive-Security-Certified-Professional/blob/master/Cours%20r%C3%A9seau/Images/En-t%C3%AAte%20de%20paquet%20IPV4.png)



Les champs importants de l&#39;en-tête IPv4 sont les suivants :

-
  - Version :  ce champ contient une valeur binaire de 4 bits définie sur 0100 indiquant qu&#39;il s&#39;agit d&#39;un paquet IP version 4.
  - Services différenciés ou DiffServ (DS) : anciennement appelé champ de type de service, le champ Services différenciés est un champ de 8 bits utilisé pour définir la priorité de chaque paquet. Les six bits de poids fort du champ DiffServ sont représentés par le marquage DSCP (Differentiated Services Code Point) et les deux derniers bits sont des bits ECN (Explicit Congestion Notification).
  - Time-to-live (durée de vie, TTL) : ce champ contient une valeur binaire de 8 bits utilisée pour limiter la durée de vie d&#39;un paquet. L&#39;expéditeur du paquet définit la valeur TTL initiale et celle-ci diminue d&#39;un point chaque fois que le paquet est traité par un routeur. Si la valeur du champ TTL arrive à zéro, le routeur rejette le paquet et envoie un message de dépassement du délai ICMP (Internet Control Message Protocol) à l&#39;adresse IP source.
  - Le champ  Protocole  est utilisé pour identifier le prochain protocole de niveau. Cette valeur binaire de 8 bits indique le type de données utiles transportées par le paquet, ce qui permet à la couche réseau de transmettre les données au protocole de couche supérieure approprié. Les valeurs les plus courantes sont notamment ICMP (1), TCP (6) et UDP (17).
  - Adresse IPv4 source :  ce champ contient une valeur binaire de 32 bits, qui représente l&#39;adresse IP source du paquet. L&#39;adresse IPv4 source est toujours une adresse de monodiffusion.
  - Adresse IPv4 de destination :  ce champ contient une valeur binaire de 32 bits qui représente l&#39;adresse IP de destination du paquet. L&#39;adresse IPv4 de destination est une adresse de monodiffusion, de diffusion ou de multidiffusion.

Les deux champs les plus utilisés sont les adresses IP source et de destination. Ces champs indiquent d&#39;où vient le paquet et où il va. Généralement, ces adresses ne changent pas lors du déplacement entre la source et la destination.

Les champs Longueur d&#39;en-tête Internet (IHL), Longueur totale et Somme de contrôle d&#39;en-tête permettent d&#39;identifier et de valider le paquet.

D&#39;autres champs sont utilisés pour remettre dans l&#39;ordre un paquet fragmenté. En particulier, le paquet IPv4 utilise les champs Identification, Indicateurs et Décalage du fragment pour garder la trace des fragments. Un routeur peut être amené à fragmenter un paquet pour le transmettre d&#39;un support à un autre

_ _

Aujourd&#39;hui il y&#39;a une pénurie d&#39;adresses IPV4 :

Le nombre d&#39;adresse IPV4 étant de 4 milliards avec l&#39;arrivé des objets connectés les 4 milliards d&#39;adresse sont quasiment toutes prises

Les routes IPV4 consomment beaucoup de mémoire et de ressources processeur sur les routeurs internet

Et il y&#39;a un manque de connectivité de bout en bout

C&#39;est pour cela que IPV6 à été crée:

IPV6 à 340 undécillions d&#39;adresses disponible (10puissance 36 )

Plus de NAT

En-tête IP simplifié



![img](https://github.com/StevenDias33/-Offensive-Security-Certified-Professional/blob/master/Cours%20r%C3%A9seau/Images/En-t%C3%AAte%20de%20paquet%20IPV6.png)



-
  Version :  ce champ contient une valeur binaire de 4 bits définie sur 0110 indiquant qu&#39;il s&#39;agit d&#39;un paquet IP version 6.
  Classe de trafic :  ce champ de 8 bits est l&#39;équivalent du champ de services différenciés pour l&#39;IPv4.

  Étiquetage de flux :  ce champ de 20 bits indique que tous les paquets portant la même étiquette de flux doivent être traités de la même manière par les routeurs.

  Longueur des données utiles :  ce champ de 16 bits indique la longueur de la partie données (utiles) du paquet IPv6.

  En-tête suivant :  ce champ de 8 bits est l&#39;équivalent du champ de protocole de l&#39;IPv4. Il indique le type de données utiles transportées par le paquet, permettant ainsi à la couche réseau de transmettre les données au protocole de couche supérieure approprié.

  Limite du nombre de tronçons :  ce champ de 8 bits remplace le champ de durée de vie (TTL) de l&#39;IPv4. Cette valeur est réduite d&#39;un point chaque fois qu&#39;un routeur transmet le paquet. Lorsque le compteur atteint 0, le paquet est rejeté et un message ICMPv6 de délai dépassé est transféré à l&#39;hôte émetteur, indiquant que le paquet n&#39;a pas atteint sa destination en raison du dépassement du nombre limite de tronçons.

   Adresse source IPv6 :  ce champ de 128 bits identifie l&#39;adresse IPv6 de l&#39;hôte émetteur.

  Adresse IPv6 de destination :  ce champ de 128 bits identifie l&#39;adresse IPv6 de l&#39;hôte destinataire.



Dans un réseau pour communiquer avec d&#39;autres réseau on a besoin d&#39;une passerelle par défaut

![img](https://github.com/StevenDias33/-Offensive-Security-Certified-Professional/blob/master/Cours%20r%C3%A9seau/Images/Table%20routage.png)
-
  Interface List (liste des interfaces) : répertorie les adresses MAC et les numéros d&#39;interface attribués à chaque interface réseau de l&#39;hôte, notamment les adaptateurs Ethernet, Wi-Fi et Bluetooth.

  IPv4 Route Table (table de routage IPv4) : répertorie toutes les routes IPv4 connues, y compris les connexions directes, le réseau local et les routes locales par défaut.

  IPv6 Route Table (table de routage IPv6) : répertorie toutes les routes IPv6 connues, y compris les connexions directes, le réseau local et les routes locales par défaut.



Lorsque la passerelle par défaut reçoit un paquet à transmettre vers un autre réseau elle vérifie sa table de routage

La table de routage d&#39;un routeur stocke des information sur :

 Les routes distantes : ces routes correspondent aux réseaux distants connectés à d&#39;autres routeurs. Les routes vers ces réseaux peuvent être configurées manuellement sur le routeur local par l&#39;administrateur réseau ou être configurées de manière dynamique en permettant au routeur local d&#39;échanger des informations de routage avec d&#39;autres routeurs à l&#39;aide d&#39;un protocole de routage dynamique.

 Route par défaut : si il n&#39;existe aucune autre route jusqu&#39;au réseau souhaite par le paquet reçu le routeur va forward le paquet vers une route par défaut
