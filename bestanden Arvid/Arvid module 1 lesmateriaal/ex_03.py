"""
Maak een lege lijst
Blijf aan de gebruiker namen vragen
Voeg de naam telkens toe aan de lijst
Stop als de gebruiker 'Stop' ingeeft als naam.
Print de lijst
"""

names = []
while True:
    name = input("Geef een naam in: ")
    if name == "Stop":
        break
    names.append(name)
print(names)

def print_reverse1(lst: list):
    """
    Print a list in reverse order
    :param lst: input list
    """
    temp_list = lst[::-1]
    print(temp_list)

def print_reverse2(lst: list):
    """
    Print a list in reverse order
    :param lst: input list
    """
    temp_list = []
    for val in lst:
        temp_list.insert(0, val)
    print(temp_list)

def print_reverse3(lst: list):
    """
    Print a list in reverse order
    :param lst: input list
    """
    lst.reverse()
    print(lst)
    lst.reverse()

"""
3/ Schrijf een method waaraan je een lijst meegeeft en twee getallen. De method print de waardes uit de lijst van index getal1 tot index getal2
"""
def print_slice(lst: list, start:int, end: int):
    """
    Prints a sliced portion of a list to the standard output.
    :param lst: The list from which a slice will be printed.
    :param start: The starting index for the slice (inclusive).
    :param end: The ending index for the slice (exclusive).
    """
    print(lst[start:end])


"""
4/ Schrijf een functie die de maat van een broek omzet naar S/M/L/XL
"""

def print_trouser_size1(size: float):
    """
    Prints the name of a trouser size.
    :param size: Size of the trouser
    """
    if size < 40:
        print("Small")
        return
    if size < 50:
        print("Medium")
        return
    if size < 60:
        print("Large")
        return
    if size < 70:
        print("XL")
        return
    print("XXL or larger")

def print_trouser_size2(size: float):
    """
    Prints the name of a trouser size.
    :param size: Size of the trouser
    """
    if size < 40:
        ret = "Small"
    elif size < 50:
        ret = "Medium"
    elif size < 60:
        ret = "Large"
    elif size < 70:
        ret = "XL"
    else:
        ret = "XXL or larger"
    print(ret)
