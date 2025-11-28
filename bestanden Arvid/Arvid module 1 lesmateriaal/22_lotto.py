"""
Opgave:
    De lotto is een kansspel met een aantal ballen met een waarde tussen 1 en een maximum
    De kans dat jouw kruisjes overeenkomen met de wekelijkse trekking is:
        CHANCE = RANGE! / (COUNT! * (RANGE-COUNT)!)
        Met x! = x * (x-1) * (x-2) * ... * 3 * 2 * 1

    Schrijf een programma dat:
       * een winnende lotto trekking bepaalt
       * opeenvolgende trekkingen genereert tot een trekking overeenkomt met de winnend combinatie
       * afdrukt hoeveel pogingen nodig zijn om de trekking te winnen.
       * beoordeelt of dat aantal pogingen beter is dan de geschatte kans.


    De code:
    * robuust voor fouten in de parameters.
    * Bij fouten moet het programma eindigen met een error boodschap en code 1
    * PEP8
    * volledig getypeerd
    * volledig gedocumenteerd
    * loggen van het programma naar de console, geen print statements

    Hints:
        * math.factorial(x): x!
        * random.sample(range(1, RANGE), COUNT): COUNT verschillende willekeurige getallen tussen 1 en RANGE:
"""
import csv
import logging
import os
import random
import sys
from math import factorial as fac
from typing import List, Tuple

chance = lambda balls, range_: fac(range_) // (fac(balls) * fac(range_ - balls))

def draw(balls: int, range_: int) -> List[int]:
    """
    Draw a specified number of values from a specified range.
    :param balls: Number of values to draw
    :param range_: Ranges of possible values
    :return: sorted list of drawn values
    """
    return sorted(random.sample(range(1, range_ + 1), balls))


def sim_lottery(balls: int, range_: int) -> Tuple[int, bool]:
    """
    Simulate how many different attempts it takes to win the lottery.
    Decide whether the actual number of attempts is better than the expected chance.
    :param balls: Number of balls
    :param range_: the different values on the balls
    :return: (number of attempts,
    """
    attempt = 0
    winners = draw(balls, range_)
    print(f"Dit zijn de winnaars die we zoeken {winners}")
    while True:
        attempt += 1
        cur_draw = draw(balls, range_)
        if cur_draw == winners:
            print(f"We hebben een winnende trekking bij poging {attempt}")
            break

    expected = chance(balls, range_)
    print(f"The expected chance is: {expected:}")
    return attempt, attempt < expected




count = 6
maxi = 45
attempts, better = sim_lottery(count, maxi)
if better:
    print(f"De kans is beter dan de geschatte kans.")
else:
    print(f"Je hebt geen geluk vandaag.")

# Soms zijn de getallen erg groot
# In code kan je 1000000 schrijven als 1_000_000.
# in f-string kan je aangeven hoe je het getal kan wil weergeven

