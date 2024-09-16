import sys
import random
from enum import Enum

# Sample user input

# value = input("please enter a name: ")
# print(value)

# value = int(input("Enter a value: "))
# print(value)

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSOR = 3
    
# sample demo

# print(RPS(2))
# print(RPS.ROCK)
# print(RPS['ROCK'])
# print(RPS.ROCK.value)
# sys.exit()


print("")
playerchoice = input("Enter....\n1. for Rock,\n2. for Paper,\n3. for Scissors:")

player = int(playerchoice)

if player < 1 | player > 3 :
    #print("You must enter 1, 2, or 3.")
    sys.exit("You must enter 1, 2, or 3.")
    
computerchoice = random.choice("123")
computer = int(computerchoice)

print("")
# print("You choose "+playerchoice+".")
# print("Python choose "+computerchoice+".") # or
print("You choose "+str(RPS(player)).replace('RPS.','')+".")
print("Python choose "+str(RPS(computer)).replace('RPS.','')+".")
print("")

if player == 1 and computer == 3 :
    print("🎉 You win!")
elif player == 2 and computer == 1 :
    print("🎉 You win!")
elif player == 3 and computer == 2 :
    print("🎉 You win!")
elif player == computer :
    print("😲 Tie game!")
else:
    print("🐍 Python Wins!")
    