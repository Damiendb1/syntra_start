# Deze dunder methodes hebben we al gezien: __init__, __str__, __repr__, __equal__
# Er zijn nog nuttige dunder methods

from decimal import Decimal


# Maak een klasse die een gewicht in gram weergeeft.

class Gram:
    """
    Class to represent a weight in grams
    """

    def __init__(self, value: Decimal = Decimal(0)):
        self.value = value

    def __repr__(self) -> str:
        if self.value is None:
            return "None"
        return f"{self.value:_}g"

    def __eq__(self, other):
        return self.value == other.value


weight = Gram(Decimal('250.3'))
print(weight)
w2 = Gram(Decimal('250.3'))
print(f"{weight == w2=}")
w3 = Gram(Decimal('25'))
print(f"{w2 == w3=}")

# We willen nu weten of w2 minder weegt dan w3
# Onderstaande code faalt
try:
    if w2 < w3:
        print("w2 weegt minder dan w3")
    else:
        print("w3 weegt minder dan w2")
except TypeError as e:
    print("Probleem met vergelijking tussen {w2} en {w3}: e")

# Python weet niet hoe twee objecten van de class Weight vergeleken moeten worden
# Hiervoor dienen de dunder methods:
# __eq__:  equal
# __ne__: not equal
# __lt__: less than / kleiner dan
# __le__: less or equal / kleiner of gelijk aan
# __gt__: greater than / groter dan
# __ge__: greater or equal / groter of gelijk aan

class Gram:
    """
    Class to represent a weight in grams
    """

    def __init__(self, value: Decimal = Decimal(0)):
        self.value = value

    def __repr__(self) -> str:
        if self.value is None:
            return "None"
        return f"{self.value:_}g"

    def __eq__(self, other):
        return self.value == other.value

    def __lt__(self, other):
        return self.value < other.value

    def __le__(self, other):
        return self.value <= other.value

    def __gt__(self, other):
        return self.value > other.value

    def __ge__(self, other):
        return self.value>= other.value

    def __ne__(self, other):
        return not self.__eq__(other)

w1 = Gram(Decimal('250.3'))
print(weight)
w2 = Gram(Decimal('250.3'))
print(f"{weight == w2=}")
w3 = Gram(Decimal('25'))
print(f"{w2 == w3=}")
print(f"{w1 < w2=}")
print(f"{w1 <= w2=}")
print(f"{w1 <= w3=}")
print(f"{w1 > w3=}")
print(f"{w1 >= w3=}")
print(f"{w1 != w3=}")
print(f"{w1 != w2=}")

# Het is niet altijd zinvol om __lt__, __gt__ enz. te implementeren.
# Wat betekent adres_1 < adres_2? Weinig zinvol, dus hoeven we in de class Address __lt__ e.d. niet te implementeren.
# Wat betekent person1 >= persoon2? Ook hier is dat weinig zinvol



#
# def __bool__(self):
#     return bool(self.value)
#
#
#
# def __add__(self, other):
#     return self.__class__((self.weight_in_grams() + other.weight_in_grams()) / self.factor())
#
# def __sub__(self, other):
#     return self.__class__((self.weight_in_grams() - other.weight_in_grams()) / self.factor())
#
# def __eq__(self, other):
#     return self.weight_in_grams() == other.weight_in_grams()
#
#
#


from decimal import Decimal
from abc import ABC, abstractmethod


class Weight(ABC):
    """
    Generic class to represent a weight
    The implied unit is g
    """

    def __init__(self,
                 value: Decimal = Decimal(0),
                 unit: str = "g",
                 factor: Decimal = Decimal(1)) -> None:
        self.value = value

    def __repr__(self) -> str:
        if self.value is None:
            return "None"
        return f"{self.value:_}{self.unit()}"

    @abstractmethod
    def factor(self):
        pass

    @abstractmethod
    def unit(self):
        pass

    def weight_in_grams(self):
        return self.value * self.factor()

    def __add__(self, other):
        return self.__class__((self.weight_in_grams() + other.weight_in_grams()) / self.factor())

    def __sub__(self, other):
        return self.__class__((self.weight_in_grams() - other.weight_in_grams()) / self.factor())

    def __eq__(self, other):
        return self.weight_in_grams() == other.weight_in_grams()

    def __lt__(self, other):
        return self.weight_in_grams() < other.weight_in_grams()

    def __le__(self, other):
        return self.weight_in_grams() <= other.weight_in_grams()

    def __gt__(self, other):
        return self.weight_in_grams() > other.weight_in_grams()

    def __ge__(self, other):
        return self.weight_in_grams() >= other.weight_in_grams()

    def __ne__(self, other):
        return not self.__eq__(other)

    def __bool__(self):
        return bool(self.value)


class Gram(Weight):
    def factor(self):
        return Decimal(1)

    def unit(self):
        return "g"


class Kilo(Weight):
    """
    Representation of a weight in kilograms
    """

    def factor(self):
        return Decimal(1000)

    def unit(self):
        return "kg"


w2 = Kilo(Decimal('250'))
print(w2)


class Ton(Weight):
    """
    Representation of a weight in kilograms
    """

    def factor(self):
        return Decimal(1000_000)

    def unit(self):
        return "kg"


class Ounce(Weight):
    def factor(self):
        return Decimal('28.349523125')

    def unit(self):
        return "oz"


class Pound(Weight):
    def factor(self):
        return Decimal('453.59237')

    def unit(self):
        return "lb"


class Stone(Weight):
    def factor(self):
        return Decimal('6350.29318')

    def unit(self):
        return "lb"


w3 = Ton(Decimal('12'))
print(w3)
print(w2.weight_in_grams())
print(w3.weight_in_grams())

print(w3 + w2)
print(w2 + w3)
print(w1 + w3)
print(w3 + w1)

w5 = Kilo(Decimal('1'))
w4 = Ounce(Decimal('1'))
print(w5 + w4)
print(w4 + w5)
