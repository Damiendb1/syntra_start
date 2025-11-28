# door @dataclass voor de class te zetten doet python een aantal onzichtbare stappen
# die we als programmeur meestal zelf willen doen.
# - Het invullen van de class attributes
# - Weergeven hoe een object geprint moet worden.
from decimal import Decimal


# We hernemen de klasse Person, maar nu zonder @dataclass
# Dat betekent dat we zelf een moeten bepalen met welke parameters een object kan worden gemaakt.
# en in welke attributen die parameters gestockeerd worden.
# Dit gebeurt via de __init__ functie.
# De naam moet exact __init__ zijn met twee underscores voor en na de naam.
# __init__ is een dunder function, zoals we er nog een hele reeks gaan zien.
# dunder staat voor 'double underscore'.
# In spreektaal wordt __init__ dan dunder-init genoemd,
# ipv underscore, underscore, init, underscore, underscore

# Onderstaande class is geen dataclass meer maar een echte Python class
# De attributen worden langer opgesomd in de klasse maar aangemaakt in __init__
# De __init__ functie heeft typisch een parameter voor elk attribuut in de klasse.
# __init__ heeft ook de parameter self om aan te geven over welk object het gaat.
class Person:

    def __init__(self,
                 name:str,
                 firstname:str,
                 sex:str,
                 length:Decimal,
                 weight:Decimal):
        # onderstaande lijn maakt het attribuut self.naam aan voor het object
        # en geeft attribuut de waarde van de parameter name
        self.name = name
        self.firstname = firstname

        # de naam van de parameter en de naam van het attribuut
        # moeten niet hetzelfde zijn.
        # De parameter is sex en de waarde stockeren we in het attribuut gender.
        self.gender = sex

        self.length = length
        self.weight = weight

    def salutation(self):
        """
        Generate a salutation string
        """
        return f"Beste {self.firstname} {self.name}"

# Een object van de class Person aanmaken gebeurt nu als volgt (identiek als voorheen)
arvid = Person(name="Arvid", firstname="Claassen", sex ="M",
               length=Decimal('1.765'), weight=Decimal('65.4'))
# Merk op dat we het geslacht meegeven met de parameter sex
# maar als we het geslacht van een persoon willen weten, we het attribuut gender gebruiken.
# Dat komt omdat in __init__ we  de parameter sex  in het attribuut gender stockeren.
print(arvid.gender)
# print(arvid.sex)  #dit zal niet werken, want sex is geen attribuut
print(arvid.salutation())

# @dataclass vertelt ook aan python hoe hij een object moet printen.
# als we @dataclass niet vermelden valt python terug op een technische print
print(arvid) # technische voorstelling van het object.

# We moeten in de class expliciet aangeven in welk formaat we het object willen printen.
# Dit doen we met de class function __str__(), wederom een dunder function.

# We voegen __str__ toe.
class Person:
    def __init__(self,
                 name:str,
                 firstname:str,
                 sex:str,
                 length:Decimal,
                 weight:Decimal):
        self.name = name
        self.firstname = firstname
        self.gender = sex
        self.length = length
        self.weight = weight

    def __str__(self):
        return (f"Persoon-object(naam:{self.name}, voornaam:{self.firstname}, geslacht:{self.gender}, "
                f"lengte:{self.length}, gewicht:{self.weight})")

    def salutation(self):
        """
        Generate a salutation string
        """
        return f"Beste {self.firstname} {self.name}"

arvid = Person(name="Arvid", firstname="Claassen", sex ="M",
               length=Decimal('1.765'), weight=Decimal('65.4'))

print(arvid) #de output is nu wel mooi geformatteerd.

# Oefening: Herwerk de dataclass Address naar een echte python class zonder @dataclass
# - verwijder @dataclass
# - maak een class function __str__ aan
# - maak een class function __repr__ aan
# Maak een paar adressen aan en print ze. 