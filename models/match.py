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

    def update_player1_global_score(self):
        self.player1.global_score += self.player1_score

    def update_player2_global_score(self):
        self.player2.global_score += self.player2_score

    def update_player1_tournament_score(self):
        self.player1.tournament_score += self.player1_score

    def update_player2_tournament_score(self):
        self.player2.tournament_score += self.player2_score


"""
print(match1)
match1.player1_wins()
match1.draw()
print(f"Score Bob : {match1.player1_score}")
print(f"Score Patrick : {match1.player2_score}")
match1.update_player1_global_score()
match1.update_player2_global_score()
print(bob.global_score)
print(patrick.global_score)
print(match1.tuple)



#Déplacer dans une vue
    def show_match_composition(self):
        print("Ce match se compose de :")
        for player in self.pair_list:
            print(f"{player.first_name} {player.name}")
"""