import datetime
import json
import os
from os import path, makedirs, listdir
from random import shuffle, sample
from models import match, rounds, player


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
                 description: str,):
        self.name = name
        self.location = location
        self.description = description
        self.start_date = None
        self.end_date = None
        self.current_round_number = 0
        self.rounds_list = []
        self.players_list = []
        self.pairs_list = []
        self.winners_list = []
        self.draw_list = []
        self.players_scores = None

    def __repr__(self):
        """Définit le nom du tournoi en tant que représentation de l'objet Tournoi."""
        return f"{self.name}"

    @classmethod
    def create_from_json(cls, name):
        """Charge un tournoi à partir d'un fichier JSON."""
        existing_json_file_path = f"data/tournaments/{name}.json"
        if path.exists(existing_json_file_path):
            with open(existing_json_file_path, "r", encoding="utf-8") as json_file:
                tournament_data = json.load(json_file)
                temporary_tournament = cls(tournament_data["name"],
                                           tournament_data["location"],
                                           tournament_data["description"])
                temporary_tournament.start_date = tournament_data.get("start_date")
                temporary_tournament.end_date = tournament_data.get("end_date")
                temporary_tournament.current_round_number = tournament_data.get("current_round_number")
                temporary_tournament.rounds_list = []
                for round_data in tournament_data.get("rounds_list", []):
                    round_name = round_data["round_name"]
                    round_object = rounds.Round(round_name)
                    temporary_tournament.rounds_list.append(round_object)
                temporary_tournament.players_list = []
                for participant in tournament_data.get("players_list", []):
                    participant_name = participant["name"]
                    participant_first_name = participant["first_name"]
                    participant_object = player.Player.create_from_json(participant_name, participant_first_name)
                    temporary_tournament.players_list.append(participant_object)
                temporary_tournament.pairs_list = []
                for participant in tournament_data.get("pairs_list", []):
                    participant_name = participant["name"]
                    participant_first_name = participant["first_name"]
                    participant_object = player.Player.create_from_json(participant_name, participant_first_name)
                    temporary_tournament.pairs_list.append(participant_object)
                temporary_tournament.winners_list = []
                for participant in tournament_data.get("winners_list", []):
                    participant_name = participant["name"]
                    participant_first_name = participant["first_name"]
                    participant_object = player.Player.create_from_json(participant_name, participant_first_name)
                    temporary_tournament.winners_list.append(participant_object)
                temporary_tournament.draw_list = []
                for participant in tournament_data.get("draw_list", []):
                    participant_name = participant["name"]
                    participant_first_name = participant["first_name"]
                    participant_object = player.Player.create_from_json(participant_name, participant_first_name)
                    temporary_tournament.draw_list.append(participant_object)
                temporary_tournament.players_scores = tournament_data.get("players_scores")

                return temporary_tournament
        else:
            return

    def set_start_date(self):
        """Initialise la date et l'heure de début du tournoi."""
        self.start_date = str(datetime.datetime.now().replace(microsecond=0))

    def set_round_number(self):
        """Règle le numéro du round actuel."""
        if self.current_round_number <= 4:
            self.current_round_number += 1
        else:
            return

    def set_end_date(self):
        """Initialise la date et l'heure de fin du tournoi."""
        self.end_date = str(datetime.datetime.now().replace(microsecond=0))

    def add_player_to_tournament(self, player_to_add):
        """Ajoute le joueur sélectionné dans la liste des joueurs participants au tournoi."""
        self.players_list.append(player_to_add)

    def shuffle_players(self):
        """Mélange les joueurs participants."""
        shuffle(self.players_list)

    def create_pairs(self):
        """Crée les paires de matchs dans la liste des paires."""
        pairings = sample(self.players_list, len(self.players_list))
        self.pairs_list.extend(pairings)

    def create_first_round_matches(self, first_round):
        """Crée les matchs du premier round selon la liste des paires."""
        for participant in range(0, len(self.pairs_list), 2):
            try:
                first_round.add_match(match.Match(self.pairs_list[participant], self.pairs_list[participant + 1]))
            except IndexError:
                return

    def create_next_round_matches(self, next_round):
        """
        Crée les matchs du round suivant selon la liste des paires.
        Les joueurs auront préalablement été triés dans la liste de scores de façon décroissante.
        """
        sorted_players = sorted(self.players_scores, key=self.players_scores.get, reverse=True)
        for player in range(0, len(sorted_players), 2):
            next_round.add_match(match.Match(sorted_players[player], sorted_players[player+1]))

    def sort_players(self):
        """Trie la liste des scores de façon décroissante."""
        self.players_scores = dict(sorted(self.players_scores.items(), key=lambda x: x[1], reverse=True))

    def save_json_file(self):
        """
        Crée les dossiers ci-dessous s'ils n'existent pas.
        Ensuite, crée ou met à jour le fichier JSON.
        """
        directory_path = f"data/tournaments/"
        json_file_name = f"data/tournaments/{self.name}.json"

        if not path.exists(directory_path):
            makedirs(directory_path)

        with open(json_file_name, "w", encoding="utf-8") as json_file:
            json.dump(self.to_dict(), json_file, indent=4, ensure_ascii=False)

    def initialize_players_scores(self):
        """Initialise le score des joueurs à zéro dans le cadre du tournoi."""
        default_value = 0
        self.players_scores = dict.fromkeys(self.players_list, default_value)

    def add_one_point_to(self, participant):
        """
        Ajoute la valeur ci-dessous au score joueur sélectionné dans le cadre du tournoi.
        Ajoute également cette même valeur au score global du joueur (elo).
        """
        self.players_scores[participant] += 1
        participant.global_score += 1

    def add_half_point_to(self, participant):
        """
        Ajoute la valeur ci-dessous au score joueur sélectionné dans le cadre du tournoi.
        Ajoute également cette même valeur au score global du joueur (elo).
        """
        self.players_scores[participant] += 0.5
        participant.global_score += 0.5

    def save_players_score(self):
        """Sauvegarde les données des joueurs."""
        for participant in self.players_list:
            participant.update_json_file()

    @staticmethod
    def list_existing_tournaments():
        """Liste les tournois présents dans la base de données."""
        existing_tournaments = []
        directory_path = "data/tournaments/"

        for tournament in os.listdir(directory_path):
            file_names = os.path.join(directory_path, tournament)

            if tournament.endswith(".json") and os.path.isfile(file_names):
                existing_tournaments.append(tournament.replace("_", " ").replace(".json", ""))

        return sorted(existing_tournaments)

    def to_dict(self):
        """Renvoie le dictionnaire du tournoi."""
        data = {
            "name": self.name,
            "location": self.location,
            "description": self.description,
            "start_date": self.start_date if self.start_date else None,
            "end_date": self.end_date if self.end_date else None,
            "current_round_number": self.current_round_number,
            "rounds_list": [r.to_dict() for r in self.rounds_list] if self.rounds_list else [],
            "players_list": [participant.to_dict() for participant in self.players_list] if self.players_list else [],
            "pairs_list": [participant.to_dict() for participant in self.pairs_list] if self.pairs_list else [],
            "winners_list": [participant.to_dict() for participant in self.winners_list] if self.winners_list else [],
            "draw_list": [participant.to_dict() for participant in self.draw_list] if self.draw_list else [],
            "players_scores": [participant.to_dict() for participant in self.players_scores] if self.players_scores else [],
        }
        return data

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