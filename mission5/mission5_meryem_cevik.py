# Créé par mcevi, le 05/01/2023 en Python 3.7, version 1

"""--------------------------------------------------------------------------------------
----------------------------Défauts de sécurité -----------------------------------------
------------------------------------------------------------------------------------------


--------------------------------------- SOLUTION  1-----------------------------------------

Je pense que programme de craquage de mot de passe reste faible ne matière de cyber-sécurité.
On peut transformer le fichier python .py en .pyc, l'extension .pyc est le fichier .py compilé
en bytescode se qui rend le programme illisible pour une personne physique.

Pour cela, il faut executé les instructions (que je ne vais pas le faire mais expliqué) :
    -Cliquez sur le bouton "Démarrer " puis sur " Ordinateur". Naviguez vers le répertoire
    contenant les fichiers PY que vous souhaitez convertir en fichiers PYC .
    -Appuyez et maintenez enfoncée la touche "Shift" et cliquez à droite espace vide dans
    le répertoire du fichier PY . Cliquez sur " Ouvrir la fenêtre de commande ici " option de menu.
    - écrire « python- m compileall " sur la ligne de commande et appuyez sur "Entrée".
    - Tapez "dir" à l'invite de commande et appuyez sur " Entrée". afficher la sortie de ligne
    de commande pour confirmer que tous les fichiers PY ont un fichier PYC correspondant .

Pour le lire, il faudrait le reconvertir en .py avec un des logiciels en ligne que l'on peut
trouver sur le site : http://fr.filedict.com/python-45907/

L'inconvénient c'est que c'est facilement reversibles si on fait un minimum de recherche sur internet.
C'est pour ça, on va utiliser le cryptage :)

--------------------------------------- SOLUTION  2--------------------------------------------------------------

Avce crypto (pip install pycryptodome), on pourra faire un crypatage RSA de notre programme qui devrait compliquer
encore plus le "reverse engineering". La clé public va être communiqué aux salariés pour le décrypté en
sécurité.

Pour cela, il faudrait coder cela ou bien utiliser delui d'un autre pour crypté notre programme.
Le tutoriel à l'url suivante https://askcodez.com/cryptage-et-decryptage-rsa-en-python.html est très bien fait.

On peut tout a fait crypter autrement par exemple on peut décaler les lettres pour crypter .
Par exemple j'ai un code tel que :

"""
strssmall = 'abcdefghijklmnopqrstuvwxyz'
strscaps = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

shift =  1 # How many characters need to shift
def encrypt(inp):
    data = []
    for i in inp:
        if i.strip() and i in strssmall:
            data.append(strssmall[(strssmall.index(i) + shift) % 26])
        elif i.strip() and i in strscaps:
            data.append(strscaps[(strscaps.index(i) + shift) % 26])
        else:
            data.append(i)
    output = ''.join(data)
    return output
def decrypt(inp):
    data = []
    for i in inp:
        if i.strip() and i in strssmall:
            data.append(strssmall[(strssmall.index(i) - shift) % 26])
        elif i.strip() and i in strscaps:
            data.append(strscaps[(strscaps.index(i) - shift) % 26])
        else:
            data.append(i)
    output = ''.join(data)
    return output

choice = input('Do you want to decrypt or encrypt a sentence? (d / e) :')
question = 'Give me a sentence to %s\n'

if choice == 'd':
    #encrypted_str = input(question % 'decrypt')
    decrypted_str = decrypt("\n neq_ibtifs = cdszqu.ibtiqx(npuefqbttf, tfm) \n neq_ibtifs=tus(neq_ibtifs,'vug-8')")
    print(decrypted_str)

elif choice == 'e':
    #plaintext = input(question % 'encrypt')
    encrypted_str = encrypt("\n mdp_hasher = bcrypt.hashpw(motdepasse, sel) \n mdp_hasher=str(mdp_hasher,'utf-8')")
    print(encrypted_str)

else:
    print('That is not a valid option')



"""
Ce code va permettre de crypter un programme entier. Puis pour décrypter rien de plus facile. Il suffit d'utiliser ce programme automatisé.
Source du programme (https://www.useblackbox.io/search).

Pour crypter:

    mdp_hasher = bcrypt.hashpw(motdepasse, sel)
    mdp_hasher=str(mdp_hasher,'utf-8')

 ------Le résultat sur la console de l'utilisation du programme----------
|                                                                        |
|    Do you want to decrypt or encrypt a sentence? (d / e) :e            |
|     neq_ibtifs = cdszqu.ibtiqx(npuefqbttf, tfm)                        |
|     neq_ibtifs=tus(neq_ibtifs,'vug-8')                                 |
 ------------------------------------------------------------------------

En décryptant on a:

 ------Le résultat sur la console de l'utilisation du programme----------
|    Do you want to decrypt or encrypt a sentence? (d / e) :d           |
|     mdp_hasher = bcrypt.hashpw(motdepasse, sel)                       |
|     mdp_hasher=str(mdp_hasher,'utf-8')                                |
 ------------------------------------------------------------------------


 """