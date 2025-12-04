# opdracht 1: schrijf een functie uniq(lst: list) -> bool die controleert
# of een gegeven lijst dubbele waardes bevat
#  Voor wie al meer python kent: je mag hiervoor geen set gebruiken.
# uniq([]) -> False
# uniq([1,2]) -> False
# uniq([1,2,1]) -> True
# uniq(['A','B','A'])-> True
# uniq(['A','B','C'])-> True

def uniq(lst: list) -> bool:
    for val in lst:
        if lst.count(val) > 1:
            return False
    return True

def uniq2(lst: list) -> bool:
    for i in range(len(lst)):
        val = lst[i]
        for j in range(i+1, len(lst), 1):
            if lst[j] == val:
                return False
    return True

# opdracht 2:
# Je hebt een dictionary met punten voor verschillende vakken.
grades = {
    "wiskunde": 7.5,
    "nederlands": 8.0,
    "geschiedenis": 6.5,
    "biologie": 9.0
}
# Schrijf een functie calculate_average(grades: dict) -> float
# die het gemiddelde van alle punten berekent.

def calculate_average(grades: dict) -> float:
    """
    Calculate the average of all grades
    :param grades: dict with grades
    :return: average
    """
    return sum(grades.values()) / len(grades)

# Opdracht 3:
nl_to_en = {
    "hond": "dog",
    "kat": "cat",
    "vis": "fish",
    "vogel": "bird"
}

# Schrijf een functie translate_to_english(text: str) -> str die een woord
# vertaalt naar het engels. Als het woord niet in de dict voorkomt,
# dan is de vertaling "Ik ken het woord niet"
# Los dit op met twee manieren:
#  - zonder een try except blok
#  - met een try except blok

def translate_to_english_no_try(text: str) -> str:
    return nl_to_en.get(text, "Ik ken het woord niet")

def translate_to_english_try(text: str) -> str:
    try:
        return nl_to_en[text]
    except KeyError:
        return "Ik ken het woord niet"


# opdracht 4:
# Je krijgt deze dict.
names_to_gender = {"Maggie":"F",
                   "Bart":"M",
                   "Homer":"M",
                   "Lisa": "X",
                   "Marge": "F"}
# Schrijf een function die telt hoeveel mannen en vrouwen er zijn.

def count_gender(dct: dict) -> (int,int):
    count_m = count_f = 0
    count_m = 0
    count_f = 0
    for gender in dct.values():
        if gender == 'F':
            count_f += 1
        elif gender == 'M':
            count_m += 1
        if gender == 'F':
            count_f += 1
        else:
            count_m += 1
    return count_m, count_f


# Opdracht 5:
# Transformeer names_to_gender naar gender_to_names
# Het resultaat is een dict van deze vorm:
# { "F": ["Lisa", "Marge", "Maggie"],
#  "M": ["Homer", "Bart" ]}
# De volgorde van de namen is niet belangrijk
# Hint: Maak een dict ret = {"F":[], "M":[]}
#       Overloop de items in names_to_gender
#       Als het M is, vraag ret["M"] op en voeg de naam toe
#       Als het F is, vraag ret["F"] op en voeg de naam toe

gender_to_names = { "F": [], "M": []}
for name, gender in names_to_gender.items():
    if gender == 'F':
        gender_to_names["F"].append(name)
    elif gender == 'M':
        gender_to_names["M"].append(name)

