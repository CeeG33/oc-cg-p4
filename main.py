import datetime
import time
from models import tournament, player, match, rounds
from random import sample
import itertools

bob = player.Player("L'Éponge", "Bob", "02/02/2002")
patrick = player.Player("Étoile de Mer", "Patrick", "01/01/2004")
carlo = player.Player("Calamar", "Carlo", "03/03/2003")
crabs = player.Player("Crabs", "Captain", "02/03/1993")
sandy = player.Player("Écureuil", "Sandy", "04/05/2000")
plankton = player.Player("Sheldon", "Plankton", "01/02/1992")
pearl = player.Player("Crabs", "Pearl", "01/02/2005")
gary = player.Player("L'Escargot", "Gary", "05/02/2008")
liste1 = []

liste1.append(bob)
liste1.append(patrick)
liste1.append(carlo)
liste1.append(crabs)
liste1.append(sandy)
liste1.append(plankton)
liste1.append(pearl)
liste1.append(gary)

for playa in liste1:
    playa.update_json_file()


tournoi1 = tournament.Tournament("Tournoi Pâté de Crabe", "Bikini Bottom", "Meilleur tournoi des mers !!")

for playa in liste1:
    tournoi1.add_player_to_tournament(playa)

print(f"Liste joueurs: {tournoi1.players_list}")

tournoi1.shuffle_players()
tournoi1.create_pairs()

print(f"Liste joueurs mélangée: {tournoi1.pairs_list}")

round1 = rounds.Round("Round 1")

print(f"Liste matches Round 1 avant création : {round1.match_list}")

tournoi1.create_first_round_matches(round1)

print(f"Liste matches Round 1 après création : {round1.match_list}")

print(f"Résultats du Round 1 :")

round1.match_list[0].draw()
round1.match_list[1].draw()
round1.match_list[2].player1_wins()
round1.match_list[3].player2_wins()
print(round1.match_list[0].tuple)
print(round1.match_list[1].tuple)
print(round1.match_list[2].tuple)
print(round1.match_list[3].tuple)

for contest in round1.match_list:
    contest.update_player1_global_score()
    contest.update_player1_tournament_score()
    contest.update_player2_global_score()
    contest.update_player2_tournament_score()

for playa in tournoi1.players_list:
    playa.update_json_file()

tournoi1.players_list.sort()
post_round1_list = tournoi1.players_list
print(f"Liste joueurs après Round 1 : {post_round1_list}")

"""
for playa in range(0, len(tournoi1.pairs_list), 2):
    round1.add_match(match.Match(tournoi1.pairs_list[playa], tournoi1.pairs_list[playa+1]))
    
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



time.sleep(5)
tournament1.end_date.append(datetime.datetime.now().replace(microsecond=0))
"""












