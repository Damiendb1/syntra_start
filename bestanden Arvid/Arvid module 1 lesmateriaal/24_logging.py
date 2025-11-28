# Logging is het systematisch vastleggen van gebeurtenissen in je applicatie.
# sommige boodschappen zijn belangrijk sommige zijn details.

def safe_division(numerator: float, denominator: float) -> float | None:
    print("informatief: ", numerator, "/", denominator, " =")
    try:
        print("debug", numerator / denominator)
        result = numerator / denominator
        return result
    except ZeroDivisionError:
        print("error: kan niet delen door 0")
        return None

# Code staat vol print statements
# Als de code ontwikkeld en getest is, mogen de meeste print
# statements weggelaten worden. Maar je e kan minder belangrijke boodschappen niet eenvoudig weglaten.

"""
debug (laagste niveau)
  Gedetailleerde diagnostische informatie tijdens ontwikkeling
  Variabele waarden, functie parameters, loop iteraties

info
  Bevestiging dat dingen werken zoals verwacht
  Applicatie gestart, gebruiker ingelogd, taak voltooid
 
  
warning 
  Iets onverwachts gebeurde, maar applicatie werkt nog
  Deprecated functies, lage schijfruimte, fallback gebruikt

error
  Serieus probleem, een functie kon niet uitgevoerd worden
  Database fout, bestand niet gevonden, API timeout

critical (hoogste niveau)
  Zeer ernstig probleem, applicatie kan mogelijk niet verder
  Database server down, out of memory, configuratie corrupt
"""


import logging

# basis configuratie van logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(message)s')

logging.basicConfig(level=logging.WARNING,
                    format='%(asctime)s %(levelname)s %(message)s')
# basis config voor loggen naar file
logging.basicConfig(level=logging.DEBUG,
                    filename="d:/dev/learning/log.txt",
                    format='%(message)s')


def safe_division_log(numerator: float, denominator: float) -> float:
    logging.warning("waarschuwing: deze functie werkt misschien nog niet")
    try:
        logging.debug(f"debug {numerator=} / {denominator=}")
        result =  numerator / denominator
        logging.info(f"informatief: {result}")
        return result
    except ZeroDivisionError:
        logging.error("error: kan niet delen door 0")
        return None

# Afhankelijk van de basis configuratie bovenaan:
#    log  level
#    formaat van boodschap
#

print(safe_division_log(10, 5))
print()

print(safe_division_log(10, 0))


# oefening:
# Schrijf een function die een getal tussen 1 en 10 vraagt:
# Als de gebruiker stop ingeeft:
#   info naar het scherm
# Als waarde geen getal is:
#   error naar het scherm
# Als de waarde niet tussen 1 en 10 is:
#   warning naar het scherm
# Als de waarde tussen 1 en 10 is:
#   info naar het scherm

