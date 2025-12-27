# Soms heb je variabelen nodig zonder dat hun waarde van belang is.
# Bijvoorbeeld:
#       deur status: een deur is open, dicht, op slot.
#       kleding maat: S, M, L, XL,..

# python heeft hiervoor de class Enum

from enum import Enum, unique, auto

# Als je waarden wil groeperen onder hetzelfde type, maak
# dan een nieuwe class met daarin de opsomming van alle variabelen, die overerft van Enum

class ClothingSize(Enum):
    """
    De waardes 1, 2, 3, 4 zijn eigelijk niet relevant
    """
    S = 1
    L = 2
    M = 3
    XL = 4

# je kan clothing size nu gebruik als een datatype

class Shirt:
    def __init__(self, size: ClothingSize):
        self._size = size

    @property
    def size(self):
        return self._size
    @size.setter
    def size(self, value):
        if isinstance(value, ClothingSize):
            self._size = value
        else:
            raise TypeError("Value must be of type ClothingSize")

# De decorator @unique forceert dat de waardes in een enum uniek zijn.
# Pycharm zal geen opmerkingen maken op onderstaande class
# maar python zal bij uitvoering van wel een exception raisen.
@unique
class Sizes:
    Large = 1
    Medium = 1

# Wanneer de waardes die je toekent aan de items van een enum niet relevant zijn
# dan kan je met auto() waardes aanmaken

@unique
class DoorType(Enum):
    OPENED = auto()
    CLOSED = auto()
    LOCKED = auto()


class Door:
    """
    Class for a door
    """

    def __init__(self, number: int):
        self.number = number
        # We veronderstellen dat een deur steeds start in status open.
        # We maken status protected door er een _ onder te zetten.
        self._status = DoorType.OPENED

    def __repr__(self):
        return f"Door {self.number} is {self._status.name} ({self._status.value})"

    def is_status(self, status: DoorType):
        return self._status == status

    # de toestand kan wel opgevraagd worden
    @property
    def toestand(self):
        return self._status

    # de toestand mag niet gewijzigd worden
    @toestand.setter
    def toestand(self, value):
        if isinstance(value, DoorType):
            self._status = value
        else:
            raise TypeError("Value must be of type Doortype")

    def open(self):
        """
        You can open a door when it is not DoorType.LOCKED
        """
        if self._status == DoorType.OPENED:
            return
        if self._status == DoorType.CLOSED:
            self._status = DoorType.OPENED

        if self._status == DoorType.LOCKED:
            self._status = DoorType.LOCKED

    def close(self):
        if self.toestand == DoorType.OPENED:
            self._status = DoorType.CLOSED
        if self._status == DoorType.CLOSED:
            return
        if self._status == DoorType.LOCKED:
            self._status = DoorType.LOCKED

    def lock(self):
        if self.toestand == DoorType.OPENED:
            return
        if self._status == DoorType.CLOSED:
            self._status = DoorType.LOCKED
        if self._status == DoorType.LOCKED:
            self._status = DoorType.LOCKED



    def __lt__(self, other):
        # number is een publiek (niet-protected) class attribute
        # zowel self als other hebber en toegang toe.
        return self.number < other.number

    def __eq__(self, other):
        # Stel dat twee deuren gelijk zijn als het toestand gelijk is
        # _status is protected. Enkel self heeft er toegang toe
        return self.toestand > other.toestand  # ==> Dit is correct
        # return self._status > other.toestand  # ==> Dit is correct maar ziet er raar uit
        # return self._status > other._status  # Dit hoort niet.  You SHOULD not do this.


d = Door(4)
print(d)
print(d.is_status(DoorType.OPENED))
d.close()
print(d.is_status(DoorType.OPENED))


# de items van een enum hebben ook attributen, zoals name en value
for v in DoorType:
    print(v.name, ':', v.value)


# opdracht:
# - maak twee enums:
#        Gender voor man, vrouw of x
#        Title: voor cursist of docent
# - lees het cursisten bestand in als een list of list
# - geslacht 'M', 'V' en 'X' moeten de  juiste Gender-enum waarde worden
# - 'Cursist' en 'Docent' moeten de juiste Title-enum waarde worden
