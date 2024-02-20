import random
import sys
from enum import Enum

class RPS(Enum):
    SHOTGUN = 1
    RELOAD = 2
    SHIELD = 3

playermove = input("Enter:\n1 for SHOTGUN\n2 for RELOAD\n3 for SHIELD\n\n")
player = int(playermove)

if player < 1 or player > 3:
    sys.exit("You must enter 1, 2, or 3")

computerchoice = random.choice("123")
computer = int(computerchoice)

print("You entered " + str(RPS(player)).replace('RPS.', '') + ".") 
print("Python entered " + str(RPS(computer)).replace('RPS.', '') + ".")

# SHOTGUN = 1
# RELOAD = 2
# SHIELD = 3

if player == 1 and computer == 2:
    print("You Win")
elif player == 2 and computer == 1:
    print("Python Wins")
else:
    print("Tie Game")
