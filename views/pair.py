
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