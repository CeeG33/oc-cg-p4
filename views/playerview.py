import re

class PlayerView:

    def __init__(self, player_controller):
        self.player_controller = player_controller
        self.SEATS_NUMBER = 8
        self.user_choice = 0
        self.existing_players = self.player_controller.get_existing_players()
        self.menu_list = ["[1] > Créer un nouveau joueur.",
                          "[2] > Charger un joueur existant en entrant son nom et prénom manuellement.",
                          "[3] > Charger un joueur existant en parcourant la base de données.",
                          "[4] > Afficher les joueurs présents dans la base de données.",
                          "[5] > Revenir au menu principal."]

    def show_menu(self):
        """Affiche le menu principal de la vue PlayerController à l'utilisateur."""
        print("---- MENU JOUEUR----")
        print()
        self.show_waiting_room()
        self.update_remaining_seats()
        print()
        self.show_menu_list()
        self.prompt_user()

    def show_menu_list(self):
        """Affiche le menu selon la liste définie dans l'init."""
        for choice in self.menu_list:
            print(choice)

    def show_waiting_room(self):
        """Affiche les joueurs présents dans la salle d'attente."""
        if not self.player_controller.waiting_room:
            print("Salle d'attente : Vide")
        else:
            print(f"Salle d'attente : {self.player_controller.waiting_room}")

    def prompt_user(self):
        """Affiche l'option sélectionnée par l'utilisateur."""
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
            elif self.user_choice == "2":
                self.get_existing_player_info_manually()
            elif self.user_choice == "3":
                self.show_players_in_database()
                self.select_player_in_database()
            elif self.user_choice == "4":
                self.show_players_in_database()
            elif self.user_choice == "5":
                break
            elif int(self.user_choice) not in range(1, len(self.menu_list)):
                print()
                print("Vous avez choisi un mauvais numéro.")
                print(f"Veuillez choisir un numéro entre 1 et {len(self.menu_list)}.")
                print()

    def get_player_name(self):
        """Récupère le nom du joueur auprès de l'utilisateur."""
        name = input("Nom du joueur (Respectez les accents. Exemple : L'éponge) : ").capitalize()
        if not name.isalpha():
            print()
            print("Mauvais caractères, veuillez écrire un nom en lettres.")
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
        if not first_name.isalpha():
            print()
            print("Mauvais caractères, veuillez écrire un prénom en lettres.")
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
        birthdate = input("Date de naissance (Format JJ/MM/AAAA. Exemple : 01/02/1960) : ")
        pattern = r"^\d{2}/\d{2}/\d{4}$"
        if not re.match(pattern, birthdate):
            print()
            print("Mauvais format, veuillez suivre le format JJ/MM/AAAA.")
            print()
            self.get_player_birthdate()
        else:
            return birthdate

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

    def get_existing_player_info_manually(self):
        """Charge un joueur dans le salon selon le nom et prénom renseigné par l'utilisateur manuellement."""
        name = self.get_player_name()
        first_name = self.get_player_first_name()

        self.player_controller.load_existing_player(name, first_name)
        print()
        self.show_waiting_room()
        self.show_menu_list()

    def show_players_in_database(self):
        """Affiche la liste des joueurs enregistrés dans la base de données."""
        print("Liste des joueurs existants :")
        print("")
        for index, player in enumerate(self.existing_players, 1):
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
            print(f"Les joueurs sont au complet. Le tournoi peut commencer !")
        else:
            self.show_menu_list()

    def select_player_in_database(self):
        """Sélectionne le joueur existant et l'ajoute à la salle d'attente."""
        print("Quel joueur souhaitez-vous ajouter ?")

        try:
            self.user_choice = input("Numéro : ")
            selected_player = self.existing_players[int(self.user_choice) - 1]
        except IndexError:
            print()
            print("Vous avez choisi un mauvais numéro. Veuillez réessayer.")
            print()
            self.show_players_in_database()
            self.select_player_in_database()
            return
        except ValueError:
            print()
            print("Vous devez renseigner un chiffre. Veuillez réessayer")
            print()
            self.show_players_in_database()
            self.select_player_in_database()
            return

        if selected_player in self.player_controller.waiting_room:
            print()
            print("Attention, ce joueur est déjà dans la salle d'attente !")
            print()
            self.show_waiting_room()
            print()
            print("Veuillez sélectionner un autre joueur.")
            print()
            self.show_players_in_database()
            self.select_player_in_database()
        else:
            self.player_controller.waiting_room.append(selected_player)
            print()
            self.show_waiting_room()
            self.show_menu_list()



"""


"""