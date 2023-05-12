import json
import os.path
from os import stat, path

class Player:
    """
    Nous aimerions que l'application hors ligne contienne une base de données des joueurs
    dans des fichiers JSON. Le programme devrait avoir une section dédiée à l'ajout de joueurs
    et chaque joueur devrait contenir au moins les données suivantes :
        ● Nom de famille
        ● Prénom
        ● Date de naissance
    """

    def __init__(self, name="str", first_name="str", birthdate="str"):
        self.name = name
        self.first_name = first_name
        self.birthdate = birthdate
        self.global_rank = 0
        self.global_score = 0
        self.tournament_rank = 0
        self.tournament_score = 0

    def __repr__(self):
        return f"{self.first_name} {self.name}"

    def __lt__(self, other):
        return self.tournament_score > other.tournament_score

    def update_json_file(self):
        directory_path = f"data/players/"
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)
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

    def create_from_json(self, name, first_name):
        name = name
        first_name = first_name
        existing_json_file_path = f"data/players/{first_name}_{name}.json"
        if path.exists(existing_json_file_path):
            with open(existing_json_file_path, "r", encoding="utf-8") as json_file:
                player_data = json.load(json_file)
                print(player_data.get("name"))
        else:
            return "Ce joueur n'existe pas"




bob = Player("L'Éponge", "Bob", "02/02/2002")
patrick = Player("Étoile de Mer", "Patrick", "01/01/2004")
carlo = Player("Calamar", "Carlo", "03/03/2003")
crabs = Player("Crabs", "Captain", "02/03/1993")
sandy = Player("Écureuil", "Sandy", "04/05/2000")
plankton = Player("Sheldon", "Plankton", "01/02/1992")


"""
print("Le joueur 1 est : ")
print(f"Nom : {joueur1.name}")
print(f"Prénom : {joueur1.first_name}")
print(f"Date de naissance : {joueur1.date_of_birth}")
print(f"Rang : {joueur1.rank}")
print()
print("Le joueur 2 est : ")
print(f"Nom : {joueur2.name}")
print(f"Prénom : {joueur2.first_name}")
print(f"Date de naissance : {joueur2.date_of_birth}")
print(f"Rang : {joueur2.rank}")
"""