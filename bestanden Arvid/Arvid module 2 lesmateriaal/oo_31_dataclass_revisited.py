# We zijn de module OO begonnen met dataclasses.
# dataclasses
# - hebben geen __init__ function nodig
# - objecten zijn gelijk wanneer al hun attributen identiek zijn
# - print() geeft meteen een overzichtelijke output




from dataclasses import dataclass

# Voor een adres is deze data class een goede voorbeeld
# Door @dataclass toe te voegen, voert Python heel wat werk
# voor jou uit.

@dataclass
class Address:
    street : str
    number : int
    zipcode : str
    city : str
    country : str

# bovenstaande clas wordt omgevormd
# in een class van deze vorm, met __init__, __repr__, __eq__, en __hash__

class Address:
    def __init__(self, street, number, zipcode, city, country):
        self.street = street
        self.number = number
        self.zipcode = zipcode
        self.city = city
        self.country = country

    def __repr__(self):
        return f"{self.street}, {self.number}, {self.zipcode}, {self.city}, {self.country}"

    def __eq__(self, other):
        return self.street == other.street and self.number == other.number # ....

    def __hash__(self):
        return hash((self.street, self.number, self.zipcode, self.city, self.country))

    ...

# Wanneer gebruik je dataclass en wanneer een volledig uitgewerkt class?
# Als je objecten alleen maar nodig hebt om waarden in te stockeren
# maar verder niets speciaal wil doen, dan volstaat allicht een dataclass.
# Wanneer werk je beter met een volledige class:
# - Als je properties wil aanmaken, vergelijkingen en operaties wil definiëren
# - Als je met een klasse hiërarchie werkt (polymorfisme)
# - Als jouw klasse meer doet dan data stockeert.

