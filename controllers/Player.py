

class Player:
    """
    Nous aimerions que l'application hors ligne contienne une base de données des joueurs
    dans des fichiers JSON. Le programme devrait avoir une section dédiée à l'ajout de joueurs
    et chaque joueur devrait contenir au moins les données suivantes :
        ● Nom de famille
        ● Prénom
        ● Date de naissance
    """
    def __init__(self, name, first_name, date_of_birth):
        self.name = name
        self.first_name = first_name
        self.date_of_birth = date_of_birth
    pass