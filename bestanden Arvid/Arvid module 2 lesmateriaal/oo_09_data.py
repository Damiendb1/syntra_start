import csv


class Gender:
    def __init__(self, value: str):
        if value not in ["M", "V"]:
            raise ValueError("Value must be 'M' or 'V'")
        self.value = value

    def __repr__(self):
        return "vrouw" if self.value == "V" else "man"


class Person:
    def __init__(self, name: str, gender: Gender):
        name = name.strip()
        self.name = name
        self.gender = gender

    def __repr__(self):
        return f"{self.name} is een {self.gender}"

    @staticmethod
    def coffee_price():
        return 3


class Student(Person):
    def coffee_price(self):
        return 2


class Teacher(Person):
    def coffee_price(self):
        return 0

def main():
    visitors = []
    with open("d:/dev/learning/filedata/persons.csv", "r") as f:
        r = csv.reader(f)
        next(r)
        for row in r:
            name = row[0]
            gender = Gender(row[1])
            type_ = row[2].upper()
            if type_ == "CURSIST":
                visitors.append(Student(name, gender))
            elif type_ == "DOCENT":
                visitors.append(Teacher(name, gender))
            else:
                visitors.append(Person(name, gender))
    price = 0
    for visitor in visitors:
        print(visitor.name, "betaalt voor een koffie", visitor.coffee_price())
        price += visitor.coffee_price()
    print(f"De prijs is {price}")


if __name__ == "__main__":
    main()