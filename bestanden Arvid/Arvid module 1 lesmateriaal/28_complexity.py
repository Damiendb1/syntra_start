# De complexiteit van een functies geeft aan hoe snel de uitvoertijd van een functie oploopt
# in relatie tot de input grootte
import random
from decimal import Decimal, getcontext
from typing import Any


def search_in(lst:list, val: Any) -> (bool, int):
    """
    search a value in a list
    :param lst: List to search in
    :param val: value to search
    :return: True if value is in list, number of operations
    """
    cnt = 0
    for item in lst:
        cnt += 1
        if item == val:
            return True, cnt
    return False, cnt


N=10000
M = 100
lst = [i for i in range(N)]
total = 0
for i in range(M):

    random.shuffle(lst)
    res, cnt = search_in(lst, N//2)
    print(i, ':', cnt)
    total += cnt
print(i, ':', search_in(lst,  N+2))
print("gemiddelde:", total/M)

# gemiddelde zal de functie search_in N // 2 operaties nodig hebben


def sort_lst(lst: list)-> int:
    cnt = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            cnt += 1
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
    return cnt

N = 100
M = 10
lst = [i for i in range(N)]
total = 0
for i in range(M):
    random.shuffle(lst)
    res = sort_lst(lst)
    print(i, ':', res)
    total += res

print("gemiddelde:", total / M)

# de functie sort_lst zal altijd N * N // 2 operaties nodig hebben

# Er zijn verschillende manieren om het n-de fibonacci getal te berekenen

def fib_1(n: int) -> int:
    """
    Recursive function to calculate the n-th fibonacci number
    :param n: index
    :return: nth fibonacci number
    """
    global cnt
    cnt += 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_1(n-1) + fib_1(n-2)

def fib_2(n: int) -> int:
    """
    Linear function to calculate the n-th fibonacci number
    :param n: index
    :return: nth fibonacci number
    """
    global cnt

    if n == 0:
        return 0
    elif n == 1:
        return 1
    l = [1,1]
    for i in range(2, n):
        cnt += 1
        l.append(l[i-1] + l[i-2])
    return l[n-1]

SQRT5 = 2.2360679775
def fib_3(n: int) -> int:
    """
    Closed form to calculate the n-th fibonacci number
    :param n: index
    :return: nth fibonacci number
    """
    global cnt
    cnt = 1
    phi = (1 + SQRT5) / 2
    psi = (1 - SQRT5) / 2
    return int((phi**n - psi**n) / SQRT5)
getcontext().prec = 100
SQRT5_DEC = Decimal.sqrt(Decimal(5))
def fib_4(n: int) -> int:
    """
    Closed form to calculate the n-th fibonacci number
    :param n: index
    :return: nth fibonacci number
    """
    global cnt
    cnt = 1
    phi = (1 + SQRT5_DEC) / 2
    psi = (1 - SQRT5_DEC) / 2
    return round((phi**n - psi**n) / SQRT5_DEC)


for i in range(1, 100):
    print(i)
    cnt = 0
    print(f'{fib_1(i)=}=, {cnt}')
    cnt = 0
    print(f'{fib_2(i)=}, {cnt}')
    cnt = 0
    print(f'{fib_3(i)=}, {cnt}')
    cnt = 0
    print(f'{fib_4(i)=}, {cnt}')

i = 10
while True:
    i+=1
    print(i)

    if fib_2(i) != fib_4(i):
        print(f"{fib_2(i)=}, {fib_4(i)=}")
        break

# we zien dat vooral fib_1 steeds langer gaat duren.
# Als we de code analyseren: zien we dat voor n > 1: er telkens 2 nieuwe calls zijn:
#   fib_1(n-1) en fib_1(n-2)
#  fib(5)= fib_1(4) + fib_1(3)
#  fib(5)= fib_1(3)+fib_1(2)   + fib_1(2) + fib_1(1)
#  fib(5)= fib_1(2) + fib_1(1) + fib_1(1) + fib_1(1) + fib_1(1) + fib_1(0)  + fib_1(0)
#  fib(5)= fib_1(2) + fib_1(1) + fib_1(1) + fib_1(1) + fib_1(1) + fib_1(0)  + fib_1(0)
#  fib(5)= fib_1(1) + fib_1(0) + fib_1(1) + fib_1(1) + fib_1(1) + fib_1(1) + fib_1(0)  + fib_1(0)
#  de complexiteit is 2**n: dit stijgt erg snel   1,2,4,8, 16, 32, 64, 128,     2 ** 16 = 65536  2**30= 1073741824

# fib_2 doet ongeveer evenveel berekeningen als de input waarde (loop van 2 t.e.m. n). De complexiteit is n
# fib_3 doet telkens 1 berekening onafhankelijk van de input waarde. De complexiteit is 1

# Op zoek naar de meest efficiënte waarden kunnen we dus voor fib_3 kiezen.
# Wel oppassen want fib_3 doet floating point berekeningen. Vanaf ongeveer fib(50) wordt de rekenfout te groot
# en is berekening fout



# Een ander voorbeeld is het algoritme om een getal te raden tussen 1 en 1000
# Je kan gewoon beginnen raden bij 1 en telkens 1 getal hoger gaan:
# Stel je moet 340 raden.
# is het 1? Nee!
# is het 2? Nee!
# ...
# is het 339? Nee!
# is het 340? Ja!!!!
# In het beste geval moet je maar 1 keer raden. In het slechtste geval 1000 keer.
# Gemiddeld moet je n/2 keer raden.  Dus de complexiteit is n ( deling door 2 mag je weglaten)


def lineair_guess(number:int, lower:int , upper:int) -> int:
    """
    linear guess towards number between two values

    :param number: number to guess
    :param lower: lower bound
    :param upper: upper bound
    :return: number of guesses taken
    """
    cnt = 0
    for i in range(lower, upper+1):
        cnt += 1
        if i == number:
            return cnt
    return -1

# Je kan ook slimmer raden
# Begin halverwege:
# Is het 500? Nee, het is lager
# Als het lager is, raad dan de helft tussen 1 en 499
# Als het hoger is, raad dan de helft tussen 501 en 1000
# Is het 250? Nee, het is hoger
# Als het lager is, raad dan de helft tussen 1 en 249
# Als het hoger is, raad dan de helft tussen 251 en 499
# Is het 375? Nee, het is lager
# Als het lager is, raad dan de helft tussen 251 en 374
# Als het hoger is, raad dan de helft tussen 376 en 499
# Is het 312? Nee, het is hoger
# Als het lager is, raad dan de helft tussen 251 en 311
# Als het hoger is, raad dan de helft tussen 313 en 374
# Is het 343? Ja!!!!
# In het beste geval moet je maar 1 keer raden. In het slechtste geval 10 keer.
# Gemiddeld moet je log2(n) keer raden.  complexiteit is log2(n)

def binary_guess(number:int, lower:int , upper:int) -> int:
    """
    binary guess towards number between two values
    :param number: number to guess
    :param lower: lower bound
    :param upper: upper bound
    :return: number of guesses taken
    """
    cnt = 0
    while lower <= upper:
        cnt += 1

        guess = (lower + upper) // 2
        # print(guess, lower, upper)
        if guess == number:
            return cnt
        elif guess < number:
            lower = guess + 1
        else:
            upper = guess - 1
    return -1

import timeit

res = {"linear" : [], "binary" : []}
avg = lambda x: sum(x) / len(x)
for i in range(1,1001,1):
    res["linear"].append(lineair_guess(i, 1, 1000))
    res["binary"].append(binary_guess(i, 1, 1000))
print(f"{sum(res['linear'])=} iteraties")
print(f"{sum(res['linear'])=} iteraties")
print(f"{avg(res['linear'])=} iteraties")
print(f"{avg(res['binary'])=} iteraties")


def is_in_1(val: str, lst: list) -> bool:
    return val in lst

def is_in_2(val: str, lst: list) -> bool:
    return  val.count(val) >= 0

limit = 1000
stars = ['*' * i for i in range(1, limit + 1)]

runs = 100000
print(timeit.timeit(lambda: is_in_1('a', stars), number=runs))
print(timeit.timeit(lambda: is_in_2('a', stars), number=runs))

# Het is dus belangrijk om steeds te zoeken naar een oplossing met een lage complexiteit
# en bij vergelijkbare functions te beoordelen welke het snelste werkt.

# Om het woord 'Peer' in een woordenboek te zoeken kan je van de eerste tot de laatste pagina kijken
# of het woord op de pagina staat: lineair met het aantal paginas.
# Of ja kan eerst de naar de pagina gaan met woorden die beginnen met 'P' en dan naar de pagina met woorden
# die beginnen met 'PE', daan 'PEE' om zo bij PEER terecht te komen, log(aantal letters)
