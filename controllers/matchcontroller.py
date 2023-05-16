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

    def save_matches(self):
        if len(self.match_list) >= 1:
            for m in self.match_list:
                m.update_json_file()
            return "Matches saved successfully"
        else:
            return "There are no matches yet !"

    def select_winner(self, match_index, player):
        self.match_list[match_index].chose_winner(player)
        self.match_list[match_index].update_json_file()

    def declare_draw_match(self, match_index):
        self.match_list[match_index].is_draw()
        self.match_list[match_index].update_json_file()

    def restore_match_result(self, match_index):
        self.match_list[match_index].winner = None
        self.match_list[match_index].draw = None
        self.match_list[match_index].update_json_file()

