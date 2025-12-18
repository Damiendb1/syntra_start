# Een klasse kan ook bestaan uit een collectie van andere klassen.
# Bijvoorbeeld een hotel bestaat uit kamers
import os
from abc import abstractmethod, ABC


class Room(ABC):
    """
    Abstract base class for rooms
    Any subclass must implement the price_per_night() method
    """

    def __init__(self, number, floor):
        self.number = number
        self.floor = floor
        self._price = self.price_per_night()

    def __repr__(self):
        return f"Room {self.number} on floor {self.floor} costs {self._price} EUR per night"

    def __eq__(self, other):
        return self.number == other.number

    @abstractmethod
    def price_per_night(self) -> int:
        """
        Determine the price per night for this room
        :return: Price per night
        """
        ...


class BasicRoom(Room):
    """
    A basic room costs 120 EUR per night
    """

    def price_per_night(self):
        """
        Determine the price per night for this room
        :return: Price per night
        """
        return 120


class PremiumRoom(Room):
    """
    A premium room costs 250 EUR per night but has a better view
    """

    def price_per_night(self):
        return 250


class Presidential(Room):
    def price_per_night(self):
        return 25000


class Suite(Room):
    """
    A suite costs 400 EUR per night but has a better view and a balcony
    """

    def price_per_night(self):
        return 400


class Excelsior(Room):
    """
    A suite costs 400 EUR per night but has a better view and a balcony
    """

    def price_per_night(self):
        return 1400


class VeryCheap(Room):
    """
    A suite costs 400 EUR per night but has a better view and a balcony
    """

    def price_per_night(self):
        return 40


# De uitleg voor factory methods volgt in een volgende les.
def factory_ifs(room_type, number, floor):
    if room_type == 'B':
        room = BasicRoom(number, floor)
    elif room_type == 'P':
        room = PremiumRoom(number, floor)
    elif room_type == 'S':
        room = Suite(number, floor)
    elif room_type == 'E':
        room = Excelsior(number, floor)
    elif room_type == 'V':
        room = VeryCheap(number, floor)
    else:
        raise ValueError(f"Type {room_type} is niet gekend.")
    return room


FACTORY_DICT = {
    "B": BasicRoom,
    "P": PremiumRoom,
    "E": Excelsior,
    "V": VeryCheap,
    'S': Suite,
    "PR": Presidential
}


def factory_dict(room_type, number, floor):
    target_type = FACTORY_DICT.get(room_type)
    if target_type is None:
        raise ValueError("Room type niet gevonden")
    room = target_type(number, floor)  # BasicRoom(number, floor)
    return room


class Hotel:
    def __init__(self, name: str):
        self.name = name
        self._rooms = []

    def __repr__(self):
        return f"{self.name} ({len(self._rooms)} rooms)"

    def full_description(self):
        rooms = [str(room) for room in self._rooms]
        return self.name + os.linesep + os.linesep.join(rooms)

    @property
    def rooms(self):
        return self._rooms

    def add_room(self, room: Room):
        """Add a room to the hotel"""
        if isinstance(room, Room):
            if room in self._rooms:
                raise ValueError(f"Room {room.number} already exists")
            self._rooms.append(room)
        else:
            raise ValueError("Room must be of type Room")


def main():
    syntra_palace = Hotel("Syntra Palace")
    syntra_palace.add_room(BasicRoom("10", 1))
    syntra_palace.add_room(BasicRoom("11", 1))
    syntra_palace.add_room(BasicRoom("12", 1))
    syntra_palace.add_room(BasicRoom("13", 1))
    syntra_palace.add_room(PremiumRoom("20", 2))
    syntra_palace.add_room(PremiumRoom("21", 2))
    syntra_palace.add_room(PremiumRoom("22", 2))
    syntra_palace.add_room(Suite("30", 3))
    print(syntra_palace)
    print(syntra_palace.full_description())

    # Voeg een bestaande kamer toe

    syntra_palace.add_room(Suite("22", 3))
    print(syntra_palace)


if __name__ == "__main__":
    main()

# Oefening 1A:
# Maak een class Book met attributen title (str), author (Person) en chapters (list of Chapter)
# Een chapter heeft een titel en een aantal pagina's
# Zorg er voor dat enkel Chapters kunnen worden toegevoegd aan een Book.

# Oefening 1B:
# Maak sub klassen van Chapter: Introduction, Conclusion, Index
# Zorg er voor dat een book slechts 1 Introduction, 1 Conclusion en 1 Index kan hebben

# oefening 1C:
# Zorg ervoor dat een introductie steeds vooraan staat, de conclusie steeds achteraan

# oefening 1D
# De index staat ofwel voor de introductie ofwel na de conclusie

# Oefening 1E:
# Zorg er voor dat chapters enkel in stijgende volgorde kunnen worden toegevoegd en dat er geen
# dubbele nummer zijn.
# Maak een class Library met attributen name (str) en books (list of Book)

# Oefening 2:
# Maak een class Library (naam, adres) die een verzameling boeken omvat.
# Boeken mogen meermaals voorkomen.
# Voorzie een function search_book(book_title) die controleert hoeveel keer een boek voorkomt.
