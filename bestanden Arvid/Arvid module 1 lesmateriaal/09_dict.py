"""
Een dict is een samengesteld datatype dat werkt zoals een woordenboek.
In een woordenboek zoek je een woord om dan de betekenis te lezen.

achromatisch; bn licht doorlatend zonder breking van kleuren
acht: I zn v (m) cijfer 8 II geven of slaan, in _ nemen: letten op
achtbaar: bn eerwaardig
achtbladig: bn met acht bladen

In python maak je een lege dict met {}.
"""

empty = {}
print(empty)
print(type(empty))

empty = dict()
print(empty)
print(type(empty))

"""
Je kan ook een dict meteen vullen.
{ sleutel1 : waarde1,
  sleutel2 : waarde2,
  sleutel3 : waarde3 }
  
De sleutels (links van :) moeten uniek zijn.
De waardes (rechts van :) kunnen dezelfde waarde hebben. 
Net zoals twee woorden (sleutel) dezelfde betekenis kunnen hebben. 
"""

dictionary = {
    "achromatisch": "bn licht doorlatend zonder breking van kleuren",
    "acht": "I zn v (m) cijfer 8 II geven of slaan, in _ nemen: letten op",
    "achtbaar": "bn eerwaardig",
    "achtbladig": "bn met acht bladen"
}

print(dictionary)
print(type(dictionary))

"""
Een dict laat toe om snel data terug te vinden op basis van een sleutel.
"""
print(dictionary["acht"])
print(dictionary["achtbaar"])

print(dictionary["tien"])  # sleutel bestaat niet => key_error
print(dictionary["Acht"]) # sleutel bestaat niet => key_error

"""
De methode  woordenboek.get(key) geeft een None terug als de sleutel niet bestaat.
Dat is veiliger dan woordenboek[key] 
"""
print(dictionary.get("acht"))
print(dictionary.get("Acht"))

# Als get de sleutel niet vindt, dan wordt standaard None teruggegeven.
# Je kan ook meegeven welke waarde je wil terugkrijgen als de sleutel niet bestaat.
print(dictionary.get("Acht", "Staat niet in het woordenboek"))

# opdracht: maak een dict digits die de 10 cijfers mapt op hun naam.  0 -> "zero, 1 -> "een", ...
# Oplossing
digits = {0: "zero",
          1: "een",
          2: "twee",
          3: "drie",
          4: "vier",
          5: "vijf",
          6: "zes",
          7: "zeven",
          8: "acht",
          9: "negen"}
print(digits)

print(len(dictionary))

# alle sleutels oplijsten
print(f"{list(dictionary.keys())=}")
for key in dictionary:
    print(key)

# alle sleutels oplijsten, 2de mogelijkheid
for key in dictionary.keys():
    print(key)

# alle waardes oplijsten
print(f"{list(dictionary.values())=}")

# alle items oplijsten (key, waarde)
print(f"{list(dictionary.items())=}")

# itereren over de items
# de items van een dict zijn lijst van 2-tuples: [(key1, value1), (key2, value2), ... ]
for item in dictionary.items():
    print(item[0], "betekent", item[1])


# vermits de items 2-tuples zijn, kan ze meteen uitpakken in 2 variabelen
for key, value in dictionary.items():
    print(key, "betekent", value)

# opdracht itereer over de digits(dict)

# om de waarde die bij een key hoort aan te passen
dictionary["acht"] = "Gewoon acht"
print(dictionary)

# Waardes toevoegen
dictionary["achillishiel"] = "kwetsbare plaats"  # voegt één key:waarde toe
print(dictionary)

# waarde verwijderen
dictionary.pop("acht")
print(dictionary)
dictionary.pop("acht")  # genereert een key_error want "acht" zit niet meer in de dict




# keys hoeven geen strings te zijn.
number_names = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five"}
print(number_names[2])

