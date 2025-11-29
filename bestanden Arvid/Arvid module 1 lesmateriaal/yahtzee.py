"""
Eenvoudige implementatie van Yahtzee
door de groep cursisten van Python Data developer
"""

"""
Snelle functionele analyse.
Wat moet het spel kunnen

Worp:
    - 3 keer kunnen gooien
    - aantal dobbelstenen: 5
    - aantal worpen: 3
    - plek om dobbelstenen vast te houden/blokkeren

Scores:
    - tellen hoeveel keer een getal voorkomt
    - som van dobbelstenen
    - som van alle scores
    - voorwaarden om te kunnen scoren
    - score types / score namen
    -  score-vakje kiezen

Spel:
    - 13 beurten
    - max 3 worpen
    - score in vult
     Totaal afdrukken
"""

import random

# Scoreblad is een dict van str: score.
# None betekent: 'Nog geen score', 0 betekent een 0-score
scores = {
    " 1 - Aces": None,
    " 2 - Twos": None,
    " 3 - Threes": None,
    " 4 - Fours": None,
    " 5 - Fives": None,
    " 6 - Sixes": None,
    " 7 - 3 of a kind": None,
    " 8 - 4 of a kind": None,
    " 9 - Full house": None,
    "10 - Small straight": None,
    "11 - Large straight": None,
    "12 - Yahtzee": None,
    "13 - Chance": None
}


def user_roll() -> list[int]:
    """
    :return: The dice after max 3 rolls
    """

    # Een gebruiker mag 3 keer werpen
    # Bij elke worp mogen 1 tot en met 5 dobbelstenen vastgezet worden
    # Dobbelstenen die worden vastgehouden
    hold = []
    roll = []
    # TODO: als gebruiker alle stenen vasthoudt, moet niet meer gerold worden.
    # TODO: een gebruiker mag ook vestgehouden stenen, weer lossen.
    for j in range(3):
        # TODO: review: deze variable is eigenlijk niet nodig
        cnt = 5
        cnt = cnt - len(hold)
        roll = [random.randint(1, 6) for _ in range(cnt)]

        print("Uw worp: ", roll)
        # Geef de gebruiker de mogelijkheid om dobbelstenen te blokkeren
        if j < 2:
            res = input("Kies jouw dobbelstenen (indices gescheiden door spaties: ")

            if res:
                parts = res.split(" ")
            else:
                parts = []
            # TODO: error handling toevoegen
            for part in parts:
                index = int(part) - 1
                hold.append(roll[index])
            #
            print("Vastgehouden: ", hold)
    return roll + hold


def print_sheet():
    """
    Druk het scoreblad af
    """
    print("Scoreblad")
    for key, score in scores.items():
        print(key, "-" if score is None else score)
    print("Totaal: ", sum(v for v in scores.values() if v is not None))


def sum_of_value(value: int, dice: list) -> int:
    """
    Calculate sum of dice with specific value
    e.g., value:5, dice: [1,5,4,5,5] => 15
    e.g., value:5, dice: [1,1,4,1,2] => 0

    :param value: value to check
    :param dice: dice to check
    :return: sum of dice with specific value
    """
    # TODO: dit kan in 1 comprehension
    ret = 0
    for die in dice:  # [1,5,4,5,5]
        if die == value:
            ret += die
    return ret


def three_of_kind(dice: list) -> int:
    """
    :param dice:
    :return: sum of dice if there are at least 3 equal dice, else 0
    """
    # TODO: three_of_kind / four_of_kind kunnen herwerkt worden tot 1 function
    d = {}
    for die in dice:
        d[die] = d.get(die, 0) + 1

    for v in d.values():
        if v >= 3:
            return sum(dice)
    return 0


def four_of_kind(dice: list) -> int:
    """
    :param dice:
    :return: sum of dice if there are at least 4 equal dice, else 0
    """
    d = {}
    for die in dice:
        d[die] = d.get(die, 0) + 1

    for v in d.values():
        if v >= 4:
            return sum(dice)
    return 0


def five_of_kind_aka_yahtzee(dice: list) -> int:
    """
    :param dice:
    :return: sum of dice if there are at least 5 equal dice, else 0
    """
    if dice[0] == dice[1] == dice[2] == dice[3] == dice[4]:
        return 50
    return 0


