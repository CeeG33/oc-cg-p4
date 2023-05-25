import json
from os import path, makedirs


class Match:

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.winner = None
        self.draw = None

    def __repr__(self):
        """Définit la composition du match en tant que représentation de l'objet Match."""
        return f"{self.player1} -- VS -- {self.player2}"

    @classmethod
    def create_from_json(cls, player1, player2):
        """
        Charge un match à partir d'un fichier JSON.
        Les paramètres sont le joueur 1 et le joueur 2 du match que l'on souhaite charger.
        """
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
            return

    def chose_winner(self, player):
        """Ajoute le gagnant du match à la liste du gagnant."""
        self.winner = player

    def is_draw(self):
        """Ajoute les deux joueurs dans la liste du match nul."""
        self.draw = [self.player1, self.player2]

    def update_json_file(self):
        """
        Crée les dossiers ci-dessous s'ils n'existent pas.
        Ensuite, crée ou met à jour le fichier JSON.
        """
        directory_path = f"data/matches/"
        json_file_name = f"data/matches/{self.player1}_VS_{self.player2}.json"
        if not path.exists(directory_path):
            makedirs(directory_path)
            if path.exists(json_file_name):
                with open(json_file_name, "r+", encoding="utf-8") as json_file:
                    match_data = json.load(json_file)
                    match_data.update(self.to_dict())
                with open(json_file_name, "w", encoding="utf-8") as json_file:
                    json.dump(match_data, json_file, indent=4, ensure_ascii=False)
            else:
                with open(json_file_name, "w", encoding="utf-8") as json_file:
                    json.dump(self.to_dict(), json_file, indent=4, ensure_ascii=False)
        else:
            if path.exists(json_file_name):
                with open(json_file_name, "r+", encoding="utf-8") as json_file:
                    match_data = json.load(json_file)
                    match_data.update(self.to_dict())
                with open(json_file_name, "w", encoding="utf-8") as json_file:
                    json.dump(match_data, json_file, indent=4, ensure_ascii=False)
            else:
                with open(json_file_name, "w", encoding="utf-8") as json_file:
                    json.dump(self.to_dict(), json_file, indent=4, ensure_ascii=False)

    def to_dict(self):
        """Renvoie le dictionnaire du match."""
        data = {
            "player1": self.player1.to_dict(),
            "player2": self.player2.to_dict(),
            "winner": self.winner.to_dict() if self.winner else None,
            "draw": [player.to_dict() for player in self.draw] if self.draw else []
        }
        return data

"""
#Déplacer dans une vue
    def show_match_composition(self):
        print("Ce match se compose de :")
        for player in self.pair_list:
            print(f"{player.first_name} {player.name}")
"""