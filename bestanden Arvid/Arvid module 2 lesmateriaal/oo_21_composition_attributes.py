"""
Een klasse kan een andere klasse bevatten
bv. Een persoon woont op een adres
Als een klasse andere klasses omvat is het een goed principe om een methode te voorzien
om de waarde van die attributen aan te passen.
"""
from dataclasses import dataclass
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

# Maar je kan ook een waarde van een andere datatype aan het adres geven
arvid.address = Decimal('1.765')
# Bij het printen van het object zie je dat het adres nu ook wordt weergegeven.
# Dit is hier niet gewenst.
print(arvid)   # arvid.adddress is nu een decimal

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
class DutchAddress(Address):
    def __init__(self, street: str, number: int, zipcode: str, city: str):
        super().__init__(street, number, zipcode, city, "The Netherlands")
        self.check_zip()

    def check_zip(self):
        if len(self.zipcode) != 6 or not self.zipcode[-2:].isalpha():
            raise ValueError("Zipcode must be 4 digits + 2 letters")

dadr= DutchAddress("Kerkplein", 12, "9000VV", "Amsterdam")
arvid.address = dadr
print(arvid)


# Oefening 1
# Maak een class FrenchAdress, waarbij de zip code uit 5 cijfers moet bestaan.

# Oefening 2:
# Maak een class Book met attributen title en author.
# Waarbij author van type Person moet zijn
