import datetime
import time
from models import tournament, player, match, rounds
from controllers import playercontroller
from random import sample
import itertools

controller = playercontroller.PlayerController()

controller.load_existing_player("L'Éponge", "Bob")

print(controller.players_list)



"""
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


tournoi1 = tournament.Tournament("Tournoi Pâté de Crabe", "Bikini Bottom", "Meilleur tournoi des mers !!")

tournoi1.set_start_date()

for playa in liste1:
    tournoi1.add_player_to_tournament(playa)
    playa.update_json_file()

print(f"Liste joueurs: {tournoi1.players_list}")

tournoi1.shuffle_players()
tournoi1.create_pairs()

print(f"Liste joueurs mélangée: {tournoi1.pairs_list}")

round1 = rounds.Round("Round 1")

round1.set_start_date()
tournoi1.begin_round()

print(f"Liste matches Round 1 avant création : {round1.match_list}")

tournoi1.create_first_round_matches(round1)

print(f"Liste matches Round 1 après création : {round1.match_list}")

print(f"Résultats du Round 1 :")

round1.match_list[0].chose_winner(round1.match_list[0].player1)
round1.match_list[1].chose_winner(round1.match_list[1].player2)
round1.match_list[2].is_draw()
round1.match_list[3].is_draw()

print(round1.match_list[0].winner)
print(round1.match_list[1].winner)
print(round1.match_list[2].draw)
print(round1.match_list[3].draw)

round1.set_end_date()
tournoi1.end_round(round1)

print(tournoi1.rounds_list)
tournoi1.get_scores()

for r in tournoi1.rounds_list:
    for m in r.get_matches():
        if m.winner:
            tournoi1.winners_list.append(m.winner)
        if m.draw:
            tournoi1.draw_list.extend(m.draw)

for p in tournoi1.winners_list:
    tournoi1.add_one_point_to(p)

for p in tournoi1.draw_list:
    tournoi1.add_half_point_to(p)

print(tournoi1.players_scores)
tournoi1.sort_players()
print(tournoi1.players_scores)
tournoi1.reinitialise_winners_list()
tournoi1.reinitialise_draw_list()



round2 = rounds.Round("Round 2")

round2.set_start_date()
tournoi1.begin_round()

print(f"Liste matches Round 2 avant création : {round2.match_list}")

tournoi1.create_next_round_matches(round2)


print(f"Liste matches Round 2 après création : {round2.match_list}")


print(f"Résultats du Round 2 :")

round2.match_list[0].chose_winner(round2.match_list[0].player2)
round2.match_list[1].chose_winner(round2.match_list[1].player2)
round2.match_list[2].chose_winner(round2.match_list[2].player2)
round2.match_list[3].is_draw()

print(round2.match_list[0].winner)
print(round2.match_list[1].winner)
print(round2.match_list[2].winner)
print(round2.match_list[3].draw)

round2.set_end_date()
tournoi1.end_round(round2)

print(tournoi1.rounds_list)
tournoi1.get_scores()

for r in tournoi1.rounds_list:
    for m in r.get_matches():
        if m.winner:
            tournoi1.winners_list.append(m.winner)
        if m.draw:
            tournoi1.draw_list.extend(m.draw)

for p in tournoi1.winners_list:
    tournoi1.add_one_point_to(p)

for p in tournoi1.draw_list:
    tournoi1.add_half_point_to(p)

print(tournoi1.players_scores)
tournoi1.sort_players()
print(tournoi1.players_scores)

tournoi1.show_players_rank()
tournoi1.update_json_file()

print(tournoi1.players_list)

for playa in tournoi1.players_list:
    playa.update_json_file()


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












