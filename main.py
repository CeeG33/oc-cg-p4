import datetime
import time
from models import tournament, player, match, rounds

player1 = player.Player("L'Eponge", "Bob", "02/04/2000")
player2 = player.Player("Etoile de mer", "Patrick", "01/01/2000")


tournament1 = tournament.Tournament("Tournoi Pâté de Crabe",
                                    "Bikini Bottom",
                                    "Capitaine Crabs surveille ce tournoi !")
tournament1.start_date = (datetime.datetime.now().replace(microsecond=0))

match1 = match.Match(player1, player2)

tournament1.players_list.append(player1)
tournament1.players_list.append(player2)

tournament1.current_round_number = 1

print(f"Bonjour à tous ! Bienvenu au {tournament1.name} !!")
print(f"Aujourd'hui, en direct de {tournament1.location} s'affronteront d'un côté : {match1.player1.first_name}")
print(f"Et de l'autre : {match1.player2.first_name}")
print("")
print(f"Voici le début exact du tournoi : {tournament1.start_date}")
print(f"Un commentaire du Directeur du tournoi ? {tournament1.description}")
print("")
print(f"Début du round N°{tournament1.current_round_number}")
print("Suspens...")
time.sleep(2)
print("..")
time.sleep(2)
print(".")
time.sleep(4)
print("Le match s'achève avec une victoire écrasante de Patrick !!")
print("")


"""
time.sleep(5)
tournament1.end_date.append(datetime.datetime.now().replace(microsecond=0))
"""












