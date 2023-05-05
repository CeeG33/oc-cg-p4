import datetime
import random
from random import shuffle, sample
import match

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
                 end_date: str = None,
                 current_round_number: int = 0):
        self.name = name
        self.location = location
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.current_round_number = current_round_number
        self.rounds_list = []
        self.players_list = []
        self.pairs_list = []

    def set_start_date(self):
        self.start_date = datetime.datetime.now().replace(microsecond=0)

    def begin_round(self):
        self.current_round_number += 1

    def set_end_date(self):
        self.end_date = datetime.datetime.now().replace(microsecond=0)

    def add_player_to_tournament(self, player_to_add):
        self.players_list.append(player_to_add)

    def shuffle_players(self):
        shuffle(self.players_list)

    def create_pairs(self):
        pairings = sample(self.players_list, 2)
        self.pairs_list.extend(pairings)


tournoi1 = Tournament("Pâté de crabe", "Bikini Bottom", "Meilleur tournoi des mers")
tournoi1.add_player_to_tournament("Bob")
tournoi1.add_player_to_tournament("Patrick")
tournoi1.add_player_to_tournament("Carlo")
tournoi1.add_player_to_tournament("Sandy")
tournoi1.add_player_to_tournament("Crabs")
tournoi1.add_player_to_tournament("Plankton")
print(tournoi1.players_list)
tournoi1.shuffle_players()
tournoi1.create_pairs()
print(tournoi1.pairs_list)



"""
match1 = match.Match(*random.sample(tournoi1.players_list, 2))
print(match1)

Donne la date et l'heure actuelles >>> datetime.datetime.now().replace(microsecond=0)

#A ranger dans Vues
    def show_players_list(self):
        print("Voici la liste des participants !")
        for player in self.players_list:
            print(f"{player.first_name} {player.name}")
"""