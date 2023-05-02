import json

class Player:
    """
    Nous aimerions que l'application hors ligne contienne une base de données des joueurs
    dans des fichiers JSON. Le programme devrait avoir une section dédiée à l'ajout de joueurs
    et chaque joueur devrait contenir au moins les données suivantes :
        ● Nom de famille
        ● Prénom
        ● Date de naissance
    """

    def __init__(self, name=str, first_name=str, birthdate=str):
        self.name = name
        self.first_name = first_name
        self.birthdate = birthdate
        self.rank = 0

    def add_player_to_database(self):
        with open(f"../data/players/{self.first_name}_{self.name}.json", "w", encoding="utf-8") as json_file:
            json.dump(self.__dict__, json_file, indent=4, ensure_ascii=False)


joueur1 = Player("Etoile de mer", "Patrick", "01/02/2000")
joueur2 = Player("L'Éponge", "Bob", "05/06/2002")

Player.add_player_to_database(joueur1)
Player.add_player_to_database(joueur2)

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