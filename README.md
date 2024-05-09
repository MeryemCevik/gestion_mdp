# Application de gestion de mot de passe
-----------------------------------------------
L'objectif de mon projet est de créer un vérificateur de mot de passe qui va tester sa force donner sa force sous forme de pourcentage par rapport aux recommandations de l'ANSSI.
Langages informatique utilisés : Python
Logiciels utilisés : Visual Studio Code
-----------------------------------------------

Mission 1 : J'ai développé une application en Python pour chiffrer les mots de passe des utilisateurs. Cette application permet à l'utilisateur de saisir un mot de passe, puis d'utiliser la fonction de hachage bcrypt pour le sécuriser. J'ai également inclus une mesure de la force du mot de passe, qui évalue sa robustesse à mesure que l'utilisateur le saisit. De plus, j'ai donné à l'utilisateur la possibilité d'ajouter un salage choisi ou généré par l'application.

Mission 2 : J'ai créé une application Python pour craquer les mots de passe hachés avec bcrypt. Cette application offre plusieurs techniques d'attaque, notamment la force brute, l'utilisation de dictionnaires, des techniques de substitution de caractères, et des méthodes combinées telles que la force brute avec dictionnaire. Elle prend également en compte l'utilisation de salage dans les mots de passe.

Mission 3 : Pour tester mon application, j'ai mis en place un ensemble de tests automatisés. Ces tests mettent en évidence la résistance des mots de passe en fonction de leur taille et de leur composition. J'ai utilisé des timers pour évaluer le temps nécessaire pour craquer les mots de passe en utilisant les différentes techniques d'attaque décrites dans la Mission 2.

Mission 4 : J'ai proposé une méthode pour accélérer l'attaque par dictionnaire en utilisant un catalogue. De plus, j'ai ajouté une fonctionnalité à mon programme qui permet de générer son propre catalogue en utilisant les techniques de hachage et de salage de la Mission 1.

Mission 5 : En analysant mon logiciel de craquage de mots de passe, j'ai identifié son principal défaut : sa sensibilité aux attaques de type force brute, notamment sur des mots de passe plus faibles ou simples. Pour améliorer cela, je propose d'implémenter des politiques de mot de passe plus strictes, encourageant les utilisateurs à choisir des mots de passe plus complexes et plus longs. Cette approche peut considérablement renforcer la sécurité des mots de passe contre les attaques par force brute.
