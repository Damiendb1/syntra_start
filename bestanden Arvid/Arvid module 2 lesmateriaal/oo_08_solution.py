# Oefening 1:
# Maak een klasse Employee met als attributen name: string, date_of_birth: datetime; departement: str en salary: Decimal.
# Zorg dat init, repr, eq in orde zijn
# Zorg voor een function promote die het salaris van een employee verhoogt met 5%.
# Maak een subklasse Manager van Employee met function promote die het salaris verhoogt met 10%, zorg
# dat repr in orde is
# Uitbreiding
# Maak een subklasse CEO  van Manager  met function promote die het salaris verhoogt met 15%.
# Zorg dat repr in orde is
from datetime import datetime
from decimal import Decimal


class Employee:
    """ Representation of an employee """

    def __init__(self, name: str, date_of_birth: datetime, salary: Decimal):
        self.name = name
        self.date_of_birth = date_of_birth
        self.salary = salary

    def __repr__(self):
        return f"Employee(name={self.name}, date_of_birth={self.date_of_birth.strftime('%D%M%Y')}, salary={self.salary}€)"

    def __eq__(self, other):
        return self.name == other.name and self.date_of_birth == other.date_of_birth

    def promote(self):
        self.salary *= Decimal('1.05')

class Manager(Employee):
    def promote(self):
        self.salary *= Decimal('1.1')


class Ceo(Employee):
    def promote(self):
        self.salary *= Decimal('1.2')

e1 = Employee("Arvid", datetime(1975, 4, 3), Decimal(1000))
e2 = Manager("Homer", datetime(1982, 4, 3), Decimal(1500))
e3 = Ceo("Burns", datetime(1951, 4, 3), Decimal(15000))

personnel = [e1, e2, e3]

for p in personnel:
    p.promote()

print(personnel)