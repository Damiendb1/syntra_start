# Stel je hebt een klasse en je wilt bijhouden hoeveel instanties van die klasse er gemaakt zijn.

counter = 0

class Person1:
    def __init__(self, fullname: str):
        global counter
        counter += 1
        self.fullname = fullname


p1 = Person1("Homer")
p1 = Person1("Lisa")
p1 = Person1("Marge")

print("Er zijn",counter, "personen aangemaakt.")

# Het werkt wel, maar als er nog een soortgelijke klass bijkomt moet je weer een counter aanmaken.

counter_a = 0

class Address:
    def __init__(self, street: str):
        global counter_a
        counter_a += 1
        self.fullname = street

a = Address("Kerkplein 1")
a = Address("Kerkplein 2")
print("Er zijn",counter, "personen aangemaakt.")
print("Er zijn",counter_a, "adressen aangemaakt.")

# Het is logischer dat de counter bij de klasse hoort.
# Een klasse zelf kan ook attributen hebben.
# Een klasse attribuut is een attribuut dat tot de klasse behoort en niet tot een specifiek object.
# De waarde van een klasse attribuut is gelijk voor alle objecten.

class Person:
    counter = 0 # Dit is een class attribute

    def __init__(self, fullname: str):
        self.fullname = fullname
        # Je krijgt toegang tot een class attribute via  Classname.attribute
        Person.counter += 1

p1 = Person("Homer")
p2 = Person("Lisa")

print(f"Er zijn",Person.counter, "personen aangemaakt.")
print(f"{p1.counter=}")

Person.counter = 100
print(Person.counter)


# Een voorbeeld van een klasse attribuut in een class hiërarchie

class Dog:
    # Class attribute
    species = "Hond"

    def __init__(self, name, age):
        # Instance attributes
        self.name = name
        self.age = age

class DanishDog(Dog):
    species = "Deense dog"

class DanishLittleDog(DanishDog):
    pass


# All dogs share the same species
dog1 = Dog("Buddy", 3)
dog2 = Dog("Lucy", 5)
ddog1 = DanishDog("Tjorven", 2)
ddog2 = DanishDog("Joppe", 5)
ld = DanishLittleDog("Lassie", 1)

print(dog1.species)
print(dog2.species)
print(ddog1.species)
print(ddog1.species)
print(ld.species)


print("------")

Dog.species = "Canis lupus familiaris"
print(dog1.species)
print(dog2.species)
print(ddog1.species)
print(ddog2.species)
print(ld.species)

DanishDog.species = "Deutsche Dogge"
print(dog1.species)
print(dog2.species)
print(ddog1.species)
print(ddog2.species)
print(ld.species)



