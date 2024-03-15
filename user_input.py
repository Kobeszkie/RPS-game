import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

#rock paper scissors
player_choice = input("Enter...\n1 for Rock,\n2 for Raper, or \n3 for Scissors:\n\n")

player = int(player_choice)

if player < 1 | player > 3:
    sys.exit("Invalid input")

computer_choice = random.choice("123")

computer = int(computer_choice)

print("\nYou chose " + str(RPS(player)).replace('RPS.','') + ".")
print("Python chose " + str(RPS(computer)).replace('RPS.','') + ".\n")

if player == 1 and computer == 3:
    print("🙌 You win!")
elif player == 2 and computer == 1:
    print("🙌 You win!")
elif player == 3 and computer == 2:
    print("🙌 You win!")
elif player == computer:
    print("😲 Draw game")
else:
    print("🐍 Python wins!")