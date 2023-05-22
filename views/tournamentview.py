import re
from controllers import tournamentcontroller

class TournamentView:

    def __init__(self, tournament_controller):
        self.tournament_controller = tournament_controller
        self.selected_tournament = None
        self.user_choice = 0
        self.existing_tournament = self.tournament_controller.get_existing_tournaments()
        self.menu_list = ["[1] > Créer un nouveau tournoi.",
                          "[2] > Charger un tournoi existant en entrant son nom manuellement.",
                          "[3] > Charger un tournoi existant en parcourant la base de données.",
                          "[4] > Afficher les tournois présents dans la base de données."]

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
        if self.user_choice == "1":
            self.create_tournament()
            self.show_menu()
        elif self.user_choice == "2":
            self.get_existing_tournament_info_manually()
            self.show_menu()
        elif self.user_choice == "3":
            self.show_tournaments_in_database()
            self.select_tournament_in_database()
            self.show_loaded_tournaments()
            self.load_tournament_from_database()
        elif self.user_choice == "4":
            self.show_tournaments_in_database()
            self.show_menu_list()
            self.prompt_user()
        elif int(self.user_choice) not in range(1, len(self.menu_list)):
            print()
            print("Vous avez choisi un mauvais numéro.")
            print(f"Veuillez choisir un numéro entre 1 et {len(self.menu_list)}.")
            print()
            self.show_menu_list()
            self.prompt_user()

    def create_tournament(self):
        name = self.get_tournament_name()
        location = self.get_tournament_location()
        description = self.get_tournament_description()
        new_tournament = self.tournament_controller.create_new_tournament(name, location, description)
        new_tournament.update_json_file()

    def get_tournament_name(self):
        """Récupère le nom du tournoi auprès de l'utilisateur."""
        name = input("Nom du tournoi (Respectez les accents. Exemple : Étoile) : ").capitalize()
        pattern = r"^[a-zA-Z\s]+$"
        if not re.match(pattern, name):
            print()
            print("Mauvais caractères, veuillez écrire un nom en lettres.")
            print()
            self.get_tournament_name()
        elif len(name) <= 1:
            print()
            print("Nom trop court. Il doit au moins contenir deux caractères.")
            print()
            self.get_tournament_name()
        else:
            return name

    def get_tournament_location(self):
        """Récupère la localisation du tournoi auprès de l'utilisateur."""
        location = input("Localisation du tournoi (Respectez les accents. Exemple : Élancourt) : ").capitalize()
        pattern = r"^[a-zA-Z\s]+$"
        if not re.match(pattern, location):
            print()
            print("Mauvais caractères, veuillez écrire un nom en lettres.")
            print()
            self.get_tournament_location()
        elif len(location) <= 1:
            print()
            print("Nom trop court. Il doit au moins contenir deux caractères.")
            print()
            self.get_tournament_location()
        else:
            return location

    def get_tournament_description(self):
        """Récupère la description du tournoi auprès de l'utilisateur."""
        description = input("Description du tournoi : ").capitalize()
        if len(description) <= 1:
            print()
            print("Description trop courte. Elle doit au moins contenir deux caractères.")
            print()
            self.get_tournament_description()
        else:
            return description

    def get_existing_tournament_info_manually(self):
        """Charge un tournoi selon le nom et prénom renseigné par l'utilisateur manuellement."""
        name = self.get_tournament_name()
        self.tournament_controller.load_existing_tournament(name)
        self.show_menu()

    def show_tournaments_in_database(self):
        """Affiche la liste des tournois enregistrés dans la base de données."""
        print("Liste des tournois existants :")
        print("")
        for index, tournament in enumerate(self.existing_tournament, 1):
            print(f"{index} >> {tournament}")
        print("")
        print("###############")
        print("Fin de la liste")
        print("")

    def select_tournament_in_database(self):
        """Sélectionne le tournoi existant."""
        print("Quel tournoi souhaitez-vous sélectionner ?")

        try:
            self.user_choice = input("Numéro : ")
            self.selected_tournament = self.existing_tournament[int(self.user_choice) - 1]
            self.tournament_controller.load_existing_tournament(self.selected_tournament)
        except IndexError:
            print()
            print("Vous avez choisi un mauvais numéro. Veuillez réessayer.")
            print()
            self.show_tournaments_in_database()
            self.select_tournament_in_database()
            return
        except ValueError:
            print()
            print("Vous devez renseigner un chiffre. Veuillez réessayer")
            print()
            self.show_tournaments_in_database()
            self.select_tournament_in_database()
            return

        self.show_menu()

    def show_loaded_tournaments(self):
        for index, tournament in self.tournament_controller.tournament_list:
            print(f"{index} >> {tournament}")

    def load_tournament_from_database(self):
        """Sélectionne le tournoi existant."""
        print("Quel tournoi souhaitez-vous charger ?")

        try:
            self.user_choice = input("Numéro : ")
            self.selected_tournament = self.tournament_controller.tournament_list[int(self.user_choice) - 1]
        except IndexError:
            print()
            print("Vous avez choisi un mauvais numéro. Veuillez réessayer.")
            print()
            self.show_tournaments_in_database()
            self.select_tournament_in_database()
            return
        except ValueError:
            print()
            print("Vous devez renseigner un chiffre. Veuillez réessayer")
            print()
            self.show_tournaments_in_database()
            self.select_tournament_in_database()
            return

        self.show_menu()