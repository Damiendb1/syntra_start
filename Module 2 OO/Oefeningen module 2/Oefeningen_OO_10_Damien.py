import datetime

# Oefening 1: Neem onderstaande class Person
# 1.1: Zorg er voor dat naam niet meer gewijzigd kan worden.
# 1.2: Voeg een attribuut date_of_birth toe aan de klasse Person.
#      Zorg er voor dat deze datum niet voor 1/1/1900 kan liggen en ook niet in de toekomst.
#
#





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



class Person:
    def __init__(self, name: str, gender: str, date_of_birth: str):
        name = name.strip()
        self._name = name
        self.gender = gender
        self.date_of_birth = date_of_birth

    def __repr__(self):
        return f"{self.name} is een {self.gender}, geboren op {self.date_of_birth}"

    @property
    def date_of_birth(self):
        return self._date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, value):
        if value < "1900-01-01":
            raise ValueError("Datum kan niiet voor 1900-01-01 zijn")
        if value > datetime.date.today().isoformat():  #<- AI zwaar geholpen
            raise ValueError("Datum kan niet in de toekomst liggen")
        self._date_of_birth = value

    @staticmethod
    def coffee_price():
        return 3

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        raise AttributeError("Name mag niet gewijzigd worden")

p1 = Person("Damien", "V", "1996-04-22")
#p2 = Person("Jean-luc_de_derde", "X", "1303-03-03")
#p3 = Person("Prins Clement Junior", "M", "2030-05-01")
p4 = Person("Flipke", "M", "1965-05-05")
print(p1.name, p1.gender, p1.date_of_birth)
#print(p2.name, p2.gender)
#print(p3.name, p3.gender)
print(p4.name, p4.gender, p4.date_of_birth)
#print(p2.date_of_birth)
#print(p3.date_of_birth)
#print(p4.date_of_birth)
exit()

