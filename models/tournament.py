import datetime
import json
from os import path, makedirs
from random import shuffle, sample
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
        self.winners_list = []
        self.draw_list = []
        self.players_scores = None

    def __repr__(self):
        return f"Tournoi : {self.name} - Localisation : {self.location}"

    @classmethod
    def create_from_json(cls, name):
        name = name
        existing_json_file_path = f"data/tournaments/{name}.json"
        if path.exists(existing_json_file_path):
            with open(existing_json_file_path, "r", encoding="utf-8") as json_file:
                tournament_data = json.load(json_file)
                temporary_tournament = cls(tournament_data["name"],
                                           tournament_data["location"],
                                           tournament_data["description"],
                                           tournament_data["start_date"],
                                           tournament_data["end_date"],
                                           tournament_data["current_round_number"])
                temporary_tournament.rounds_list = tournament_data.get("rounds_list")
                temporary_tournament.players_list = tournament_data.get("players_list")
                temporary_tournament.pairs_list = tournament_data.get("pairs_list")
                temporary_tournament.winners_list = tournament_data.get("winners_list")
                temporary_tournament.draw_list = tournament_data.get("draw_list")
                temporary_tournament.players_scores = tournament_data.get("players_scores")
                return temporary_tournament
        else:
            return "Ce tournoi n'existe pas"

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
        sorted_players = sorted(self.players_scores, key=self.players_scores.get, reverse=True)
        for player in range(0, len(sorted_players), 2):
            next_round.add_match(match.Match(sorted_players[player], sorted_players[player+1]))

    def sort_players(self):
        self.players_scores = dict(sorted(self.players_scores.items(), key=lambda x: x[1], reverse=True))

    def show_players_rank(self):
        sorted_players = sorted(self.players_scores, key=self.players_scores.get, reverse=True)
        print("Classement actuel des joueurs :")
        for index, player in enumerate(sorted_players, 1):
            print(f"{index} >> {player}")

    def end_round(self, round_to_end):
        self.rounds_list.append(round_to_end)

    def update_json_file(self):
        directory_path = f"data/tournaments/"
        if not path.exists(directory_path):
            makedirs(directory_path)
            json_file_name = f"data/tournaments/{self.name}.json"
            data = {
                "name": f"{self.name}",
                "location": f"{self.location}",
                "description": f"{self.description}",
                "start_date": f"{self.start_date}",
                "end_date": f"{self.end_date}",
                "current_round_number": self.current_round_number,
                "rounds_list": f"{self.rounds_list}",
                "players_list": f"{self.players_list}",
                "pairs_list": f"{self.pairs_list}",
                "winners_list": f"{self.winners_list}",
                "draw_list": f"{self.draw_list}",
                "players_scores": f"{self.players_scores}",
            }
            if path.exists(json_file_name):
                with open(json_file_name, "r", encoding="utf-8") as json_file:
                    tournament_data = json.load(json_file)
                    tournament_data.update(data)
                with open(json_file_name, "w", encoding="utf-8") as json_file:
                    json.dump(tournament_data, json_file, indent=4, ensure_ascii=False)
            else:
                with open(json_file_name, "w", encoding="utf-8") as json_file:
                    json.dump(data, json_file, indent=4, ensure_ascii=False)
        else:
            json_file_name = f"data/tournaments/{self.name}.json"
            data = {
                "name": f"{self.name}",
                "location": f"{self.location}",
                "description": f"{self.description}",
                "start_date": f"{self.start_date}",
                "end_date": f"{self.end_date}",
                "current_round_number": self.current_round_number,
                "rounds_list": f"{self.rounds_list}",
                "players_list": f"{self.players_list}",
                "pairs_list": f"{self.pairs_list}",
                "winners_list": f"{self.winners_list}",
                "draw_list": f"{self.draw_list}",
                "players_scores": f"{self.players_scores}",
            }
            if path.exists(json_file_name):
                with open(json_file_name, "r", encoding="utf-8") as json_file:
                    tournament_data = json.load(json_file)
                    tournament_data.update(data)
                with open(json_file_name, "w", encoding="utf-8") as json_file:
                    json.dump(tournament_data, json_file, indent=4, ensure_ascii=False)
            else:
                with open(json_file_name, "w", encoding="utf-8") as json_file:
                    json.dump(data, json_file, indent=4, ensure_ascii=False)

    def get_scores(self):
        default_value = 0
        self.players_scores = dict.fromkeys(self.players_list, default_value)

    def add_one_point_to(self, player):
        self.players_scores[player] += 1
        player.global_score += 1

    def add_half_point_to(self, player):
        self.players_scores[player] += 0.5
        player.global_score += 0.5

    def reinitialise_winners_list(self):
        self.winners_list = []

    def reinitialise_draw_list(self):
        self.draw_list = []


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