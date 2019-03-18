# Write up : Remote01

Catégorie :

```
Remote
```

Consigne :

```
Trouver le flag à travers le réseau.<br>

<FONT COLOR="#ff0000">nc game1.marshack.fr 30001</FONT> <br>
```

Pièce jointe :

```
Aucune
```

Serveur :

```
game1
```

Points attribués :

```
40
```

Flag :

```
MARS{D0nt_s3nd_st@tus_strcmp}
```

## Solution

Dans ce challenge, on retourne le statut des comparaisons, ce qui va permettre au joueur de reconstituer la chaîne stockée dans le binaire.

Fonction strcmp :

```

strcmp("chaineA","chaineB")  

  status
valeur retournée          signification
     0                    les chaines sont identiques
   < 0                    la chaineA est supèrieur  à chaineB      
   > 0                    la chaineB est supréireur à chaineC
```



### Fonctionnement du challenge

Le joueur doit deviner la chaîne contenue dans le binaire en commençant par envoyer le premier caractère.
Le programme retourne le statut de la comparaison. 

Avec les statuts retournés, le joueur peut deviner le premier caractère.

Pour deviner le deuxième caractère, le joueur devra envoyer le 1er et 2ème caractère et ainsi de suite...   

ainsi de suite ...   


Une difficulté est ajoutée, car on doit retrouver la chaîne dans un temps limité (10 secondes), ce qui ne laisse aucune chance aux tentatives manuelles.

Il faut donc créer un script 

 Source : remote01.c

```c
// fichier source :  remote01.c
// gcc -m64 -o remote01 remote01.c


#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include <unistd.h>
#include <time.h>
#include <stdlib.h>


int main()
{
        printf("strcmp(user_input,flag) ?\n");
        fflush(stdout);
        int ret;
        int longueur;
        char *flag="MARS{D0nt_s3nd_st@tus_strcmp}";
                         
        char user_input[50];
       
        time_t origine = time(NULL);
        time_t stop;   
 

        while(true) {
           fgets(user_input,45,stdin);
           char *pos;
           if ((pos=strchr(user_input, '\n')) != NULL)
               *pos = '\0'; 
                      
           
           stop = time(NULL);
           if ((stop-origine) >= 10)
              { 
              printf("Too late !!!!\n");
              break;
              }
 
           ret = strcmp(user_input,flag);
           if (ret == 0){
             printf("Congratulations, The flag is %s\n\n",flag);
             fflush(stdout);
             //printf("\x00");
             //fflush(stdout);
             break;
             } 
           if (ret > 0)
             {
             printf("Status : %x\n",ret);
             fflush(stdout);
             }
           if (ret < 0)
             {
             printf("Status : %x\n",ret);
             fflush(stdout);
             }
           } 

}

```





Script python 2.7 exécuté sous kali

Prérequis : installer le module pwntools
	      

​                  pip2 install pwntools 



```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-


# F5 paste/no paste (copier coller sans indentation)
# F6 pour executer le script python 2.7
# F7 pour executer le script python 3
# F8 highlighting on/off, and show current value.


from pwn import *
import numpy

p = remote("game1.marshack.fr",30001)  

#print p.recvline(keepends=False,timeout=1)
#print p.recvline(keepends=False,timeout=1)
#print p.recvline(keepends=False,timeout=1)


print p.recvuntil("strcmp(user_input,flag) ?\n")


plage_caractere= "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"


# print plage_caractere


flag=""

while(1):
   fl = 0
   for car in plage_caractere:
      testcar=chr(ord(car)-1)
      p.sendline(flag)
      res01 = p.recvline(timeout=1)
      if "Status" not in res01:
         fl=2
         print res01
         break
         
      p.sendline(flag+testcar)
      res01 = p.recvline(timeout=1)
      if "Status" in res01:
           res02 = int(res01[9:],16)
      elif res01 == "":
         fl == 0
         print p.recvline(timeout=1)
         break
      else:
         print(res01)
         fl == 2
         break
      if (numpy.int32(res02))==-1:
          print 'flag : {:s}'.format(flag+car)
          flag=flag+car 
          fl= 1
          break
   if fl == 2:
      print 'flag : {:s}'.format(flag)
      
      break
   if fl == 0:
      print "pas trouvé le prochain caractère"
      break
   
p.close()

```





Arborescence docker remote01 sur le host (path : /home/esioc/ctf-mdm/epreuves/remote01)

```
remote01
├── Dockerfile
└── file
    ├── binary-remote01
    ├── entrypoint.sh
    ├── fail.txt
    ├── flag.txt
    ├── success.txt
    └── xinetd-remote01


```



Si le script est correctement executé, il renverra le flag.

Résultat : MARS{D0nt_s3nd_st@tus_strcmp}