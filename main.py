
# VUES #
"""
Une fois le programme lancé, l'utilisateur utilisera le menu principal pour effectuer des
actions. Nous vous laissons le soin de décider de la liste des menus. Tant que l'utilisateur
peut effectuer les actions spécifiées ci-dessus, nous serons contents !
"""

class Rank:
    pass

class Pair:
    """
    GÉNÉRATION DES PAIRES
        ● Au début du premier tour, mélangez tous les joueurs de façon aléatoire.
        ● Chaque tour est généré dynamiquement en fonction des résultats des joueurs dans
        le tournoi en cours.
            ○ Triez tous les joueurs en fonction de leur nombre total de points dans le
            tournoi.
            ○ Associez les joueurs dans l’ordre (le joueur 1 avec le joueur 2, le joueur 3
            avec le joueur 4 et ainsi de suite.)
            ○ Si plusieurs joueurs ont le même nombre de points, vous pouvez les choisir
            de façon aléatoire.
            ○ Lors de la génération des paires, évitez de créer des matchs identiques
            (c’est-à-dire les mêmes joueurs jouant plusieurs fois l’un contre l’autre).
                ■ Par exemple, si le joueur 1 a déjà joué contre le joueur 2,
                associez-le plutôt au joueur 3.
        ● Mettez à jour les points de tous les joueurs après chaque tour et répétez le
        processus de triage et d’association jusqu'à ce que le tournoi soit terminé.
        ● Un tirage au sort des joueurs définira qui joue en blanc et qui joue en noir ; il n'est
        donc pas nécessaire de mettre en place un équilibrage des couleurs
    """
    pass

class Report:
    """
    RAPPORTS
    Nous aimerions pouvoir afficher les rapports suivants dans le programme :
        ● liste de tous les joueurs par ordre alphabétique ;
        ● liste de tous les tournois ;
        ● nom et dates d’un tournoi donné ;
        ● liste des joueurs du tournoi par ordre alphabétique ;
        ● liste de tous les tours du tournoi et de tous les matchs du tour.
    Nous aimerions les exporter ultérieurement, mais ce n'est pas nécessaire pour l'instant.
    Les rapports peuvent être en texte brut, à condition qu'ils soient bien formatés et faciles à
    lire. Vous pouvez même utiliser des modèles HTML !
    """
    pass

class SaveData:
    """
    Nous devons pouvoir sauvegarder et charger l'état du programme à tout moment entre
    deux actions de l'utilisateur. Plus tard, nous aimerions utiliser une base de données, mais
    pour l'instant nous utilisons des fichiers JSON pour garder les choses simples.

    Les fichiers JSON doivent être mis à jour à chaque fois qu'une modification est apportée
    aux données afin d'éviter toute perte. Le programme doit s'assurer que les objets en
    mémoire sont toujours synchronisés avec les fichiers JSON. Le programme doit également
    charger toutes ses données à partir des fichiers JSON et pouvoir restaurer son état entre
    les exécutions.

    """
    pass

class LoadData:
    """
    Nous devons pouvoir sauvegarder et charger l'état du programme à tout moment entre
    deux actions de l'utilisateur. Plus tard, nous aimerions utiliser une base de données, mais
    pour l'instant nous utilisons des fichiers JSON pour garder les choses simples.

    Les fichiers JSON doivent être mis à jour à chaque fois qu'une modification est apportée
    aux données afin d'éviter toute perte. Le programme doit s'assurer que les objets en
    mémoire sont toujours synchronisés avec les fichiers JSON. Le programme doit également
    charger toutes ses données à partir des fichiers JSON et pouvoir restaurer son état entre
    les exécutions.

    """
    pass







