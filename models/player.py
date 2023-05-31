import json
import os
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
                player.national_chess_id = player_data.get("national_chess_id")
                return player
        else:
            return

    def update_json_file(self):
        directory_path = f"data/players/"
        json_file_name = f"data/players/{self.first_name}_{self.name}.json"
        if not path.exists(directory_path):
            makedirs(directory_path)
            if path.exists(json_file_name):
                with open(json_file_name, "r+", encoding="utf-8") as json_file:
                    player_data = json.load(json_file)
                    player_data.update(self.__dict__)
            else:
                with open(json_file_name, "w", encoding="utf-8") as json_file:
                    json.dump(self.__dict__, json_file, indent=4, ensure_ascii=False)
        else:
            if path.exists(json_file_name):
                with open(json_file_name, "r+", encoding="utf-8") as json_file:
                    player_data = json.load(json_file)
                    player_data.update(self.__dict__)
            else:
                with open(json_file_name, "w", encoding="utf-8") as json_file:
                    json.dump(self.__dict__, json_file, indent=4, ensure_ascii=False)

    def add_national_chess_id(self, national_chess_id):
        self.national_chess_id = national_chess_id

    @staticmethod
    def list_existing_players():
        existing_players = []
        directory_path = "data/players/"

        for file in os.listdir(directory_path):
            file_name = os.path.join(directory_path, file)

            if file.endswith(".json") and os.path.isfile(file_name):
                player_name = file.replace("_", " ").replace(".json", "")
                splitted_player_name = player_name.split()
                created_player = Player.create_from_json(splitted_player_name[1], splitted_player_name[0])
                existing_players.append(created_player)

        return sorted(existing_players, key=lambda x: x.first_name)

    def to_dict(self):
        data = {
            "name": self.name,
            "first_name": self.first_name,
            "birthdate": self.birthdate,
            "global_rank": self.global_rank,
            "global_score": self.global_score,
            "national_chess_id": self.national_chess_id
        }
        return data

"""
player1 = Player("Test1", "Test1NDF", "02/04/2003")
player2 = Player("Test2", "Test2NDF", "02/04/2002")
player3 = Player("Test3", "Test3NDF", "02/04/2003")
player4 = Player("Test4", "Test4NDF", "02/04/2004")

players_list = [player1, player2, player3, player4]

print(players_list)

directory_path = f"data/tournaments/"
json_file_name = f"data/tournaments/test2.json"
data = {
    "players_list": [player.to_dict() for player in players_list],

}
if not path.exists(directory_path):
    makedirs(directory_path)
    if path.exists(json_file_name):
        with open(json_file_name, "r+", encoding="utf-8") as json_file:
            tournament_data = json.load(json_file)
            tournament_data.update(data)
    else:
        with open(json_file_name, "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4, ensure_ascii=False)
else:
    if path.exists(json_file_name):
        with open(json_file_name, "r+", encoding="utf-8") as json_file:
            tournament_data = json.load(json_file)
            tournament_data.update(data)
    else:
        with open(json_file_name, "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4, ensure_ascii=False)


"""