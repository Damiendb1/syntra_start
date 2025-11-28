# Er is ook een Object Oriented method om te bepalen of een persoon volwassen is.
# We voegen een function toe.

class Person:
    """
    Represents a person with a name and an age.
    """

    def __init__(self, name: str, age: int, length: int = 175):
        self.name = name
        self.age = age
        self.length = length

    def __repr__(self):
        return f"Person(name={self.name}, age={self.age})"

    def is_adult(self):
        """
        Determines if the individual is considered an adult based on their age.
        :return: True if the individual is an adult
        """
        return self.age >= 18


john = Person("John", 36, length=160)
jane = Person("Jane", 15, length=175)
print(f"is {john.name} an adult: {john.is_adult()}")
print(f"is {jane.name} an adult: {jane.is_adult()}")
print(dir(jane))
print(vars(jane))

john = Person("John", 36, length=160)

# Python laat toe om attributen van een object te wijzigen.
# Het mag wel, maar beter niet.
# Maak jouw code zo onafhankelijk mogelijk van de attributen van een klasse
john.length = 161


# Als je op voorhand weet dat een attribuut dikwijls kan wijzigen.
# Schrijf hiervoor dan een extra method.
class Person:
    """
    Represents a person with a name and an age.

    This class is designed to encapsulate the basic attributes of a person,
    specifically their name and age. It provides a convenient way to represent
    a person object and display it as a string for debugging or logging purposes.
    """

    def __init__(self, name: str, age: int, length: int = 175):
        self.name = name
        self.age = age
        self.length = length

    def __repr__(self):
        return f"Person(name={self.name}, age={self.age})"

    def is_adult(self):
        """
        Determines if the individual is considered an adult based on their age.
        :return: True if  the individual is an adult
        """
        return self.age >= 18

    def set_length(self, length: int):
        """
        Sets the length to a new value.
        This method updates the current length value with
        a new integer provided as an argument.
        :param length: The new length value to be set, must be an integer.
        """
        self.length = length


john = Person("John", 36, 160)
john.set_length(161)


# OO is een programmeer stijl met drie grote concepten: encapsulation is het eerste grote concept.
# Een class kan heel veel attributen en functies hebben.
# De attributen geven een status weer van het object.  Ze worden ingekapseld in het object.
# De functions laten toe de status ope te vragen en te manipuleren. De manier waarop is ingekapseld.

# Als je een Person class aanmaakt en de logic wil inbouwen dat een persoon enkel kan groeien, nooit krimpen, dan kan
# je die logica inbouwen in de class. De code die jouw class gebruikt hoeft zich hier geen zorgen over te maken.
# We willen ook controleren dat lengte nooit kleiner dan 45 of groter dan 250 is.

class Person:
    """
    Represents a person with a name and an age.
    """

    def __init__(self, name: str, age: int, length: int = 175):
        self.name = name
        self.age = age
        self.length = length

    def __repr__(self):
        return f"Person(name={self.name}, age={self.age})"

    def is_adult(self):
        """
        Determines if the individual is considered an adult based on their age.
        :return: True if  the individual is an adult
        """
        return self.age >= 18

    def set_length(self, length: int):
        """
        Sets the length to a new value.
        This method updates the current length value with
        a new integer provided as an argument.
        :param length: The new length value to be set, must be an integer.
        :raises ValueError: If the new length value is not within the allowed range.
        """
        if not (45 < length < 250):
            raise ValueError("Lengte moet tussen 45 en 250 liggen.")
        if length < self.length:
            raise ValueError("Een persoon kan enkel groeien")
        self.length = length


john = Person("John", 36, 160)
john.set_length(161)
john.set_length(42)

# Oefening: Maak een class Car met passende attributen and functions.
# Een auto heeft een merk, bouwjaar en een prijs. Vanaf 50 000€ noemen we het een luxe auto. => is_deluxe()
# Bouwjaar kan niet in de toekomst liggen. Auto's ouder dan 30 jaar zijn old timers => is_old_timer()
