from models import player, tournament


class PlayerController:

    def __init__(self):
        self.model = player.Player
        self.players_list = []

    def create_new_player(self, name, first_name, birthdate, national_chess_id):
        new_player = self.model(name, first_name, birthdate)
        new_player.add_national_chess_id(national_chess_id)
        new_player.update_json_file()
        self.players_list.append(new_player)

    def load_existing_player(self, name, first_name):
        existing_player = self.model.create_from_json(name, first_name)
        self.players_list.append(existing_player)


"""
class PlayerController:
    def __init__(self):
        self.players_list = []

    def add_new_player(self, name, first_name, birthdate, national_chess_id):
        new_player = player.Player(name, first_name, birthdate)
        new_player.add_national_chess_id(national_chess_id)
        self.players_list.append(new_player)
        new_player.update_json_file()

    def load_existing_player(self, name, first_name):
        existing_player = player.Player.create_from_json(name, first_name)
        self.players_list.append(existing_player)
"""