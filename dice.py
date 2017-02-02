"""Simulate various dice rolls"""

import random


def die(x):
    """Roll a die with x sides"""
    return random.randint(1, x)


def xdy(x, y):
    """Roll x number of y sided dice"""
    return sum(die(y) for i in range(x))


def xdyd(x, y):
    """Roll x number of y sided dice and drop lowest roll"""
    return sum(sorted(die(y) for _ in range(x))[1:])


def explodedie(x):
    """Roll exploding die with x sides. """
    current_roll = die(x)
    total_roll = current_roll
    while current_roll == x:
        current_roll = die(x)
        total_roll += current_roll
    return total_roll


def standard_roll():
    return xdy(3, 6)


def mighty_roll():
    return xdyd(4, 6)
