from datetime import datetime


# 1.1: Zorg er voor dat naam niet meer gewijzigd kan worden.
# 1.2: Voeg een attribuut date_of_birth toe aan de klasse Person.
#      Zorg er voor dat deze datum niet voor 1/1/1900 kan liggen en ook niet in de toekomst.
#
#

EARLIEST = datetime(1900, 1, 1)

class Person:
    def __init__(self, name: str, gender: str, dob:datetime):
        name = name.strip()
        self._name = name
        self.gender = gender
        if not self.check_dob(dob):
            raise ValueError("Date of birth is invalid")
        self._dob = dob

    def __repr__(self):
        return f"{self.name} is een {self.gender}"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name:str):
        raise AttributeError("name is read-only")

    @property
    def dob(self):
        return self._dob

    @staticmethod
    def check_dob(dob:datetime):
        return EARLIEST <= dob <= datetime.now()

    @dob.setter
    def dob(self, dob:datetime):
        if self.check_dob(dob):
            self._dob = dob
        else:
            raise ValueError("Date of birth is invalid")





