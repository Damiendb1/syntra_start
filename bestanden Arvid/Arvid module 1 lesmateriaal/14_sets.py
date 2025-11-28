# Reeds behandelde collectie datatypes: list, tuple en dict
# Python heeft nog een ingebouwd datatype: set
# Een set is een collectie van unieke waardes zonder behoud van volgorde.

# Er is maar 1 manier om een lege set
empty_set = set()  #  {} is een dict

# Om een set te maken met waardes:
# Zet de waardes tussen accolades (EN: curly braces)
filled_set = {1, 2, 3, 4, 5}
print(type(filled_set))
print(filled_set)
print(len(filled_set))


# net als de andere collecties, kan je itereren over een set
for value in filled_set:
    print(value)

# een element toevoegen via add()
# De functie heet bewust niet append() zoals bij list, omdat je nooit met zeker weer waar in de lijst
# een waarde zal toegevoegd worden.
filled_set.add(6)
print(filled_set)
print(len(filled_set))

# het toevoegen van een waarde die reeds in een set zit, heeft geen effect.
filled_set.add(4)
print(filled_set)
print(len(filled_set))

# een element verwijderen kan met twee methodes
# discard() is een veilige methode. Werkt ook als de waarde niet in het set zit.
filled_set.discard(7)     # Remove safely (no error)
# remove is een strikte methode. Genereert een key_error als de waarde niet in het set zit.
try:
    filled_set.remove(7)      # Remove item (KeyError if not found)
except KeyError:
    print("element niet gevonden")

# bij kleine sets met eenvoudige waardes zal de volgorde lang bewaard worden, maar dit is niet gegarandeerd.
for i in range(10000):
    filled_set.add(i)
print(filled_set)  # waarschijnlijk in volgorde

filled_set = set()
for i in range(100):
    filled_set.add(f"{i} : {'*'*i}")
print(filled_set) # bijna zeker niet meer in volgorde

try:
    print(filled_set[1])
except:
    print("set is niet indexeerbaar")


# sets zijn vergelijkbaar
s1 = {1, 2, 3}
s2 = {4, 5, 6}
s3 = { 3, 2, 1}
print(f"{s1 == s2=}")
print(f"{s1 != s2=}")
print(f"{s1 == s3=}")

# toepassingen:
# Deduplication
# De set() methode is een eenvoudige manier om dubbele waardes uit een lijst te halen.
# je kan een list omzetten naar een set
l = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]
s = set(l)
print(s)
print(len(s))

def uniq(lst: list) -> bool:
    l_set = set(lst)
    if len(l_set) == len(lst):
        return True
    else:
        return False
    # of korter:
    # return len(lst) == len(set(lst))

print(f"{uniq([1,2,3,4,5])=}")
print(f"{uniq([1,2,3,3,5])=}")

names_to_gender = {"Maggie":"F",
                   "Bart":"M",
                   "Homer":"M",
                   "Lisa": "F",
                   "Marge": "F"}

only_females =  set(names_to_gender.values()) == {'F'}
print(only_females)

# een set mag enkel onwijzigbare waardes bevatten.
try:
    names = { ["1", "Homer"], ["2", "Marge"] }
    print(names)
except TypeError:
    print("set mag geen lijst bevatten")

try:
    names = {("1", "Homer"), ("2", "Marge")}
    print(names)
except TypeError:
    print("set mag geen lijst bevatten")


# om er voor te zorgen dat een set niet wijzigbaar is, maar alleen leesbaar is,
# kan je de set omzetten naar een frozenset
l = [2, 4, 6]
f_set = frozenset(l)
print(f_set)
print(type(f_set))
try:
    f_set.add(3)
except AttributeError:
    print("set is niet wijzigbaar")

# Nut van frozenset:
# - Een set is wijzigbaar, dus een set kan geen sets bevatten, wel frozensets
# - Een set is wijzigbaar, dus een set kan geen key zijn in een dict, frozensets wel

# s = {{3,2}}  # TypeError: unhashable type: 'set'
s = {frozenset({3,2})}
print(s)


# overzicht datatypes:
#      list: volgorde blijft behouden,      dubbele waarden blijven behouden,     indexeerbaar,        kan gewijzigd worden
#     tuple: volgorde blijft behouden,      dubbele waarden blijven behouden,     indexeerbaar,        kan niet gewijzigd worden
#       set: volgorde blijft niet behouden, dubbele waarden worden niet behouden, niet indexeerbaar,   kan gewijzigd worden
# frozenset: volgorde blijft niet behouden, dubbele waarden worden niet behouden, niet indexeerbaar,   kan niet gewijzigd worden
#      dict: volgorde blijft behouden,      dubbele keys worden niet behouden,    indexeerbaar op key, kan gewijzigd worden



# opdracht 1:
# Vraag de gebruiker om woorden in te geven ("Stop" stopt). Geef na elk woord feedback of het woord al eens gegeven is.

history =  set()
while True:
    word = input("Geef een woord:")
    if word == 'Stop':
        break
    if word in history:
        print("Woord is al gegeven")
    else:
        print("Woord is nog niet eerder gegeven")
        history.add(word)


# opdracht 2:
# Vraag de gebruiker om woorden in te geven ("Stop" stopt).
# Geef pas op het einde feedback of er dubbele woorden zijn ingegeven.


# Je krijgt een dict die "Voornaam" mapt op "Familienaam".
dct={ "Arvid": "Claassen",
      "Nico" : "Van den Branden",
      "Patrick" : "Heirwegh",
      "Alexander": "Van den Branden",
      "Sofie": "Agten",
      "Karel": "De Rammelaere",
      "Arvid": "Van Tychem",
      "Homer": "Simpson"
      }
print(dct)
# opdracht 3: maak een set van alle familienamen
print(set( dct.values()))
# opdracht 4: Controleer of er een dubbele familienaam in zit: True/ False
print(len(set( dct.values())) != len(dct.values()))
# opdracht 5: Maak een set met alle dubbele voornamen.
# kan niet voorkomen vermits de keys in een dict per definite uniek zijn.

