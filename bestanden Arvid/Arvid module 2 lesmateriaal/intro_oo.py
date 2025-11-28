from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal


# om een klasse te definieren: keyword class gevolgd door de naam van de klasse.
# PEP8: klasse namen in CamelCase

@dataclass
class Address:
    street : str
    number : int
    city : str
    zipcode : str

home = Address("Bollnaamstraat", 1, "Amsterdam", "1234AB")

@dataclass
class Person:
    name : str
    gender : str
    address : Address
    zipcode: str
    length : Decimal
    date_of_birth : datetime

# om een instantie van een klasse te maken: de naam van de klasse gevolgd door ()
# arvid = object
arvid = Person(name="Arvid",
               gender="M",
               address=home,
               zipcode="1234AB",
               length=Decimal('1.765'),
               date_of_birth= datetime(1975, 4, 3))


jan = Person("Jan", "v", "Bollna ", "123", Decimal('1.65'), datetime(1975, 4, 3))
print(type(arvid))
print(arvid)
print(" Naam: " ,arvid.name)
print("Adres: ", arvid.address)
print("Huisnummer", arvid.address.number)
print("Huisnummer * ", arvid.address.number * 2)
print("geboorte jaar:", arvid.date_of_birth.year)
arvid2 = Person(name="Arvid",
               gender="M",
               address=home,
               zipcode="1234AB",
               length=Decimal('1.765'),
               date_of_birth= datetime(1975, 4, 3))

print(arvid2)
print(arvid == arvid2)
arvid.length = Decimal('1.74')
print(arvid == arvid2)



@dataclass
class Response:
    id_ : int
    start_time : str
    submit_time : str
    number : str
    colour : str
    place : str
    q_word : str

    def get_submit_date(self):
        val = self.submit_time.split(' ')[0]
        return val if val else None

    def get_decimal_number(self):
        try:
            return Decimal(self.number.replace(",","."))
        except:
            return None

    def real_q_word(self):
        return 'Q' in self.q_word.upper()


# resp = Response(id_=1,
#                 start_time="2023-01-01 12:00:00",
#                 submit_time="2023-01-01 12:00:00",
#                 number="123",
#                 colour="yellow",
#                 place="Gent",
#                 q_word="Quiz")
# print(type(resp))
# print(resp)
# print(resp.id_)
# resp.colour='geel'
# print(resp.colour)
#
# exit()


@dataclass
class Response:
    id_ : int
    start_time : str
    submit_time : str
    number : str
    colour : str
    place : str
    q_word : str

    def get_submit_date(self):
        val = self.submit_time.split(' ')[0]
        return val if val else None

    def get_decimal_number(self):
        try:
            return Decimal(self.number.replace(",","."))
        except:
            return None

    def real_q_word(self):
        return 'Q' in self.q_word.upper()


resp = Response(id_=1,
                start_time="2023-01-01 12:00:00",
                submit_time="2023-01-01 12:00:00",
                number="123",
                colour="yellow",
                place="Gent",
                q_word="Quiz")
print(type(resp))
print(resp)
print(resp.id_)
resp.colour='geel'
print(resp.colour)

# oefening
# Schrijf een klasse Name met een attributen naam, voornaam, aanspreking
# Maak twee objecten van die objecten.
# Voeg een class function FullName()
# toe die "Beste aanspreking naam voornaam" teruggeeft.
