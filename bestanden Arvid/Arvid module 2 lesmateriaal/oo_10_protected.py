class Gender:
    def __init__(self, value: str):
        if value not in ["M", "V", "X"]:
            raise ValueError("Value must be M, v, of X")
        self.value = value

    def __repr__(self):
        if self.value == "X":
            return "onbekend"
        if self.value == "M":
            return "man"
        if self.value == "V":
            return "vrouw"

MALE = Gender("M")
FEMALE = Gender("V")
X = Gender("X")

print(MALE)
print(FEMALE)
print(X)

# Het is op dit moment niet mogelijk om een Gender aan te maken met een waarde verschillend van X, M of V.
# Het is echter wel toegelaten (maar ongewenst) om een Gender aan te maken met een waarde van X en dan te wijzigen naar Y
X.value = "Y" # dit is ongewenst

# Dit geeft een error bij print.


# we kunnen een property toevoegen aan de class
# Voor een property kan je met code bepalen:
#   Opvragen:
#      - mag de waarde opgevraagd worden, of niet
#      - indien de waarde opgevraagd mag worden, welke waarde wil je dan ontvangen
#   Wijzigen:
#      - mag de waarde gewijzigd worden, of niet
#      - indien de waarde gewijzigd mag worden, welke waardes zijn dan toegelaten.

# om een property 'prop_x' toe te voegen aan een class
#   - voeg self._prop_x = value toe aan de init functie. Met underscore !
#   - voeg deze code toe aan de class
#       @property
#       def prop_x(self):
#           # voeg code toe om opvragen te verbieden om of de waarde in een bepaalde vorm te retourneren
#           return self._prop_x
#
#       @prop_x.setter
#       def prop_x(self, value):
#           voeg code toe om wijzigen te verbieden om of om de waarde te controleren en dat _prop_x te wijzigen
#           self._prop_x = value



class Gender2:
    def __init__(self, value: str):
        if value not in ["M", "V", "X"]:
            raise ValueError("Value must be M, V, of X")
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        # Optie 1: Niet toelaten dat waarde wordt aangepast
        #           raise NotImplementedError("Je mag value niet aanpassen")
        # Optie 2: Waarde overnemen
        #           self._value = value
        # Optie 3: Combinatie:
        #          waarde controleren, en ValueError raisen
        #          als het geen toegelaten waarde is
        #          anders, de waarde overnemen.
        if value not in ["M", "V", "X"]:
            raise ValueError("Value must be M, V, of X")
        self._value = value

    def __repr__(self):
        if self._value == "X":
            return "onbekend"
        if self._value == "M":
            return "man"
        if self._value == "V":
            return "vrouw"


M = Gender2("M")
M.value = "Y"

# Je kan op die manier ook verbieden dat een attribuut wordt gewijzigd.
# Wijzig de code van def value(self, value): naar
# @value.setter
# def value(self, value):
#     raise AttributeError("Value cannot be changed")


# Oefening 1: Neem onderstaande class Person
# 1.1: Zorg er voor dat naam niet meer gewijzigd kan worden.
# 1.2: Voeg een attribuut date_of_birth toe aan de klasse Person.
#      Zorg er voor dat deze datum niet voor 1/1/1900 kan liggen en ook niet in de toekomst.
#
# class Person:
#     def __init__(self, name: str):
#         name = name.strip()
#         self.name = name
#
#     def __repr__(self):
#         return f"{self.name} is een {self.gender}"
#

from oo_09_data import Person

class Book:
    def __init__(self, input_title, author):
        self._title = input_title
        self.author = author
        self._publisher = None

    def __repr__(self):
        return f"{self._title} geschreven door '{self.author}'"

    @property
    def title(self):
        return f"De titel van het book is {self._title}"

    @title.setter
    def title(self, value):
        # raise AttributeError("Titel van een een boek mag niet wijzigen")
        if isinstance(value, str):
            self._title = value
        else:
            raise TypeError("Titel moet een string zijn")



book = Book("Python in 30minutes", Person("Superman", Gender("M")))

print(book)
print(book.title)
book.title = "Python in 24 uur"
book.title = 24
print(book._title)
print(book._publisher)
book._publisher = "Marvel"
print(book._publisher)
