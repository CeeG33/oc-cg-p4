import os
from controllers import tournamentcontroller, reportcontroller


NUMBER_OF_PLAYERS_IN_TOURNAMENT = 8
tournament_controller = tournamentcontroller.TournamentController()
tournament_view = tournament_controller.tournament_view
player_controller = tournament_controller.player_controller
player_view = player_controller.player_view
report_controller = reportcontroller.ReportController()
report_view = report_controller.report_view

running = True
while running:
    print("--- MENU PRINCIPAL ---")
    print()

    main_menu_list = [f"[1] > Ajouter un joueur - Salle d'attente : "
                      f"{len(player_controller.waiting_room)} / {NUMBER_OF_PLAYERS_IN_TOURNAMENT} joueurs",
                      "[2] > Démarrer / continuer un tournoi.",
                      "[3] > Générer des rapports.",
                      "[4] > Quitter le programme."]

    for choice in main_menu_list:
        print(choice)
    print()
    print("Que souhaitez-vous faire ?")
    user_choice = input("Numéro : ")
    if user_choice == "1":
        player_view.show_menu()
    elif user_choice == "2":
        tournament_view.show_menu()
    elif user_choice == "3":
        if os.path.exists("data/rounds/"):
            report_view.show_menu()
        else:
            print("Impossible d'accéder au menu Rapport car la base de données est vide !")
    elif user_choice == "4":
        print("Fermeture du programme !")
        quit()
    else:
        print()
        print(f"Erreur. Veuillez choisir un numéro entre 1 et {len(main_menu_list)}.")
        print()
