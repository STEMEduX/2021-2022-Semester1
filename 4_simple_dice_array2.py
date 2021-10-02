##
## simple_dice.py

import random


def roll(sides=6):
    num_rolled = random.randint(1,sides)
    return num_rolled
  
def main():
    sides = 6
    sides = input("How many faces/sides of your die? ")
    if sides.isnumeric():
        sides = int(sides)
    else:
        sides = 6

    a = [0] * (sides + 1)
    totalrolls = 0

    totalrolls = input("How many times do you want to roll?")

    if totalrolls.isnumeric():
        for i in range(0, int(totalrolls)):
        
            num_rolled = roll(sides)
            print("You rolled a ", num_rolled)

            a[num_rolled] = a[num_rolled] + 1

        print("Thanks for playing.")
        print("Total rolls", totalrolls);

        for j in range(1, int(sides + 1)):
            print("number", j, "showed up", a[j], " probability ", a[j]/int(totalrolls));

    else:
        print("You should enter a number for playing. Please start over")

main()