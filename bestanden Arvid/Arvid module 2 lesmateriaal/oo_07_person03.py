class Person:
    """
    Represents a person with a name and an age.
    """
    def __init__(self, name:str, age: int, length: int = 175):
        self.name = name
        self.age = age
        self.length = length

    def __repr__(self):
        return f"Person(name={self.name}, age={self.age})"

# We maken twee personen met dezelfde eigenschappen.
# Eigenlijk gaat het over de zelfde persoon.
a = Person("John", 36, 175)
b = Person("John", 36, 175)

print(f"{a} == {b} : {a==b}")
# om te controleren of twee personen hetzelfde zijn, kunnen we aan python duidelijk maken hoe == werkt
# voor twee objecten van persoon.

# Hoe werkt == in python?
# Als python ergens a == b tegenkomt, dan wordt onderliggend (en onzichtbaar) deze code gegenereerd:
#  a.__eq__(b)
#  b == a   wordt dan:  b.__eq__(a)
# Elke class heeft altijd een __eq__ methode die een bool retourneert.
# Als een class __eq__ niet expliciet invult, dan zal python  a == b interpreteren als id(a) == id(b)

a = 3
b = 3
print(f"{a=} == {b=} : {a==b=}")
print(f"{a=} == {b=} : {a.__eq__(b)=}")
b = 2

print(f"{a=} == {b=} : {a==b=}")
print(f"{a=} == {b=} : {a.__eq__(b)=}")



a = Person("John", 36, 175)
b = Person("John", 36, 175)
print(f"{a} == {b} : {a==b}")  # False
a = b  # a wijst nu ook naar b, id(a) == id(b)
print(f"{a} == {b} : {a==b}")  # True


#Stel dat op de wereld geen twee personen bestaan met dezelfde naam, leeftijd en lengte,
# dan kunnen we __eq__ als volgt toevoegen:
class Person:
    """
    Represents a person with a name and an age.
    """
    def __init__(self, name:str, age: int, length: int = 175):
        self.name = name
        self.age = age
        self.length = length

    def __repr__(self):
        return f"Person(name={self.name}, age={self.age})"

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age and self.length == other.length

a = Person("John", 36, 175)
b = Person("John", 36, 175)
print(f"{id(a)=} == {id(b)=} : {id(a)==id(b)=}")
print(f"{a=} == {b=} : {a==b=}")

# We kennen nu al drie dunder function van een class
#  __init__, __repr__ en __eq__