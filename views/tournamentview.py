import re
from controllers import tournamentcontroller

class TournamentView:

    def __init__(self, tournament_controller):
        self.tournament_controller = tournament_controller

        try:
            self.selected_tournament = self.tournament_controller.current_tournament
        except AttributeError:
            self.selected_tournament = None

        self.user_choice = 0
        self.menu_list = ["[1] > Créer un nouveau tournoi.",
                          "[2] > Charger un tournoi existant en entrant son nom manuellement.",
                          "[3] > Charger un tournoi existant en parcourant la base de données.",
                          "[4] > Afficher les tournois présents dans la base de données.",
                          "[5] > Commencer / continuer le tournoi sélectionné.",
                          "[6] > Revenir au menu principal."]

    def show_menu(self):
        """Affiche le menu principal de la vue TournamentController à l'utilisateur."""

        print("---- MENU TOURNOI----")
        print()
        self.show_selected_tournament()
        print()
        self.show_menu_list()
        self.prompt_user()

    def show_menu_list(self):
        """Affiche le menu selon la liste définie dans l'init."""
        for choice in self.menu_list:
            print(choice)

    def show_selected_tournament(self):
        """Affiche le nom du tournoi sélectionné."""
        if self.selected_tournament is not None:
            print(f"Tournoi sélectionné : {self.selected_tournament}")
        else:
            print(f"Tournoi sélectionné : Aucun")

    def prompt_user(self):
        """Affiche l'option sélectionnée par l'utilisateur."""
        print("")
        print("Que souhaitez-vous faire ?")
        self.user_choice = input("Numéro : ")
        while True:
            if self.user_choice == "1":
                self.create_tournament()
            elif self.user_choice == "2":
                self.get_existing_tournament_info_manually()
            elif self.user_choice == "3":
                self.show_tournaments_in_database()
                self.select_tournament_in_database()
            elif self.user_choice == "4":
                self.show_tournaments_in_database()
            elif self.user_choice == "5":
                pass
            elif self.user_choice == "6":
                break
            elif int(self.user_choice) not in range(1, len(self.menu_list)):
                print()
                print("Vous avez choisi un mauvais numéro.")
                print(f"Veuillez choisir un numéro entre 1 et {len(self.menu_list)}.")
                print()

    def create_tournament(self):
        name = self.get_tournament_name()
        location = self.get_tournament_location()
        description = self.get_tournament_description()
        self.tournament_controller.create_new_tournament(name, location, description)

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

    def get_existing_tournament_info_manually(self):
        """Charge un tournoi selon le nom et prénom renseigné par l'utilisateur manuellement."""
        name = self.get_tournament_name()
        self.tournament_controller.load_existing_tournament(name)

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
        self.show_menu()

