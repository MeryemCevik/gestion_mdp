# Créé par mcevi, le 05/01/2023 en Python 3.7, version 1

import time
import bcrypt
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


"""---------------------Mission 4-------------------------

1) - Proposer une solution ou méthode qui permettrait d’accélérer la vitesse de traitement de l’attaque par catalogue

"""
#Bcrypt est loin d'être le meilleur des types de hachage en terme de vitesse de traitemnt
img = mpimg.imread('Terahash.jpg')
plt.title('Voici une image qui liste les hachages les plus vites')
imgplot = plt.imshow(img)
manager = plt.get_current_fig_manager()
manager.window.showMaximized()
plt.show()
#on voit que bcrypt est l'avant dernier de la liste :( , ce qui pose un vrai problème de vitesse
#Changer le type de hachage peut éventuellement accélérer la vitesse de traitement
#D'après le tableau, le mieux serait d'utliser le hachage ntlm pour plus de rapidité

import hashlib,binascii

def hachage_ntlm(mdp):
    hash = hashlib.new('md4', mdp.encode('utf-16le')).digest()
    mdp_hashe = binascii.hexlify(hash)
    return str(mdp_hashe,'utf-8')

"""

2) - Proposer un ajout à votre programme pour créer votre propre catalogue en utilisant les missions précédentes et la première question de la mission 4

"""
#

#-----------------fonctions de la mission 3------------------------
liste=['a', 'b', 'c','d', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C','D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','0','1','2','3','4','5','6','7','8','9','$', '@', '#', '%', '_', '"', '!', '§', '&', '/', '(', ')', '=', '?', '*', '€', ',', ';', ':','.']


def hachage_bcrypt(motdepasse):
    motdepasse = motdepasse.encode('utf-8')
    # On génère un sel
    sel = bcrypt.gensalt()
    # On hache le mot de passe avec le sel
    mdp_hasher = bcrypt.hashpw(motdepasse, sel)
    mdp_hasher=str(mdp_hasher,'utf-8')             # ! changement ! : ajout d'une ligne pour convertire le mdp en bytes en string
    return mdp_hasher # On retourne le mot de passe haché et selé

def force_brute(mdp,liste):
    chaine = str() #chaine pour stocker les lettres trouvé
    if(mdp!=""): # si l'utilisateur à bien écrit un mot de passe
        for l in mdp : # pour chaque lettre du mdp
            for c in liste : # pour chaque caractère du liste
                if l == c: #on compare
                    chaine=chaine+c
    print('Le mot de passe trouvé est ',chaine)

#--------------exemple de TEST pour comparer----------------

#le mot de passe choisi
mdp=""

#2 - hachage ntlm
print("----------------hachage ntlm------------------")
print("Attaque force brut avec seulement des caractères alpha en minuscule")
mdp="motdepassemotdepassemotdepassemotdepasse"
mdp1=hachage_ntlm(mdp)
print("La longueur du mdp haché est ",len(mdp1))
#mdp="motdepasse"
start1 = time.time()
force_brute(mdp1,liste)
end1 = time.time()
temps1 = end1 - start1
print("Le temps de craquage de votre mot de passe est de ",temps1)
if (len(mdp)<=12):
    print("Force : très faible")
elif(len(mdp)<=16):
    print("Force : faible")
elif(len(mdp)<=20):
    print("Force : moyen")
elif(len(mdp)>20):
    print("Force : fort")
print("--------------------------------------------------")


#2 - hachage bcrypt
print("--------------hachage bcrypt------------------")
print("Attaque force brut avec seulement des caractères alpha en minuscule")
mdp="motdepassemotdepassemotdepassemotdepasse"
mdp1=hachage_bcrypt(mdp)
print("La longueur du mdp haché est ",len(mdp1))
#mdp="motdepasse"
start1 = time.time()
force_brute(mdp1,liste)
end1 = time.time()
temps1 = end1 - start1
print("Le temps de craquage de votre mot de passe est de ",temps1)
if (len(mdp)<=12):
    print("Force : très faible")
elif(len(mdp)<=16):
    print("Force : faible")
elif(len(mdp)<=20):
    print("Force : moyen")
elif(len(mdp)>20):
    print("Force : fort")
print("--------------------------------------------------")

# une capture d'écran du résultat affiché dans la console
img = mpimg.imread('ss-résultat.png')
plt.title('Résultat pour bcrypt et ntlm')
imgplot = plt.imshow(img)
manager = plt.get_current_fig_manager()
manager.window.showMaximized()
plt.show()
