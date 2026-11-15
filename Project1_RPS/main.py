from asyncio import wait

from ASCII_RPS import *
import random

player_input = input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors!")

if player_input == 0:
    print(rock)
elif player_input == 1:
    print(paper)
elif player_input == 2:
    print(scissors)
else:
    print("Invalid input")

comp_choice = random.randint(0,2)
print(comp_choice)
