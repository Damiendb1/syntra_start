"""
Python is een object georiënteerde programmeertaal.
Dat betekent dat je objecten kan maken met bijbehorende data en operaties.

We hebben al heel wat objecten gemaakt
s = set()
l = [] # lst
now = datetime.now()  # date
f = open("d:/dev/test.txt", "w")

datetime is een datatype/klasse/class.
now is een instance/object van de class datetime.
"""


# We kunnen ook zelf een class maken.
# De naamgeving is CamelCase: Engels, verschillende woorden gescheiden met hoofdletter
class Person:
    pass


p = Person()
print(p)
print(type(p))


# Je hebt zonet een class Person gemaakt en er een object p van geïnstantieerd.
# Een lege class heeft meestal weinig zin.

# Een persoon heeft een naam en een leeftijd.
# Om dat in python duidelijk te maken, gebruik je de function __init__.
# De __init__ functie wordt aangeroepen als je een object van de class Person maakt.
# De dubbele underscores voor en na de naam geven aan dat het een speciale function
# De parameter self is een wijzer naar het object dat je aan het maken bent.


class Person:
    def __init__(self):
        self.name = "Arvid"
        self.age = 50


arvid = Person()
print(arvid.name)
print(arvid.age)

# de ingebouwde functie vars toont alle attributen van een object.
print(vars(arvid))

# We noemen name en age attributen van de class Person.
# We kunnen deze attributen ook wijzigen.
arvid.age = 40
print(arvid.age)

# We kunnen meerdere objecten van Person maken
p2 = Person()
p2.name = "Homer"
p2.age = 30
print(vars(p2))
print()


# Willen we de lengte van een persoon ook bijhouden,
# dan moeten we het attribuut toevoegen in de __init__ functie.
class Person:
    def __init__(self):
        self.name = "Arvid"
        self.age = 50
        self.length = 176


arvid = Person()
print(vars(arvid))

print(arvid)  # geeft <__main__.Person object at 0x000001.....>


# We kunnen bij een class aangeven hoe ze geprint moeten worden.
# We voegen de __repr__ functie toe. repr staat voor  representation.

class Person:
    def __init__(self):
        self.name = "Arvid"
        self.age = 50
        self.length = 176

    def __repr__(self):
        return f"Person(naam:{self.name}, leeftijd:{self.age}, lengte={self.length})"


arvid = Person()
homer = Person()
homer.name = "Homer"
homer.age = 30
homer.length = 164
print(arvid)
print(homer)


# Om te vermijden dat je telkens zelf de attributen voor Homer moet
# goed zetten, geven we parameters aan __init__

class Person:
    def __init__(self, name: str, age: int, length: int):
        self.name = name
        self.age = age
        self.length = length

    def __repr__(self):
        return f"Person(naam:{self.name}, leeftijd:{self.age}, lengte={self.length})"


arvid = Person("Arvid", 50, 176)
homer = Person("Homer", 30, 164)
print(arvid)
print(homer)

# Met objecten kan je hetzelfde doen als met gelijk welke andere datatype dat je al kent.
l = [arvid, homer]
print(l)
dct = {arvid: "arvid", homer: "homer"}
print(dct)
s = {arvid, homer}
print(s)
t = (arvid, homer)
print(t)

for p in l:
    print(p.name)
    print(p)


# Hoe weten we of iemand volwassen is?
# Functionele versie

def is_adult(person: Person) -> bool:
    """
    Determine if a person is an adult
    :param person: Person to check
    :return: True if person is at least 18 years old
    """
    return person.age >= 18
