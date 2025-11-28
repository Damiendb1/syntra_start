# We beginnen terug met de class Address
from dataclasses import dataclass


@dataclass
class Address:
    street : str
    number : int
    city : str
    zipcode : str
    country : str

home = Address("Berkenlaan", 2, "Gent", "9090", "België")
print(home)


2# Voor Python is home nu een variable zoals alle andere
# Dat betekent dat je ze kan gebruiken als parameter voor een function.
# Stel we willen weten of een adres in de Benelux ligt,
# m.a.w. is het land van een adres België, Nederland of Luxemburg

BENELUX = ["België", "Nederland", "Luxemburg"]
def in_benelux(address:Address) -> bool:
    """
    Determine if an address is in the Benelux
    :param address: Address to check
    :return: True if in Benelux, False otherwise
    """
    return address.country in BENELUX

print(in_benelux(home))
home.country = "Frankrijk"
print(in_benelux(home))

# De function in_benelux is zeer nauw verwant met de klasse Adress,
# want ze werkt enkel met objecten van de klasse Address.
# De function kan toegevoegd worden aan de klasse Address.
# Het wordt dan een 'class function'.

@dataclass
class Address:
    street : str
    number : int
    city : str
    zipcode : str
    country : str

    def in_benelux(address) -> bool:
        """
        Determine if an address is in the Benelux
        :param address: Address to check
        :return: True if in Benelux, False otherwise
        """
        return address.country in BENELUX

# De function staat nu IN de class Address.
# Het maakt duidelijk aan python de class Address  een functie heeft: 'in_benelux().
# Merk op dat de code van de functie in_benelux() niet gewijzigd is.
home = Address("Berkenlaan", 2, "Gent", "9090", "België")
# We kunnen de function nu oproepen met classname.functionname(object)
print(Address.in_benelux(home))
# Deze function call zegt: in de klasse Address, voer de function in_benelux uit op het object home
# Het wordt echter zelden op deze manier gebruikt.

# python heeft een verkorte schrijfwijze voor
#     classname.functionname(object)
# namelijk:
#     object.functionname()
# toegepast op in_benelux():
#           Address.in_benelux(home)
#                wordt
#           home.in_benelux()
print(home.in_benelux())
hotel = Address(street="Roadstreet", number=11, zipcode='LD34511', city="London", country='UK')
print(hotel)
print(hotel.in_benelux())  # identiek aan: Address.in_benelux(hotel)

# class functions kunnen (net zoals gewone functions) extra parameters hebben
# We schrijven een function full_address die een string teruggeeft met de volledige adres.
# We willen met een parameter aangeven of alles naar hoofdletters omgezet moet worden.
@dataclass
class Address:
    street : str
    number : int
    city : str
    zipcode : str
    country : str

    def in_benelux(address) -> bool:
        """
        Determine if an address is in the Benelux
        :param address: Address to check
        :return: True if in Benelux, False otherwise
        """
        return address.country in BENELUX

    def full_address(address, upper:bool) -> str:
        """
        Generate a full address string
        :param upper: If true the address is returned in upper case
        :return: return full address
        """
        text= (f"""
{address.street} {address.number}
{address.zipcode} {address.city}
{address.country}""")
        if upper:
            return text.upper()
        else:
            return text

hotel = Address(street="Roadstreet", number=11, zipcode='LD34511', city="London", country='UK')
print(hotel)
print(hotel.full_address(upper=True))  # korte versie van Address.full_address(hotel, upper=True)
print(hotel.full_address(upper=False))  # korte versie van Address.full_address(hotel, upper=False)

# Er is nog een belangrijke PEP8 coding regel die tot nog toe genegeerd werd.
# Bij class functions is de eerste parameter altijd het object van de klasse zelf.
# Afspraak / Regel / Verplichting is dat we deze parameter altijd 'self' noemen.
# Zie hoe in onderstaand voorbeeld: de parameter van in_benelux() nu self geworden is.
# Bijgevolg wijzigt de code:
#    return address.country in BENELUX
#    in
#    return self.country in BENELUX
@dataclass
class Address:
    street : str
    number : int
    city : str
    zipcode : str
    country : str

    def in_benelux(self) -> bool:
        """
        Determine if an address is in the Benelux
        :return: True if in Benelux, False otherwise
        """
        return self.country in BENELUX

# oefening1: Voeg een function toe aan Address die bepaalt of het adres in een land ligt
# waar men nederlands spreekt, bv Belgie, Nederland, Zuid-afrika, ...
# Probeer de functie uit.
# Zorg dat alle class functions de naam self gebruiken

# oefening2: Herneem de klasse Person, en voeg een class function salutation toe
# die de string 'beste voornaam familienaam' teruggeeft.
# Zorg dat alle class functions de naam self gebruiken

