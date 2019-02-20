from random import random


def flip_coin():
    rand = random()
    if rand >= 0.5:
        return "Heads"
    else:
        return "Tails"


# function ovverriding
def flip_coin():
    if random() >= 0.5:
        return "HEADS"
    else:
        return "TAILS"


print(flip_coin())
print(flip_coin())
print(flip_coin())
print(flip_coin())
