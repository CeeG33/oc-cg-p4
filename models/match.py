import json
import os
from models import player


class Match:
    def __init__(self, player1, player2):
        """
        Initialise un match avec deux joueurs.
        En fonction de l'issue du match, l'attribut winner contiendra le gagnant du match
        tandis que l'attribut draw contiendra les deux joueurs.
        """
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
        if os.path.exists(existing_json_file_path):
            with open(existing_json_file_path, "r", encoding="utf-8") as json_file:
                match_data = json.load(json_file)
                player1_data = match_data["player1"]
                player1_name = player1_data["name"]
                player1_first_name = player1_data["first_name"]
                player1_object = player.Player.create_from_json(player1_name, player1_first_name)
                player2_data = match_data["player2"]
                player2_name = player2_data["name"]
                player2_first_name = player2_data["first_name"]
                player2_object = player.Player.create_from_json(player2_name, player2_first_name)
                winner_data = match_data["winner"]
                winner_name = winner_data["name"] if winner_data else None
                winner_first_name = winner_data["first_name"] if winner_data else None
                winner_object = player.Player.create_from_json(winner_name, winner_first_name) if winner_data else None
                match = cls(player1_object,
                            player2_object)
                match.winner = winner_object if match.winner else None
                match.draw = []
                for player_data in match_data.get("draw", []):
                    player_name = player_data["name"]
                    player_first_name = player_data["first_name"]
                    player_object = player.Player.create_from_json(player_name, player_first_name)
                    match.draw.append(player_object)
                return match
        else:
            return

    def chose_winner(self, participant):
        """Ajoute le joueur gagnant du match à la liste winner."""
        self.winner = participant

    def is_draw(self):
        """Ajoute les deux joueurs dans la liste draw."""
        self.draw = [self.player1, self.player2]

    def update_json_file(self):
        """
        Crée les dossiers ci-dessous s'ils n'existent pas.
        Ensuite, crée ou met à jour le fichier JSON.
        """
        directory_path = "data/matches/"
        json_file_name = f"data/matches/{self.player1}_VS_{self.player2}.json"

        if not os.path.exists(directory_path):
            os.makedirs(directory_path)

        with open(json_file_name, "w", encoding="utf-8") as json_file:
            json.dump(self.to_dict(), json_file, indent=4, ensure_ascii=False)

    def to_dict(self):
        """Renvoie le dictionnaire du match."""
        data = {
            "player1": self.player1.to_dict(),
            "player2": self.player2.to_dict(),
            "winner": self.winner.to_dict() if self.winner else None,
            "draw": [participant.to_dict() for participant in self.draw] if self.draw else []
        }
        return data
