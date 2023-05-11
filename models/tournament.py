import datetime
import random
from random import shuffle, sample
from models import rounds
from models import match

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

    def __repr__(self):
        return f"Tournoi : {self.name} - Localisation : {self.location}"

    def set_start_date(self):
        self.start_date = datetime.datetime.now().replace(microsecond=0)

    def begin_round(self):
        if self.current_round_number <= 4:
            self.current_round_number += 1
        else:
            return "Tournoi terminé."

    def set_end_date(self):
        self.end_date = datetime.datetime.now().replace(microsecond=0)

    def add_player_to_tournament(self, player_to_add):
        self.players_list.append(player_to_add)

    def shuffle_players(self):
        shuffle(self.players_list)

    def create_pairs(self):
        pairings = sample(self.players_list, len(self.players_list))
        self.pairs_list.extend(pairings)

    def create_first_round_matches(self, first_round):
        for player in range(0, len(self.pairs_list), 2):
            first_round.add_match(match.Match(self.pairs_list[player], self.pairs_list[player + 1]))

    def create_next_round_matches(self, next_round):
        for player in range(0, len(self.players_list), 2):
            next_round.add_match(match.Match(self.players_list[player], self.players_list[player + 1]))

    def sort_players(self):
        self.players_list.sort()

    def show_players_rank(self):
        print("Classement actuel des joueurs :")
        for index, player in enumerate(self.players_list, 1):
            print(f"{index} >> {player}")

    def end_round(self, round):
        self.rounds_list.append(round)

"""
tournoi1 = Tournament("Pâté de crabe", "Bikini Bottom", "Meilleur tournoi des mers")
tournoi1.add_player_to_tournament(bob)
tournoi1.add_player_to_tournament(patrick)
tournoi1.add_player_to_tournament(carlo)
tournoi1.add_player_to_tournament(sandy)
tournoi1.add_player_to_tournament(crabs)
tournoi1.add_player_to_tournament(plankton)
print(tournoi1.players_list)

tournoi1.create_pairs()
print(tournoi1.pairs_list)
print(tournoi1.players_list)

match1 = match.Match(sample(tournoi1.pairs_list, 1), sample(tournoi1.pairs_list, 1))
match2 = match.Match(sample(tournoi1.pairs_list, 1), sample(tournoi1.pairs_list, 1))
print(match1, match2)



match1 = match.Match(*random.sample(tournoi1.players_list, 2))
print(match1)

Donne la date et l'heure actuelles >>> datetime.datetime.now().replace(microsecond=0)

#A ranger dans Vues
    def show_players_list(self):
        print("Voici la liste des participants !")
        for player in self.players_list:
            print(f"{player.first_name} {player.name}")

"""