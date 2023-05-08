import random

class Match:
    """
    ○ Chaque match consiste en une paire de joueurs

    """
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.player1_score = 0
        self.player2_score = 0
        self.tuple = ([self.player1, self.player1_score], [self.player2, self.player2_score])

    def __repr__(self):
        return f"{self.player1} -- VS -- {self.player2}"

    def player1_wins(self):
        self.player1_score += 1
        self.tuple = ([self.player1, self.player1_score], [self.player2, self.player2_score])

    def player2_wins(self):
        self.player2_score += 1
        self.tuple = ([self.player1, self.player1_score], [self.player2, self.player2_score])

    def draw(self):
        self.player1_score += 0.5
        self.player2_score += 0.5
        self.tuple = ([self.player1, self.player1_score], [self.player2, self.player2_score])


"""
#Déplacer dans une vue
    def show_match_composition(self):
        print("Ce match se compose de :")
        for player in self.pair_list:
            print(f"{player.first_name} {player.name}")
"""