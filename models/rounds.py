import datetime
from match import match1


class Round:
    """
    ● Chaque tour est une liste de matchs.

    En plus de la liste des matchs, chaque instance du tour doit contenir un nom.

    Actuellement, nous appelons nos tours "Round 1", "Round 2", etc. Elle doit également
    contenir un champ Date et heure de début et un champ Date et heure de fin, qui doivent
    tous deux être automatiquement remplis lorsque l'utilisateur crée un tour et le marque
    comme terminé.
    """

    def __init__(self,
                 round_name: str,
                 start_date: str = None,
                 end_date: str = None,
                 round_number: int = range(1, 5)):

        self.round_name = round_name
        self.start_date = start_date
        self.end_date = end_date
        self.round_number = round_number
        self.match_list = []


    def set_start_date(self):
        self.start_date = datetime.datetime.now().replace(microsecond=0)

    def set_end_date(self):
        self.end_date = datetime.datetime.now().replace(microsecond=0)

    def add_match(self, match_name):
        self.match_name = match_name
        self.match_list.append(self.match_name)


round1 = Round("Round 1")
round1.add_match(match1)

print(round1.match_list)

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
