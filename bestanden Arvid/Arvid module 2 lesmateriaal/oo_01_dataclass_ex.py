# Oefening:
# Maak een klasse Persoon met attributen Naam, Voornaam, Geslacht en Lengte
# Maak verschillende objecten van die klasse
# Voeg een attribuut Gewicht toe
# Maak opnieuw een object van de klasse
# Pas nadien het gewicht van die persoon aan.

from dataclasses import dataclass
from decimal import Decimal

@dataclass
class Person:
    name : str
    firstname : str
    gender : str
    length : Decimal

arvid = Person("Claassen", "Arvid", "M", Decimal('1.765'))
print(arvid)

@dataclass
class Person:
    name : str
    firstname : str
    gender : str
    length : Decimal
    weight : Decimal

arvid = Person("Claassen", "Arvid", "M", Decimal('1.765'), weight=Decimal('60'))
print(arvid)
arvid.weight = Decimal('65')  # top secret
