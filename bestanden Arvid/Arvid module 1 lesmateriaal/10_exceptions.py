# In Python kan op veel plaatsen iets mis gaan.

def ask_integer() -> int:
    """
    Ask the user to input an integer
    :return: The integer provided by the user
    """
    # volgende lijn gaat mis indien de input bijvoorbeeld een letters is
    val = int(input("Geef een geheel getal in: "))
    return val


def odd(val: int) -> bool:
    """
    Check if the value is odd
    :param val: value to check
    :return: True is value is odd
    """
    return val % 2 == 1

def ask_integer2():
    # versie
    val = input("Geef een geheel getal in: ")
    try:
        return int(val)
    except:
        # Dit stuk code wordt uitgevoerd als int(val) faalt en Python een exception 'gooit'
        print(val," is geen getal. je krijgt een 0")
        return 0

def ask_integer3():
    # Op deze manier verplicht je de gebruiker om een geheel getal in te voeren
    # Als hij een fout maakt, geef je een foutmelding en laat je opnieuw proberen
    while True:
        val = input("Geef een geheel getal in: ")
        try:
            return int(val)
        except:
            print(val," is geen getal. Probeer opnieuw")

def ask_integer4():
    while True:
        val = input("Geef een geheel getal in: ")
        try:
            return int(val)
        except Exception as e:
            # We vangen de exception en stockeren deze in de variabele e
            # e mag ook een andere variablenaam zijn
            # We kunnen nu ook de reden van het probleem afdrukken
            print(val,f" is geen getal. reden {e} Probeer opnieuw")


"""
Er is een hele hierarchy van exceptions.
BaseException
├── SystemExit
├── KeyboardInterrupt  
├── GeneratorExit
└── Exception          # <- Dit is wat je normaal vangt
    ├── ValueError
    ├── TypeError
    ├── ZeroDivisionError
    └── ... (alle "normale" exceptions)
"""

def ask_integer5() -> int:
    while True:
        val1 = input("Geef een eerste geheel getal in: ")
        val2 = input("Geef een tweede geheel getal in: ")
        try:
            # dit kan op 3 manieren misgaan
            # int(val1) kan falen als val1 geen geheel getal is
            # int(val2) kan falen als val2 geen geheel getal is
            # int(val1)/int(val2) kan falen als val2 0 is
            return int(val1)//int(val2)
        except TypeError as reden:
            # We vangen op dat val1 of val2 geen geheel getal is
            print(val1, "of", val2, f"is geen getal. reden {reden} Probeer opnieuw")
        except ZeroDivisionError as reden:
            # We vangen op dat val2 0 is
            print(f"Deling door 0: {reden}, probeer opnieuw")


def main():
    """
    This program asks the user to input an integer and checks if it is odd.
    """
    while True:
        print("0 stopt het programma")
        number = ask_integer5()
        if number == 0:
            return
        if odd(number):
            print("Het getal is oneven")
        else:
            print("Het getal is een even getal")

main()


"""
Gebruik specifieke exceptions (ValueError, FileNotFoundError) in plaats van bare except:
Catch alleen wat je verwacht: Te brede exception handling verbergt bugs
Geef duidelijke feedback aan de gebruiker
Vermijd lege except blocks: Altijd iets doen (minimaal loggen)
"""

# opdracht:
# maak een lijst met 5 elementen
# vraag de gebruiker een getal (n)
# Haal print het n-de getal uit de lijst
# Zorg er voor da  het programma niet fout gaat als
# de gebruiker geen getal invoert, of n geen correcte index
# van de lijst is.



