# CSV staat voor comma separated values
# Het is een tekst bestand waar elke lijn een rij met data bevat, gescheiden door kommas.
# Het is eenvoudige voorstelling van tabellen, spreadsheet data banken.

python_group = [
    ['Name', 'Sex', 'Title'],
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

f = open("d:/dev/learning/filedata/persons.csv", "w")
for person in python_group:
    f.write(",".join(person) + '\n')  # we moeten zelf de newline toevoegen
f.close()

# We hebben reeds een CSV bestand ingelezen en behandeld, ongeveer als volgt:

file = open("d:/dev/learning/filedata/persons.csv", "r")
for line in file:
    values = line[:-1].split(",")
    for value in values:
        print(value)
    print()
file.close()

# Hoe moet je omgaan met waardes waar zelf een komma voorkomt?
# Je moet zelf zorgen dat een eerste line wordt overgeslagen.
# Als je rijen wil weg schrijven, moet je zelf joinen en newline toevoegen
# Wat met lege lijnen?

# De python module csv is in veel gevallen een betere optie.

import csv  # importeer de module

# lees alle data uit het CSV-bestand
file = open("d:/dev/learning/filedata/persons.csv", "r")
reader = csv.reader(file)  # reader is nu een 'intelligente' lezer van lijnen van CSV
for row in reader:
    print(row)  #row is nu geen string meer en een \n op het einde van elke lijn maar meteen een lijst van strings
file.close()

# schrijf een CSV bestand
file = open("d:/dev/learning/filedata/persons2.csv", "w")
writer = csv.writer(file)  # writer is nu een 'intelligente' schrijver
writer.writerows(python_group)  # list of list wordt nu als CSV weggeschreven
file.close()


# Oefening:
# - Lees het bestand bord.csv in met de csv module.
# - Schrijf een nieuw bestand bord2.csv met daarin enkel de volledige inzendingen.



# Alle code hieronder is louter ter informatie voor wie meer wil weten / uitdaging wil
dict_grp = [
    {"name": 'Karel', "Sex": 'M', "Title": 'Cursist'},
    {"name": "Begum", "Sex": 'V', "Title": 'Cursist'},
    {"name": 'Sven', "Sex": 'M', "Title": 'Cursist'},
    {"name": 'Alexander', "Sex": 'M', "Title": 'Cursist'},
    {"name": 'Christophe', "Sex": 'M', "Title": 'Cursist'},
    {"name": 'Hamideh', "Sex": 'V', "Title": 'Cursist'},
    {"name": 'Nico', "Sex": 'M', "Title": 'Cursist'},
    {"name": 'Jean-Pierre', "Sex": 'M', "Title": 'Cursist'},
    {"name": 'Olivier', "Sex": 'M', "Title": 'Cursist'},
    {"name": 'Damiën', "Sex": 'M', "Title": 'Cursist'},
    {"name": 'Patrick', "Sex": 'M', "Title": 'Cursist'},
    {"name": 'Nina', "Sex": 'V', "Title": 'Cursist'},
    {"name": 'Ellen', "Sex": 'V', "Title": 'Cursist'},
    {"name": 'Arvid', "Sex": 'M', "Title": 'Docent'},
    {"name": 'Raquel', "Sex": 'V', "Title": 'Cursist'},  # note de case sensitivity!
    {"name": 'Wesley', "Sex": 'M', "Title": 'Cursist'},
    {"name": 'Sofie', "Sex": 'V', "Title": 'Cursist'}
]
print(dict_grp)
file = open('d:/dev/learning/filedata/persons_dict.csv', 'w')
writer = csv.DictWriter(file,
                        fieldnames=['name', 'Title', 'Sex'])  # de labels zijn case sensitive !
writer.writeheader()
writer.writerows(dict_grp)
file.close()

# probeer delimiter parameter van DictWriter  delimiter="-"
# Kijk naar het effect op de naam Jean-Pierre
# probeer quoting parameter van DictWriter quoting=csv.QUOTE_ALL

# er is ook een dictreader

file = open('d:/dev/learning/filedata/persons_dict.csv', 'r')
reader = csv.DictReader(file,
                        delimiter="-")

for row in reader:
    print(row)
file.close()
