from models import tournament
from models import rounds


class TournamentController:
    SELECTED_TOURNAMENT_INDEX = 0

    def __init__(self):
        self.model = tournament.Tournament
        self.tournaments_list = []
        self.tournament = self.tournaments_list[self.SELECTED_TOURNAMENT_INDEX]

    def create_new_tournament(self, name, location, description):
        new_tournament = self.model(name, location, description)
        new_tournament.update_json_file()
        self.tournaments_list.append(new_tournament)

    def load_existing_tournament(self, tournament_name):
        existing_tournament = self.model.create_from_json(tournament_name)
        self.tournaments_list.append(existing_tournament)

    def begin_tournament(self):
        self.tournament.set_round_number()

        round_number = self.tournament.current_round_number
        new_round = rounds.Round(f"Round {round_number}")

        self.tournament.shuffle_players()
        self.tournament.create_pairs()
        new_round.set_start_date()
        self.tournament.create_first_round_matches(new_round)
        self.tournament.rounds_list.append(new_round)
        self.tournament.update_json_file()

    def end_round(self, round_index):
        self.tournament.rounds_list[round_index].set_end_date()
        self.tournament.update_json_file()

    def create_next_round(self):
        self.tournament.set_round_number()

        round_number = self.tournament.current_round_number
        new_round = rounds.Round(f"Round {round_number}")

        new_round.set_start_date()
        self.tournament.create_next_round_matches(new_round)
        self.tournament.rounds_list.append(new_round)
        self.tournament.update_json_file()

    def end_tournament(self):
        self.tournament.set_end_date()
        self.tournament.update_json_file()

    def add_players(self, player_controller):
        player_controller_list = player_controller.players_list

        for player in player_controller_list:
            self.tournament.add_player_to_tournament(player)

        self.tournament.update_json_file()


