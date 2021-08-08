import random


def roll_die():
    die1 = random.randrange(1, 7)
    die2 = random.randrange(1, 7)
    return die1, die2


def display_dice(dice):
    die1, die2 = dice
    print(f'player played {die1} and {die2} = {sum(die1, die2)}')


die_values = roll_die()
display_dice(die_values)

sum_of_die = sum(die_values)