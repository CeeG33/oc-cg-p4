from models import tournament

SELECTED_TOURNAMENT_INDEX = 0
class TournamentController:

    def __init__(self):
        self.model = tournament.Tournament
        self.tournaments_list = []

    def create_new_tournament(self, name, location, description):
        new_tournament = self.model(name, location, description)
        new_tournament.update_json_file()
        self.tournaments_list.append(new_tournament)

    def load_existing_tournament(self, tournament_name):
        existing_tournament = self.model.create_from_json(tournament_name)
        self.tournaments_list.append(existing_tournament)

    def begin_tournament(self):
        self.tournaments_list[SELECTED_TOURNAMENT_INDEX].begin_round()
        self.tournaments_list[SELECTED_TOURNAMENT_INDEX].shuffle_players()
        self.tournaments_list[SELECTED_TOURNAMENT_INDEX].create_pairs()
        self.tournaments_list[SELECTED_TOURNAMENT_INDEX].create_first_round_matches()
        self.tournaments_list[SELECTED_TOURNAMENT_INDEX].update_json_file()

    def end_tournament(self):
        self.tournaments_list[SELECTED_TOURNAMENT_INDEX].set_end_date()
        self.tournaments_list[SELECTED_TOURNAMENT_INDEX].update_json_file()

    def add_players(self, player_controller):
        player_controller_list = player_controller.players_list

        for player in player_controller_list:
            self.tournaments_list[SELECTED_TOURNAMENT_INDEX].add_player_to_tournament(player)

        self.tournaments_list[SELECTED_TOURNAMENT_INDEX].update_json_file()


