from models import player, tournament
from views import reportview


class ReportController:
    def __init__(self):
        self.player_model = player.Player
        self.tournament_model = tournament.Tournament
        self.report_view = reportview.ReportView(self)
        self.selected_tournament = None

    def get_existing_players(self):
        """Retourne la liste des joueurs."""
        if self.player_model.list_existing_players():
            return self.player_model.list_existing_players()
        else:
            return

    def get_existing_tournaments(self):
        """Retourne la liste des tournois."""
        if self.tournament_model.list_existing_tournaments():
            return self.tournament_model.list_existing_tournaments()
        else:
            return

    def load_existing_tournament(self, chosen_tournament):
        """Charge le tournoi sélectionné dans le paramètre selected_tournament."""
        if self.tournament_model.list_existing_tournaments():
            created_tournament = self.tournament_model.create_from_json(chosen_tournament)
            self.selected_tournament = created_tournament
        else:
            return
