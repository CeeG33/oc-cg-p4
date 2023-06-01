import datetime
import json
import os
from models import match


class Round:
    def __init__(self, round_name: str):
        self.round_name = round_name
        self.start_date = None
        self.end_date = None
        self.match_list = []

    def __repr__(self):
        """Définit le nom du round en tant que représentation de l'objet Round."""
        return f"{self.round_name}"

    @classmethod
    def create_from_json(cls, round_name):
        """Charge un objet round à partir d'un fichier JSON existant selon le nom du round."""
        existing_json_file_path = f"data/rounds/{round_name}.json"
        if os.path.exists(existing_json_file_path):
            with open(existing_json_file_path, "r", encoding="utf-8") as json_file:
                round_data = json.load(json_file)
                created_round = cls(round_data["round_name"])
                created_round.start_date = round_data.get("start_date")
                created_round.end_date = round_data.get("end_date")
                created_round.match_list = []
                for match_data in round_data.get("match_list", []):
                    player1_data = match_data["player1"]
                    player1_name = player1_data["name"]
                    player1_first_name = player1_data["first_name"]
                    player2_data = match_data["player2"]
                    player2_name = player2_data["name"]
                    player2_first_name = player2_data["first_name"]
                    match_object = match.Match.create_from_json(f"{player1_first_name} {player1_name}",
                                                                f"{player2_first_name} {player2_name}")
                    created_round.match_list.append(match_object)
                return created_round
        else:
            return

    def set_start_date(self):
        """Initialise la date et l'heure de début du round."""
        self.start_date = str(datetime.datetime.now().replace(microsecond=0))

    def set_end_date(self):
        """Initialise la date et l'heure de fin du round."""
        self.end_date = str(datetime.datetime.now().replace(microsecond=0))

    def add_match(self, match_name):
        """Ajoute le match sélectionné dans la liste de matchs du round."""
        self.match_list.append(match_name)

    def update_json_file(self):
        """
        Crée le dossier ci-dessous s'ils n'existent pas.
        Ensuite, crée ou écrase le fichier JSON.
        """
        directory_path = "data/rounds/"
        json_file_name = f"data/rounds/{self.round_name}.json"

        if not os.path.exists(directory_path):
            os.makedirs(directory_path)

        with open(json_file_name, "w", encoding="utf-8") as json_file:
            json.dump(self.to_dict(), json_file, indent=4, ensure_ascii=False)

    def to_dict(self):
        """Renvoie le dictionnaire du round."""
        data = {
            "round_name": self.round_name,
            "start_date": str(self.start_date) if self.start_date else None,
            "end_date": str(self.end_date) if self.end_date else None,
            "match_list": [contest.to_dict() for contest in self.match_list],
        }
        return data
