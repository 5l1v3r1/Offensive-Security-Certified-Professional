# Labo Sécurité 2019

## Test d'intrusion 


Le test d'intrusion est un audit de sécurité technique qui consiste à :

- Détecter les failles 
- L'évaluation de leurs criticités
- proposer des contre-mesures
- Tout en respectant le cadre légal et en étant maitrisé
- et en respectant le périmètre d'attaque définie

Il existe plusieurs paramètres de test d'intrusion : 
- Boite noires : on dispose d'aucune info et accès au site cet audit dure quelques jours

- Boite grise: On dispose d'un compte utilisateur cet audit dure environ 1 semaine

- Boite Blanche: Accès total ce qui permet de lire le code des applis et de faire un audit en profondeur cet audit dure + d'1 semaine


![enter image description here](http://cyber-serenite.fr/bundles/cybercommon/images/schema-test-intrusion.png)

A la fin du test d'intrusion on effectue une synthèse des tests effectués : 
 - Scénario dans lequel les tests ont été effectués
 - Vulnérabilité trouvés 
 - Détails technique
 - Recommandations pour corriger les failles 

## Attaque SSRF

Qu'est ce que les Server Side  Request  Forgery ?

Les Server Side  Request  Forgery, ou en abrégé SSRF, sont des vulnérabilités Web permettant de lire des fichiers sur le serveur local.

Il ne faut pas les confondre avec les CSRF (Cross Site Request  Forgery), qui, elles, ont pour but l'exécution d'une requête à l'insu d'un autre utilisateur.

Un des gros avantages des SSRF est la possibilité de contourner les pare-feux.

En effet, les actions se faisant côté serveur, il est possible d'interroger des services n'étant disponibles que localement tels que :

- Des bases de données NoSQL : Redis, MongoDB.
- Des bases de données relationnelles : Oracle, MSSQL, MySQL,PostgreSQL.
- Des services mail : Postfix, Dovecot.
- Des services Web accessibles localement.

Ce genre de faille est particulièrement présent sur les proxy Web : Un utilisateur du service proxy peut avoir accès à des données internes au serveur, données auxquelles il n'aurait normalement pas du avoir accès.

![enter image description here](https://www.dailysecurity.fr/images/Schema_SSRF_Proxy.png)

Les exploit les plus intéréssant avec cet attaque sont : 

- Loopback scan
- Inclusion de fichier
- scan interne
- Communication avec services internes 

Comment les éviter ? : 

- Mettre en place une liste blanche* plutôt qu'une liste noire sur les serveurs 
- Analyse des réponses tiers du serveur 
- Désactiver les schémas d'URL utilisé 
- Authentification sur les services internes 

*Au contraire de la liste blanche (white list), la liste noire (black list) contient l’ensemble des sites et applicatifs vers lesquels la navigation est interdite.
Liste blanche (tout interdit et autorisation manuel) 
Liste noire (tout autorisé et interdit manuellement)


## Anti-DDOS OVH VAC 

Une attaque DDoS vise à rendre un serveur, un service ou une infrastructure indisponible. L'attaque peut prendre différentes formes : une saturation de la bande passante du serveur pour le rendre injoignable, un épuisement des ressources système de la machine, l'empêchant ainsi de répondre au trafic légitime.

Voici un exemple d'attaque DDOS par réplication.  ![illu zombie](https://www.ovh.com/fr/files/IlluZombie.png)


Illustration du réseau OVH

![Illustration réseau ovh](https://www.ovh.com/fr/files/IlluQuestceQue_0.png)


Backbone router :

Un routeur  utiliser pour connecter des systeme  autonome à un large reseau tel  qu’internet 
Data Center OVH = Systeme Autonome

Les objectifs de l'anti-DDOS OVH sont:
-   analyser rapidement et en temps réel tous les paquets ;
-   détourner le trafic entrant sur votre serveur ;
-   séparer les éléments non légitimes du reste pour laisser passer le trafic légitime.

OVH est une entreprise française spécialisée dans les services de [cloud](https://fr.wikipedia.org/wiki/Cloud_computing) [computing](https://fr.wikipedia.org/wiki/Cloud_computing)

Ovh à été crée en 1999 et compte aujourd'hui 22 000 employé, l'entreprise dispose de bureaux dans 14 pays différent dont 1 à Bordeaux

OVH c'est /16TB de bandwidth
  
Depuis 2016 OVH à développer et conçu son propre anti DDOS appeler VAC

![enter image description here](https://www.ovh.com/fr/files/IlluAntiddosShe2%20%281%29.png)  

En cas nominal:
- Le trafic transite normalement
 - Echantillonnage du trafic est effectué par le routeur

En début d'attaque:
- Il y'a une détection qui est faite pour éviter une saturation le système VAC se met alors en place

Pré-firewall (Arista) :
- Effectue un premier filtrage
- Isole le trafic et forward au firewall network
- S'active automatiquement
- Non debrayable
- Filtrage de niveau 4 (couche transport du modèle OSI)
- Config par le client des protocole et des ports qu'ils n'utilisent pas pour faciliter le travail de VAC
- Home made via DPDK

Firewall network :
- 2e filtrage
- Le Firewall Network est une solution qui permet de limiter l’exposition aux attaques provenant du réseau public. Il s’active automatiquement à chaque attaque DDoS.

Shield:

- Intervient dans le cas d'attaque par amplification
- Décharge le cpu de la machine cible
- Contrôle de protocole

Armor:
- L’Armor est le filtre le plus avancé de  VAC et intervient dans la mitigation des attaques les plus perfectionnées.
- Solution hybride
- PDGA
- Rate limit
- Syncookie
- X86
- Filtres
- Pattern matching

Exemple: Attaque par reflexion
-   Tripartite attaquante
-   Peu d'intérêt
-   Principalement en UDP

En mars 2018 OVH à subi une attaque DDOS avec une force de 1.03 TB secondes l'anti DDOS VAC n'a eu aucun problème et est capable de tenir la charge d'une attaque d'environ 6TB/s

## Forensic de trame réseau

Forensic : Analyse post-attaque 
Dans le cadre de mars@hack j'ai eu l'occasion de flag le challenge Easy Network.

Le principe de cet épreuve était d'analyser un fichier pcap et de retrouver le flag de celui ci 

Cet épreuve à été complexe pour moi car pour trouver le flag il fallait extraire les donnée des data des pings sur le pcap et je ne conaissais pas encore la commande avec tcpdump et tshark 
ensuite je n'avais pas encore la méthodologie étant donnée que c'était mon premier CTF mais toutefois j'ai réussi à flag cet épreuve,


> Written with [Metasploit](https://stackedit.io/).
