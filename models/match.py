import json
import os.path
import random
from os import path

class Match:
    """
    ○ Chaque match consiste en une paire de joueurs

    """
    def __init__(self, player1: str, player2: str):
        self.player1 = player1
        self.player2 = player2
        self.winner = None
        self.draw = None


    def __repr__(self):
        return f"{self.player1} -- VS -- {self.player2}"

    def chose_winner(self, player):
        self.winner = player

    def is_draw(self):
        self.draw = self.player1, self.player2

    def update_json_file(self):
        directory_path = f"data/matches/"
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)
            json_file_name = f"data/matches/{self.player1}_VS_{self.player2}.json"
            data = {
                "player1": str(self.player1),
                "player2": str(self.player2),
                "player1_score": self.player1_score,
                "player2_score": self.player2_score,
                "tuple": f"{self.tuple}"
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
                "player1_score": self.player1_score,
                "player2_score": self.player2_score,
                "tuple": f"{self.tuple}"
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

    def create_from_json(self, player1, player2):
        player1 = player1
        player2 = player2
        existing_json_file_path = f"data/matches/{player1}_VS_{player2}.json"
        if path.exists(existing_json_file_path):
            with open(existing_json_file_path, "r", encoding="utf-8") as json_file:
                match_data = json.load(json_file)
                self.player1 = match_data.get("player1")
                self.player2 = match_data.get("player2")
                self.player1_score = match_data.get("player1_score")
                self.player2_score = match_data.get("player2_score")
                self.tuple = match_data.get("tuple")
        else:
            return "Ce match n'existe pas"


"""
print(match1)
match1.player1_wins()
match1.draw()
print(f"Score Bob : {match1.player1_score}")
print(f"Score Patrick : {match1.player2_score}")
match1.update_player1_global_score()
match1.update_player2_global_score()
print(bob.global_score)
print(patrick.global_score)
print(match1.tuple)



#Déplacer dans une vue
    def show_match_composition(self):
        print("Ce match se compose de :")
        for player in self.pair_list:
            print(f"{player.first_name} {player.name}")
"""