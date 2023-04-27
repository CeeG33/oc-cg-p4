

class Player:
    """
    Nous aimerions que l'application hors ligne contienne une base de données des joueurs
    dans des fichiers JSON. Le programme devrait avoir une section dédiée à l'ajout de joueurs
    et chaque joueur devrait contenir au moins les données suivantes :
        ● Nom de famille
        ● Prénom
        ● Date de naissance
    """
    rank = "Non défini"
    def __init__(self, name, first_name, date_of_birth):
        self.name = name
        self.first_name = first_name
        self.date_of_birth = date_of_birth
    pass

joueur1 = Player("Etoile de mer", "Patrick", "01/02/2000")
joueur2 = Player("L'Éponge", "Bob", "05/06/2002")

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