import datetime

class Tournament:
    """
    Le programme utilise les fichiers de données JSON pour la persistance des informations sur
    les tournois. Les fichiers de données sont généralement situés dans le dossier
    data/tournaments.

    ● Un tournoi a un nombre de tours défini.

    Chaque tournoi doit contenir au moins les informations suivantes :
        ● nom ;
        ● lieu ;
        ● date de début et de fin ;
        ● nombre de tours – réglez la valeur par défaut sur 4 ;
        ● numéro correspondant au tour actuel ;
        ● une liste des tours ;
        ● une liste des joueurs enregistrés ;
        ● description pour les remarques générales du directeur du tournoi.
    """
    NUMBER_OF_ROUNDS = 4

    def __init__(self, name, location, description):
        self.name = name
        self.location = location
        self.description = description
        self.start_date = str
        self.end_date = str
        self.current_round_number = []
        self.rounds_list = []
        self.players_list = []
    pass

    def set_start_date(self):
        self.start_date = datetime.datetime.now().replace(microsecond=0)

    def set_end_date(self):
        self.end_date = datetime.datetime.now().replace(microsecond=0)



tournoi1 = Tournament("Tournoi des rois", "Paris", "Il s'agit d'un tournoi exceptionnel !")



"""
Donne la date et l'heure actuelles >>> datetime.datetime.now().replace(microsecond=0)

"""