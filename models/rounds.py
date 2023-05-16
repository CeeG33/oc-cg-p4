import datetime
import json
from os import path, makedirs


class Round:
    """
    ● Chaque tour est une liste de matchs.

    En plus de la liste des matchs, chaque instance du tour doit contenir un nom.

    Actuellement, nous appelons nos tours "Round 1", "Round 2", etc. Elle doit également
    contenir un champ Date et heure de début et un champ Date et heure de fin, qui doivent
    tous deux être automatiquement remplis lorsque l'utilisateur crée un tour et le marque
    comme terminé.
    """

    def __init__(self,round_name: str):
        self.round_name = round_name
        self.start_date = None
        self.end_date = None
        self.match_list = []

    def __repr__(self):
        return f"{self.round_name} >> Début : {self.start_date} Fin : {self.end_date}"

    @classmethod
    def create_from_json(cls, round_name):
        round_name = round_name
        existing_json_file_path = f"data/rounds/{round_name}.json"
        if path.exists(existing_json_file_path):
            with open(existing_json_file_path, "r", encoding="utf-8") as json_file:
                round_data = json.load(json_file)
                temporary_round = cls(round_data["round_name"])
                temporary_round.start_date = round_data.get("start_date")
                temporary_round.end_date = round_data.get("end_date")
                temporary_round.match_list = round_data.get("match_list")
                return temporary_round
        else:
            return "Ce round n'existe pas"

    def set_start_date(self):
        self.start_date = datetime.datetime.now().replace(microsecond=0)

    def set_end_date(self):
        self.end_date = datetime.datetime.now().replace(microsecond=0)

    def add_match(self, match_name):
        self.match_list.append(match_name)

    def update_json_file(self):
        directory_path = f"data/rounds/"
        if not path.exists(directory_path):
            makedirs(directory_path)
            json_file_name = f"data/rounds/{self.round_name}.json"
            data = {
                "round_name": f"{self.round_name}",
                "start_date": f"{self.start_date}",
                "end_date": f"{self.end_date}",
                "match_list": f"{self.match_list}"
            }
            if path.exists(json_file_name):
                with open(json_file_name, "r", encoding="utf-8") as json_file:
                    round_data = json.load(json_file)
                    round_data.update(data)
                with open(json_file_name, "w", encoding="utf-8") as json_file:
                    json.dump(round_data, json_file, indent=4, ensure_ascii=False)
            else:
                with open(json_file_name, "w", encoding="utf-8") as json_file:
                    json.dump(data, json_file, indent=4, ensure_ascii=False)
        else:
            json_file_name = f"data/rounds/{self.round_name}.json"
            data = {
                "round_name": f"{self.round_name}",
                "start_date": f"{self.start_date}",
                "end_date": f"{self.end_date}",
                "match_list": f"{self.match_list}"
            }
            if path.exists(json_file_name):
                with open(json_file_name, "r", encoding="utf-8") as json_file:
                    round_data = json.load(json_file)
                    round_data.update(data)
                with open(json_file_name, "w", encoding="utf-8") as json_file:
                    json.dump(round_data, json_file, indent=4, ensure_ascii=False)
            else:
                with open(json_file_name, "w", encoding="utf-8") as json_file:
                    json.dump(data, json_file, indent=4, ensure_ascii=False)

    def get_matches(self):
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
