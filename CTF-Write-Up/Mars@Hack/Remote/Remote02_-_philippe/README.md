# Write up : Remote02

Catégorie :

```
Remote
```

Consigne :

```
Trouver le flag à travers le réseau.<br>

<FONT COLOR="#ff0000">nc game1.marshack.fr 30002</FONT> <br>
```

Pièce jointe :

```
Aucune
```

Serveur :

```
game1
```

Points attribués

```
60
```

Flag :

```
MARS{Ps3udo_Random_Numb3r_G3n3rator}
```



connection :

```
nc 10.0.3.5 30002
 __  __                        _    _            _    
|  \/  |                 ____ | |  | |          | |   
| \  / | __ _ _ __ ___  / __ \| |__| | __ _  ___| | __
| |\/| |/ _` | '__/ __|/ / _` |  __  |/ _` |/ __| |/ /
| |  | | (_| | |  \__ \ | (_| | |  | | (_| | (__|   < 
|_|  |_|\__,_|_|  |___/\ \__,_|_|  |_|\__,_|\___|_|\_\
                        \____/                        

Find the 6th number ?

0220	0706	0271	0312	0815	????

> 

```

Il existe plusieurs fonctions de la libc capable de générer des valeurs aléatoires, dont une bien particulière qui, lorsqu'on l'appelle plusieurs fois, génére les mêmes nombres aléatoires.

On peut ajouter un sel qui sera un vecteur d'initialisation des valeurs aléatoires à générer.



Le joueur devra retrouver le seed pour retrouvé les 5 nombres aléatoires affichés.

Une fois le seed obtenu, le joueur pourra ainsi calculer la 6ème valeur.



Exemple de résultat

```
./30002.py
[+] Opening connection to 10.0.3.5 on port 30002: Done
 __  __                        _    _            _    
|  \/  |                 ____ | |  | |          | |   
| \  / | __ _ _ __ ___  / __ \| |__| | __ _  ___| | __
| |\/| |/ _` | '__/ __|/ / _` |  __  |/ _` |/ __| |/ /
| |  | | (_| | |  \__ \ | (_| | |  | | (_| | (__|   < 
|_|  |_|\__,_|_|  |___/\ \__,_|_|  |_|\__,_|\___|_|\_\
                        \____/                        

Find the 6th number ?


trouvé
index
215
[108, 738, 460, 608, 577]
suite : 108 738 460 608 577 
348
Congratulations, The flag is MARS{Ps3udo_Random_Numb3r_G3n3rator}

[*] Closed connection to 10.0.3.5 port 30002

```



remote02.c

```c
// fichier source :  remote02.c
// gcc -m64 -o remote02 remote02.c


#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <time.h>
#include <stdlib.h>
#include <fcntl.h>

int main()
	{
                time_t origine = time(NULL);
                time_t stop;   
                int nb01,nb02,nb03,nb04,nb05=0;
                long int seed=0; 
                char suite[20];
                int res;
                char *flag="MARS{Ps3udo_Random_Numb3r_G3n3rator}";
                FILE *fp;

         
                fp = fopen("/dev/urandom","r");
                seed = fgetc(fp); 

                // seed = seed % 256;
                // printf("seed %ld\n",seed);                 
                srand(seed);


                // srand(4);

                printf("Find the 6th number ?\n\n");
		
                int i;
                for (i=0;i<10;i++)
                     {
                     rand();
                     }
                
                nb01 = rand() % 1000;
                nb02 = rand() % 1000;
                nb03 = rand() % 1000;
                nb04 = rand() % 1000;
                nb05 = rand() % 1000;
                                
                printf ("%04d\t%04d\t%04d\t%04d\t%04d\t????\n",nb01,nb02,nb03,nb04,nb05);
                
                
                
                
                
                printf("\n");
                printf("> ");
		       fflush(stdout);


                fgets(suite,5,stdin);
                char *pos;
                if ((pos=strchr(suite, '\n')) != NULL)
                        *pos = '\0'; 

                stop = time(NULL);
                if ((stop-origine) >= 10)
                   { 
                   printf("Too late !!!!\n");
                   return(0);
                   } 

                res = rand() % 1000;
                if (res == atoi(suite))
                   {
                   printf("\nCongratulations, The flag is %s\n\n",flag);
		          fflush(stdout);
                   }
                else
                   {
                   printf("\n");
                   printf("Lost :(\n\n");
		          fflush(stdout);
                   }
                    
                // printf ("Solutions : %d\n",res);


        return(0);
	}

```



Script python 2.7 : (exécuté sous kali)

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-


# F5 paste/no paste (copier coller sans indentation)
# F6 pour executer le script python 2.7
# F7 pour executer le script python 3
# F8 highlighting on/off, and show current value.


from pwn import *
#import numpy
import re
from ctypes import CDLL
libc = CDLL('libc.so.6')

#libc.srand(38)

#for x in range(10):
#   a=libc.rand()

#for x in range(5):
#   print (libc.rand() % 1000)


# calcul chaine possible

maliste=[]
for x in range(0,256):
   libc.srand(x)
   for y in range(0,10):
      libc.rand()
   maliste.append([libc.rand() % 1000 ,libc.rand() % 1000,libc.rand() % 1000,libc.rand() % 1000,libc.rand() % 1000])
      
#print maliste
#print match



#p = remote("10.0.2.15",30002)  
p = remote("game1.marshack.fr",30002) 

#print p.recvline(timeout=1)
#print p.recvline(timeout=1)

print p.recvuntil("Find the 6th number ?\n\n")


res01 = p.recvline(timeout=1)
pattern=r"[0-9][0-9][0-9][0-9]"
#print res01
match=re.findall(pattern,res01,flags=0)

for x in range(5):
    match[x]=int(match[x])
    #print match[x]

#print match
if match in maliste:
   print "trouvé"
   print "index"
   index = maliste.index(match)
   print index
   print maliste[index]

   
   libc.srand(index)
   for y in range(0,10):
      libc.rand()
   #for y in range(6):
   print 'suite : {:d} {:d} {:d} {:d} {:d} '.format(libc.rand() % 1000,libc.rand() % 1000,libc.rand() % 1000 ,libc.rand() % 1000 ,libc.rand() % 1000) 
   
   solution = libc.rand() % 1000
   print solution
   p.sendline(str(solution))
   p.recvline(timeout=1)
   p.recvline(timeout=1)
   print p.recvline(timeout=1)

else:
   print "pas trouvé"
p.close()
```



solution erable :

```python
from pwn import *
from ctypes import *

libc=cdll.LoadLibrary("libc.so.6")

dic={}

for i in range (0,256):
	libc.srand(i)
	for c in range (0,10):
		libc.rand()

	l=[]
	for c in range(0,7):
		 l.append(libc.rand() % 1000)

	dic[tuple(l[0:5])]=l[5]


conn = remote('10.10.10.70',30002)
conn.recvuntil("suite 5 nombres\n")
values=conn.recvline().split('\t')
values=tuple([int(x) for x in values[0:5]])
# print values
if values in dic:
	resu=dic[values]
	conn.sendline(str(resu))
	conn.recvuntil(">bravo\n")
	print "BRAVO : " , resu
	# TODO afficher le flag
conn.close()
```





Arborescence docker remote02 sur le host (/home/esioc/ctf-mdm/epreuves/remote02)

```
remote02
├── Dockerfile
└── file
    ├── binary-remote02
    ├── entrypoint.sh
    ├── fail.txt
    ├── flag.txt
    ├── success.txt
    └── xinetd-remote02


```


Si le script est correctement executé, le serveur acceptera la réponse et renverra le flag.

Résultat : MARS{Ps3udo_Random_Numb3r_G3n3rator}