# opdracht 1:
# Vraag de gebruiker om een bestandsnaam in te geven.
# Blijf vragen tot de gebruiker "Stop" ingeeft, of een bestandsnaam die bestaat.
# Zorg dat de code alle mogelijk errors opvangt.

while True:
    filename = input("Enter a filename: ")
    if filename.lower() == "stop":
        exit()
    try:
        file = open(filename)
        file.close()
        break
    except FileNotFoundError:
        print(f"File {filename} does not exist!")

# opdracht 2:
# Maak een bestand met deze inhoud:
"""
Naam,Geslacht,Leeftijd
Homer,M,36
Marge,F,34
Lisa,F,8
Bart,M,10
Maggie,F,1
"""
# Lees het bestand in.
# Lijn 1 bevat de kolomnamen en moet overgeslagen worden.
# Maak een lijst van dicts "Name" -> (Sex, Age)

# try: except: voor file operaties zijn weggelaten voor bondigheid
lst = []
my_file = "C:\\Users\\Documents\\Python Data Developer\\Bestand.txt"

file = open(my_file, "r")
file.readline()
for line in file:
    if line[-1] == '\n':
        line = line[:-1]
    name, sex, age = line.split(",")
    lst.append({name:(sex, age)})
file.close()
print(lst)


# opdracht 3:
# lees het bestand van opdracht 2 in (kies zelf: met of zonder header)
# schrijf de lijnen met mannen naar  bestandsnaam.m.txt
# schrijf de lijnen met vrouwen naar bestandsnaam.f.txt
# maak je code zo robuust mogelijk.

# try: except: voor file operaties zijn weggelaten voor bondigheid
in_file = "C:\\Users\\Documents\\Python Data Developer\\Bestand.txt"

in_file = open(in_file, "r")
m_file = open("C:\\Users\\Documents\\Python Data Developer\\Bestand_m.txt", "a")
f_file = open("C:\\Users\\Documents\\Python Data Developer\\Bestand_f.txt", "a")
in_file.readline()
for line in in_file:
    if line[-1] == '\n':
        line = line[:-1]
    name, sex, age = line.split(",")
    if sex == "M":
        m_file.write(line + '\n')
    elif sex == "F":
        f_file.write(line + '\n')
in_file.close()
m_file.close()
f_file.close()

# opdracht 4: lees een python bestand in en tel het aantal lijnen ide starten met een #

count = 0
python_file = "C:\\Users\\\\Documents\\Python Data Developer\\PyCharmProjects\\Les2.py"
try:
    python_file = open(python_file, "r")
    for line in python_file:
        if line[0] == "#":
            count += 1
    python_file.close()

except Exception as e:
    print(f"{e}")
print(f"The file contains {count} lines starting with #")

# opdracht 5: pas def safe_open(filename:str) uit 12_file.py ook werkt als het bestand bijvoorbeeld geopend is in MS-Word.
def safe_open(filename:str):
    try :
        file = open(filename,"r")
        return file
    except FileNotFoundError:
        print(f"Bestand '{filename}' niet gevonden")

    except PermissionError:
        print(f"Bestand '{filename}' is in gebruik.")

    return None