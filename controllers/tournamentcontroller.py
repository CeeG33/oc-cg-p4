from models import tournament, rounds, match
from controllers import playercontroller


class TournamentController:

    def __init__(self):
        self.tournament_model = tournament.Tournament
        self.round_model = rounds.Round
        self.match_model = match.Match
        self.player_controller = playercontroller.PlayerController()
        self.tournaments_list = []
        self.selected_tournament_index = 0
        self.tournament = self.tournaments_list[self.selected_tournament_index]
        self.current_round = self.tournament.rounds_list[-1]

    def create_new_tournament(self, name, location, description):
        new_tournament = self.tournament_model(name, location, description)
        new_tournament.update_json_file()
        self.tournaments_list.append(new_tournament)

    def add_players(self):
        player_controller_waiting_room = self.player_controller.waiting_room

        if player_controller_waiting_room != 0:

            for player in player_controller_waiting_room:
                self.tournament.add_player_to_tournament(player)
                player_controller_waiting_room.remove(player)

            self.tournament.update_json_file()

        else:
            return

    def get_match_result(self, result: int = 0):
        for contest in self.current_round:
            if result == 1:
                winner = contest.player1
                contest.chose_winner(winner)
                self.tournament.add_one_point_to(winner)
                contest.update_json_file()
            elif result == 2:
                winner = contest.player2
                contest.chose_winner(winner.player2)
                self.tournament.add_one_point_to(winner)
                contest.update_json_file()
            elif result == 3:
                contest.is_draw()
                for participant in contest.draw:
                    self.tournament.add_half_point_to(participant)
                contest.update_json_file()

    def load_existing_tournament(self, tournament_name):
        existing_tournament = self.tournament_model.create_from_json(tournament_name)
        self.tournaments_list.append(existing_tournament)

    def select_tournament(self, tournament_index):
        self.tournament.update_json_file()
        self.selected_tournament_index = tournament_index
        self.tournament.update_json_file()

    def begin_tournament(self):
        self.tournament.set_round_number()
        self.tournament.shuffle_players()
        self.tournament.create_pairs()
        self.tournament.update_json_file()

    def create_first_round(self):
        first_round = self.round_model("Round 1")
        first_round.update_json_file()
        self.tournament.rounds_list.append(first_round)
        self.tournament.update_json_file()

    def begin_first_round(self):
        first_round_index = 0
        first_round = self.tournament.rounds_list[first_round_index]
        self.tournament.create_first_round_matches(first_round)
        first_round.set_start_date()
        first_round.update_json_file()
        self.tournament.update_json_file()

    def end_round(self):
        self.current_round.set_end_date()
        self.current_round.update_json_file()
        self.get_match_result()
        self.tournament.update_json_file()

    def create_next_round(self):
        self.tournament.set_round_number()
        round_number = self.tournament.current_round_number
        new_round = rounds.Round(f"Round {round_number}")
        new_round.update_json_file()
        self.tournament.rounds_list.append(new_round)
        self.tournament.update_json_file()

    def begin_next_round(self):
        next_round_index = len(self.tournament.rounds_list)
        next_round = self.tournament.rounds_list[next_round_index]
        self.tournament.create_next_round_matches(next_round)
        next_round.set_start_date()
        next_round.update_json_file()
        self.tournament.update_json_file()

    def end_tournament(self):
        self.tournament.set_end_date()
        self.tournament.update_json_file()


