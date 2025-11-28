# Oefening: Herwerk de dataclass Address naar een echte python class zonder @dataclass
# - verwijder @dataclass
# - maak een class function __str__ aan
# - maak een class function __repr__ aan
# Maak een paar adressen aan en print ze.

class Address:
    def __init__(self, street:str, number:int, city:str, zipcode:str, country:str):
        self.street = street
        self.number = number
        self.zipcode = zipcode
        self.city = city
        self.country = country

    def __str__(self):
        return f"{self.street} {self.number} {self.zipcode} {self.city} {self.country}"

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


hotel = Address(street="Roadstreet", number=11, zipcode='LD34511', city="London", country='UK')
print(hotel)
