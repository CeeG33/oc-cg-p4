import re


class TournamentView:
    def __init__(self, tournament_controller):
        self.tournament_controller = tournament_controller

        try:
            self.selected_tournament = self.tournament_controller.current_tournament
        except AttributeError:
            self.selected_tournament = None

        self.user_choice = 0
        self.menu_list = ["[1] > Créer un nouveau tournoi.",
                          "[2] > Charger un tournoi existant en parcourant la base de données.",
                          "[3] > Afficher les tournois présents dans la base de données.",
                          "[4] > Commencer / continuer le tournoi sélectionné.",
                          "[5] > Revenir au menu principal."]

    def show_menu(self):
        """Affiche le menu principal de la vue à l'utilisateur."""
        print("---- MENU TOURNOI----")
        print()
        self.show_selected_tournament()
        print()
        self.show_menu_list()
        self.prompt_user()

    def show_menu_list(self):
        """Affiche le menu selon la liste définie dans le constructeur."""
        for choice in self.menu_list:
            print(choice)

    def show_selected_tournament(self):
        """Affiche le nom du tournoi sélectionné."""
        if self.selected_tournament is not None:
            print(f"Tournoi sélectionné : {self.selected_tournament}")
        else:
            print("Tournoi sélectionné : Aucun")

    def prompt_user(self):
        """Demande l'action de l'utilisateur dans le menu."""
        while True:
            print("")
            print("Que souhaitez-vous faire ?")
            self.user_choice = input("Numéro : ")
            if self.user_choice == "1":
                if len(self.tournament_controller.player_controller.waiting_room) < 8:
                    print()
                    print("Vous n'avez pas assez de joueurs pour créer un tournoi !")
                    print("Retour au menu.")
                    print()
                    self.show_menu_list()
                else:
                    self.create_tournament()
            elif self.user_choice == "2":
                existing_tournaments = self.tournament_controller.get_existing_tournaments()
                if existing_tournaments:
                    self.show_tournaments_in_database()
                    self.select_tournament_in_database()
                else:
                    print("La base de données est vide !")
                    print("Retour vers le menu.")
                    print()
                    self.show_menu_list()
            elif self.user_choice == "3":
                existing_tournaments = self.tournament_controller.get_existing_tournaments()
                if existing_tournaments:
                    self.show_tournaments_in_database()
                    self.show_menu_list()
                    print()
                else:
                    print("La base de données est vide !")
                    print("Retour vers le menu.")
                    print()
                    self.show_menu_list()
            elif self.user_choice == "4":
                if self.selected_tournament:
                    self.show_selected_tournament()
                    if not self.tournament_controller.current_round:
                        print()
                        print("Le tournoi peut commencer !")
                        self.tournament_controller.begin_tournament()
                        self.tournament_controller.create_first_round()
                        user_choice = self.prompt_user_to_start_round()
                        if user_choice == "1":
                            try:
                                self.tournament_controller.begin_round()
                            except IndexError:
                                print("Vous n'avez pas le nombre de joueurs suffisant !")
                                print("Il faut 8 joueurs pour démarrer un tournoi.")
                                print("Retour au menu principal")
                                break
                            self.tournament_controller.end_round()
                            self.tournament_controller.create_next_round()
                        elif user_choice == "2":
                            self.tournament_controller.save_tournament()
                            break
                        while self.tournament_controller.current_tournament.current_round_number <= 3:
                            user_choice = self.prompt_user_to_start_round()
                            if user_choice == "1":
                                try:
                                    self.tournament_controller.begin_round()
                                except IndexError:
                                    print("Vous n'avez pas le nombre de joueurs suffisant !")
                                    print("Il faut 8 joueurs pour démarrer un tournoi.")
                                    print("Retour au menu tournoi.")
                                    break
                            elif user_choice == "2":
                                self.tournament_controller.save_tournament()
                                break
                            self.tournament_controller.end_round()
                            self.tournament_controller.create_next_round()
                            if self.tournament_controller.current_tournament.current_round_number == 4:
                                user_choice = self.prompt_user_to_start_round()
                                if user_choice == "1":
                                    try:
                                        self.tournament_controller.begin_round()
                                    except IndexError:
                                        print("Vous n'avez pas le nombre de joueurs suffisant !")
                                        print("Il faut 8 joueurs pour démarrer un tournoi.")
                                        print("Retour au menu tournoi.")
                                        break
                                self.tournament_controller.end_round()
                                print("Le tournoi est désormais terminé !")
                                self.tournament_controller.end_tournament()
                                print()
                                print("Voici le classement du tournoi",
                                      f"{self.tournament_controller.current_tournament} :")
                                self.show_scores()
                                print()
                                print("Félicitations à tous les participants !")
                                print()
                                print("Retour au menu tournoi.")
                                break
                        break

                    else:
                        while self.tournament_controller.current_tournament.current_round_number <= 3:
                            user_choice = self.prompt_user_to_start_round()
                            if user_choice == "1":
                                try:
                                    self.tournament_controller.begin_round()
                                except IndexError:
                                    print("Vous n'avez pas le nombre de joueurs suffisant !")
                                    print("Il faut 8 joueurs pour démarrer un tournoi.")
                                    print("Retour au menu principal")
                                    break
                                self.tournament_controller.end_round()
                                self.tournament_controller.create_next_round()

                            elif user_choice == "2":
                                self.tournament_controller.save_tournament()
                                break

                            if self.tournament_controller.current_tournament.current_round_number == 4:
                                user_choice = self.prompt_user_to_start_round()
                                if user_choice == "1":
                                    try:
                                        self.tournament_controller.begin_round()
                                    except IndexError:
                                        print("Vous n'avez pas le nombre de joueurs suffisant !")
                                        print("Il faut 8 joueurs pour démarrer un tournoi.")
                                        print("Retour au menu principal")
                                        break
                                    self.tournament_controller.end_round()
                                    self.tournament_controller.end_tournament()
                                    print()
                                    print("Voici le classement du tournoi"
                                          f" {self.tournament_controller.current_tournament} :")
                                    self.show_scores()
                                    print()
                                    print("Félicitations à tous les participants !")
                                    print()
                                    print("Retour au menu tournoi.")
                                    break
                                elif user_choice == "2":
                                    self.tournament_controller.save_tournament()
                                    break
                        if self.tournament_controller.current_tournament.current_round_number == 4 and not \
                                self.tournament_controller.current_tournament.end_date:
                            user_choice = self.prompt_user_to_start_round()
                            if user_choice == "1":
                                try:
                                    self.tournament_controller.begin_round()
                                except IndexError:
                                    print("Vous n'avez pas le nombre de joueurs suffisant !")
                                    print("Il faut 8 joueurs pour démarrer un tournoi.")
                                    print("Retour au menu principal")
                                    break
                                self.tournament_controller.end_round()
                                self.tournament_controller.end_tournament()
                                print()
                                print("Voici le classement du tournoi",
                                      f"{self.tournament_controller.current_tournament} :")
                                self.show_scores()
                                print()
                                print("Félicitations à tous les participants !")
                                print()
                                print("Retour au menu tournoi.")
                                break
                            elif user_choice == "2":
                                self.tournament_controller.save_tournament()
                                break
                        print()
                        print("---- MENU TOURNOI----")
                        print()
                        self.show_menu_list()
                else:
                    print()
                    print("Attention, vous n'avez pas sélectionné ou créé un tournoi.")
                    print()
                    print("Retour au menu.")
                    self.show_menu_list()
            elif self.user_choice == "5":
                break
            else:
                print()
                print(f"Erreur. Veuillez choisir un numéro entre 1 et {len(self.menu_list)}.")
                print("Retour au menu")
                print()
                self.show_menu_list()

    def create_tournament(self):
        """Crée un tournoi selon les données de l'utilisateur et le sélectionne."""
        name = self.get_tournament_name()
        location = self.get_tournament_location()
        description = self.get_tournament_description()
        self.tournament_controller.create_new_tournament(name, location, description)
        self.selected_tournament = self.tournament_controller.current_tournament
        print()
        self.show_selected_tournament()
        print()
        self.show_menu_list()

    @staticmethod
    def get_tournament_name():
        """Récupère le nom du tournoi auprès de l'utilisateur."""
        name = input("Nom du tournoi (Respectez les accents. Exemple : Étoile) : ").capitalize()
        pattern = r"^[a-zA-Z0-9\s]+$"
        if not re.match(pattern, name):
            print()
            print("Mauvais caractères, veuillez écrire un nom en lettres.")
            print()
        elif len(name) <= 1:
            print()
            print("Nom trop court. Il doit au moins contenir deux caractères.")
            print()
        else:
            return name

    @staticmethod
    def get_tournament_location():
        """Récupère la localisation du tournoi auprès de l'utilisateur."""
        location = input("Localisation du tournoi (Respectez les accents. Exemple : Élancourt) : ").capitalize()
        pattern = r"^[a-zA-Z0-9\s]+$"
        if not re.match(pattern, location):
            print()
            print("Mauvais caractères, veuillez écrire un nom en lettres.")
            print()
        elif len(location) <= 1:
            print()
            print("Nom trop court. Il doit au moins contenir deux caractères.")
            print()
        else:
            return location

    @staticmethod
    def get_tournament_description():
        """Récupère la description du tournoi auprès de l'utilisateur."""
        description = input("Description du tournoi : ").capitalize()
        if len(description) <= 1:
            print()
            print("Description trop courte. Elle doit au moins contenir deux caractères.")
            print()
        else:
            return description

    def show_tournaments_in_database(self):
        """Affiche la liste des tournois enregistrés dans la base de données."""
        existing_tournaments = self.tournament_controller.get_existing_tournaments()
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
        existing_tournaments = self.tournament_controller.get_existing_tournaments()
        print("Quel tournoi souhaitez-vous sélectionner ?")
        try:
            user_choice = input("Numéro : ")
            self.selected_tournament = existing_tournaments[int(user_choice) - 1]
        except IndexError:
            print()
            print("Vous avez choisi un mauvais numéro. Veuillez réessayer.")
            print()
            self.show_tournaments_in_database()
        except ValueError:
            print()
            print("Vous devez renseigner un chiffre. Veuillez réessayer")
            print()
            self.show_tournaments_in_database()
        self.tournament_controller.load_existing_tournament(self.selected_tournament)
        self.tournament_controller.select_current_round()
        print()
        print("Le tournoi est chargé avec succès !")
        print()
        self.show_selected_tournament()
        print()
        self.show_menu_list()

    @staticmethod
    def get_match_result():
        """Demande le résultat du match à l'utilisateur."""
        print("Qui est le vainqueur ?")
        print("[1] > Joueur 1")
        print("[2] > Joueur 2")
        print("[3] > Match nul")
        user_choice = input("(1/2/3) : ")
        while user_choice not in ["1", "2", "3"]:
            print("Erreur. Veuillez sélectionner 1, 2 ou 3.")
            user_choice = input("(1/2/3) : ")
        else:
            return user_choice

    def prompt_user_to_start_round(self):
        """
        Affiche le tournoi, le round et la liste des matchs actuels puis demande à l'utilisateur s'il veut
        démarrer le round.
        """
        print(f"Tournoi actuel : {self.tournament_controller.current_tournament}")
        print(f"Round actuel : {self.tournament_controller.current_round}")
        print(f"Liste des matchs : {self.tournament_controller.select_current_match_list()}")
        print()
        print("Souhaitez-vous démarrer le round ?")
        print()
        print("[1] > Oui.")
        print("[2] > Arrêter le tournoi.")
        user_choice = input("(1/2) : ")
        while user_choice not in ["1", "2"]:
            print("Erreur. Veuillez sélectionner 1 ou 2.")
            user_choice = input("(1/2) : ")
        else:
            return user_choice

    def show_scores(self):
        """Affiche le classement des joueurs selon leur score."""
        sorted_scores_list = self.tournament_controller.get_players_scores()
        for index, (participant, score) in enumerate(sorted_scores_list, 1):
            print(f"{index} >> {participant} >> {score} points")
