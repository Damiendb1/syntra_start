"""
Voor een programma moeten we de gegevens van een adres kunnen opslaan
Adres:
    Straatnaam
    Huisnummer
    Postcode
    Woonplaats/Stad
    Land
"""

# we groeperen deze gegevens in een klasse Address.
# Address is de klasse naam.
#     straatnaam, huisnummer, postcode, woonplaats, land zijn 'attributen' van de klasse
#
# Ook hier is PEP8 van toepassing.
#    - klasse namen in het Engels en in CamelCase
#    - attributen in het Engels en in lowercase met underscores

# De eenvoudigste manier om een klasse te maken is met de @dataclass decorator.

from dataclasses import dataclass

@dataclass
class Address:
    pass

# De klasse address is nu gemaakt in de meest eenvoudige vorm.
# @dataclass is een 'class decorator'
# Voor alle voorbeelden die volgen MOET @dataclass erbij staan.
# De werking hiervan zal later duidelijk worden.

# Python kent nu de lege klasse Address
# Lege klasses zijn meestal weinig zinvol.
# We voegen twee attributen toe.

@dataclass
class Address:
    street : str
    number : int

# street, number zijn 'Attributen' van de klasse.
# Een klasse is een beschrijving van hoe python de data moet structureren:
#    - klasse naam
#    - attributen
# Nu weet python wat de structuur van de klasse Address is.

# We gaan objecten van de klasse Address maken.
# Objecten zijn instanties van een klasse, waarbij de
# attributen van een klasse een specifieke waarde krijgen.

ad = Address(street="Kerkplein", number=33)
# ad is nu een object van het type Address.
print(ad)
print(type(ad))
# Om een object te maken van een dataclass
#   variable = ClassName(parameters)   waarbij parameters een oplijsting is
#                                      van de attributen van de klasse

# Dus voor Address moeten de parameters street en number meegegeven worden.
ad1 = Address("Kerkplein", 33)
ad2 = Address(street="Groentenmarkt", number=44)
print(ad1)
print(ad2)

# ad1 en ad2 zijn twee verschillende objecten van de klasse Address.
# Beide objecten hebben dezelfde structuur zoals voor geschreven door de klasse
# maar zitten op een andere plaats in het geheugen.
# Ze hebben een verschillende id.
print(id(ad1))
print(id(ad2))
print(type(ad1))
print(type(ad2))

# We hebben in onze code nu rechtstreeks toegang tot de attributen van een object.
# objectnaam.attributenaam geeft toegang tot de waarde het attribuut 'attribuutnaam'
print(ad1.street)
print(ad2.number)

# je kan de waarde ook wijzigen.
print(ad1)
ad1.street = "Kerkelijk"
print(ad1) # street is nu gewijzigd


# Wanneer de we class Address uitbreiden met de attributen zipcode, city en country
# dan ziet de class er zo uit
@dataclass
class Address:
    street : str
    number : int
    zipcode : str
    city : str
    country : str

# Om een object aan te maken van deze klasse, moeten we ook waardes voorzien voor de nieuwe attributen.
ad1 = Address("Buurtwijk", 20 , "1234AB", "Amsterdam", "Netherlands")
print(ad1)

# Oefening:
# Maak een klasse Persoon met attributen Naam, Voornaam, Geslacht en Lengte
# Maak verschillende objecten van die klasse
# Voeg een attribuut Gewicht toe
# Maak opnieuw een object van de klasse
# Pas nadien het gewicht van die persoon aan.
