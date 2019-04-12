# Write up : Crackme01

Catégorie :

```
Reverse
```

Consigne :

```
Retrouvez le password<p>
Le password trouvé devra être intégré dans MARS{} afin de pouvoir le soumettre.
```

Pièce jointe :

```
crackme01
```

Serveur :

```
CTFD
```

Points attribués : 

```
30
```

Flag :

```
MARS{3735928559}
```





source :  crackme01.asm

```assembly
; source : crackme01.asm    
; Assemble:  nasm -f elf64 -l crackme01.lst  crackme01.asm
; Link:      gcc -m64 -no-pie -o crackme01  crackme01.o
; Run:       ./crackme01 <flag>

; fonctions de la libc qui doivent etre utilisees
extern printf             
extern atoi

section .rodata


banner: db 10 
        db "   __  __                        _    _            _",10    
        db "  |  \/  |                 ____ | |  | |          | |",10   
        db "  | \  / | __ _ _ __ ___  / __ \| |__| | __ _  ___| | __",10
        db "  | |\/| |/ _` | '__/ __|/ / _` |  __  |/ _` |/ __| |/ /",10
        db "  | |  | | (_| | |  \__ \ | (_| | |  | | (_| | (__|   < ",10
        db "  |_|  |_|\__,_|_|  |___/\ \__,_|_|  |_|\__,_|\___|_|\_\",10
        db "                          \____/",10                         
        db 0

fmt3: db "%s", 10, 0           ; The printf format, "\n",'0'

help: db "Help :",10
      db "    crackme01 <password>",10,0 


msg1: db "   Congratulations !",10
      db "   Validation : MARS{<password>}", 0   ; C string needs 0
fmt1: db "%s", 10,10, 0        ; The printf format, "\n",'0'

msg2: db "Failed", 0           ; C string needs 0
fmt2: db "%s", 10,10, 0           ; The printf format, "\n",'0'

section .data                  ; Data section, initialized variables

global main                    
section .text                  ; Code section.

main:                          ; the standard gcc entry point
                               ; the program label for the entry point
push rbp                       ; set up stack frame, must be alligned


; ---- verifie l'existence d'un paramêtre sur la ligne de commande    ---------


push rdi
push rsi
mov rsi,banner                 ; affiche la banner asciiart 
mov rdi,fmt3             
xor rax,rax                 
call printf                    ; appelle de la fonction c printf


pop rsi
pop rdi

cmp rdi,$2                     ; rdi => argc ,  rsi : argv
je continu                

mov rsi,help                   ; affiche l aide 
mov rdi,fmt3                
xor rax,rax                 
call printf                    ; appelle de la fonction c printf
jmp fin

continu:
mov rsi,qword[rsi+8]           ; [rsi+8] pointeur sur argument 1 => le password

mov rdi,rsi                    ; pointeur sur argument 1
call atoi                      ; fonction : conversion string en nombre 

mov rsi,0xdeadbeef             ; 0xdeadbeef = 3735928559 en décimal
cmp rax,rsi

jne badpassword 

goodpassword:
mov rdi,fmt1                
mov rsi,msg1                   ; affiche : congratulations 
xor rax,rax                 
;call [printf wrt ..got]       ; type d'appelle de la fonction c printf (pour pie)
call printf                    ; appelle de la fonction c printf
jmp fin

badpassword: 
 
mov rdi,fmt2
mov rsi,msg2                   ; affiche : Failed 
xor rax,rax                
;call [printf wrt ..got]       ; type d'appelle de la fonction c printf (pour pie)
call printf                    ; appelle de la fonction c printf

fin:
pop rbp                        ; restaure la pile
xor rax,rax                    ; normale, pas d'erreur
ret                            ; return


```



Succès

```
./reverse01 3735928559
Congratulations - validation : MARS{<user input>}
```



Echec

```
./reverse01 abcd
Failed
```



Options de compilation

```bash
nasm -f elf64 -l crackme01.lst  crackme01.asm
gcc -m64 -no-pie -o crackme01  crackme01.o
```



## Solution

Challenge de type reverse. Trouver le password.

```
./crackme01 3735928559
```

Utilisation de `objdump` pour éditer les diverses sections

```
objdump -D -M intel32 -j .text crackme01
objdump -s -M intel32 -j .data crackme01
objdump -s -M intel32 -j .rodata crackme01
```



Contenu de la section .rodata

```
 402000 01000200 636f6e67 72617475 6c617469  ....congratulati
 402010 6f6e730a 00257310 00666169 6c65640a  ons..%s..failed.
 402020 00257307 00                          .%s..    

 Adresse Chaine de caractères
 4020004 congratulations\n
 4020009 failed\n
