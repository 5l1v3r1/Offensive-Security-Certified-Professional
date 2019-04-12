# Write up : AndroidForensic



Catégorie :

```
forensic
```
Consignes :

```
Vous recevez par mail la sauvegarde d'un téléphone Android. Votre contact vous demande de réaliser une investigation car il suspecte l'utilisateur d'avoir volontairement caché des informations.<p>

sdcard.zip : md5 **57e9566511849a52e81a6f4b0f5710b0**<p>

Le flag trouvé devra être intégré dans MARS{} afin de pouvoir le soumettre.
```

Pièce jointe :

```
sdcard.img
```

Serveur

```
CTFD
```
Points attribués
```
50
```
Flag :
```
MARS{3nDr01dF0r3v3r}
```

```



## Création de l'image à partir d'avd ##

```


## Création de l'image à partir d'avd ##

```
/users/xophidia/Library/Android/sdk/platform-tools/adb shell
su

mount
rootfs / rootfs ro 0 0
tmpfs /dev tmpfs rw,nosuid,mode=755 0 0
devpts /dev/pts devpts rw,mode=600 0 0
proc /proc proc rw 0 0
sysfs /sys sysfs rw 0 0
none /acct cgroup rw,cpuacct 0 0
tmpfs /mnt/asec tmpfs rw,mode=755,gid=1000 0 0
tmpfs /mnt/obb tmpfs rw,mode=755,gid=1000 0 0
none /dev/cpuctl cgroup rw,cpu 0 0
/dev/block/mtdblock0 /system yaffs2 ro 0 0
/dev/block/mtdblock1 /data yaffs2 rw,nosuid,nodev 0 0
/dev/block/mtdblock2 /cache yaffs2 rw,nosuid,nodev 0 0

cat /proc/partitions
```

## Montage de l'image ##

```
mkdir /mnt/sdcard
mount -o ro sdcard.img /mnt/sdcard/
```
## Solution ##

L'historique de navigation va donner une indication sur la recherche effectuée afin de determiner le second mot de passe de l'archive.

`cd /mnt/sdcard/data/data/com.android.browser/databases`

```

sqlite3 browser2.db

SQLite version 3.7.11 2012-03-20 11:35:50
Enter ".help" for instructions
Enter SQL statements terminated with a ";"
sqlite> .tables
_sync_state            history                thumbnails
_sync_state_metadata   images                 v_accounts
android_metadata       searches               v_omnibox_suggestions
bookmarks              settings

sqlite> select * from history;
1|Google|https://www.google.fr/webhp?source=android-home&gws_rd=cr&ei=Fo97WLnPC6LM6ASh15jwBg|0|1538731118652|3|0
2|mot de passe top 10 - Recherche Google|https://www.google.fr/search?source=android-home&source=hp&ei=byy3W9OhFMvosAeK7aso&ins=false&q=mot+de+passe+top+10&oq=mot+de+passe+top+10&gs_l=mobile-gws-wiz-hp.12..0i22i30j33i22i29i30l4.13465.30588..32936...2.0..2.2924.21390.3-2j0j2j4j4j3j2......0....1.......0..0j46j0i131.uFnYtR-pD9E|0|1538731172213|1|0
3|Voici la liste des 25 mots de passe les plus populaires (et probablement les moins sûrs) de 2017 | Journal du Geek|https://www.journaldugeek.com/2017/12/20/voici-la-liste-des-25-mots-de-passe-les-plus-populaires-et-probablement-les-moins-surs-de-2017/|0|1538731215066|2|0
4|https://www.google.fr/url?sa=t&source=web&cd=1&ved=2ahUKEwjzjvKm_O7dAhXMC8AKHU_XCBgQFjAAegQIAxAB&url=https%3A%2F%2Fwww.journaldugeek.com%2F2017%2F12%2F20%2Fvoici-la-liste-des-25-mots-de-passe-les-plus-populaires-et-probablement-les-moins-surs-de-2017%2F&usg=AOvVaw04XxGwXOpe-iCloFwf_tIm|https://www.google.fr/url?sa=t&source=web&cd=1&ved=2ahUKEwjzjvKm_O7dAhXMC8AKHU_XCBgQFjAAegQIAxAB&url=https%3A%2F%2Fwww.journaldugeek.com%2F2017%2F12%2F20%2Fvoici-la-liste-des-25-mots-de-passe-les-plus-populaires-et-probablement-les-moins-surs-de-2017%2F&usg=AOvVaw04XxGwXOpe-iCloFwf_tIm|0|1538731809465|2|0
.exit


```


