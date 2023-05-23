from models import player
from views import playerview


class PlayerController:

    def __init__(self):
        self.model = player.Player
        self.player_view = playerview.PlayerView(self)
        self.waiting_room = []

    def create_new_player(self, name, first_name, birthdate, national_chess_id):
        new_player = self.model(name, first_name, birthdate)
        new_player.add_national_chess_id(national_chess_id)
        new_player.update_json_file()
        self.waiting_room.append(new_player)

    def load_existing_player(self, name, first_name):
        existing_player = self.model.create_from_json(name, first_name)
        existing_player.update_json_file()
        self.waiting_room.append(existing_player)

    def get_existing_players(self):
        return self.model.list_existing_players()


