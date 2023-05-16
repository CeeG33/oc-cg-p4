import json
from os import path, makedirs


class Match:
    """
    ○ Chaque match consiste en une paire de joueurs

    """
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.winner = None
        self.draw = None

    def __repr__(self):
        return f"{self.player1} -- VS -- {self.player2}"

    @classmethod
    def create_from_json(cls, player1, player2):
        player1 = player1
        player2 = player2
        existing_json_file_path = f"data/matches/{player1}_VS_{player2}.json"
        if path.exists(existing_json_file_path):
            with open(existing_json_file_path, "r", encoding="utf-8") as json_file:
                match_data = json.load(json_file)
                match = cls(match_data["player1"],
                            match_data["player2"])
                match.winner = match_data.get("winner")
                match.draw = match_data.get("draw")
                return match
        else:
            return "Ce match n'existe pas"

    def chose_winner(self, player):
        self.winner = player

    def is_draw(self):
        self.draw = self.player1, self.player2

    def update_json_file(self):
        directory_path = f"data/matches/"
        if not path.exists(directory_path):
            makedirs(directory_path)
            json_file_name = f"data/matches/{self.player1}_VS_{self.player2}.json"
            data = {
                "player1": str(self.player1),
                "player2": str(self.player2),
                "winner": self.winner,
                "draw": self.draw,
            }
            if path.exists(json_file_name):
                with open(json_file_name, "r", encoding="utf-8") as json_file:
                    match_data = json.load(json_file)
                    match_data.update(data)
                with open(json_file_name, "w", encoding="utf-8") as json_file:
                    json.dump(match_data, json_file, indent=4, ensure_ascii=False)
            else:
                with open(json_file_name, "w", encoding="utf-8") as json_file:
                    json.dump(data, json_file, indent=4, ensure_ascii=False)
        else:
            json_file_name = f"data/matches/{self.player1}_VS_{self.player2}.json"
            data = {
                "player1": str(self.player1),
                "player2": str(self.player2),
                "winner": self.winner,
                "draw": self.draw,
            }
            if path.exists(json_file_name):
                with open(json_file_name, "r", encoding="utf-8") as json_file:
                    match_data = json.load(json_file)
                    match_data.update(data)
                with open(json_file_name, "w", encoding="utf-8") as json_file:
                    json.dump(match_data, json_file, indent=4, ensure_ascii=False)
            else:
                with open(json_file_name, "w", encoding="utf-8") as json_file:
                    json.dump(data, json_file, indent=4, ensure_ascii=False)


"""
#Déplacer dans une vue
    def show_match_composition(self):
        print("Ce match se compose de :")
        for player in self.pair_list:
            print(f"{player.first_name} {player.name}")
"""