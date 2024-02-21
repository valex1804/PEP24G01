# import random
#
# print(random.choice(['p', 'h', 'f']))
import random

import random

while True:
    nume_p = input('banga nume: ')
    optiuni = {'p': 'piatra', 'f': 'foarfeca', 'h': 'hartie', 'q': 'renunta'}
    optiuni_afisate = str()

    for key, value in optiuni.items():
        optiuni_afisate += f'{key}, ({value})'

    optiune_player = input(f'Alege optiune: [{optiuni_afisate}]')
    optiuni_server = list(optiuni.keys())
    optiuni_server.remove('q')

    optiune_server = random.choice(optiuni_server)
    print(f'> Server: {optiuni[optiune_server]}')
    print(f'> {nume_p}: {optiuni[optiune_player]}')

    if optiune_server == "p" and optiune_player == "f":
        print("Serverul a castigat")
        break
    elif optiune_server == "h" and optiune_player == "p":
        print("Serverul a castigat")
        break
    elif optiune_server == "f" and optiune_player == "h":
        print("Serverul a castigat")
        break
    elif optiune_server == optiune_player:
        print("Egalitate")

    else:
        print(nume_p, "A castigat")
        break

# Varianta 2 with tuples

import random

# rock = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''
#
# paper = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''
#
# scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''
#
# choices = {"rock": rock, "paper": paper, "scissors": scissors}
#
# player_name = input("Player name: ")
#
# for key, value in choices.items():
#     print_choices = "".join(key + value)
#     print(print_choices)
#
# combinations = {("rock", "paper"): False, ("paper", "rock"): True,
#                 ("rock", "scissors"): True, ("scissors", "rock"): False,
#                 ("paper", "scissors"): False, ("scissors", "paper"): True}
#
# game_on = True
#
# while game_on:
#     player_choice = input("Type an option rock/paper/scissors or q if you want to quit: ").lower()
#     if player_choice == "q":
#         game_on = False
#         print("Bye bye!")
#         break
#     elif player_choice not in choices.keys():
#         player_choice = input("Invalid option. Type rock/paper/scissors or q if you want to quit: ").lower()
#     else:
#         pc_choice = random.choice(list(choices.keys()))
#         print(f"{player_name}'s choice:\n", choices[player_choice])
#         print("Computer choice:\n", choices[pc_choice])
#         if player_choice == pc_choice:
#             print("Draw!")
#             continue
#         result = combinations[(player_choice, pc_choice)]
#         if result:
#             print(f"{player_name} won!")
#             break
#         else:
#             print("Server won! You lose!")
#             break
