# we kennen intussen the basis vorm van try except
try:
    print(1/0)
except ZeroDivisionError as e:
    print(f"Error: {e}")


# try except meot niet noodzakelijk meteen rond de code staan die misgaat
def divide(numerator: float, denominator: float) -> float:
    """
    Divides two numbers
    :param numerator: left side of division
    :param denominator: right side of division
    :return: division result
    """
    return numerator / denominator

def repeat_division() -> None:
    """
    Ask the user for numbers and print the result of the division
    """
    while True:
        try:
            numerator = float(input("Geef een numerator?"))
            if numerator == "Stop":
                return
            denominator = float(input("Geef een denominator?"))
            if denominator == "Stop":
                return
            print(f"{divide(numerator, denominator)=}")
        except ValueError as e:
            print(f"Error: {e}")

try:
    # repeat_division()
    pass
except ZeroDivisionError as e:
    print(f"Error: {e}")

# Je kan ook zelf een exception genereren
# Je gooit dan zelf een exception op die ergens anders in jouw code opgevangen wordt,
# of die het programma doet stoppen

def bake_cookies() -> None:
    """
    Ask the user for a baking time and check if it's within the correct range
    """
    time = int(input("Baktijd in minuten: "))
    if time < 5:
        raise ValueError("Te kort. Het deeg zal nog zacht zijn")
    elif time > 15:
        raise ValueError("Te lang! De koekjes zullen zwart zijn")




bake_cookies()
print("Mmm, lekkere koekjes")

try:
    bake_cookies()
except ValueError as e:
    print(f"Verkeerde baktijd: {e}")
    exit(0)
print("Mmm, lekkere koekjes")

# Je kan aan een try: except: blok een else deel toevoegen
# Het else blok wordt aangeroepen als er geen exception plaatsvindt in het try blok

try:
    bake_cookies()
except ValueError as e:
    print(f"Verkeerde baktijd: {e}")
else:
    print("Mmm, lekkere koekjes")  # wordt enkel uitgevoerd als er geen exception plaatsvindt in bake_cookies()

# Je kan  een finally: blok toevoegen.
# Het finally blok wordt altijd uitgevoerd ongeacht of er een exception plaatsvindt in het try blok of niet.

try:
    bake_cookies()
except ValueError as e:
    print(f"Verkeerde baktijd: {e}")
else:
    print("Mmm, lekkere koekjes")  # wordt enkel uitgevoerd als er geen exception plaatsvindt in bake_cookies()
finally:
    print("Poets nu de keuken.")


# na een try block moest minstens een except of een finally block staan
try:
    x = int(input("Geef een getal in: "))
    x= 10 / x
finally:
    print("Einde van de programma")



def write_to_file(path:str, text:str) -> str:
    """
    Try to write text to a file
    :param path: full path to the file
    :param text: text to write
    :return: result message
    """
    try:
        file = open(path, "w")
        file.write(text)
    except IOError:
        return "Fout bij schrijven naar bestand."
    else:
        return "Bestand succesvol geschreven."
    finally:
        file.close()
        print("Bestand gesloten.")

# Opdracht maak gebruik van een try/except/else/finally blok om te bepalen of een bestand leeg is.
# is_empty(path:str) -> bool.   True/False of None bij problemen
def is_empty(path:str) -> bool:
    """
    Determine if a file is empty
    :param path: Full path to the filename
    :return: None in case of error, True if file is empty, False if file is not empty
    """
    try:
        file =  open(path, "r")
        contents = file.read()
        if not contents:
            raise ValueError("Bestand is leeg.")
    except FileNotFoundError:
        return None
    except ValueError as fout:
        return False
    else:
        return True
    finally:
        print("Controle afgerond.")



