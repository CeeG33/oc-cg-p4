from models import tournament, rounds, match
from controllers import playercontroller
from views import tournamentview


class TournamentController:
    def __init__(self):
        """Initialise un contrôleur gérant les tournois.

        Attrs:
        - tournament_model (obj): contient un modèle Tournament.
        - round_model (obj): contient un modèle Round.
        - match_model (obj): contient un modèle Match.
        - tournament_view (obj): contient la vue TournamentView associée.
        - player_controller (obj): contient le contrôleur PlayerController.
        - current_tournament (obj): contient le tournoi sélectionné ou créé (initialisé en None).
        - current_round (obj): contient le round en cours du tournoi sélectionné ou créé (initialisé en None).
        """
        self.tournament_model = tournament.Tournament
        self.round_model = rounds.Round
        self.match_model = match.Match
        self.tournament_view = tournamentview.TournamentView(self)
        self.player_controller = playercontroller.PlayerController()
        self.current_tournament = None
        self.current_round = None

    def create_new_tournament(self, name, location, description):
        """Crée un nouveau tournoi, l'enregistre dans la base de données et le sélectionne comme tournoi par défaut."""
        new_tournament = self.tournament_model(name, location, description)
        new_tournament.save_json_file()
        self.current_tournament = new_tournament

    def add_players(self):
        """Ajoute les joueurs de la salle d'attente à la liste des joueurs du tournoi."""
        player_controller_waiting_room = self.player_controller.waiting_room

        if len(player_controller_waiting_room) > 0:
            while len(player_controller_waiting_room) > 0:

                for player in player_controller_waiting_room:
                    self.current_tournament.add_player_to_tournament(player)
                    player_controller_waiting_room.remove(player)

        else:
            return

    def get_match_result(self):
        """Cherche le résultat des matchs auprès de l'utilisateur."""
        for contest in self.current_round.match_list:
            print(f"Match >>> Joueur 1 : {contest.player1} -- VS -- Joueur 2 : {contest.player2}")
            result = self.tournament_view.get_match_result()
            if result == "1":
                winner = contest.player1
                contest.chose_winner(winner)
                self.current_tournament.add_one_point_to(winner)
                contest.update_json_file()
                self.current_tournament.save_json_file()
            elif result == "2":
                winner = contest.player2
                contest.chose_winner(winner)
                self.current_tournament.add_one_point_to(winner)
                contest.update_json_file()
                self.current_tournament.save_json_file()
            elif result == "3":
                contest.is_draw()
                for participant in contest.draw:
                    self.current_tournament.add_half_point_to(participant)
                contest.update_json_file()
                self.current_tournament.save_json_file()

    def load_existing_tournament(self, tournament_name):
        """Charge un tournoi existant puis sélectionne le tournoi et son dernier round."""
        existing_tournament = self.tournament_model.create_from_json(tournament_name)
        self.current_tournament = existing_tournament
        self.current_round = self.current_tournament.rounds_list[-1] if self.current_tournament.rounds_list else None

    def begin_tournament(self):
        """
        Commence le tournoi. Initialise le numéro de round, mélange les joueurs et crée les paires puis
        sauvegarde le tout.
        """
        self.add_players()
        self.current_tournament.save_json_file()
        self.current_tournament.set_round_number()
        self.current_tournament.shuffle_players()
        self.current_tournament.create_pairs()
        self.current_tournament.set_start_date()
        self.current_tournament.save_json_file()

    def create_first_round(self):
        """
        Crée le premier round du tournoi.
        Sélectionne automatiquement le round créé.
        Crée les matchs au sein de la liste des matchs du round sélectionné.
        Initialise le score des joueurs.
        Enregistre le tout.
        """
        first_round = self.round_model("Round 1")
        self.current_tournament.rounds_list.append(first_round)
        self.current_round = self.current_tournament.rounds_list[-1]
        self.current_tournament.create_first_round_matches(self.current_round)
        self.current_tournament.initialize_players_scores()
        for contest in self.current_round.match_list:
            contest.update_json_file()
        self.current_round.update_json_file()
        self.current_tournament.save_json_file()

    def end_round(self):
        """
        Termine le round en cours.
        Demande le résultat des matchs auprès de l'utilisateur.
        Horodate la fin du round.
        Enregistre le tout.
        """
        self.current_tournament.save_json_file()
        self.get_match_result()
        self.current_tournament.save_players()
        self.current_round.set_end_date()
        self.current_round.update_json_file()
        self.current_tournament.save_json_file()

    def create_next_round(self):
        """
        Change le numéro de round actuel de l'objet Tournoi.
        Crée le prochain round, l'ajoute à la liste de rounds du tournoi puis le sélectionne.
        Crée les matchs du nouveau round.
        Enregistre le tout.
        """
        self.current_tournament.set_round_number()
        round_number = self.current_tournament.current_round_number
        new_round = rounds.Round(f"Round {round_number}")
        self.current_tournament.rounds_list.append(new_round)
        self.select_current_round()
        self.current_tournament.create_next_round_matches(new_round)
        self.current_round.update_json_file()
        self.current_tournament.save_json_file()

    def begin_round(self):
        """
        Sélectionne le dernier round créé.
        Horodate le début du round.
        Enregistre le tout.
        """
        self.current_round = self.current_tournament.rounds_list[-1]
        self.current_round.set_start_date()
        self.current_round.update_json_file()
        self.current_tournament.save_json_file()

    def end_tournament(self):
        """
        Termine le tournoi.
        Horodate la fin du tournoi.
        Enregistre le tournoi.
        """
        self.current_tournament.set_end_date()
        self.current_tournament.save_json_file()

    def get_existing_tournaments(self):
        """Retourne une liste des tournois qui sont sous forme de fichier JSON dans la base de données."""
        return self.tournament_model.list_existing_tournaments()

    def get_players_scores(self):
        """Retourne la liste des joueurs classés selon leur score."""
        sorted_scores_list = self.current_tournament.sort_players()
        return sorted_scores_list

    def save_tournament(self):
        """Sauvegarde le tournoi."""
        for contest in self.current_round.match_list:
            contest.update_json_file()
        self.current_round.update_json_file()
        self.current_tournament.save_json_file()

    def select_current_round(self):
        """Sélectionne le round actuel."""
        self.current_round = self.current_tournament.rounds_list[-1] if self.current_tournament.rounds_list else None

    def select_current_match_list(self):
        """Renvoie la liste des matchs du round en cours."""
        return self.current_round.match_list
