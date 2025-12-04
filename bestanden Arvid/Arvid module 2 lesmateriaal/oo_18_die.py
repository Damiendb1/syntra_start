"""
Een praktische applicatie: een class voor een dobbelsteen.
Een dobbelsteen heeft een aantal zijden en kan gegooid worden: to roll a die.
We onthouden de laatst geworpen waarde.
Een dobbelsteen met 6 zijden wordt voorgesteld als
   'D6' - als er nog niet mee geworpen is.
   'D6(2) - met 2 de laatste geworpen waarde.
Twee dobbelstenen zijn aan elkaar gelijk wanneer ze dezelfde waarde hebben geworpen.
De som van twee dobbelstenen is de waarde van hun laatst geworpen waarde.
Een dobbelsteen is fair wanneer elke waarde ongeveer evenveel keer voorkomt.
De vermenigvuldiging van een dobbelsteen met een int (bv. 5) geeft het resultaat van 5 keer rollen met de dobbelsteen
"""

import random
from typing import List


class Die:
    """
    representation of an n-sides die
    """

    def __init__(self, sides: int):
        self._sides = sides  # waarde overgenomen van parameter
        self._last_roll = None

    def __repr__(self):
        if self._last_roll is not None:
            return f"D{self._sides}({self._last_roll})"
        return f"D{self._sides}"

    @property
    def sides(self):
        """
        PropertyName: sides
        """
        return self._sides

    @sides.setter
    def sides(self, sides: int):
        raise AttributeError("sides is read-only")

    @property
    def value(self):
        """Property name: value"""
        return self._last_roll

    @value.setter
    def value(self, sides: int):
        raise AttributeError("value is read-only")

    def _check_nones(self, other):
        if self._last_roll is None:
            raise ValueError("This die has not been rolled yet. ")
        if other.value is None:
            raise ValueError("This die has not been rolled yet. ")

    def __eq__(self, other):
        self._check_nones(other)
        return self._last_roll == other.value

    def __add__(self, other):
        self._check_nones(other)
        return self._last_roll + other.value

    def __radd__(self, other):
        return self._last_roll + other

    def __mul__(self, other):
        if not isinstance(other, int):
            raise TypeError("Can only multiply by an integer")
        res = sum([self.roll() for _ in range(other)])
        return res

    def __rmul__(self, other):
        return self.__mul__(other)

    def roll(self) -> int:
        """
        Roll this die. Store and result the result
        :return: Value of the roll.
        """
        self._last_roll = random.randint(1, self._sides)
        return self._last_roll

    @staticmethod
    def _fair(value, expected):
        """
        Helper function to check if a value is within 10% of the expected value.
        :param value: Value to check
        :param expected: Expected value
        :return: True if within 10% of the expected value, False otherwise
        """
        return expected * 0.9 < value < expected * 1.1

    def is_fair(self, counter: int = 6000) -> bool:
        """
        Verify is a die is fair i.e., has a result distribution that is within 10%.
        :param counter: Number of samples
        :return: True is distribution is within 10%, False otherwise
        """
        res = {side + 1: 0 for side in range(self._sides)}
        expected = counter / self._sides
        for _ in range(counter):
            res[self.roll()] += 1
        dev = [side for side, count in res.items() if not self._fair(count, expected)]
        return len(dev) == 0

    @staticmethod
    def roll_all(dice: List["Die"]) -> List[int]:
        """
        Roll every die in the list.
        :param dice: List of dice
        :return: Roll results of every die
        """
        res = [d.roll() for d in dice]
        return res


# Die is een algemene klasse, waar we specifieke subklassen voor kunnen maken
class Die6(Die):
    def __init__(self):
        super().__init__(6)


class Die20(Die):
    def __init__(self):
        super().__init__(20)


def main():
    d6 = Die(6)
    print(f"{d6.is_fair()=}")
    d6_2 = Die(6)
    print(f"{Die.roll_all([d6, d6_2])=}")
    d4 = Die(4)
    print([d4.roll() for _ in range(10)])

    d8 = Die(8)
    d10 = Die(10)
    d12 = Die(12)
    d20 = Die(20)

    print([d8.roll() for _ in range(10)])
    print([d10.roll() for _ in range(10)])
    print([d12.roll() for _ in range(10)])
    print([d20.roll() for _ in range(10)])

    print(Die.roll_all([d6, d4, d8, d10, d12, d20]))

    print(f"{d6 + d4=}")

    d6 = Die6()
    d20 = Die20()

    for _ in range(10):
        print(f"{3 * d6 +  d20 *2 = }")


if __name__ == "__main__":
    main()
