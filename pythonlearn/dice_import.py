# Make a class Die with one attribute called sides, which has a default
# value of 6. Write a method called roll_die() that prints a random number
# between 1 and the number of sides the die has. Make a 6-sided die and roll it
# 10 times.

from random import randint


class Dice:

    """ create a dice object and instantiate"""
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        return randint(1, self.sides)


# this function rolls the die passed in 10 times
def roll_dice(dice_type):
    print(f"\nYou are rolling a {dice_type.sides} sided die!")
    for die_roll in range(10):
        print(f"You rolled a: {dice_type.roll_die()}")


# create and roll six sided die
hex_die = Dice()
roll_dice(hex_die)

# Make a 10-sided die and a 20-sided die. Roll each die 10 times.
deca_die = Dice(10)
roll_dice(deca_die)

poly_die = Dice(20)
roll_dice(poly_die)


