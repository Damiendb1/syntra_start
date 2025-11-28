class Person:
    """
    Represents a person with a name and an age.
    """

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person(name={self.name}, age={self.age})"

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    def __lt__(self, other):
        return self.age < other.age

    def salute(self):
        print(f"Beste {self.name}")

    def is_adult(self):
        """
        Determines if the individual is considered an adult based on their age.
        :return: A boolean value indicating if the individual is an adult (True) or
        """
        return self.age >= 18

    def verify_age(self) -> None:
        if not isinstance(self.age, int):
            raise ValueError("Age must be an integer")
        if 0 <= self.age <= 120:
            raise ValueError("Age must be between 0 and 120")


a = Person("John", "Thirty")
a.salute()


# We willen een programma maken waarbij onderscheid wordt gemaakt
# tussen personen en VIPs.
# Een VIP heeft net zoals een persoon een naam en leeftijd.
# Het grote verschil is dat een VIP met meet stijl wordt aangesproken.
# Voor de rest is een VIP een Person, of nog VIP is een specifiek subtype van Person.

# We kunnen in Python een sub-classe maken van een ander klasse.
# VIP is een subklasse van Person.
# Person is de superclass van VIP

# JE maakt een klasse X een subclass van Y door de naam van Y te
# te vermelden na de definitie van X.
class Y:
    pass


class X(Y):
    # Y is superclass van X
    # X is subclass van Y
    pass


# voor een VIP ziet dat er als volgt uit
class VeryImportantPerson(Person):
    pass


# De class VIP erft alle functies en attributen over van Person

p = Person("Arvid", 50)
v = VeryImportantPerson("Homer", 39)
print(p)
print(p.__class__.__mro__)
print(v)
print(v.__class__.__mro__)

# Zet een breakpoint in Persion.is_adult
# Als je onderstaande code debugt, zal je zien dan v.is_adult()
# de code van de class Person uitvoert.

print(v.is_adult())


# Op dit moment is er functioneel geen verschil tussen VIP en Person.
# Maar wij definiëren ene VIP als iemand die met meer respect moet worden
# aangesproken.
# Het verschil tussen VIP en Person wordt bepaald door wat er function salute() print

class VeryImportantPerson(Person):
    def salute(self):
        print(f"Weledele {self.name}")


# Een VIP is nu identiek aan een persoon, behalve de begroeting

p = Person("Arvid", 50)
v = VeryImportantPerson("Homer", 39)
p.salute()
v.salute()


# Oefening: Pas ook __str__ of __repr__ aan zodat er 'VIP(naam, leeftijd)' geprint wordt
class VeryImportantPerson(Person):
    def salute(self):
        print(f"Weledele {self.name}")

    def __repr__(self):
        return f"VIP({self.name}, {self.age})"


# Een subklasse is instantie van de eigen klasse én van de superclass

persons = [
    Person("Arvid", 50),
    VeryImportantPerson("Homer", 39),
    Person("Jane", 15),
    VeryImportantPerson("Bart", 13),
    Person("Bob", 19),
    Person("Els", 45)
]

print(persons)

for p in persons:
    p.salute()

adults = [p for p in persons if p.is_adult()]
print(adults)

vips = [p for p in persons if isinstance(p, VeryImportantPerson)]
print(vips)

#  wat druk deze code af en waarom?
persons = [p for p in persons if isinstance(p, Person)]  # [p for p in persons if p.age > 30]
print(persons)

# Oefening 1:
# Maak een klasse Employee met als attributen name: string, date_of_birth: datetime;
# departement: str en salary: Decimal.
# Zorg dat init, repr, eq in orde zijn
# Zorg voor een function promote die het salaris van een employee verhoogt met 5%.
# Maak een subklasse Manager van Employee met function promote die het salaris verhoogt met 10%, zorg
# dat repr in orde is
# Uitbreiding
# Maak een subklasse CEO van Manager met function promote die het salaris verhoogt met 15%.
# Zorg dat repr in orde is

