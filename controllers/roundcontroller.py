from models import rounds


class RoundController:

    def __init__(self):
        self.model = rounds.Round
        self.round_list = []

    def create_new_round(self, round_name):
        new_round = self.model(round_name)
        new_round.set_start_date()
        new_round.update_json_file()
        self.round_list.append(new_round)

    def load_existing_round(self, round_name):
        existing_round = self.model.create_from_json(round_name)
        self.round_list.append(existing_round)

    def save_rounds(self):
        if len(self.round_list) >= 1:
            for r in self.round_list:
                r.update_json_file()
            return "Rounds saved successfully"
        else:
            return "There are no rounds yet !"

    def add_match(self, round_index, match_name):
        self.round_list[round_index].add_match(match_name)
        self.round_list[round_index].update_json_file()

    def end_round(self, round_index):
        self.round_list[round_index].set_end_date()


"""get_matches à utiliser"""