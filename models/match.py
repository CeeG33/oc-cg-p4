from player import joueur1, joueur2

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

    def player1_wins(self, player1):
        self.player1 = player1
        self.player1_score += 1
        self.tuple = ([self.player1, self.player1_score], [self.player2, self.player2_score])

    def player2_wins(self, player2):
        self.player2 = player2
        self.player2_score += 1
        self.tuple = ([self.player1, self.player1_score], [self.player2, self.player2_score])

match1 = Match(joueur1, joueur2)

print(match1)
print(match1.tuple)
print("Match en cours...")
match1.player1_wins(joueur1)
print(match1.tuple)
print("Match en cours... Round 2")
match1.player2_wins(joueur2)
print(match1.tuple)

"""
#Déplacer dans une vue
    def show_match_composition(self):
        print("Ce match se compose de :")
        for player in self.pair_list:
            print(f"{player.first_name} {player.name}")
"""