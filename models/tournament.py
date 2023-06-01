import datetime
import json
import os
import random
from models import match, rounds, player


class Tournament:
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
        self.players_scores = {}

    def __repr__(self):
        """Définit le nom du tournoi en tant que représentation de l'objet Tournoi."""
        return f"{self.name}"

    @classmethod
    def create_from_json(cls, name):
        """Charge un objet tournoi à partir d'un fichier JSON selon le nom du tournoi renseigné en paramètre."""
        existing_json_file_path = f"data/tournaments/{name}.json"
        if os.path.exists(existing_json_file_path):
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
                    round_object = rounds.Round.create_from_json(round_name)
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
                temporary_tournament.players_scores = {}
                for national_chess_id, score in tournament_data.get("players_scores", []):
                    temporary_tournament.players_scores[national_chess_id] = score

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
        """Mélange la liste des joueurs participants."""
        random.shuffle(self.players_list)

    def create_pairs(self):
        """Crée les paires de matchs dans la liste des paires."""
        pairings = random.sample(self.players_list, len(self.players_list))
        self.pairs_list.extend(pairings) if (len(self.pairs_list)) == 0 else None

    def create_first_round_matches(self, first_round):
        """Crée les matchs du premier round selon la liste des paires."""
        for participant in range(0, len(self.pairs_list), 2):
            try:
                first_round.add_match(match.Match(self.pairs_list[participant], self.pairs_list[participant + 1]))
            except IndexError:
                return

    def create_next_round_matches(self, next_round):
        """Crée les matchs du round suivant selon les scores des joueurs par ordre décroissant."""
        sorted_players = sorted(self.players_list, key=lambda participant: self.players_scores[
            participant.national_chess_id],
                                reverse=True)
        for participant in range(0, len(sorted_players), 2):
            next_round.add_match(match.Match(sorted_players[participant], sorted_players[participant+1]))

    def sort_players(self):
        """Trie la liste des scores de façon décroissante."""
        temporary_ranking = [(participant, self.players_scores[participant.national_chess_id]) for participant in
                             self.players_list]
        sorted_ranking = sorted(temporary_ranking, key=lambda x: x[1], reverse=True)
        return sorted_ranking

    def save_json_file(self):
        """
        Crée les dossiers ci-dessous s'ils n'existent pas.
        Ensuite, crée ou met à jour le fichier JSON.
        """
        directory_path = "data/tournaments/"
        json_file_name = f"data/tournaments/{self.name}.json"

        if not os.path.exists(directory_path):
            os.makedirs(directory_path)

        with open(json_file_name, "w", encoding="utf-8") as json_file:
            json.dump(self.to_dict(), json_file, indent=4, ensure_ascii=False)

    def initialize_players_scores(self):
        """Initialise le score des joueurs à zéro dans le cadre du tournoi."""
        players_id = []
        for participant in self.players_list:
            players_id.append(participant.national_chess_id)
        default_value = 0

        self.players_scores = dict.fromkeys(players_id, default_value)

    def add_one_point_to(self, participant):
        """Ajoute la valeur ci-dessous au score joueur sélectionné dans le cadre du tournoi."""
        participant_id = participant.national_chess_id
        self.players_scores[participant_id] += 1

    def add_half_point_to(self, participant):
        """Ajoute la valeur ci-dessous au score joueur sélectionné dans le cadre du tournoi."""
        participant_id = participant.national_chess_id
        self.players_scores[participant_id] += 0.5

    def save_players(self):
        """Sauvegarde les données des joueurs."""
        for participant in self.players_list:
            participant.update_json_file()

    @staticmethod
    def list_existing_tournaments():
        """Renvoie la liste des tournois présents dans la base de données par ordre alphabétique."""
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
            "players_scores": [
                [national_chess_id, score]
                for national_chess_id, score in self.players_scores.items()
            ] if self.players_scores else [],
        }
        return data
