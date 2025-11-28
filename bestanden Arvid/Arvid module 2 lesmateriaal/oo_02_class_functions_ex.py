
# oefening1: Voeg een function toe aan Address die bepaalt of het adres in een land ligt
# waar men nederlands spreekt, bv Belgie, Nederland, Zuid-afrika, ...
# Probeer de functie uit.
# Zorg dat alle class functions de naam self gebruiken

# oefening2: Herneem de klasse Person, en voeg een class function salutation toe
# die de string 'beste voornaam familienaam' teruggeeft.
# Zorg dat alle class functions de naam self gebruiken

from dataclasses import dataclass
from decimal import Decimal


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

    def full_address(self, upper:bool) -> str:
        """
        Generate a full address string
        :param upper: If true the address is returned in upper case
        :return: return full address
        """
        text= (f"""
{self.street} {self.number}
{self.zipcode} {self.city}
{self.country}""")
        if upper:
            return text.upper()
        else:
            return text

    def dutch_speaking(self) -> bool:
        """
        Determine if the address is in a dutch speaking country
        :return: True if in dutch speaking country, False otherwise
        """
        return self.country in ["België", "Nederland", "Zuid-Afrika"]


# oefening2: Herneem de klasse Person, en voeg een class function salutation toe
# die de string 'beste voornaam familienaam' teruggeeft.
@dataclass
class Person:
    name : str
    firstname : str
    gender : str
    length : Decimal
    weight : Decimal

    def salution(self):
        """
        Generate a salutation string
        """
        return f"Beste {self.firstname} {self.name}"

arvid = Person("Arvid", "Claassen", "M", Decimal('1.765'), Decimal('65.4'))
print(arvid.salution())

