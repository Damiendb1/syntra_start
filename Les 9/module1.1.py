"""Evaluatie Modele 01 - Functioneel programmeren"""



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

#print_inhoud(contents)




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

#print_datum(contents)




def print_getalstats(contents):
    """print hoogste/laagste/gemiddeld willekeurig getal"""
getallen = []
for rij in contents:
        raw= rij[3]
        if raw is None:
            continue

        waarde= raw.strip()
        if waarde == "":
            continue

        waarde = waarde.replace(' ', '').replace(',','.')

        try:
            getal= float(waarde)
            getallen.append(getal)
        except:
            continue

Highest = max (getallen)
Lowest = min (getallen)
Middle = sum (getallen) / len(getallen)

print(f"Aantal getallen gevonden: {len(getallen)}")
print(f"Aantal getallen laagste: {(getallen)}")
print(f"Gemiddelde: {Middle}")
print(f"Highest Number: {Highest}")
print(f"Lowest Number: {Lowest}")

#print_getalstats(contents)




def print_kleur(contents):
    """Print hoeveel keer elke kleur vooorkomt"""

kleuren_teller = {}

for i in range(len(contents)):
    kleur = contents[i][5].strip().lower()
    if kleur == "":
        continue

    if (kleur in kleuren_teller):
          kleuren_teller[kleur] += 1
    else:
          kleuren_teller[kleur] = 1

print("aantal keer dat kler voorkomt:")
for kleur, aantal in kleuren_teller.items():
    print(f"{kleur.upper()}: {aantal}")

hoogste_kleur = None
hoogste_aantal = 0

for kleur, aantal in kleuren_teller.items():
    if aantal > hoogste_aantal:
        hoogste_kleur = kleur
        hoogste_aantal = aantal
print(f"De kleur dat het meest voorkomt: {hoogste_kleur.upper()}")

#print_kleur(contents)



def print_plaatsnaam(contents):
    """print plaatsnamen zonder dubbels hoofdletter ongevoelig"""
    unieke_plaatsen = set()
    for i in range(len(contents)):
        plaats = contents[i][4].strip().lower()
        if plaats == "":
            continue

        unieke_plaatsen.add(plaats)

    print("unieke plaats:")
    for plaats in unieke_plaatsen:
        print(plaats.upper())

    print(f"totaal: {len(unieke_plaatsen)} unieke plaatsnamen")


#print_plaatsnaam(contents)



def print_deelname(contents):
    """print volledig & onvolledige deelnames """
    totaal = len(contents)
    volledig = 0
    onvolledig = 0
    for i in range(len(contents)):
        datestamp = contents[i][2].strip()
        if datestamp == "":
            onvolledig += 1
        else:
            volledig += 1

    print(f"Er zijn {totaal} inzendingen: volledig: {volledig} en onvolledig: {onvolledig} ")
#print_deelname(contents)



def print_id(contents):
    """Print id stats. Welke ontbreken en oplopende rij"""
    ids = []

    for i in range(len(contents)):
        try:
            ids.append(int(contents[i][0].strip()))
        except:
            continue

    min_id = min(ids)
    max_id = max(ids)

    ontbrekende_ids = []
    for nummer in range(min_id, max_id + 1):
        if nummer not in ids:
            ontbrekende_ids.append(nummer)
    print(f"De ontbrekende id's: {ontbrekende_ids}")

#print_id(contents)



def print_Q_stats(contents):
    """print hoeveel woorden beginnen met Q.
    Hoeveel niet beginnen met Q
    Hoeveel woorden geen Q bevatten"""
    beginnen_met_Q = 0
    bevatten_Q = 0
    geen_Q = 0

    for i in range(len(contents)):
        qwooord = contents[i][6].strip().lower()

        if qwooord == "":
            continue
        if "q" not in qwooord:
            geen_Q += 1
            continue
        elif qwooord.startswith("q"):
            beginnen_met_Q += 1
        else:
            bevatten_Q += 1
    print(f"{beginnen_met_Q} woorden beginnen met Q")
    print(f"{bevatten_Q} woorden bevatten Q maar niet als eerste")
    print(f"{geen_Q} zonder Q")

#print_Q_stats(contents)




def save_q_inzendingen(contents):
    """Vraag bestandsnaam en schrijf velden weg id,getal,kleur,q-woord"""
    bestandsnaam = input("Geef een bestandsnaam om op te slaan (of typ STOP): ").strip().strip('"')

    if bestandsnaam.lower() == "stop":
        print("Opslaan geannuleerd.")
        return

    try:
        f = open(bestandsnaam, "w", encoding="utf-8")
    except:
        print(f"Kon bestand '{bestandsnaam}' niet openen om te schrijven.")
        return

    for i in range(len(contents)):
        id_str = contents[i][0].strip()
        getal_str = contents[i][3].strip()
        kleur = contents[i][5].strip()
        qwoord = contents[i][6].strip()

        try:
            float(getal_str.replace(",", "."))
        except:
            continue

        if qwoord == "":
            continue
        if not qwoord.lower().startswith("q"):
            continue

        f.write(f"{id_str};{getal_str};{kleur};{qwoord}\n")

    f.close()
    print(f"Inzendingen succesvol opgeslagen in: {bestandsnaam}")


#save_q_inzendingen(contents)



def toon_menu():
    print("\n--- MENU ---")
    print("1) Print het aantal lijnen")
    print("2) Print de inhoud")
    print("3) Print datums")
    print("4) Print getal stats")
    print("5) Print kleur stats")
    print("6) Print plaatsnamen")
    print("7) Print deelname stats")
    print("8) Print id stats")
    print("9) Print Q stats")
    print("10) Save (naar bestand)")
    print("STOP) Programma stoppen")


while True:
    toon_menu()
    choice = input("Maak een keuze 1-10 of Stop").strip().lower()
    if choice == "stop":
        print("Programa stopped.")
        break
    elif choice == "1":
        print_x_lines(contents)
    elif choice == "2":
        print_inhoud(contents)
    elif choice == "3":
        print_datum(contents)
    elif choice == "4":
        print_getalstats(contents)
    elif choice == "5":
        print_kleur(contents)
    elif choice == "6":
        print_plaatsnaam(contents)
    elif choice == "7":
        print_deelname(contents)
    elif choice == "8":
        print_id(contents)
    elif choice == "9":
        print_Q_stats(contents)
    elif choice == "10":
        save_q_inzendingen(contents)
    else:
        print("ongeldig, probeer opnieuw")