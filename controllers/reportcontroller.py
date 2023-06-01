from models import player, tournament
from views import reportview

class ReportController:

    def __init__(self):
        self.player_model = player.Player
        self.tournament_model = tournament.Tournament
        self.report_view = reportview.ReportView(self)
        self.selected_tournament = None

    def get_existing_players(self):
        return self.player_model.list_existing_players()

    def get_existing_tournaments(self):
        return self.tournament_model.list_existing_tournaments()

    def load_existing_tournament(self, chosen_tournament):
        created_tournament = self.tournament_model.create_from_json(chosen_tournament)
        self.selected_tournament = created_tournament


