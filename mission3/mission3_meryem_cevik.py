# Créé par mcevik, le 29/12/2022 en Python 3.7, version 3
import time
import bcrypt
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


"""Mission 3
- timer
- test avec rapport
1) attaque par dictionnaire
2) attaque force brut avec seulement des caractères alpha en minuscule
3) attaque force brut avec seulement des caractères alpha en minuscules et majuscules
4) attaque force brut avec seulement des caractères alphanumériques en minuscule
5) attaque force brut avec seulement des caractères alphanumériques en minuscule et majuscules
6) attaque force brut avec seulement des caractères alphanumériques et des signes en minuscule
7) attaque force brut avec seulement des caractères alphanumériques et des signes en minuscule et majuscule
8) attaque force brut avec seulement des caractères alpha en minuscule et le remplacement de certaine lettre par une correspondance ou leur numéro dans l’alphabet
9) attaque force brut sur toutes les caractéristiques ci-dessus

"""

#-----------------fonctions de la mission 2------------------------
liste=['a', 'b', 'c','d', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C','D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','0','1','2','3','4','5','6','7','8','9','$', '@', '#', '%', '_', '"', '!', '§', '&', '/', '(', ')', '=', '?', '*', '€', ',', ';', ':','.']

def hachage(motdepasse):
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

def util_dict(mdp):
    #mot de passe les plus utilisé
    dic=open('french_passwords_top20000.txt',mode='r')
    for mot in dic:
        mot=mot.strip()#élimination espace
        if mot==mdp:
            print("Mot de passe trouvé ",mot)

    #mots d'un dictionnaire
    dic=open('dictionnaire.txt',mode='r')#ouvre fichier texte ayant les mots du dictionnaire
    for mot1 in dic:
        mot1=mot1.strip()#élimination espace
        if mot1==mdp:
            print("Mot de passe trouvé ",mot1)

    #sinon attaque force brute
    force_brute(mdp,liste)

def remplacmt(mdp):
    liste_origine=['a','e','o','i','l','s','b','s','et','b','g']
    liste_remplacement=['@','€','0','1','1','5','8','$','&','6','9']
    chaine=str() #pour stocker le mot après remplacement
    for j,c in enumerate(mdp):
        for i in range(len(liste_remplacement)):
            if c==liste_remplacement[i]: #compare la lettre du mdp avec les caractères de la liste_remplacment
                chaine=chaine+liste_origine[i]
        if mdp[j] not in liste_remplacement:
            chaine=chaine+mdp[j]
    return chaine

def ajout_lettre(mdp):
    # supprime l'occurence de la lettre répété plusieurs fois
    import re # ici j'importe la libraririe regex pour utiliser la fonction re.compile et re.sub
    return re.compile( r"(.)\1+" ).sub( r"\1", mdp )
    """---------Courte explication de l'utilisation de la librairie Regex----------
    la partie compile nous permet de déterminer la forme et ce qui va comporter, on l'obligation d'ajouter un r pour référencer la chaine
    le point permet de faire une recherche pour tout carcatère confondus
    la partie sub permet de faire un remplacemen spécifié, remplace la partie souhaiter(r"\1") dans le mdp
    """
def util_maj(mdp): #on transforme tout en minuscule pour faciliter par après la comparaison
    chaine=mdp.lower()
    return chaine

#---------------------------------------------------TEST--------------------------------------------------------------------

#le mot de passe choisi
mdp=""

#1
mdp="pomme"
print("----------Analyse attaque par dictionnaire----------------")
start = time.time()
util_dict(mdp)
end = time.time()
temps=end - start
print("Le temps de craquage de votre mot de passe est de ",temps)
print("--------------------------------------------------")
#2
print("Attaque force brut avec seulement des caractères alpha en minuscule")
mdp="mo"
mdp1=hachage(mdp)
print(mdp1)
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

#3
print("attaque force brut avec seulement des caractères alpha en minuscules et majuscules")
mdp="Mo"
mdp1=hachage(mdp)
#mdp="MotDePasse"
start = time.time()
force_brute(mdp1,liste)
end = time.time()
temps= end - start
print("Le temps de craquage de votre mot de passe est de ",temps)
if (len(mdp)<=12):
    print("Force : très faible")
elif(len(mdp)<=16):
    print("Force : moyen")
elif(len(mdp)>16):
    print("Force : fort")
print("--------------------------------------------------")
#4
print("attaque force brut avec seulement des caractères alphanumériques en minuscule")
mdp="mot1"
mdp1=hachage(mdp)
#mdp="motdepasse1234"
start = time.time()
force_brute(mdp1,liste)
end = time.time()
temps= end - start
print("Le temps de craquage de votre mot de passe est de ",temps)
if (len(mdp)<=12):
    print("Force : très faible")
elif(len(mdp)<=16):
    print("Force : moyen")
elif(len(mdp)>16):
    print("Force : fort")
print("--------------------------------------------------")
#5
print("attaque force brut avec seulement des caractères alphanumériques en minuscule et majuscules")
#mdp="MotDePasse1234"
mdp="Mot1"
mdp1=hachage(mdp)
start = time.time()
force_brute(mdp1,liste)
end = time.time()
temps= end - start
print("Le temps de craquage de votre mot de passe est de ",temps)
if (len(mdp)<=12):
    print("Force : très faible")
elif(len(mdp)<=16):
    print("Force : moyen")
elif(len(mdp)>16):
    print("Force : fort")
print("--------------------------------------------------")
#6
print("attaque force brut avec seulement des caractères alphanumériques et des signes en minuscule")
mdp="mot1$"
mdp1=hachage(mdp)
#mdp="motd€passe1234$"
start = time.time()
force_brute(mdp1,liste)
end = time.time()
temps= end - start
print("Le temps de craquage de votre mot de passe est de ",temps)
if (len(mdp)<=12):
    print("Force : très faible")
elif(len(mdp)<=16):
    print("Force : moyen")
elif(len(mdp)>16):
    print("Force : fort")
print("--------------------------------------------------")
#7
print("attaque force brut avec seulement des caractères alphanumériques et des signes en minuscule et majuscule")
mdp="Mmo1$"
mdp1=hachage(mdp)
#mdp="MotDePasse1234$$$$"
start = time.time()
force_brute(mdp1,liste)
end = time.time()
temps= end - start
print("Le temps de craquage de votre mot de passe est de ",temps)
if (len(mdp)<=10):
    print("Force : très faible")
elif(len(mdp)<=12):
    print("Force : faible")
elif(len(mdp)>16):
    print("Force : fort")
print("--------------------------------------------------")
#8
print("attaque force brut avec seulement des caractères alpha en minuscule et le remplacement de certaine lettre par une correspondance ou leur numéro dans l’alphabet")
mdp="all€r"
#mdp="motd€pa$$e"
start = time.time()
mdp=remplacmt(mdp)
mdp1=hachage(mdp)
force_brute(mdp1,liste)
end = time.time()
temps= end - start
print("Le temps de craquage de votre mot de passe est de ",temps)
if (len(mdp)<=10):
    print("Force : très faible")
elif(len(mdp)<=12):
    print("Force : faible")
elif(len(mdp)>16):
    print("Force : fort")
print("--------------------------------------------------")
#9
print("attaque force brut sur toutes les caractéristiques ci-dessus")
mdp="all€r1$"
#mdp="MotD€Passe1234$*%"
start = time.time()
mdp=remplacmt(mdp)
mdp1=hachage(mdp)
util_dict(mdp1)
force_brute(mdp1,liste)
end = time.time()
temps= end - start
print("Le temps de craquage de votre mot de passe est de ",temps)
if (len(mdp)<=10):
    print("Force : très faible")
elif(len(mdp)<=12):
    print("Force : faible")
elif(len(mdp)>16):
    print("Force : fort")
print("--------------------------------------------------")
#10 : affiche le graphique qui permet d'obtenir la résistance moyenne des mots de passe selon la taille et la composition
img = mpimg.imread('Hive+Systems+Password+Table.png')
plt.title('Résistance moyenne des mots de passe selon la taille et la composition')
imgplot = plt.imshow(img)
plt.show()
