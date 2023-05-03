import datetime
import player

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

    def __init__(self,
                 name: str,
                 location: str,
                 description: str,
                 start_date: str = None,
                 end_date: str = None):
        self.name = name
        self.location = location
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.current_round_number = []
        self.rounds_list = []
        self.competitors_list = []


    def set_start_date(self):
        self.start_date = datetime.datetime.now().replace(microsecond=0)

    def set_end_date(self):
        self.end_date = datetime.datetime.now().replace(microsecond=0)

    def add_player_to_tournament(self, player_to_add):
        self.player_to_add = player_to_add
        self.competitors_list.append(self.player_to_add)



tournoi1 = Tournament("Tournoi des rois", "Paris", "Il s'agit d'un tournoi exceptionnel !")


joueur1 = player.Player("Etoile de mer", "Patrick", "01/02/2000")
joueur2 = player.Player("L'Éponge", "Bob", "05/06/2002")
tournoi1.add_player_to_tournament(joueur1)
tournoi1.add_player_to_tournament(joueur2)





"""
Donne la date et l'heure actuelles >>> datetime.datetime.now().replace(microsecond=0)


#A ranger dans Vues
    def show_players_list(self):
        print("Voici la liste des participants !")
        for player in self.players_list:
            print(f"{player.first_name} {player.name}")
"""