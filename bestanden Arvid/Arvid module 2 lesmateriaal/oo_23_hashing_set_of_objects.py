# Ter herinnering
# - een set bevat enkel unieke waarden
# - de keys van een dict zijn unieke waarden

import datetime


class Person:

    def __init__(self, name: str, firstname: str, date_of_birth: datetime.date):
        self.name = name
        self.first_name = firstname
        self.date_of_birth = date_of_birth

    def __repr__(self):
        return f"{self.first_name} {self.name} : ({self.date_of_birth})"


p1 = Person("Claassen", "Arvid", datetime.date(1975, 4, 3))
p2 = Person("Simpson", "Homer", datetime.date(1990, 1, 1))
p3 = Person("Simpson", "Homer", datetime.date(1990, 1, 1))

# p2 en p3 zijn identieke personen
# dus als we een set maken met {p2 en p3} dan mag daar maar 1 waarde inzitten.
s = {p2, p3}
print(s)

# p1 en p2 (of p3) zijn niet identieke personen.
s = {p2, p3}
print(s)

# standaard beschouwt Python objecten gelijk als hun id() gelijk
print(f"op basis van id: {p2==p3=}")  # dit is False want p2 en p3 zijn twee totaal verschillende objecten


# Hoewel p2 en p3 dezelfde waardes hebben voor de attributen name, firstname en date_of_birth,
# zijn ze niet gelijk aan elkaar. Person implementeert geen __eq__ dunder.

class Person:
    def __init__(self, name: str, firstname: str, date_of_birth: datetime.date):
        self.name = name
        self.first_name = firstname
        self.date_of_birth = date_of_birth

    def __repr__(self):
        return f"{self.first_name} {self.name} : ({self.date_of_birth})"

    def __eq__(self, other):
        return self.name == other.name and self.first_name == other.first_name and self.date_of_birth == other.date_of_birth


p1 = Person("Claassen", "Arvid", datetime.date(1975, 4, 3))
p2 = Person("Simpson", "Homer", datetime.date(1990, 1, 1))
p3 = Person("Simpson", "Homer", datetime.date(1990, 1, 1))

print(
    f"Op basis van attributen: {p2==p3=}")  # dit is nu True want p2 en p3 worden du vergeleken op basis van hun attributen
# Kan Python nu wel een goede set aanmaken?

try:
    s = {p2, p3}
    print(s)

except TypeError as e:
    print(e)

# Je krijgt een erg specifieke error: cannot use 'Person' as a set element (unhashable type: 'Person')

"""
Volledig ter info:
Hashing is het omzetten data (string, getal of object) naar uniek getal, de hash-waarde
Dit wordt gedaan door een hash-functie.
In Python speelt hashing een belangrijke rol bij het gebruik van collecties zoals `set` en `dict`.
 - set: Om te bepalen of een element al in een set zit.
 - dict: Om snel de waarde te vinden die bij een sleutel (key) hoort.

Dankzij hashing kan Python direct naar de juiste locatie in het geheugen springen zonder 
elk item één voor één te vergelijken.
"""

"""
Je hoeft in deze opleiding niet te weten hoe hashing werkt.
Je moet wel weten dat er een strikte regel is in Python: 
Als twee objecten gelijk zijn (volgens __eq__), moeten ze dezelfde hash-waarde hebben.
Vandaar dat __hash__ dikwijls samen met __eq__ wordt geïmplementeerd.
In quasi alle gevallen volstaat het om __hash__ als volgt te implementeren:

def __hash__(self):
    # Steek alle attributen in een tuple en hash het tuple.
    return hash((self.attr1, self.attr2,  ..., self.attr))
"""


# toegepast op Person geeft dat:

class Person:
    def __init__(self, name: str, firstname: str, date_of_birth: datetime):
        self.name = name
        self.first_name = firstname
        self.date_of_birth = date_of_birth

    def __repr__(self):
        return f"{self.first_name} {self.name} : ({self.date_of_birth})"

    def __eq__(self, other):
        return self.name == other.name and self.first_name == other.first_name and self.date_of_birth == other.date_of_birth

    def __hash__(self):
        return hash((self.name, self.first_name, self.date_of_birth))


# p2 en p3 zijn identieke personen
# dus als we een set maken met {p2 en p3} dan mag daar maar 1 waarde inzitten.

p1 = Person("Claassen", "Arvid", datetime.date(1975, 4, 3))
p2 = Person("Simpson", "Homer", datetime.date(1990, 1, 1))
p3 = Person("Simpson", "Homer", datetime.date(1990, 1, 1))
s = {p2, p3}

print(s)  # eindelijk
s = {p1, p2, p3}
print(s)
p3.name = "Janssens"
s = {p1, p2, p3}
print(s)