# values  hoeven geen strings te zijn.
math_rows = {
    "even" : [1, 2, 4, 6, 8],
    "odd" :[1, 3, 5, 7, 9],
    "all" : [1, 2, 3, 4, 5, 6, 7, 8, 9],
    "powers of 2": [1, 2, 4, 8, 16, 32, 64, 128, 256],
    "fib": [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
}
print(math_rows["even"])

<ont_do_this = {
    1: "one",
    "odd": 2,
    False: "Onwaar",
    None : "Onbestaand"}
print(dont_do_this)


# opdracht
# schrijf een loop die naam en geslacht ('M'/'F') inleest
# en telkens een dict aanvult met naam: geslacht

genders = {}
while True:
    name = input("Geef een naam in: ")
    if name == "Stop":
        break
    gender = input("Geef een geslacht in: ")
    genders[name] = gender

print(genders)

# opdracht past de vorige oplossing aan zodat een
# naam enkel maar wordt toegevoegd als die nog niet voorkomt.
genders = {}
while True:
    name = input("Geef een naam in: ")
    if name == "Stop":
        break
    gender = input("Geef een geslacht in: ")
    if name not in genders:
        genders[name] = gender

print(genders)



"""
- dict is niet “gesorteerd”; het is “invoeg-geordend”. 
  De volgorde hangt af van wanneer je sleutels toevoegt.
  keys(), values() en items() volgen dezelfde invoegvolgorde.
- Een bestaande sleutel opnieuw toewijzen verandert diens  positie niet.
- Verwijderen en opnieuw toevoegen plaatst de sleutel aan het einde.
- update() voegt sleutels toe in de iteratievolgorde van de bron.
- popitem() verwijdert het laatst toegevoegde item (LIFO).
- Gelijkheid van dicts negeert volgorde: twee dicts zijn gelijk als ze dezelfde key-value paren hebben, ongeacht volgorde.
- Heb je een echte sortering nodig, gebruik dan sorted(...) bij het itereren, of gebruik collections.OrderedDict alleen als je de extra order-methoden (zoals move_to_end) nodig hebt.
"""


########## Hier is de lest op 2/10 gestopt



# opdracht :
# def remove_keys(dct: dict, keys: list):
#     # todo: remove all items with a key in keys from dict


# uitdaging
# def remove_values(dct: dict, values: list):
#     # todo: remove all items with a value in values from dict




def text_statistics(text: str) -> dict:
    """
    Count how many times each letter appears in text.
    :param text: Text to analyze
    :return: dict with a count per letter
    """
    ret = dict()
    for letter in text:
        if not letter.isalpha():
            continue
        letter = letter.lower()
        if letter in ret:
            ret[letter] += 1
        else:
            ret[letter] = 1
    return ret


def text_statistics2(text: str) -> dict:
    """
    Count how many times each letter appears in text.
    :param text: Text to analyze
    :return: dict with a count per letter
    """
    ret = dict()
    for letter in text:
        if not letter.isalpha():
            continue
        letter = letter.lower()
        ret.setdefault(letter, 0)
        ret[letter] += 1

    return ret

def print_stats(text :str) -> None:
    """
    Print the statistics of text.
    :param text: Text to analyze
    """
    statistics = text_statistics(text)
    for letter in statistics:
        print(letter, statistics[letter])
    statistics = text_statistics2(text)
    for letter in statistics:
        print(letter, statistics[letter])

text = """ dict is niet “gesorteerd”; het is “invoeg-geordend”. 
  De volgorde hangt af van wanneer je sleutels toevoegt.
  keys(), values() en items() volgen dezelfde invoegvolgorde.
- Een bestaande sleutel opnieuw toewijzen verandert diens  positie niet.
- Verwijderen en opnieuw toevoegen plaatst de sleutel aan het einde.
- update() voegt sleutels toe in de iteratievolgorde van de bron.
- popitem() verwijdert het laatst toegevoegde item (LIFO).
- Gelijkheid van dicts negeert volgorde: twee dicts zijn gelijk als ze dezelfde key-value paren hebben, ongeacht volgorde.
- Heb je een echte sortering nodig, gebruik dan sorted(...) bij het itereren, of gebruik collections.OrderedDict alleen als je de extra order-methoden (zoals move_to_end) nodig hebt. """

print_stats(text)

dictionary.update(Accu="accumulator", Aceton ="Azijngeest")
print(dictionary)

# je kan een hele dict toevoegen
dictionary.update({'Accuraat': 'bn & bw nauwkeurig', 'accordeon': ' v & m harmonika'})
print(dictionary)


