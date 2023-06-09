import re
import datetime


class PlayerView:
    def __init__(self, player_controller):
        """Initialise une vue affichant le menu de gestion des joueurs.
        Args:
        - player_controller (obj): contient un contrôleur PlayerController.

        Attrs:
        - player_controller (obj): contient un contrôleur PlayerController.
        - SEATS_NUMBER (int): correspond au nombre de joueurs par tournoi (initialisé sur 8 par défaut).
        - user_choice (int): contient le choix de l'utilisateur dans le menu PlayerView (initialisé sur 0).
        - existing_players (list): liste des joueurs existants contenue dans le contrôleur.
        - menu_list (list): contient les options de navigation de la vue.
        """
        self.player_controller = player_controller
        self.SEATS_NUMBER = 8
        self.user_choice = 0
        self.existing_players = self.player_controller.get_existing_players()
        self.menu_list = ["[1] > Créer un nouveau joueur.",
                          "[2] > Charger un joueur existant en parcourant la base de données.",
                          "[3] > Afficher les joueurs présents dans la base de données.",
                          "[4] > Revenir au menu principal."]

    def show_menu(self):
        """Affiche le menu principal de la vue à l'utilisateur."""
        print("---- MENU JOUEUR----")
        print()
        self.show_waiting_room()
        self.update_remaining_seats()
        print()
        self.show_menu_list()
        self.prompt_user()

    def show_menu_list(self):
        """Affiche le menu selon la liste définie dans le constructeur."""
        for choice in self.menu_list:
            print(choice)

    def show_waiting_room(self):
        """Affiche les joueurs présents dans la salle d'attente."""
        if not self.player_controller.waiting_room:
            print("Salle d'attente : Vide")
        else:
            print(f"Salle d'attente : {self.player_controller.waiting_room}")

    def prompt_user(self):
        """Demande l'action de l'utilisateur dans le menu."""
        while True:
            print("")
            print("Que souhaitez-vous faire ?")
            self.user_choice = input("Numéro : ")
            if self.user_choice == "1":
                name = self.get_player_name()
                first_name = self.get_player_first_name()
                birthdate = self.get_player_birthdate()
                national_chess_id = self.get_player_national_chess_id()
                self.player_controller.create_new_player(name, first_name, birthdate, national_chess_id)
                print()
                self.show_waiting_room()
                print()
                self.update_remaining_seats()
                print()
                self.show_menu_list()
            elif self.user_choice == "2":
                if self.existing_players:
                    if len(self.player_controller.waiting_room) == 8:
                        print()
                        print("La salle d'attente est au complet déjà !")
                        print("Retour au menu.")
                        print()
                        self.show_menu_list()
                    else:
                        self.show_players_in_database()
                        self.select_player_in_database()
                else:
                    print("La base de données est vide. ",
                          "Il faut d'abord sauvegarder un tournoi avec des joueurs",
                          "pour pouvoir les retrouver dans la base de données.")
                    print()
                    print("Retour au menu.")
                    print()
                    self.show_waiting_room()
                    print()
                    self.update_remaining_seats()
                    print()
                    self.show_menu_list()
            elif self.user_choice == "3":
                if self.existing_players:
                    self.show_players_in_database()
                    self.show_waiting_room()
                    print()
                    self.update_remaining_seats()
                    print()
                    self.show_menu_list()
                else:
                    print("La base de données est vide. ",
                          "Il faut d'abord sauvegarder un tournoi avec des joueurs",
                          "pour pouvoir les retrouver dans la base de données.")
                    print()
                    print("Retour au menu.")
                    print()
                    self.show_waiting_room()
                    print()
                    self.update_remaining_seats()
                    print()
                    self.show_menu_list()
            elif self.user_choice == "4":
                break
            else:
                print()
                print("Vous avez choisi un mauvais numéro.")
                print(f"Veuillez choisir un numéro entre 1 et {len(self.menu_list)}.")
                print("Retour au menu.")
                print()
                self.show_menu_list()

    def get_player_name(self):
        """Récupère le nom du joueur auprès de l'utilisateur."""
        name = input("Nom du joueur (Respectez les accents. Exemple : L'éponge) : ").capitalize()
        pattern = "^[A-Za-zÀ-ÿ'-]+$"
        if not re.match(pattern, name):
            print()
            print("Mauvais caractères, veuillez écrire un nom en lettres sans les apostrophes.")
            print()
            self.get_player_name()
        elif len(name) <= 1:
            print()
            print("Nom trop court. Il doit au moins contenir deux caractères.")
            print()
            self.get_player_name()
        else:
            return name

    def get_player_first_name(self):
        """Récupère le prénom du joueur auprès de l'utilisateur."""
        first_name = input("Prénom du joueur (Respectez les accents. Exemple : Jean-édouard) : ").capitalize()
        pattern = "^[A-Za-zÀ-ÿ'-]+$"
        if not re.match(pattern, first_name):
            print()
            print("Mauvais caractères, veuillez écrire un nom en lettres.")
            print()
            self.get_player_first_name()
        elif len(first_name) <= 1:
            print()
            print("Prénom trop court. Il doit au moins contenir deux caractères.")
            print()
            self.get_player_first_name()
        else:
            return first_name

    def get_player_birthdate(self):
        """Récupère la date de naissance du joueur auprès de l'utilisateur."""
        pattern = r"^\d{2}/\d{2}/\d{4}$"
        current_year = datetime.datetime.now().year
        player_minimum_birth_year = 1920
        player_maximum_birth_year = current_year - 5

        while True:
            birthdate = input("Date de naissance (Format JJ/MM/AAAA. Exemple : 01/02/1960) : ")
            if not re.match(pattern, birthdate):
                print()
                print("Mauvais format, veuillez suivre le format JJ/MM/AAAA.")
                print()
            else:
                day, month, year = map(int, birthdate.split("/"))
                if year < player_minimum_birth_year or year > player_maximum_birth_year:
                    print()
                    print("Année de naissance invalide.",
                          "Veuillez entrer une année comprise entre ",
                          f"{player_minimum_birth_year} et {player_maximum_birth_year}.")
                    print()
                else:
                    try:
                        datetime.datetime(year, month, day)
                        return birthdate
                    except ValueError:
                        print()
                        print("Erreur, veuillez saisir un numéro de jour et de mois valide !")
                        print()

    def get_player_national_chess_id(self):
        """Récupère l'identifiant national d'échec du joueur auprès de l'utilisateur."""
        national_chess_id = input("Identifiant national d'échec (Exemple : AA12345) : ").upper()
        pattern = r"[A-Z]{2}\d{5}$"
        if not re.match(pattern, national_chess_id):
            print()
            print("Mauvais format, veuillez suivre le format AA11111.")
            print()
            self.get_player_national_chess_id()
        else:
            return national_chess_id

    def show_players_in_database(self):
        """Affiche la liste des joueurs enregistrés dans la base de données."""
        existing_players = self.player_controller.get_existing_players()
        print("Liste des joueurs existants :")
        print("")
        for index, player in enumerate(existing_players, 1):
            print(f"{index} >> {player}")
        print("")
        print("###############")
        print("Fin de la liste")
        print("")

    def update_remaining_seats(self):
        """Affiche le nombre de joueurs manquant pour commencer un tournoi."""
        current_seats = self.SEATS_NUMBER - len(self.player_controller.waiting_room)
        if current_seats > 0:
            print(f"Il manque encore {current_seats} joueurs pour démarrer un tournoi !")
        elif current_seats == 0:
            print("Les joueurs sont au complet. Le tournoi peut commencer !")
        else:
            self.show_menu_list()

    def select_player_in_database(self):
        """Sélectionne le joueur existant et l'ajoute à la salle d'attente."""
        existing_players = self.player_controller.get_existing_players()
        while True:
            print("Quel joueur souhaitez-vous ajouter ?")
            try:
                self.user_choice = input("Numéro : ")
                selected_player = existing_players[int(self.user_choice) - 1]
                if str(selected_player) in str(self.player_controller.waiting_room):
                    print()
                    print("Attention, ce joueur est déjà dans la salle d'attente !")
                    print()
                    self.show_waiting_room()
                    self.update_remaining_seats()
                    print()
                    print("Veuillez sélectionner un autre joueur.")
                    print()
                    self.show_players_in_database()
                    print()
                else:
                    self.player_controller.waiting_room.append(selected_player)
                    print()
                    self.show_waiting_room()
                    print()
                    self.update_remaining_seats()
                    print()
                    self.show_menu_list()
                    break
            except (ValueError, IndexError):
                print()
                print("Vous avez choisi un mauvais numéro. Veuillez réessayer.")
                print()
                self.show_waiting_room()
                self.update_remaining_seats()
                print()
                self.show_players_in_database()
                print()