def full_house(dice: list) -> int:
    """
    :param dice:
    :return: 25 if there are at 2 +3  equal dice, else 0
    """
    # 3,4,5,3,5   =>      3,3, 4, 5,5
    # 3,4,4,3,3   =>       3,3,3, 4 4
    # 1, 4,4, 4, 4
    lst = sorted(dice)
    # als de lijst gesorteerd wordt, dan moet voldaan worden aan één van deze patronen
    # [X, X, Y, Y, Y] of [X,X,X, Y,Y]
    if lst[0] == lst[1] and lst[2] == lst[3] == lst[4]:
        return 25
    if lst[0] == lst[1] == lst[2] and lst[3] == lst[4]:
        return 25
    return 0


def small_straight(dice: list):
    """
    :return 30: if there are 4 sequential dice, else 0
    """
    # 1,1,2,3,4   1,2,2,3,4,    1,2,3,3,4,  1,2,3,4,4   1,2,3,4,5   2,2,3,4,5 ...
    lst = set(sorted(dice))
    if lst == {1, 2, 3, 4} or lst == {2, 3, 4, 5}:
        return 30
    return 0


def large_straight(dice: list):
    """
    :return:  40 if there are 5 sequential dice, else 0
    """
    lst = sorted(dice)
    # 1 , 2 ,3 ,4 ,5   of  2, 3, 4, 5, 6
    if lst == [1, 2, 3, 4, 5] or lst == [2, 3, 4, 5, 6]:
        return 40
    return 0


def chance(dice: list):
    """
    :return: sum of dice
    """
    return sum(dice)


def total_scores() -> int:
    # Dict aflopen
    ret = 0
    for score, value in scores.items():
        ret += value
    return ret


for i in range(13):
    u_roll = user_roll()
    print_sheet()
    print("uw worp: ", u_roll)
    while True:
        choice = int(input("Kies een score (1-13): "))

        match choice:
            case 1:
                if scores[" 1 - Aces"] is not None:
                    print("U heeft al 1'en gekozen")
                    continue
                scores[" 1 - Aces"] = sum_of_value(1, u_roll)
            case 2:
                if scores[" 2 - Twos"] is not None:
                    print("U heeft al 2'en gekozen")
                    continue
                scores[" 2 - Twos"] = sum_of_value(2, u_roll)
            case 3:
                if scores[" 3 - Threes"] is not None:
                    print("U heeft al 3'en gekozen")
                    continue
                scores[" 3 - Threes"] = sum_of_value(3, u_roll)
            case 4:
                if scores[" 4 - Fours"] is not None:
                    print("U heeft al 4'en twee gekozen")
                    continue
                scores[" 4 - Fours"] = sum_of_value(4, u_roll)
            case 5:
                if scores[" 5 - Fives"] is not None:
                    print("U heeft al 5'en twee gekozen")
                    continue
                scores[" 5 - Fives"] = sum_of_value(5, u_roll)
            case 6:
                if scores[" 6 - Sixes"] is not None:
                    print("U heeft al 6'en  gekozen")
                    continue
                scores[" 6 - Sixes"] = sum_of_value(6, u_roll)
            case 7:
                if scores[" 7 - 3 of a kind"] is not None:
                    print("U heeft al 6'en  gekozen")
                    continue
                scores[" 7 - 3 of a kind"] = three_of_kind(u_roll)

            case 8:
                if scores[" 8 - 4 of a kind"] is not None:
                    print("U heeft al 6'en  gekozen")
                    continue
                scores[" 8 - 4 of a kind"] = four_of_kind(u_roll)

            case 9:
                if scores[" 9 - Full house"] is not None:
                    print("U heeft al 6'en  gekozen")
                    continue
                scores[" 9 - Full house"] = full_house(u_roll)

            case 10:
                if scores["10 - Small straight"] is not None:
                    print("U heeft al 6'en  gekozen")
                    continue
                scores["10 - Small straight"] = small_straight(u_roll)

            case 11:
                if scores["11 - Large straight"] is not None:
                    print("U heeft al 6'en  gekozen")
                    continue
                scores["11 - Large straight"] = large_straight(u_roll)

            case 12:
                if scores[" 12 - Yahtzee"] is not None:
                    print("U heeft al yahtzee gekozen")
                    continue
                scores[" 12 - Yahtzee"] = five_of_kind_aka_yahtzee(u_roll)

            case 13:
                if scores["13 - Chance"] is not None:
                    print("U heeft al yahtzee gekozen")
                    continue
                scores["13 - Chance"] = chance(u_roll)
        break