```



Contenu de la section .text

```assembly
0000000000401140 <main>:
  401140:	55                   	push   rbp
  401141:	57                   	push   rdi
  401142:	56                   	push   rsi
  401143:	48 be 04 20 40 00 00 	movabs rsi,0x402004
  40114a:	00 00 00 
  40114d:	48 bf 76 21 40 00 00 	movabs rdi,0x402176
  401154:	00 00 00 
  401157:	48 31 c0             	xor    rax,rax
  40115a:	e8 d1 fe ff ff       	call   401030 <printf@plt>
  40115f:	5e                   	pop    rsi
  401160:	5f                   	pop    rdi
  401161:	48 83 ff 02          	cmp    rdi,0x2
  401165:	74 1e                	je     401185 <continu>
  401167:	48 be 7a 21 40 00 00 	movabs rsi,0x40217a
  40116e:	00 00 00 
  401171:	48 bf 76 21 40 00 00 	movabs rdi,0x402176
  401178:	00 00 00 
  40117b:	48 31 c0             	xor    rax,rax
  40117e:	e8 ad fe ff ff       	call   401030 <printf@plt>
  401183:	eb 50                	jmp    4011d5 <fin>

0000000000401185 <continu>:
  401185:	48 8b 76 08          	mov    rsi,QWORD PTR [rsi+0x8]
  401189:	48 89 f7             	mov    rdi,rsi
  40118c:	e8 af fe ff ff       	call   401040 <atoi@plt>
  401191:	be ef be ad de       	mov    esi,0xdeadbeef
  401196:	48 39 f0             	cmp    rax,rsi
  401199:	75 1e                	jne    4011b9 <badpassword>

000000000040119b <goodpassword>:
  40119b:	48 bf d1 21 40 00 00 	movabs rdi,0x4021d1
  4011a2:	00 00 00 
  4011a5:	48 be 9b 21 40 00 00 	movabs rsi,0x40219b
  4011ac:	00 00 00 
  4011af:	48 31 c0             	xor    rax,rax
  4011b2:	e8 79 fe ff ff       	call   401030 <printf@plt>
  4011b7:	eb 1c                	jmp    4011d5 <fin>

00000000004011b9 <badpassword>:
  4011b9:	48 bf dd 21 40 00 00 	movabs rdi,0x4021dd
  4011c0:	00 00 00 
  4011c3:	48 be d6 21 40 00 00 	movabs rsi,0x4021d6
  4011ca:	00 00 00 
  4011cd:	48 31 c0             	xor    rax,rax
  4011d0:	e8 5b fe ff ff       	call   401030 <printf@plt>

00000000004011d5 <fin>:
  4011d5:	5d                   	pop    rbp
  4011d6:	48 31 c0             	xor    rax,rax
  4011d9:	c3                   	ret    
  4011da:	66 0f 1f 44 00 00    	nop    WORD PTR [rax+rax*1+0x0]

```




En x64, argv qui est un tableau de pointeurs est contenu dans rsi.  


[rsi+0x4] = nom du programme
[rsi+0x8] = argument 1 (password)

La fonction libc atoi convertit une chaîne de caractères en un entier (nombre).
Cela siginifie que la chaîne de caractères doit contenir des chiffres, sinon la conversion est impossible

Exemple :

```
atoi("1234") => 1234  ok 
atoi("abcd") =>       error
```



Comparaison de la chaîne saisie (convertie en un entier) contenu dans rax avec la valeur hexadécimal : 0xdeadbeef

```
mov    esi,0xdeadbeef
cmp    rax,rsi
```

Attention 0xdeadbeef est une valeur hexadécimale. la conversion en décimal donne 3735928559.
On peut modifier la première ligne de code de la facon suivante

```
mov    esi, 3735928559
cmp    rax,rsi
```


Donc rax doit être égal à : 3735928559

Le flag est : 3735928559

```
./crackme01 3735928559
```

```
   __  __                        _    _            _
  |  \/  |                 ____ | |  | |          | |
  | \  / | __ _ _ __ ___  / __ \| |__| | __ _  ___| | __
  | |\/| |/ _` | '__/ __|/ / _` |  __  |/ _` |/ __| |/ /
  | |  | | (_| | |  \__ \ | (_| | |  | | (_| | (__|   < 
  |_|  |_|\__,_|_|  |___/\ \__,_|_|  |_|\__,_|\___|_|\_\
                          \____/

   Congratulations !
   Validation : MARS{<password>}
 
```



Résultat : MARS{3735928559}







