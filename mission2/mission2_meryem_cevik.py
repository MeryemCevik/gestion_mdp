# Créé par meryem cevik, le 21/12/2022 en Python 3.7, version 1
import bcrypt
import string

"""-------------------Mission 2:------------------------
Créer en python une application permettant de craquer les mots de passe haché à l’aide de bcrypt
L’application devra permettre :
● La force brute    ok
● L’utilisation de dictionnaire     ok
● Mélange de la force brut et du dictionnaire   ok
● Remplacement de caractère par d’autre ou d’une lettre par sa position dans l’alphabet     ok
● Ajout de lettre   ok
● Par l’utilisation de majuscule    ok
● Utilisation de salage ok
--------------------------------------------------------
"""
mdp = input("Entrez votre mot de passe : ")

def hachage(motdepasse):
    motdepasse = motdepasse.encode('utf-8')
    # On génère un sel
    sel = bcrypt.gensalt()
    # On hache le mot de passe avec le sel
    mdp_hasher = bcrypt.hashpw(motdepasse, sel)
    return mdp_hasher # On retourne le mot de passe haché et selé

#stockage des caractères pouvant être utilisé pour un mot de passe
liste=['a', 'b', 'c','d', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C','D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','0','1','2','3','4','5','6','7','8','9','$', '@', '#', '%', '_', '"','`', '!', '§', '&', '/', '(', ')', '=', '?', '*', '€', ',', ';', ':','-','.',',']
#liste=list(string.printable)

def force_brute(mdp):
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
    dic=open('dictionnairev2.txt',mode='r')#ouvre fichier texte ayant les mots du dictionnaire
    for mot1 in dic:
        mot1=mot1.strip()#élimination espace
        if mot1==mdp:
            print("Mot de passe trouvé ",mot1)

def forceBrute_dict(mdp):
    dic=open('dictionnairev2.txt',mode='r')#ouvre fichier texte ayant les mots du dictionnaire
    for mot1 in dic:
        mot1=mot1.strip()#élimination espace
        for lettre in liste:
            mdp_suffixe=mot1+lettre #ajout de lettre après le mot
            mdp_prefixe=lettre+mot1 #ajout de lettre avant le mot
            if mdp_prefixe==mdp: #comparaison pour mdp_suffixe
                print("Mot de passe trouvé ",mdp_prefixe)
            if mdp_suffixe==mdp: #comparaison pour mdp_prefixe
                print("Mot de passe trouvé ",mdp_suffixe)

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
    print(chaine)

def ajout_lettre(mdp):
    # supprime l'occurence de la lettre répété plusieurs fois
    import re # ici j'importe la libraririe regex pour utiliser la fonction re.compile et re.sub
    return re.compile( r"(.)\1+" ).sub( r"\1", mdp )
    """---------Courte explication de l'utilisation de la librairie Regex----------
    la partie compile nous permet de déterminer la forme et ce qui va comporter, on l'obligation d'ajouter un r pour référencer la chaine
    le point permet de faire une recherche pour tout carcatère confondus
    la partie sub permet de faire un remplacemen spécifié, remplace la partie souhaiter(r"\1") dans le mdp
    """
def util_maj(mdp): #on transforme tout en minuscule pour faciliter la comparaison
    chaine=mdp.lower()
    return chaine

def util_salage(mdp): #l'utilisateur choisi un salage propre à lui
    salage=input("choisissez un salage devotre choix :")
    print("votre salage est ",salage)
    return mdp+salage

#-----------------------------------TEST-------------------------------
#print(mdp)
print(force_brute(mdp))
#print(util_dict(mdp))
#print(remplacmt(mdp))
#print(util_maj(mdp))
#print(ajout_lettre(mdp))
#print(forceBrute_dict(mdp))
#print(util_salage(mdp))