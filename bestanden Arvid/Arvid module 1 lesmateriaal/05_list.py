# een list is een collectie waarden.
#    - de volgorde wordt behouden
#    - de inhoud kan gewijzigd worden
#    - de lengte kan gewijzigd worden
#    - waarden mogen meermaals voorkomen
# een lege lijst maken kan als:
#  l1 = list()
#  l1 = []
#
# een lijst kan meteen waardes bevatten
# l = [waarde1, waarde2, waarde3


lst = list()
print(lst)
print(type(lst))

lst = []
print(lst)

# Je kan een lijst vullen met een willekeurig aantal waarden
lst = ['Homer', 'Bart', 'Lisa', 'Marge', 'Maggie']
print(lst)

# len(lst)  retourneert het aantal elementen in een lijst
# len([])  -> 0
# len([1,2,3]) -> 3
print("Er zijn",len(lst), "namen in de lijst.")

# met 'for' kan je itereren door elke element van de lijst
for name in lst:
    print(name)

lst = lst + ["Barny", 'Apu']
for name in lst:
    print(name)

search = input("Geef een naam in om te zoeken: ")
for name in lst:
    if name == search:
        print(name, "zit in de lijst.")
        break

# in operator
# var in list  -> True als waarde voorkomt in de lijst
if search in lst:
    print(search, " zit in de lijst.")
else:
    print(search, " zit niet in de lijst.")

# de volgorde in een lijst is gegarandeerd.
# Het is dus mogelijk om het n-de element van een lijst op te vragen
# door gebruik te maken van [ en ]

# indexing
print("Het eerste element :", lst[0])
lst[3] = "Nieuwtje"
print("Het tweede element :", lst[1])

for i in range(len(lst)):
    print(lst[i])

i = 0
while i < len(lst):
    print(lst[i])
    i = i + 1

# negatieve indexing
print("Het laatste element :", lst[-1])
print("Het voorlaatste element :", lst[-2])


# Je kan ook een deel van de lijst opvragen
print("Element 2 tot en met 4:", lst[1:5])
print("Alle element tot het 5", lst[:5])
print("Alles behalve de laatste 2 :", lst[:-2])
print("Volledige copy :", lst[:])


# sorted(lst) retourneert de gesorteerde lijst maar laat de lijst ongewijzigd
print(sorted(lst))
print(lst)

lst.sort()  # de lijst wijzigt naar de gesorteerde lijst
print(lst)

lst.reverse()  # de lijst wordt omgekeerd
print(lst)

lst.append("Arvid") # voegt een element achteraan de lijst toe


lst.insert(3, "Mo")  # voegt een element in de gevraagde positie in de lijst toe
# Opgelet: insert gebruik je beter niet bij erg grote lijsten.
print(lst)


lst.append("Mo")
print(lst.index("Mo"))  # positie van 'Mo'
print(lst.count("Mo"))  # aantal 'Mo's in de lijst

lst.remove("Mo")  # verwijder eerste 'Mo' uit de lijst
print(lst)

second = lst.pop(1) # retourneert en verwijdert het tweede element

lst *= 2
print(lst)

