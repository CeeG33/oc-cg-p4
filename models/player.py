import json
import os


class Player:
    def __init__(self, name, first_name, birthdate, national_chess_id):
        """Initialise un joueur avec son nom, prénom, date de naissance et identifiant national d'échec."""
        self.name = name
        self.first_name = first_name
        self.birthdate = birthdate
        self.national_chess_id = national_chess_id

    def __repr__(self):
        """Définit le prénom et le nom du joueur en tant que représentation de l'objet Player."""
        return f"{self.first_name} {self.name}"

    @classmethod
    def create_from_json(cls, name, first_name):
        """Charge un objet joueur à partir d'un fichier JSON existant selon le nom et prénom du joueur."""
        existing_json_file_path = f"data/players/{first_name}_{name}.json"
        if os.path.exists(existing_json_file_path):
            with open(existing_json_file_path, "r", encoding="utf-8") as json_file:
                player_data = json.load(json_file)
                player = cls(player_data["name"],
                             player_data["first_name"],
                             player_data["birthdate"],
                             player_data["national_chess_id"])
                return player
        else:
            return

    def update_json_file(self):
        """
        Crée le dossier ci-dessous s'ils n'existent pas.
        Ensuite, crée ou écrase le fichier JSON.
        """
        directory_path = "data/players/"
        json_file_name = f"data/players/{self.first_name}_{self.name}.json"

        if not os.path.exists(directory_path):
            os.makedirs(directory_path)

        with open(json_file_name, "w", encoding="utf-8") as json_file:
            json.dump(self.__dict__, json_file, indent=4, ensure_ascii=False)

    @staticmethod
    def list_existing_players():
        """Renvoie une liste classée par ordre alphabétique de tous les joueurs existants dans la base de données."""
        existing_players = []
        directory_path = "data/players/"

        if not os.path.exists(directory_path):
            os.makedirs(directory_path)

        for file in os.listdir(directory_path):
            file_name = os.path.join(directory_path, file)

            if file.endswith(".json") and os.path.isfile(file_name):
                player_name = file.replace("_", " ").replace(".json", "")
                split_player_name = player_name.split()
                created_player = Player.create_from_json(split_player_name[1], split_player_name[0])
                existing_players.append(created_player)

        return sorted(existing_players, key=lambda participant: participant.first_name)

    def to_dict(self):
        """Renvoie le dictionnaire du joueur."""
        data = {
            "name": self.name,
            "first_name": self.first_name,
            "birthdate": self.birthdate,
            "national_chess_id": self.national_chess_id
        }
        return data
