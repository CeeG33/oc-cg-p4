import json
from os import path, makedirs


class Player:
    """
    Nous aimerions que l'application hors ligne contienne une base de données des joueurs
    dans des fichiers JSON. Le programme devrait avoir une section dédiée à l'ajout de joueurs
    et chaque joueur devrait contenir au moins les données suivantes :
        ● Nom de famille
        ● Prénom
        ● Date de naissance
    """

    def __init__(self, name: str, first_name: str, birthdate: str):
        self.name = name
        self.first_name = first_name
        self.birthdate = birthdate
        self.global_rank = 0
        self.global_score = 0
        self.national_chess_id = None

    def __repr__(self):
        return f"{self.first_name} {self.name}"

    def __lt__(self, other):
        return self.global_score > other.global_score

    @classmethod
    def create_from_json(cls, name, first_name):
        existing_json_file_path = f"data/players/{first_name}_{name}.json"
        if path.exists(existing_json_file_path):
            with open(existing_json_file_path, "r", encoding="utf-8") as json_file:
                player_data = json.load(json_file)
                player = cls(player_data["name"],
                             player_data["first_name"],
                             player_data["birthdate"])
                player.global_rank = player_data.get("global_rank")
                player.global_score = player_data.get("global_score")
                return player
        else:
            return "Ce joueur n'existe pas"

    def update_json_file(self):
        directory_path = f"data/players/"
        if not path.exists(directory_path):
            makedirs(directory_path)
            json_file_name = f"data/players/{self.first_name}_{self.name}.json"
            if path.exists(json_file_name):
                with open(json_file_name, "r", encoding="utf-8") as json_file:
                    player_data = json.load(json_file)
                    player_data.update(self.__dict__)
                with open(json_file_name, "w", encoding="utf-8") as json_file:
                    json.dump(player_data, json_file, indent=4, ensure_ascii=False)
            else:
                with open(json_file_name, "w", encoding="utf-8") as json_file:
                    json.dump(self.__dict__, json_file, indent=4, ensure_ascii=False)
        else:
            json_file_name = f"data/players/{self.first_name}_{self.name}.json"
            if path.exists(json_file_name):
                with open(json_file_name, "r", encoding="utf-8") as json_file:
                    player_data = json.load(json_file)
                    player_data.update(self.__dict__)
                with open(json_file_name, "w", encoding="utf-8") as json_file:
                    json.dump(player_data, json_file, indent=4, ensure_ascii=False)
            else:
                with open(json_file_name, "w", encoding="utf-8") as json_file:
                    json.dump(self.__dict__, json_file, indent=4, ensure_ascii=False)

    def add_national_chess_id(self, national_chess_id):
        self.national_chess_id = national_chess_id
