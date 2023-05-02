

class Round:
    """
    ● Chaque tour est une liste de matchs.

    En plus de la liste des matchs, chaque instance du tour doit contenir un nom.

    Actuellement, nous appelons nos tours "Round 1", "Round 2", etc. Elle doit également
    contenir un champ Date et heure de début et un champ Date et heure de fin, qui doivent
    tous deux être automatiquement remplis lorsque l'utilisateur crée un tour et le marque
    comme terminé.
    """

    def __init__(self, round_name=int):
        self.round_name = round_name
        self.match_list = []
        self.start_date = "str"
        self.end_date = "str"
        self.round_number = "int"
    pass

round_imaginaire = Round(1)
print(round_imaginaire.round_number)

"""
    ">>> A déplacer dans EndContest : 
    Un match unique doit être stocké sous la forme d'un tuple contenant deux 
    listes, chacune contenant deux éléments : un joueur et un score. Les matchs doivent être stockés sous
    forme de liste dans l'instance du tour auquel ils appartiennent.
    
    Actuellement, nous appelons nos tours "Round 1", "Round 2", etc. Elle doit également
    contenir un champ Date et heure de début et un champ Date et heure de fin, qui doivent
    tous deux être automatiquement remplis lorsque l'utilisateur crée un tour et le marque
    comme terminé.
"""