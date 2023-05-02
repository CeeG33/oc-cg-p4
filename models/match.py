from player import joueur1, joueur2

class Match:
    """
    ○ Chaque match consiste en une paire de joueurs

    """
    def __init__(self):
        self.pair_list = []

    def create_match(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.pair_list.append(self.player1)
        self.pair_list.append(self.player2)

#Déplacer dans une vue
    def show_match_composition(self):
        print("Ce match se compose de :")
        for player in self.pair_list:
            print(f"{player.first_name} {player.name}")

match1 = Match()
match1.create_match(joueur1, joueur2)
match1.show_match_composition()



