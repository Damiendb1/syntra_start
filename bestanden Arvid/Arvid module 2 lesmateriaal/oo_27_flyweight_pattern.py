# Het flyweight pattern is een factory pattern waarbij wordt geprobeerd om zo weinig mogelijk identieke objecten
# te maken.

class Address:
    prev = {}

    def __init__(self, street: str, number: int):
        self.street = street
        self.number = number

    def __repr__(self):
        return f"{self.street} {self.number}"


class Person:
    def __init__(self, name: str, address: Address):
        self.name = name
        self.address = address

    def __repr__(self):
        return f"{self.name} lives at {self.address}"


p1 = Person("Homer", Address("Kattenbergstraat", 12))
p2 = Person("List", Address("Kattenbergstraat", 12))

print(p1)
print(p2)
print("Zijn de adressen gelijk? ", id(p1.address) == id(p2.address))

# We voegen aan de class Address en class attribute prev toe van het type dict
# We maken een factory class die op basis van een street en number een address object maakt.
# Vooraleer we een nieuw object aanmaken, controleren we het al bestaat.
# Zonee, maak een nieuw object aan en stockeer het in class variable prev.
# Zoja, retourneer dan het bestaande object: class variable prev.


def get_address(street: str, number: int):
    key = street + str(number)
    if key in Address.prev:
        return Address.prev[key]
    else:
        address = Address(street, number)
        Address.prev[key] = address
        return address


p1 = Person("Homer", get_address("Kattenbergstraat", 12))
p2 = Person("Lisa", get_address("Kattenbergstraat", 12))

print(p1)
print(p2)
print("Zijn de adressen gelijk? ", id(p1.address) == id(p2.address))

