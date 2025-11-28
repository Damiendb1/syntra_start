# Je kan een list vullen met een willekeurig aantal elementen
male = ['Karel',
        'Arvid',
        'Sven',
        'Alexander',
        'Christophe',
        'Wesley',
        'Nico',
        'Jean-Pierre',
        'Olivier',
        'Damiën',
        'Patrick']
female = [
    'Nina',
    'Begum',
    'Ellen',
    'Raquel',
    'Hamideh',
    'Sofie',
]
print(f"male  : {male}")
print(f"female: {female}")
print()

# Het type van de waarde doet er niet toe. De elementen mogen dus ook van het type list zijn
# Je krijgt dan een lijst van lijsten.
group = [male, female]
print(f"group: {group}")
print(f"{len(group)=}")

for i in range(len(group)):
    print(f"group[{i}] : {group[i]}")

print(f"{len(group)=}")
print(f"{type(group)=}")
print(f"{len(group[0])=}")
print(f"{len(group[1])=}")
print(f"{type(group[1])=}")

print("Alle dames")
for name in group[1]:
    print(f"\t{name}")

print("Alle Heren")
for name in group[0]:
    print(f"\t{name}")

# individuele waardes vinden
print(f"{group[1][3]=}")  # neem element 1 van group. Dit is een lijst. Neem daaruit het element 4. Dit een string.
print(f"{type(group[1][3])=}")

# list of list wordt veel gebruikt voor tabellen

python_group = [
    ['Karel', 'M', 'Cursist'],
    ['Begum', 'V', 'Cursist'],
    ['Sven', 'M', 'Cursist'],
    ['Alexander', 'M', 'Cursist'],
    ['Christophe', 'M', 'Cursist'],
    ['Hamideh', 'V', 'Cursist'],
    ['Nico', 'M', 'Cursist'],
    ['Jean-Pierre', 'M', 'Cursist'],
    ['Olivier', 'M', 'Cursist'],
    ['Damiën', 'M', 'Cursist'],
    ['Patrick', 'M', 'Cursist'],
    ['Nina', 'V', 'Cursist'],
    ['Ellen', 'V', 'Cursist'],
    ['Arvid', 'M', 'Docent'],
    ['Raquel', 'V', 'Cursist'],
    ['Wesley', 'M', 'Cursist'],
    ['Sofie', 'V', 'Cursist']
]


# print alle rijen van de groep af
for person in python_group:
    print(person)


# je kan dan met de verschillende elementen van een persoon informatie afdrukken
for person in python_group:
    print(f"{person[0]} is een {person[2]}")
    if person[1] == 'V':
        print(f"{person[0]} is een vrouw")
    else:
        print(f"{person[0]} is een man")
    print()

# in bovenstaande code mo"t je de hele tijd onthouden dat person[0] de naam is, persoon[1] het geslacht en
# persoon[2] het type docent / cursist.
# het is beter om die onderdelen in variabelen te stockeren met een relevante naam
for person in python_group:
    name = person[0]
    sex = person[1]
    type_ = person[2]
    print(f"{name} is een {type_}")
    if sex == 'V':
        print(f"{name} is een vrouw")
    else:
        print(f"{name} is een man")
    print()


# als je zeker weet dat elke rij uti de tabel 3 elementen bevat
# dan kan je de code inkorten
for person in python_group:
    name, sex, type_ = person
    print(f"{name} is een {type_}")
    if sex == 'V':
        print(f"{name} is een vrouw")
    else:
        print(f"{name} is een man")
    print()

# als je zeker weet dat elke rij uti de tabel 3 elementen bevat
# dan kan de code inkorten
for name, sex, type_  in python_group:
    print(f"{name} is een {type_}")
    if sex == 'V':
        print(f"{name} is een vrouw")
    else:
        print(f"{name} is een man")
    print()


# opdracht 1: print alle dames in python_group
for name, sex, type_  in python_group:
    if sex == 'V':
        print(name)

# opdracht 2: maak een lijst met alle heren namen in python_group
men = []
for name, sex, type_  in python_group:
    if sex == 'M':
        men.append(name)
print(men)
# opdracht 3: tel het aantal dames in python_group
cnt = 0
for name, sex, type_  in python_group:
    if sex == 'V':
        cnt +=1
print(f"er zijn {cnt} vrouwen in de group")

# ---------------------------------------
men = []  # will grow with all male name
cnt = 0  # will count all females
for name, sex, type_  in python_group:
    if sex == 'M':
        men.append(name)
    if sex == 'V':
        print(name)
        cnt += 1
print(f"er zijn {cnt} vrouwen in de group")
print(men)