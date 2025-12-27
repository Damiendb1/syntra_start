# We hernemen de grade class

# grades hebben een volgorde:
# F < D- < D < D+ < C- < C < C+ < B- < B < B+ < A- < A < A+
# Je wil dus de compare dunders implementeren.

# Maar hoe?
# Deze code werkt niet
#     def __lt__(self, other):
#         return self.code < other.code
# want :
#       "A' < "A-"
#       "A' < "A+"
# Je moet dus zelf een volgorde forceren.

# Je kan een __lt__ maken die de letter codes effectief met elkaar vergelijkt
# de string 'A' is kleiner dan de string 'B', want 'A' heeft ASCII waarde 65 en 'B' heeft ASCII 66
# Dus als de letter van self verschilt van de letter van other, dan kan je snel beslissen wie het grootst is.
# Als self en other dezelfde letter hebben, dan moet je kijken naar het tweede teken, enz. Het wordt ingewikkeld.

# def __lt__(self, other):
#     first_letter_self = self.name[0]
#     first_letter_other = other.name[0]
#     if first_letter_self > first_letter_other:
#         return True  # want grade A > grade B    "A" (65) < "B"  (66)
#     if self.name == other.name:
#         return False
#     ll_s = self.name[-1]
#     ll_o = other.name[-1]
#     # ....
#     # het wordt hier al snel ingewikkeld.


# Er zijn alternatieven

# Voorstel 1 (van een cursist)
# Maak een lijst met daarin alle grade-codes in volgorde
# De positie van een grade in die lijst bepaalt dan of de ene grade kleiner is dan de andere

ORDER = ['F', 'D-', 'D', 'D+', 'C-', 'C', 'C+', 'B-', 'B', 'B+', 'A-', 'A', 'A+']

# De lt-dunder van grade wordt dan
# def __lt__(self, other):
#     # Zoek de index van self.name en de index van other.name in de ORDERED lijst, en vergelijk
#     return ORDER.index(self.name) < ORDER.index(other.name)

# Voorstel 2:

# Dit kan door Grade uit te breiden met een value attribute
# Het attribuut heeft geen echte betekenis voor een grade
# maar kan onderliggende wel gebruikt om te vergelijken.
# We maken hier een protected attribuut van om duidelijk te maken,
# dat het geen publiek beschikbaar attribuut is.

class Grade:
    def __init__(self,
                 name: str,
                 description: str,
                 value: int):
        self.name = name
        self.description = description
        self._value = value

    def __repr__(self):
        return f"{self.name}"

    def __lt__(self, other):
        return self._value < other._value

    # dunders  le, eq, ne, gt, ge kunnen analoog gebouwd worden.

# De voorgedefinieerde grades moeten nu aangemaakt worden met een extra parameter value

GRADES = {
    "A+": Grade("A+", description="Outstanding", value=12),
    "A": Grade("A", description="Excellent", value=11),
    "A-": Grade("A−", description="Very good", value=10),
    "B+": Grade("B+", description="Good", value=9),
    "B": Grade("B", description="Above average", value=8),
    "B-": Grade("B−", description="Fair", value=7),
    "C+": Grade("C+", description="Satisfactory", value=6),
    "C": Grade("C", description="Average", value=5),
    "C-": Grade("C−", description="Below average", value=4),
    "D+": Grade("D+", description="Poor", value=3),
    "D": Grade("D", description="Barely passing", value=2),
    "D-": Grade("D−", description="Lowest passing", value=1),
    "F": Grade("F", description="Fail", value=0),
}

print(GRADES["B-"] > GRADES["C+"])
print(GRADES["B-"] < GRADES["C+"])

print(sorted(GRADES.values()))
print(sorted(GRADES.values(), key=lambda x: x.description))

for grade in sorted(GRADES.values(), key=lambda x: x.description):
    print(grade.description, grade.name)

# Voorstel 3:
# Je kan  de objecten in een bepaalde volgorde aanmaken en
# aan de hand van een class variabele 'counter' de value bepalen.
# In onderstaande code heeft het eerst aangemaakte object de laagste waarde.
# Grade krijgt een class attribuut counter. Elke keer als __init__ wordt opgeroepen
# wordt class counter 1 verhoogd.
# De voorgedefinieerde lijst moet geen extra parameter value meer hebben.

class Grade:
    counter = 0
    def __init__(self,
                 name: str,
                 description: str):
        self.name = name
        self.description = description
        self._value = Grade.counter
        Grade.counter += 1

    def __repr__(self):
        return f"{self.name}"

    def __lt__(self, other):

        return self._value > other._value


GRADES = {
    "A+": Grade("A+", description="Outstanding", ),
    "A": Grade("A", description="Excellent", ),
    "A−": Grade("A−", description="Very good", ),
    "B+": Grade("B+", description="Good"),
    "B": Grade("B", description="Above average"),
    "B-": Grade("B-", description="Fair"),
    "C+": Grade("C+", description="Satisfactory"),
    "C": Grade("C", description="Average"),
    "C-": Grade("C-", description="Below average"),
    "D+": Grade("D+", description="Poor"),
    "D": Grade("D", description="Barely passing"),
    "D-": Grade("D-", description="Lowest passing"),
    "F": Grade("F", description="Fail"),
}
