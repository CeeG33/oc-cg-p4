

class ReportView:

    def __init__(self, report_controller):
        self.report_controller = report_controller
        self.user_choice = 0
        self.menu_list = ["[1] > Afficher la liste des joueurs.",
                          "[2] > Afficher la liste des tournois.",
                          "[3] > Obtenir plus d'informations sur un tournoi.",
                          "[4] > Revenir au menu principal."]

    def show_menu(self):
        """Affiche le menu principal de la vue à l'utilisateur."""

        print("---- MENU RAPPORT----")
        print()
        self.show_menu_list()
        self.prompt_user()

    def show_menu_list(self):
        """Affiche le menu selon la liste définie dans l'init."""
        for choice in self.menu_list:
            print(choice)

    def prompt_user(self):
        """Demande l'action de l'utilisateur dans le menu."""
        while True:
            print("")
            print("Que souhaitez-vous faire ?")
            self.user_choice = input("Numéro : ")
            if self.user_choice == "1":
                self.show_existing_players()
            elif self.user_choice == "2":
                self.show_existing_tournaments()
                self.show_menu_list()
            elif self.user_choice == "3":
                self.show_existing_tournaments()
                self.select_tournament_in_database()
            elif self.user_choice == "4":
                break
            elif int(self.user_choice) not in range(1, len(self.menu_list)):
                print()
                print("Vous avez choisi un mauvais numéro.")
                print(f"Veuillez choisir un numéro entre 1 et {len(self.menu_list)}.")
                print()

    def show_existing_players(self):
        existing_players = self.report_controller.get_existing_players()
        print("Liste des joueurs existants :")
        print("")
        for index, player in enumerate(existing_players, 1):
            player_first_name = player.first_name
            player_name = player.name
            player_id = player.national_chess_id
            print(f"{index} >> {player_first_name} {player_name} -- Identifiant : {player_id}")
        print("")
        print("###############")
        print("Fin de la liste")
        print("")
        self.show_menu_list()

    def show_existing_tournaments(self):
        existing_tournaments = self.report_controller.get_existing_tournaments()
        print("Liste des tournois existants :")
        print("")
        for index, tournament in enumerate(existing_tournaments, 1):
            print(f"{index} >> {tournament}")
        print("")
        print("###############")
        print("Fin de la liste")
        print("")

    def select_tournament_in_database(self):
        """Sélectionne le tournoi existant."""
        existing_tournaments = self.report_controller.get_existing_tournaments()
        print("Quel tournoi souhaitez-vous sélectionner ?")

        try:
            user_choice = input("Numéro : ")
            self.report_controller.load_existing_tournament(existing_tournaments[int(user_choice) - 1])
        except IndexError:
            print()
            print("Vous avez choisi un mauvais numéro. Veuillez réessayer.")
            print()
            self.show_existing_tournaments()
        except ValueError:
            print()
            print("Vous devez renseigner un chiffre. Veuillez réessayer")
            print()
            self.show_existing_tournaments()
        print()
        self.show_tournament_name_and_dates()
        print()
        self.show_tournament_players_list()
        print()
        self.show_tournament_rounds_list()
        print()
        self.show_menu_list()

    def show_tournament_name_and_dates(self):
        tournament_name = self.report_controller.selected_tournament.name
        tournament_start_date = self.report_controller.selected_tournament.start_date
        tournament_end_date = self.report_controller.selected_tournament.end_date if True else "Non terminé"
        print(f"Nom du tournoi : {tournament_name} -- Début : {tournament_start_date} -- Fin : {tournament_end_date}")

    def show_tournament_players_list(self):
        tournament_players_list = self.report_controller.selected_tournament.players_list
        for index, player in enumerate(tournament_players_list, 1):
            player_first_name = player.first_name
            player_name = player.name
            player_id = player.national_chess_id
            print(f"{index} >> {player_first_name} {player_name} -- Identifiant : {player_id}")

    def show_tournament_rounds_list(self):
        tournament_rounds_list = self.report_controller.selected_tournament.rounds_list
        for round_object in tournament_rounds_list:
            round_name = round_object.round_name
            match_list = round_object.match_list
            print(f"{round_name} - Liste des matchs : {match_list} ")
