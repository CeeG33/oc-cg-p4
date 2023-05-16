from models import match

class MatchController:
    def __init__(self):
        self.match_list = []

    def create_new_match(self, player1, player2):
        new_match = match.Match(player1, player2)
        self.match_list.append(new_match)
        new_match.update_json_file()

    def load_existing_match(self, player1, player2):
        existing_match = match.Match.create_from_json(player1, player2)
        self.match_list.append(existing_match)