import datetime
import json
from os import path, makedirs
from models import match


class Round:
    """
    ● Chaque tour est une liste de matchs.

    En plus de la liste des matchs, chaque instance du tour doit contenir un nom.

    Actuellement, nous appelons nos tours "Round 1", "Round 2", etc. Elle doit également
    contenir un champ Date et heure de début et un champ Date et heure de fin, qui doivent
    tous deux être automatiquement remplis lorsque l'utilisateur crée un tour et le marque
    comme terminé.
    """

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
        """Charge un round à partir d'un fichier JSON."""
        existing_json_file_path = f"data/rounds/{round_name}.json"
        if path.exists(existing_json_file_path):
            with open(existing_json_file_path, "r", encoding="utf-8") as json_file:
                round_data = json.load(json_file)
                created_round = cls(round_data["round_name"])
                created_round.start_date = round_data.get("start_date")
                created_round.end_date = round_data.get("end_date")
                created_round.match_list = []
                for match_data in round_data.get("match_list", []):
                    match_player1 = match_data["player1"]
                    match_player2 = match_data["player2"]
                    match_object = match.Match(match_player1, match_player2)
                    created_round.match_list.append(match_object)
                return created_round
        else:
            return

    def set_start_date(self):
        """Initialise la date et l'heure de début du round."""
        self.start_date = str(datetime.datetime.now().replace(microsecond=0))

    def set_end_date(self):
        """Initialise la date et l'heure de fin du tournoi."""
        self.end_date = str(datetime.datetime.now().replace(microsecond=0))

    def add_match(self, match_name):
        """Ajoute le match sélectionné dans la liste de matchs du round."""
        self.match_list.append(match_name)

    def update_json_file(self):
        """
        Crée les dossiers ci-dessous s'ils n'existent pas.
        Ensuite, crée ou met à jour le fichier JSON.
        """
        directory_path = f"data/rounds/"
        json_file_name = f"data/rounds/{self.round_name}.json"
        if not path.exists(directory_path):
            makedirs(directory_path)
            if path.exists(json_file_name):
                with open(json_file_name, "r+", encoding="utf-8") as json_file:
                    round_data = json.load(json_file)
                    round_data.update(self.to_dict())
            else:
                with open(json_file_name, "w", encoding="utf-8") as json_file:
                    json.dump(self.to_dict(), json_file, indent=4, ensure_ascii=False)
        else:
            if path.exists(json_file_name):
                with open(json_file_name, "r+", encoding="utf-8") as json_file:
                    round_data = json.load(json_file)
                    round_data.update(self.to_dict())
            else:
                with open(json_file_name, "w", encoding="utf-8") as json_file:
                    json.dump(self.to_dict(), json_file, indent=4, ensure_ascii=False)

    def to_dict(self):
        """Renvoie le dictionnaire du round."""
        data = {
            "round_name": self.round_name,
            "start_date": str(self.start_date) if self.start_date else None,
            "end_date": str(self.end_date) if self.end_date else None,
            "match_list": [match.to_dict() for match in self.match_list],
        }
        return data

    def get_matches(self):
        """Retourne la liste des matchs."""
        return self.match_list


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
