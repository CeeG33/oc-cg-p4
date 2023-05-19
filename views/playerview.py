
class PlayerView:

    def __init__(self, player_controller):
        self.player_controller = player_controller
        self.SEATS_NUMBER = 8
        self.user_choice = 0

    def show_menu(self):
        print("---- MENU JOUEUR----")
        print()
        self.show_waiting_room()
        self.update_remaining_seats()
        print()
        print("[1] > Créer un nouveau joueur")
        print("[2] > Charger un joueur existant en entrant son nom et prénom manuellement")
        print("[3] > Charger un joueur existant en parcourant la base de données")
        self.prompt_user()

    def show_waiting_room(self):
        if not self.player_controller.waiting_room:
            print("Salle d'attente : Vide")
        else:
            print(f"Salle d'attente : {self.player_controller.waiting_room}")

    def prompt_user(self):
        print("")
        print("Que souhaitez-vous faire ?")
        self.user_choice = input("Numéro : ")
        if self.user_choice == "1":
            self.get_new_player_info()
        elif self.user_choice == "2":
            self.get_existing_player_info_manually()
        elif self.user_choice == "3":
            pass #à terminer


    def get_new_player_info(self):
        name = input("Nom du joueur (Respectez les accents et majuscules. Exemple : L'Éponge) : ")
        first_name = input("Prénom du joueur (Respectez les accents et majuscules. Exemple : Jean-Édouard) : ")
        birthdate = input("Date de naissance (Format JJ/MM/AAAA. Exemple : 01/02/1960) : ")
        national_chess_id = input("Identifiant national d'échec (Exemple : AA12345) : ").upper()

        self.player_controller.create_new_player(name, first_name, birthdate, national_chess_id)
        self.show_menu()

    def get_existing_player_info_manually(self):
        name = input("Nom du joueur (Respectez les accents et majuscules. Exemple : L'Éponge) : ")
        first_name = input("Prénom du joueur (Respectez les accents et majuscules. Exemple : Jean-Édouard) : ")

        self.player_controller.load_existing_player(name, first_name)
        self.show_menu()

    def show_players_in_database(self):
        name = input("Nom du joueur (Respectez les accents et majuscules. Exemple : L'Éponge) : ")
        first_name = input("Prénom du joueur (Respectez les accents et majuscules. Exemple : Jean-Édouard) : ")

        self.player_controller.load_existing_player(name, first_name)
        self.show_menu()

    def update_remaining_seats(self):
        current_seats = self.SEATS_NUMBER - len(self.player_controller.waiting_room)
        if current_seats > 0:
            print(f"Il manque encore {current_seats} joueurs pour démarrer un tournoi !")
        elif current_seats == 0:
            print(f"Les joueurs sont au complet. Le tournoi peut commencer !")
            pass #self.player_controller.tournament_view
        else:
            self.show_menu()



"""


"""