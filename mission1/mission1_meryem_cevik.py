# Créé par meryem cevik, le 13/12/2022 en Python 3.7, version 2
import bcrypt

"""--------------------Mission 1---------------------
- Saisie par l’utilisateur d’un mot de passe ok
- un hachage à l’aide de bcrypt ok
- Une mesure de la force des mots de passe (penser à utiliser les expression régulière),
indication de la valeur au fur et à mesure de la saisie du mot de passe
- Possibilité d’ajouter un salage (choisi par l’utilisateur ou généré par l’application) ok
-----------------------------------------------------
"""

"""Cette fonction hache et sèle un mot de passe"""
def hachage_selage(motdepasse):
    motdepasse = motdepasse.encode('utf-8')
    # On génère un sel
    sel = bcrypt.gensalt()
    # On hache le mot de passe avec le sel
    mdp_hasher = bcrypt.hashpw(motdepasse, sel)
    return mdp_hasher # On retourne le mot de passe haché et selé

#print("Mot de passe haché et selé",hachage_selage(mdp))

"""Cette fonction vérifie les lettres du mot de passe un par un
Contrainte mot de passe :
 - entre 8 et 20 characters long
 - doit contenir au moins un nombre
 - doit contenir au moins une lettre en majuscule et une lettre minuscule
 - doit contenir au moins un des caractère spéciale tel que !"§$%&/()=?
"""

def verif(mdp):
    score = 0 # ce score va variez selon la force du mdp, représente la force du mot de passe
    complexite="faible"
    mini, maj, nb, carac = 0, 0, 0, 0
    #initialisation des compteurs pour les lettres majuscules (maj), minuscule (mini), caractères spéciaux (carac) et nombres (nb)
    longueur=len(mdp) #longueur du mot de passe
    if (longueur >= 8):
        for i in range(longueur):
            # compte minuscules
            if (mdp[i].islower()):
                mini+=1

            # compte majuscules
            if (mdp[i].isupper()):
                maj+=1

            # compte les nombres
            if (mdp[i].isdigit()):
                nb+=1

            # compte caractères spéciaux
            if(mdp[i]=='@'or mdp[i]=='$' or mdp[i]=='_' or mdp[i]=='#' or mdp[i]=='%' or mdp[i]=='"' or mdp[i]=='!' or mdp[i]=='§' or mdp[i]=='&' or mdp[i]=='/' or mdp[i]=='(' or mdp[i]==')' or mdp[i]=='=' or mdp[i]=='?' or mdp[i]=='*' or mdp[i]=='€' or mdp[i]==',' or mdp[i]==';' or mdp[i]==':'):
                carac+=1
    else:
        complexite="très court !"

    val = True #booléen pour la vérification et pour donner une indication à l'utilisateurs
    SpecialSym =['$', '@', '#', '%', '_', '"','`', '!', '§', '&', '/', '(', ')', '=', '?', '*', '€', ',', ';', ':','-','.',','] #listes des symboles spéciales

    #Vérifie si contient au moin caractère special, un nombre, une lettre majuscule et minuscule. et que la somme des compteurs sont égaux à la longueur
    # la longueur doit etre entre 8 et 16
    if (mini>=1 and maj>=1 and carac>=1 and nb>=1 and mini+maj+nb+carac==len(mdp) and longueur>=8 and longueur<16):
        score=100
    # la longueur doit etre égal à 16 ou plus long
    elif (mini>=1 and maj>=1 and carac>=1 and nb>=1 and mini+maj+nb+carac==len(mdp) and longueur>=16):
        score=100
    #lettres majuscules et minuscules seulement
    elif (mini>=1 and maj>=1 and carac==0  and nb==0 and mini+maj==len(mdp) and longueur>=8):
        score=0
    # minuscules seulement
    elif (mini>=1 and maj==0 and carac==0  and nb==0 and mini==len(mdp) and longueur>=8):
        score=0
    # que des majuscules
    elif (mini==0 and maj>=1 and carac==0  and nb==0 and maj==len(mdp) and longueur>=8):
        score=0
    # nombres seulement
    elif (mini==0 and maj==0 and carac==0  and nb>=1 and nb==len(mdp) and longueur>=8):
        score=0

    # Addition Partie Score :
    elif (longueur>=8):
        score=0
        score+=2*(mini)
        score+=3*(maj)
        score+=5*(nb)
        score+=10*(carac)
        for i in range(longueur):
            if(mdp[i]==mdp[i-1]): #si caractères consécutifs
                score=score-2
    #éviter d'avoir un score de plus de 100% ou moins de 0%
    if ((score>100)):
        score=100
    if (score<0):
        score=0
    #Partie affichage de la complexite et score :
    #print(mini,maj,nb,carac,longueur)
    print("Score : ",("\033"*score),score,"%")
    #print(complexite)

#------------------------------------------TEST--------------------------------------------------
#demande du mot du passe
mdp = input("Entrez votre mot de passe : ")
print('\n')

#hashage
print ("-----------------Partie hachage du mot de passe-----------------------")
print("mot de passe de départ :",mdp)
print("mot de passed hashé et selé :",hachage_selage(mdp))
print('\n')

#testeur force
print ("-----------------Testeur de la force du mot de passe-----------------------")
verif(mdp)

