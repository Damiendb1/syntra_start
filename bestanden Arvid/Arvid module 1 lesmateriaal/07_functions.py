# Functies kunnen ook waardes teruggeven.
# Eigenlijk doet elke functie dat.
# een return statement is eigenlijk: return None  (return de niets waarde)

def printline(msg):
    """
    Print a message
    :param msg: message to print
    """
    print(msg)
    # impliciet staat hier return None

print(printline("hello"))  # None


def sum_until(limit: int):
    """
    Print the sum of all numbers from 1 to limit
    :param limit: Number at which to stop
    """
    ret = 0
    for num in range(1, limit+1):
        ret += num
    return ret

print(sum_until(4))

# We kunnen python duidelijk maken welk type een functie teruggeeft
#  def function_name(param1: type1, ...) -> return type
# Het is niet verplicht door python, het is wel verplicht in de best practices.
# Het helpt PyCharm om mee te denken en eventueel ontbrekende over verkeerde returns te vinden.

def sum_until2(limit: int) -> int:
    """
    Print the sum of all numbers from 1 to limit
    :param limit: Number at which to stop
    """
    ret = 0
    for num in range(1, limit+1):
        ret += num
    return ret

# We kunnen in de functie beschrijving ook aangeven wat de functie exact berekent
# :return: Beschrijving
# Het is niet verplicht door python, het is wel verplicht in de best practices.
# Het helpt PyCharm om goede documentatie te geven bij de functie.

def sum_until3(limit: int) -> int:
    """
    Print the sum of all numbers from 1 to limit
    :param limit: Number at which to stop
    :return: Sum of all numbers from 1 to limit
    """
    ret = 0
    for num in range(1, limit+1):
        ret += num
    return ret

print(sum_until3(4))


# een functie kan meerdere waardes terugsturen
def floor_division_remainder(x: float, y: float) -> (int,float):
    """
    Calculates floor division and remainder of x and y
    :param x: first number
    :param y: second number
    :return: floor division and remainder
    """
    return x // y, x % y

print(floor_division_remainder(4, 2))
print(floor_division_remainder(5.5, 2))

# floor_division_remainder retourneert twee waardes, verpakt in een tuple.

# tuple is een python datatype dat zich gedraagt als een list.
# Net zoals een list:
#   - de volgorde blijft bewaard
#   - indexeerbaar
#   - een waarde mag meermaals voorkomen
# Het verschil met list is dat tuples niet gewijzigd kunnen worden.

# een leeg tuple maken
t = tuple()
print(t)
print(type(t))

t= ()
print(t)
print(type(t))

t = (4,5,6,7,8,9)
print(t)
print(type(t))

# indexes, slices
print(f"{t[1]=}")
print(f"{t[1:5]=}")
print(f"{t[-1]=}")
print(f"{reversed(t)=}")

# niet aanpasbaar
t[3] = 33  # error

# waarom uberhaupt tuples gebruiken?
#  tuples zijn sneller en vereisen minder geheugen dan list
#  databescherming: wanneer je absoluut zeker wil zijn dat code de inhoud van een lijst niet mag/kan wijzigen.

# oefening 1:vat(amount:float) -> float. Die 21.5% btw optelt bij het gegeven bedrag.
# tax_included = vat(49.99)    # 60.73785

# oefening 2: to_k_f(temp) -> (float, float):
# Schrijf een function die een temperatuur in °C omzet naar °F en K
#   - K = °C + 273.15
#   - °F = °C * 1.8 + 32

# oefening 3: schrijf een functie die een lijst woorden omzet naar hoofdletters
#  Tip: als je een list meegeeft als parameter, dan zullen alle wijzigingen
#       aan die list ook gekend zijn in de oproepende code


# een functie mag eender wat terug sturen.
def split_odd_even(input_list: list) -> (list, list):
    """
    Find the odd and even numbers in a list.
    :param input_list: list to analyse
    :return: list of odd and even numbers
    """
    even = []
    odd =[]
    for i in input_list:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return even, odd

even_values, odd_values = split_odd_even([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89])
print(even_values)
print(odd_values)

# gewenste recursie:
# Bij kansrekening is wiskundige bewerking faculteit erg belangrijk.
#  faculteit(8) (in wiskunde ook wel: 8!) =  8 * 7 * 6 * 5 * 4 * 3 * 2 * 1
#  faculteit(n) =  product van alle getallen van 1 t.e.m. n
#  eigenschap :   n! ==  n * (n-1)!   of anders:   faculteit(n) = n * faculteit(n-1)

def factorial(val: int) -> int:
    """
    Calculate the factorial of a number.
    :param val: Input number
    :return: Factorial of val
    """
    if val == 1:
        return 1
    else:
        return val * factorial(val - 1)


print(factorial(120))
# Er zijn efficiëntere manieren om n! te berekenen.


# lambda functions
# Neem een elementaire functions square en is_odd
# Volledig uitgeschreven volgens de coding regels is dat 7 lijnen lang.

def square(value: float) -> float:
    """
    Calculates the square of a given number.
    :param value: The number to be squared
    :return: The square of the input value
    """
    return value ** 2

# Dit kan je vervangen door
square = lambda x: x ** 2
# De definitie van een lambda function is steeds van de vorm:
#     naam = lambda parameters: expressie met die parameters

def is_odd(value: int) -> bool:
    """
    Determine if a value is odd.
    :param value: value to check
    :return: True if value is odd, False if even
    """
    return value % 2 == 1

# lambda functions laten toe om dit in te korten.
is_odd2 = lambda x : x % 2 == 1

# lambda functions kunnen ook meerdere input parameters hebben.
add = lambda a, b: a + b
add(5, 2)  # 7

# lambda functions kunnen meerdere waarden retourneren..
switch = lambda x,y: (y,x)

switch(2,3) #  (3,2)

# later zullen we nog praktische toepassingen voor lambda functions zien.
