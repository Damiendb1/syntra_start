# os module laat je werken  met het besturingssysteem.

# Werken met mappen en bestanden
# Navigeren tussen directories
# Opvragen van systeeminformatie
# Verwijderen of hernoemen van bestanden

import os

# belangrijke constanten
print(os.sep)  #  pathname separator ('/' of '\\')
print(os.linesep)  # is the line separator in text files ('\n' or '\r\n')

# Huidige werkdirectory ophalen
print("Huidige map:", os.getcwd())

# 🚪 Veranderen van werkdirectory
os.chdir("../..")  # Ga één map omhoog
print("Nieuwe map:", os.getcwd())

# Mappen maken
os.mkdir("voorbeeldmap")  # maakt een map
os.makedirs("project/data/logs")  # Maakt alle tussenliggende mappen


# Geeft een lijst van bestanden en mappen
files = os.listdir("..")
print("Inhoud van de map:", files)

# Bestanden en mappen verwijderen
# os.remove() – Verwijdert een bestand
# os.rmdir() – Verwijdert een lege map
# os.removedirs() – Verwijdert geneste lege mappen

os.remove("test.txt")
os.rmdir("voorbeeldmap")

# os.rename() – Hernoemt een bestand of map
# os.path.exists() – Controleert of een pad bestaat
# os.path.join() – Combineert paden op platform-onafhankelijke manier
# python
path_ = os.path.join("project", "data", "bestand.csv")
if os.path.exists(path_):
    print("Bestand gevonden:", path_)

if os.path.isdir(path_):
    print("Pad is een map")

if os.path.isfile(path_):
    print("Pad is een map")

