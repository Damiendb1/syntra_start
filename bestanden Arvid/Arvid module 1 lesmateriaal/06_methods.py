# Stel we hebben een lijst met kwadraten, en willen die printen.
# Daarna willen we het volgende kwadraat toevoegen en weer de hele lijst printen
# Daarna willen we nog een kwadraat toevoegen en weer de hele lijst printen.
# Je krijgt dan veel herhaling van dezelfde code.

powers = [1, 4, 9, 16, 25]

print("start list")  # 1ste keer
for i in range(len(powers)):
    print(powers[i])
print("einde list")

powers.append(36)

print("start list")  # herhaling
for i in range(len(powers)):
    print(powers[i])
print("einde list")

powers.append(49)
print("start list") # herhaling 2
for i in range(len(powers)):
    print(powers[i])
print("einde list")

# Om te vermijden dat twee of meer keer dezelfde code moeten typen
# kunnen we aan python nieuwe functies leren
# Een functie is een stuk code dat een specifieke taak uitvoert,
# en daarvoor eventueel data aangereikt krijgt.

# Een functie heeft steeds dezelfde vorm

# def naam_functie():
#     code
#     code
#     code

# * Het keyword def maakt duidelijk dat we iets gaan definiëren.
# * Gevolgd door de naam van de functie. Hiervoor gelden dezelfde regels
#   als voor variabelen.  Kort en krachtig
# * Gevolgd door haakjes, met ertussen de data die we aanleveren
#   Als de functie geen data nodig heeft, dan staat er niets tussen de haakjes
# * Gevolgd door een : om aan te geven dat daarna de code volgt


# voorbeeld zonder parameters
# print een lijn met sterretjes omringd door lege lijnen
def print_line():  # dit definieert een functie
    print()
    print('*' * 100)
    print()

print_line() # dit voert een functie uit.

# voorbeeld met 1 parameter
def print_list(input_list):
    print("start list")
    for i in input_list:
        print(i)
    print("einde list")

# De methode print_list verwacht dat de gebruiker een lijst meegeeft, telkens print_list wordt opgeroepen.
even = [0, 2, 4, 6]
print_list(even)  # even is een lijst, die we als parameter meegeven.

# Als we print_list(even) oproepen, springt python naar: def print_list(input_list)
# tegelijk wordt de lijst even meegegeven. In print_list wordt de waarde van even
# overgeheveld in de waarde input_list.
# De code in print_list() wordt uitgevoerd, dus worden alle waarden afgedrukt.
# Op het einde van een functie springt Python terug naar waar
# de functie werd opgeroepen.

print_list(powers)  # alle kwadraten uit de lijst worden afgedrukt
print_list(["Homer", "Marge", "Bart", "Lisa"])  # de vier namen worden afgedrukt.


# Een functie kan ook andere functies oproepen.

def print_list_starred(input_list):
    print_line()
    print_list(input_list)
    print_line()

# Een method kan 0, 1 of meer parameters hebben.
def print_list_2(input_list, label):
    print("start lijst: ", label)
    for i in range(len(input_list)):
        print(input_list[i])
    print("einde list")

print_list_2(powers, "machten")
print_list_2([0,2,4, 6], "getallen deelbaar door 2")

# Voeg je een duidelijke beschrijving toe aan de methode.
# Dit is niet verplicht voor python, maar wel verplicht in de best practices
# Het helpt pycharm ook om jou te helpen.

def print_list_3(input_list, label):
    """
    Print a list with a label
    :param input_list: List to print
    :param label: Label to print
    """
    print("start lijst: ", label)
    for i in range(len(input_list)):
        print(input_list[i])
    print("einde list")

# Voeg ook het verwachte type to aan de parameters
# Dit is wederom niet verplicht voor python, maar wel verplicht in de best practices
# Het helpt pycharm ook om jou te helpen.

def print_list_4(input_list: list, label: str):
    """
    Print a list with a label
    :param input_list: List to print
    :param label: Label to print
    """
    print("start lijst: ", label)
    for i in range(len(input_list)):
        print(input_list[i])
    print("einde list")


# pas op voor recursie.
# Recursie gebeurt wanneer een functie zichzelf oproep.
# Er zijn situaties waar recursie gewenst is, maar veelal gebeurt het per ongeluk.

def print_stars():
    """
    Prints 2 lines of stars
    """
    print("*" * 100)
    print_stars()

print_stars()  # =>  RecursionError: maximum recursion depth exceeded


# Python voert een functie uit tot de laatste code en springt dan terug naar de oproepende code.
# Met een return commando verplicht je Python om al eerder terug te springen.

def fever(temp: float):
    """
    Print the body temperature label for a human body.
    """
    if temp < 36.6:
        print("Onderkoeld")
        return
    if temp < 37.5:
        print("Normaal")
        return
    if temp < 38.0:
        print("verhoging")
        return
    if temp < 40:
        print("Koorts")
        return
    print("Dodelijke koorts.")

print(fever(41))
print(fever(36.8))



def print_line(msg:str, surround:bool):
    """
    Print a text, optionalyy surrounded by stars.
    :param msg: Text to print
    :param surround: if True, surround the text with starrs
    """
    if surround:
        print('*' * 40)
    print(msg)
    if surround:
        print('*' * 40)

print_line("Ik ben een bank automaat", True)
print_line("Ik ben een bank automaat", False)

# Als we er vanuit kunnen gaan dat de gebruiker meestal kies voor sterretjes
# Dan kunnen we daar de default value van maken.

def print_line_2(msg:str, surround:bool = True):
    """
    Print a text, optionally surrounded by stars.
    :param msg: Text to print
    :param surround: if True, surround the text with starrs
    """
    if surround:
        print('*' * 40)
    print(msg)
    if surround:
        print('*' * 40)

# De oproepende code blijf hetzelfde.
print_line_2("Ik ben een bank automaat", True)
print_line_2("Ik ben een bank automaat", False)
# maar er komt een derde mogelijkheid bij
print_line_2("Ik ben een bank automaat")  # Debug deze oproep en je zal zijn dat surround True wordt in de uitvoering


# parameters met een default waarde moeten rechts komen van de parameters zonder default waarde

def print_line_3(msg:str, char: str = '*', surround:bool = True):
    """
    Print a text, optionally surrounded by stars.
    :param msg: Text to print
    :param char: character to print in surrounding lines
    :param surround: if True, surround the text with starrs
    """
    if surround:
        print(char * 40)
    print(msg)
    if surround:
        print(char * 40)

print_line_3("Ik ben een bank automaat", "*", True)
print_line_3("Ik ben een bank automaat", "-", False)
print_line_3("Ik ben een bank automaat", "-")
print_line_3("Ik ben een bank automaat")

# Je kan bij het oproepen van een functie meegeven welke waarde bij welke parameter hoort.

def ordered(i: int, j: int, k: int):
    """
    Print whether i, j, k are in ascending order
    """
    if i <= j <= k:
        print("De waarden zijn gesorteerd.")
    else:
        print("De waarden staan niet in volgorde")


print(ordered(1,4,5))
print(ordered(1,5,5))
print(ordered(k=1,j=5,i=6))
print(ordered(j=1,k=5,i=6))

