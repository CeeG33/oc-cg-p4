from models import tournament, rounds, match
from controllers import playercontroller
from views import playerview, tournamentview


class TournamentController:

    def __init__(self):
        self.tournament_model = tournament.Tournament
        self.round_model = rounds.Round
        self.match_model = match.Match
        self.tournament_view = tournamentview.TournamentView(self)
        self.current_tournament = None
        self.current_round = None

    def create_new_tournament(self, name, location, description):
        """Crée un nouveau tournoi et le stocke dans la liste des tournois du contrôleur."""
        new_tournament = self.tournament_model(name, location, description)
        new_tournament.update_json_file()
        self.current_tournament = new_tournament

    def add_players(self):
        """Ajoute les joueurs de la salle d'attente au tournoi."""
        player_controller_waiting_room = self.player_controller.waiting_room

        if len(player_controller_waiting_room) > 0:
            while len(player_controller_waiting_room) > 0:

                for player in player_controller_waiting_room:
                    self.current_tournament.add_player_to_tournament(player)
                    player_controller_waiting_room.remove(player)

                self.current_tournament.update_json_file()

        else:
            return

    def get_match_result(self, result: int = 3):
        """Cherche le résultat des matchs."""
        self.current_tournament.initialize_players_scores()
        for contest in self.current_round.match_list:
            if result == 1:
                winner = contest.player1
                contest.chose_winner(winner)
                self.current_tournament.add_one_point_to(winner)
                contest.update_json_file()
            elif result == 2:
                winner = contest.player2
                contest.chose_winner(winner.player2)
                self.current_tournament.add_one_point_to(winner)
                contest.update_json_file()
            elif result == 3:
                contest.is_draw()
                for participant in contest.draw:
                    self.current_tournament.add_half_point_to(participant)
                contest.update_json_file()

    def load_existing_tournament(self, tournament_name):
        """Charge un tournoi existant."""
        if self.current_tournament == None:
            pass
        else:
            self.current_tournament.update_json_file()
        existing_tournament = self.tournament_model.create_from_json(tournament_name)
        self.current_tournament = existing_tournament

    def begin_tournament(self):
        """Commence le tournoi. Initialise le numéro de round, mélange les joueurs et crée les paires."""
        self.current_tournament.set_round_number()
        self.current_tournament.shuffle_players()
        self.current_tournament.create_pairs()
        self.current_tournament.update_json_file()

    def create_first_round(self):
        """Crée le premier round du tournoi. Sélectionne automatiquement le round."""
        first_round = self.round_model("Round 1")
        first_round.update_json_file()
        self.current_tournament.rounds_list.append(first_round)
        self.current_round = self.current_tournament.rounds_list[-1]
        self.current_tournament.update_json_file()

    def begin_first_round(self):
        """Démarre le premier round du tournoi."""
        first_round_index = 0
        first_round = self.current_tournament.rounds_list[first_round_index]
        self.current_tournament.create_first_round_matches(first_round)
        first_round.set_start_date()
        first_round.update_json_file()
        self.current_tournament.update_json_file()

    def end_round(self):
        """Termine le round en cours."""
        self.current_round.set_end_date()
        self.current_round.update_json_file()
        self.get_match_result()
        self.current_tournament.save_players_score()
        self.current_tournament.update_json_file()

    def create_next_round(self):
        """Crée le prochain round."""
        self.current_tournament.set_round_number()
        round_number = self.current_tournament.current_round_number
        new_round = rounds.Round(f"Round {round_number}")
        new_round.update_json_file()
        self.current_tournament.rounds_list.append(new_round)
        self.current_tournament.update_json_file()

    def begin_next_round(self):
        """Commence le prochain round."""
        next_round_index = len(self.current_tournament.rounds_list) - 1
        next_round = self.current_tournament.rounds_list[next_round_index]
        self.current_tournament.create_next_round_matches(next_round)
        next_round.set_start_date()
        next_round.update_json_file()
        self.current_tournament.update_json_file()

    def end_tournament(self):
        """Termine le tournoi."""
        self.current_tournament.set_end_date()
        self.current_tournament.update_json_file()

    def launch_view(self):
        """Lance la vue PlayerView."""
        self.player_view.show_menu()

    def get_existing_tournaments(self):
        """Retourne une liste des tournois qui sont sous forme de fichier JSON dans la base de données."""
        return self.tournament_model.list_existing_tournaments()

    def show_main_menu_view(self):
        self.main_menu_view.show_menu()

    def show_tournament_view(self):
        self.tournament_view.show_menu()

    def show_player_view(self):
        self.player_view.show_menu()

"""
    def show_tournaments_list(self):
        Retourne les tournois présents dans la tournament_list de l'init.
        return self.tournaments_list

        self.current_round = self.tournament.rounds_list[-1]
"""