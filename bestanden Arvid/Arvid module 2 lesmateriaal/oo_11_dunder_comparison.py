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

    def __init__(self, value: str | Decimal = Decimal(0)):
        if isinstance(value, str):
            value= Decimal(value)
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

# Oefening 1: Maak een class Car(Brand, Price)
# Zorg ervoor dat auto's met elkaar vergeleken kunnen worden op basis van de prijs.