La base de données des sms contient les derniers échanges dont le premier mot de passe.

`cd /mnt/sdcard/data/data/com.android.providers.telephony/databases`



```
$ sudo sqlite3 mmssms.db 
SQLite version 3.11.0 2016-02-15 17:29:24
Enter ".help" for usage hints.
sqlite> .tables
addr                 pdu                  threads            
android_metadata     pending_msgs         words              
attachments          rate                 words_content      
canonical_addresses  raw                  words_segdir       
drm                  sms                  words_segments     
part                 sr_pending         
sqlite> select * from sms;
1|1|1 234-123-4||1484513827093|0||1|-1|2|||Yop ca va ?||0|0|1
2|1|1 2341234||1538725066844|0||1|-1|2|||Jene sais pas||0|0|1
3|1|1 2341234||1538725076804|0||1|-1|2|||Tu connais le flag ?||0|0|1
4|1|1 2341234||1538725082050|0||1|-1|2|||Y a des chances.||0|0|1
5|1|1 2341234||1538725086197|0||1|-1|2|||Attends je regarde||0|0|1
6|1|1 2341234||1538725113310|0||1|-1|2|||Essaye AnDr01dF0r3ns1c||0|0|1
7|1|1 2341234||1538725123630|0||1|-1|2|||K ty||0|0|1
.exit
```

En explorant l'arborescence du montage, on remarque un dossier **Download** qui contient une archive **234ERER4ZS.zip** 

Extraction du contenu de l'archive.

```
cd  /mnt/sdcard/Download
mkdir /root/forensic
cp 234ERER4ZS.zip /root/forensic
cd /root/forensic
unzip 234ERER4ZS.zip

Résultat de la commande unzip : 

Archive:  234ERER4ZS.zip
[234ERER4ZS.zip] flag.txt.zip password:        <==   le mdp est récupéré dans les sms (AnDr01dF0r3ns1c)
 extracting: flag.txt.zip
```

On tombe de nouveau sur une archive zip (**flag.txt.zip**) protégée par un mot de passe.


Nous avons vu précédemment en inspectant son historique de navigation que l'utilisateur a visité ce site :

https://www.journaldugeek.com/2017/12/20/voici-la-liste-des-25-mots-de-passe-les-plus-populaires-et-probablement-les-moins-surs-de-2017/

Sur lequel on trouve :

```
    1. 123456 (=)
    2. Password (=)
    3. 12345678 (+1)
    4. qwerty (+2)
    5. 12345 (-2)
    6. 123456789 (Nouveau)
    7. letmein (Nouveau)
    8. 1234567 (=)
    9. football (-4)
    10. iloveyou (Nouveau)
    11. admin (+4)
    12. welcome (=)
    13. monkey (Nouveau)
    14. login (-3)
    15. abc123 (-1)
    16. starwars (Nouveau)
    17. 123123 (Nouveau)
    18. dragon (+1)
    19. passw0rd (-1)
    20. master (+1)
    21. hello (Nouveau)
    22. freedom (Nouveau)
    23. whatever (Nouveau)
    24. qazwsx (Nouveau)
    25. trustno1 (Nouveau)
```

​    

Tester les mots de passe un à un.

Le mot de passe pour dézipper flag.txt.zip est starwars (16ème position dans la liste).

```
unzip flag.txt.zip
```

 Résultat : MARS{3nDr01dF0r3v3r}


## Références ##
https://forum.xda-developers.com/showthread.php?t=2450045
