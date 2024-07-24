import sys
import random
from enum import Enum


class combatRole(Enum):
    ASSAULT = 1
    ENGINEER = 2
    LMG = 3
    SNIPER = 4

print("")
playerchoice = input(
    "Enter...\n1 for Assault,\n2 for Engineer,\n3 for LMG,\n4 for SNIPER:\n")

player = int(playerchoice)

if player < 1 or player > 4:
    sys.exit("You must enter 1, 2, 3 or 4.")

computerchoice = random.choice("1234")

computer = int(computerchoice)

print("")
print("You chose " + str(combatRole(player)).replace('combatRole.', '') + ".")
print("Python chose " + str(combatRole(computer)).replace('combatRole.', '') + ".")
print("")

if player == 1 and computer == 3:
    print("Assault vs LMG")
elif player == 2 and computer == 1:
    print("Engineer vs Assault")
elif player == 3 and computer == 2:
    print("LMG vs Engineer")
elif player == computer:
    print("Tie Role")
else:
    print("Different Roles")