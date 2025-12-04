# oefening 1:vat(amount:float) -> float. Die 21.5% btw optelt bij het gegeven bedrag.
# tax_included = vat(49.99)    # 60.73785

def vat(amount: float) -> float:
    """
    Calculates the VAT (Value Added Tax) for a given amount.

    :param amount: The monetary value to which the VAT is applied
    :return: The resulting value after applying VAT
    """
    return amount * 1.215


# oefening 2: to_k_f(temp) -> (float, float):
# Schrijf een function die een temperatuur in °C omzet naar °F en K
#   - K = °C + 273.15
#   - °F = °C * 1.8 + 32

def to_k_f(temp: float) -> (float, float):
    """
    Converts a temperature from Celsius to both Kelvin and Fahrenheit.


    :param temp: Temperature in degrees Celsius.
    :return: A tuple containing two float values: the first element is the
             temperature in Kelvin, and the second element is the temperature
             in Fahrenheit.
    """
    return temp + 273.15, temp * 1.8 + 32  # haakjes mogen

# oefening 3: schrijf een functie die een lijst woorden omzet naar hoofdletters
#  Let op: als je een list meegeeft als parameter, dan zullen alle wijzigingen
#          aan die list ook gekend zijn in de oproepende code

def all_upper1(in_list: list) -> None:
    for i in range(len(in_list)):
        in_list[i] = in_list[i].upper()

def all_upper2(in_list: list) -> list:
    ret = []
    for i in in_list:
        ret.append(i.upper())
    return ret

print(all_upper1(["Dit", "is een", " zin"]))
l = ["Dit", "is een", " zin"]
print(all_upper1(l))
print(l)

l = ["Dit", "is een", " zin"]
print(all_upper2(l))
print(l)

# 1/ schrijf een lambda functie die de helft berekent; in : x, out: x/2
half = lambda x: x / 2

# 2/ schrijf een functie die de eerst n elementen berekent in de fibonacci reeks.
# het eerste getal in de reeks is 1, het tweede is ook 1, vanaf het derde getal is de waarde de som van de twee voorgaan. fib(8) =>[1, 1, 2, 3, 5, 8, 13, 21]
def fib(n: int) -> list:
    """
    Generate a Fibonacci sequence up to the nth number.
    :param n: The number of Fibonacci numbers to generate. Must be a positive integer.
    :return: A list containing the first n Fibonacci numbers.
    """
    if n ==1:
        return [1]
    ret = [1, 1]
    for i in range(2, n):
        ret.append(ret[i-1] + ret[i-2])
    return ret

for i in range(1, 10):
    print(fib(i))

# 3/ schrijf een functie die een zin vraagt van de gebruiker, en die zin omzet als volgt: woorden in een even positie moeten in kleine letters, op een oneven positie moeten in hoofdletters.
# input: 'Dit is een erg korte zin' => DIT is EEN erg KORTE zin
def flippy_sentence() -> str:
    """
    :return: A string where every word alternates between lowercase and uppercase
             based on its position
    """
    sentence = input("Voer een zin in: ")
    words = sentence.split()
    for i in range(len(words)):
        if i % 2 == 0:
            words[i] = words[i].lower()
        else:
            words[i] = words[i].upper()
    return(" ".join(words))

# 4/ Schrijf een functie sort(v1, v2, v3, v4) -> (float, float, float, float) die de input waarden gesorteerd retourneert.
def sort(v1:float, v2:float, v3:float, v4:float) -> (float, float, float, float):
    return sorted([v1, v2, v3, v4])

# 5/ Uitdaging: Werk deze functie correct uit
# We komen hier op terug

