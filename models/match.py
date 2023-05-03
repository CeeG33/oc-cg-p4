from player import joueur1, joueur2

class Match:
    """
    ○ Chaque match consiste en une paire de joueurs

    """
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.initial_score = 0
        self.tuple = ([self.player1, self.initial_score], [self.player2, self.initial_score])

match1 = Match(joueur1, joueur2)


"""
#Déplacer dans une vue
    def show_match_composition(self):
        print("Ce match se compose de :")
        for player in self.pair_list:
            print(f"{player.first_name} {player.name}")
"""