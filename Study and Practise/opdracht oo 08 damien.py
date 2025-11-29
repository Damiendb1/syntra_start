from datetime import datetime
from decimal import Decimal



class Employee:
    """ Info over werknemer """
    def __init__(self, name: str, date_of_birth: datetime, salary: Decimal, department: str ):
        self.name = name
        self.date_of_birth = date_of_birth
        self.salary = salary
        self.department = department

    def __repr__(self):
        return f"Employee(name= {self.name},Dathe_of_birth= {self.date_of_birth},Salary= {self.salary}, department= {self.department})"

    def __eq__(self, other):
        return self.name == other.name and self.date_of_birth == other.date_of_birth

    def promote (self):
        self.salary *= Decimal('1.05')

class Manager(Employee):
    def __repr__(self):
        return f"Manager: {self.name}, date_of_birth= {self.date_of_birth}, salary= {self.salary}, department= {self.department}"

    def promote(self):
        self.salary *= Decimal('1.1')

class Ceo(Manager):
    def __repr__(self):
        return f"CEO: {self.name},date_of_birth= {self.date_of_birth}, salary= {self.salary}, department= {self.department}"
    def promote(self):
        self.salary *= Decimal('1.15')

e1 = Employee("Damien", datetime(1996,4,22), Decimal(1000), department="WWA")
e2 = Manager("Boss", datetime(1980,1,2), Decimal(2000), department="HR")
e3 = Ceo("Bigg BOSS", datetime(1950,1,1), Decimal(15000), department="HR 2.0")
#print(e1)
#print(e2)
#print(e3)
personeel = [e1, e2, e3]
print(personeel)

for p in personeel:
    p.promote()

print(personeel)






