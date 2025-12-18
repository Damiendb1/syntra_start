"""
Een klasse kan een andere klasse bevatten
bv. Een persoon woont op een adres
Als een klasse andere klasses omvat is het een goed principe om een methode te voorzien
om de waarde van die attributen aan te passen.
"""
from decimal import Decimal


class Person:
    def __init__(self, name: str):
        self.name = name
        self.address = None

    def __repr__(self):
        suffix = "" if self.address is None else f" lives at {self.address}"
        return f"{self.name}{suffix}"


class Address:
    def __init__(self, street: str, number: int, zipcode: str, city: str, country: str):
        self.street = street
        self.number = number
        self.zipcode = zipcode
        self.city = city
        self.country = country

    def __repr__(self):
        return f"{self.street} {self.number} {self.zipcode} {self.city} {self.country}"


# Maak een object aan van de klasse Person
arvid = Person("Arvid Claassen")
print(arvid)
# Maak een adres aan
adr = Address("Kerkplein", 12, "9000", "Gent", "Belgium")
# Pas het attribuut address aan op het object arvid
arvid.address = adr
# dit heeft een gewenst effect.
# Bij het printen van het object zie je dat het adres nu ook wordt weergegeven
print(arvid)
# object arvid (van type Person) bevat nu een object adr (van type Address)


# Maar je kan ook een waarde van een ander datatype aan het attribute adres geven
arvid.address = Decimal('1.765')
# Bij het printen van het object zie je dat het adres nu ook wordt weergegeven.
# Dit is hier niet gewenst.
print(arvid)  # arvid.adddress is nu een decimal


# Het is een good practice om voor attributen van een bepaalde klasse,
# een method toe te voegen om de waarde goed te zetten.
# Dikwijls kan dit via een property


class Person:
    def __init__(self, name: str):
        self.name = name
        self._address = None

    def __repr__(self):
        suffix = "" if self._address is None else f" lives at {self._address}"
        return f"{self.name}{suffix}"

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        if isinstance(value, Address):
            self._address = value
        else:
            raise ValueError("Address must be an Address object")


# Maak een object aan van de klasse Person
arvid = Person("Arvid Claassen")
print(arvid)
# Maak een adres aan
adr = Address("Kerkplein", 12, "9000", "Gent", "Belgium")
# Pas het attribuut address aan op het object arvid met de voorgeschreven property
arvid.address = adr

# dit heeft een gewenst effect.
# Bij het printen van het object zie je dat het adres nu ook wordt weergegeven
print(arvid)

# En je kan nu geen ander datatype aan het adres geven
try:
    arvid.address = Decimal('1.765')
except ValueError as e:
    print(e)


# Het blijft ook werken voor sub klassen van Address
# Hieronder staan twee bijna identieke classes.
# DutchAddress en DutchAddressWithOtherCheck

# In DutchAddress wordt self.check_zip() opgeroepen om te controleren of
# de structuur van zipcode ok is. Zoniet wordt een ValueError gegooid.

class DutchAddress(Address):
    def __init__(self, street: str, number: int, zipcode: str, city: str):
        super().__init__(street, number, zipcode, city, "The Netherlands")
        self.check_zip()

    def check_zip(self):
        if (len(self.zipcode) != 6 or
                not self.zipcode[:4].isnumeric() or
                not self.zipcode[-2:].isalpha()):
            raise ValueError("Zipcode must be 4 digits + 2 letters")


# In DutchAddressWithOtherCheck wordt ook self.check_zip() opgeroepen
# om te controleren of de structuur correct is.
# Hier retourneert check_zip True or False.
class DutchAddressWithOtherCheck(Address):
    def __init__(self, street: str, number: int, zipcode: str, city: str):
        super().__init__(street, number, zipcode, city, "The Netherlands")
        if not self.check_zip():
            raise ValueError("Zipcode must be 4 digits + 2 letters")

    def check_zip(self) -> bool:
        return (len(self.zipcode) == 6
                and self.zipcode[:4].isnumeric()
                and self.zipcode[-2:].isalpha())


# Vraag: welke aanpak is het best? of nog: welke methode is het best om te controleren
# of de waarde die aan __init__() wordt aangeboden correct zijn?

dadr = DutchAddress("Kerkplein", 12, "9000VV", "Amsterdam")
arvid.address = dadr
print(arvid)


# Antwoord: quasi altijd is de aanpak in de tweede klasse DutchAddressWithOtherCheck
# beter. De function get_zip() blijft zo enkel verantwoordelijk om te controleren
# of de structuur goed is. Het is de verantwoordelijkheid van de oproepende
# function (hier __init()__) om te beslissen wat er moet gebeuren. Doorgaan of een
# exception gooien.


# Oefening 1
# Maak een class FrenchAdress, waarbij de zip code uit 5 cijfers moet bestaan.

# Oplossing:
class FrenchAddress(Address):
    def __init__(self, street: str, number: int, zipcode: str, city: str):
        super().__init__(street, number, zipcode, city, "The Netherlands")
        if not self.check_zip():
            raise ValueError("Zipcode must be 5 digits")

    def check_zip(self) -> bool:
        return len(self.zipcode) == 5 and self.zipcode.isnumeric()


# Oefening 2:
# Maak een class Book met attributen title en author.
# Waarbij author van type Person moet zijn

# Oplossing
writer = Person("Homer Simpsons")


class Book:
    def __init__(self, author: Person, title: str):
        self._author = author
        self.title = title

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if isinstance(value, Person):
            self._author = value
        else:
            raise ValueError("Author must be a Person object")
