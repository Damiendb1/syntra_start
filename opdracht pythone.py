"""Evaluatie Modele 01 - Functioneel programmeren"""


# while True:
#     csvbestand = input("Geef het pad van CSV bestand OF typ 'Stop': ")
#     if csvbestand.lower() == "stop":
#         print("Programma gestopt")
#         break
#     try:
#         csvbestand = open(csvbestand, "r")
#         print("Bestand succesvol geopend")
#         break
#     except FileNotFoundError:
#         print("Bestand niet gevonden. Probeer opnieuw: ")

#      C:\Users\Damien\Desktop\Python data\bord.csv
#      C:\datadev\syntra_start\opdracht pythone.py
#      C:\datadev\bord.csv


def safe_open(filename:str):
        """Probeert een bestand te openen en retourneert het bestand of None als het niet lukt"""
        try:
            file = open(filename, "r")
            return file
        except FileNotFoundError:
            print(f"Bestand '{filename}' niet gevonden, probeer opnieuw.")
            return None


while True:
    my_file = input("Geef het pad van CSV bestand of typ 'Stop': ")

    if my_file.lower() == "stop":
        print("Programma gestopt.")
        exit()

    file = safe_open(my_file)
    if file is not None:
        print("Bestand succesvol geopend")
        break

contents = []
lines = file.readlines()
file.close()

for line in lines[1:]:
    line = line.strip()
    if not line:
        continue
    parts = line.split(";")
    contents.append(parts)
print("bestand ingelezen")
print(f"Aantal rijen in contents: {len(contents)}")

               #voorbeeld eerste 10 rijen
# print("\nEerste 3 rijen van contents:")
# for row in contents[:10]:
#     print(row)

def print_x_lines(contents):
    """print aantal lijnen uit contents"""
    amount = len(contents)
    print(f"Aantal rijen in contents: {amount}")

def print_inhoud(contents):
    """print inhoud uit contents: Lijn per Lijn"""
    for i in range(len(contents)):
        id = contents[i][0]
        startdate = contents[i][1]
        datestamp = contents[i][2]
        getal = contents[i][3]
        plaats = contents[i][4]
        kleur = contents[i][5]
        Qwoord = contents[i][6]
        print(f"id {id} gestart op {startdate}, verzonden om: {datestamp}, {getal}, {plaats}, {kleur}, {Qwoord} ")

print_inhoud(contents)

def print_datum(contents):
    """print unieke datums van inzending"""
    unieke_datums = set()
    for i in range(len(contents)):
        startdate = contents[i][1]
        if startdate.strip() =="":
            continue
        datum = startdate.split(" ")[0].strip()
        unieke_datums.add(datum)

    print("unieke dagen inzending: ")
    for dag in unieke_datums:
        print(dag)

    print(f"totaal:{len(unieke_datums)} unieke dagen")

print_datum(contents)


def print_getalstats(contents):
    """print hoogste/laagste/gemiddeld willekeurig getal"""
getallen = []
for rij in contents:
        raw= rij[3]
        if raw is None:
            continue

        waarde= raw.strip()
        if not waarde:
            continue

        waarde = waarde.replace(' ', '').replace(',','.')

        try:
            getal= float(waarde)
            getallen.append(getal)
        except ValueError:
            #   print(f"Ongeldig getal: {waarde}")
            continue

Highest = max (getallen)
Lowest = min (getallen)
Middle = sum (getallen) / len(getallen)

print(f"Aantal getallen gevonden: {len(getallen)}")
print(f"Aantal getallen laagste: {(getallen)}")
print(f"Gemiddelde: {Middle}")
print(f"Highest Number: {Highest}")
print(f"Lowest Number: {Lowest}")




