import datetime
import json
import os.path
from os import path

class Round:
    """
    ● Chaque tour est une liste de matchs.

    En plus de la liste des matchs, chaque instance du tour doit contenir un nom.

    Actuellement, nous appelons nos tours "Round 1", "Round 2", etc. Elle doit également
    contenir un champ Date et heure de début et un champ Date et heure de fin, qui doivent
    tous deux être automatiquement remplis lorsque l'utilisateur crée un tour et le marque
    comme terminé.
    """

    def __init__(self,
                 round_name: str,
                 start_date: str = None,
                 end_date: str = None):
        self.round_name = round_name
        self.start_date = start_date
        self.end_date = end_date
        self.match_list = []

    def __repr__(self):
        return f"{self.round_name} >> Début : {self.start_date} Fin : {self.end_date}"

    def set_start_date(self):
        self.start_date = datetime.datetime.now().replace(microsecond=0)

    def set_end_date(self):
        self.end_date = datetime.datetime.now().replace(microsecond=0)

    def add_match(self, match_name):
        self.match_list.append(match_name)

    def update_json_file(self):
        directory_path = f"data/rounds/"
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)
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
