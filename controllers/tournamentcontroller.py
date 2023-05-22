from models import tournament, rounds, match
from controllers import playercontroller
from views import playerview, tournamentview


class TournamentController:

    def __init__(self):
        self.tournament_model = tournament.Tournament
        self.round_model = rounds.Round
        self.match_model = match.Match
        self.player_controller = playercontroller.PlayerController()
        self.player_view = playerview.PlayerView(self.player_controller)
        self.tournament_view = tournamentview.TournamentView(self)
        self.tournaments_list = []
        self.selected_tournament_index = 0

        self.tournament = None
        self.current_round = None

    def create_new_tournament(self, name, location, description):
        """Crée un nouveau tournoi et le stocke dans la liste des tournois du contrôleur."""
        new_tournament = self.tournament_model(name, location, description)
        new_tournament.update_json_file()
        self.tournaments_list.append(new_tournament)
        self.tournament = self.tournaments_list[-1]
        self.tournament.update_json_file()

        return new_tournament

    def add_players(self):
        """Ajoute les joueurs de la salle d'attente au tournoi."""
        player_controller_waiting_room = self.player_controller.waiting_room

        if len(player_controller_waiting_room) > 0:
            while len(player_controller_waiting_room) > 0:

                for player in player_controller_waiting_room:
                    self.tournament.add_player_to_tournament(player)
                    player_controller_waiting_room.remove(player)

                self.tournament.update_json_file()

        else:
            return

    def get_match_result(self, result: int = 3):
        """Cherche le résultat des matchs."""
        self.tournament.initialize_players_scores()
        for contest in self.current_round.match_list:
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
        """Charge un tournoi existant."""
        existing_tournament = self.tournament_model.create_from_json(tournament_name)
        self.tournaments_list.append(existing_tournament)

    def select_tournament(self, tournament_index):
        """Sélectionne un tournoi."""
        self.tournament.update_json_file()
        self.selected_tournament_index = tournament_index
        self.tournament.update_json_file()

    def begin_tournament(self):
        """Commence le tournoi. Initialise le numéro de round, mélange les joueurs et crée les paires."""
        self.tournament.set_round_number()
        self.tournament.shuffle_players()
        self.tournament.create_pairs()
        self.tournament.update_json_file()

    def create_first_round(self):
        """Crée le premier round du tournoi. Sélectionne automatiquement le round."""
        first_round = self.round_model("Round 1")
        first_round.update_json_file()
        self.tournament.rounds_list.append(first_round)
        self.current_round = self.tournament.rounds_list[-1]
        self.tournament.update_json_file()

    def begin_first_round(self):
        """Démarre le premier round du tournoi."""
        first_round_index = 0
        first_round = self.tournament.rounds_list[first_round_index]
        self.tournament.create_first_round_matches(first_round)
        first_round.set_start_date()
        first_round.update_json_file()
        self.tournament.update_json_file()

    def end_round(self):
        """Termine le round en cours."""
        self.current_round.set_end_date()
        self.current_round.update_json_file()
        self.get_match_result()
        self.tournament.save_players_score()
        self.tournament.update_json_file()

    def create_next_round(self):
        """Crée le prochain round."""
        self.tournament.set_round_number()
        round_number = self.tournament.current_round_number
        new_round = rounds.Round(f"Round {round_number}")
        new_round.update_json_file()
        self.tournament.rounds_list.append(new_round)
        self.tournament.update_json_file()

    def begin_next_round(self):
        """Commence le prochain round."""
        next_round_index = len(self.tournament.rounds_list) - 1
        next_round = self.tournament.rounds_list[next_round_index]
        self.tournament.create_next_round_matches(next_round)
        next_round.set_start_date()
        next_round.update_json_file()
        self.tournament.update_json_file()

    def end_tournament(self):
        """Termine le tournoi."""
        self.tournament.set_end_date()
        self.tournament.update_json_file()

    def launch_view(self):
        """Lance la vue PlayerView."""
        self.player_view.show_menu()

    def get_existing_tournaments(self):
        """Retourne une liste des tournois qui sont sous forme de fichier JSON dans la base de données."""
        return self.tournament_model.list_existing_tournaments()



"""
    def show_tournaments_list(self):
        Retourne les tournois présents dans la tournament_list de l'init.
        return self.tournaments_list

        self.current_round = self.tournament.rounds_list[-1]
"""