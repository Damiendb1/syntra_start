# Twee manieren voor herhaling

# for lus
# Wordt vooral gebruikt als op voorhand gekend is hoeveel keer herhaald moet worden
"""
Vorm:
for variabele in bereik:  # dubbelpunt is belangrijk
    commando1 # inspringen van een regel
    commando2
commando3 # Dit behoort niet meer tot de herhaling
"""

# Vorm
for i in range(10):
    print(i)



# Beslissing
# if condition:
#     command1
# command2

# Enkel wanneer de conditie True is, wordt command1 uitgevoerd.
# command2 wordt altijd uitgevoerd

name = input("Geef je naam in: ")
print("Hallo", name)
if name == "Arvid":
    print("Toevallig! Zo heet ik ook")
print("Tot ziens")

# Mogelijke condities:
#  a < b,
#  a <= b
#  a == b
#  a!=b
#  a > b
#  a >= b

#  a < b < c    a <= b <= c
a = 5
b = 3
print(a < b)
print(a == b)
print(a != b)
print(a > b)

# Beslissing 1
"""
if condition:  # dubbelpunt is belangrijk
    command1  # inspringen van een regel
"""
i = int(input("Geef een getal"))
if i % 2 == 1:
    print("Het getal is oneven")
print("Eind van de programma")

# Beslissing 2
"""
if condition:
    command1
else:
    command2
command3
"""

i = int(input("Geef een getal"))
if i % 2 == 1:
    print("Het getal is oneven")
else:
    print("Het getal is even")
print("Einde van de programma")


# Beslissing 3
"""
if condition1:
    command1
elif condition2:
    command2
elif condition3:
    command3
else:
    command4  # Geen enkele conditie is True
command5
"""

i = int(input("Geef een getal"))
if i > 0:
    print("Het getal is positief")
elif i < 0:
    print("Het getal is negatief")
else:
    print("Het getal is nul")
print("Einde van de programma")


# Negatie: not
# not True -> False
# not False -> True

number = int(input("Geef een getal: "))
negative = number < 0
print(f"Het getal is negatief: {negative}")
print(f"Het getal is positief: {not negative}")

# And
# conditie1 and conditie2 -> True als beide condities True zijn
# False and False -> False
#  True and False -> False
#  False and True -> False
#   True and True -> True
number = int(input("Geef een getal: "))
negative = number < 0
even = number % 2 == 0

if negative and even:
    print("Het getal is negatief en even")
elif not negative and even:
    print("Het getal is positief en even")
elif not negative and not even:
    print("Het getal is positief en niet even")
elif negative and not even:
    print("Het getal is negatief en niet even")

# or
# conditie1 or conditie2 -> True als één van bbeide condities True is of beide
# False or False -> False
#  True or False -> True
#  False or True -> True
#   True or True -> True

number = int(input("Geef een getal tussen 1 en 10: "))
if number < 1 or number > 10:
    print("Het is niet tussen 1 en 10")
if not (1 <= number <=10):
    print("Het is niet tussen 1 en 10")
if not number >= 1 and not number <= 10:
    print("Het is niet tussen 1 en 10")
if not (number >= 1 or number <= 10):
    print("Het is niet tussen 1 en 10")

# voorrang: haakjes -> not ->  and ->  or
print(True and False)
print(not True and False)
print(not (True and False))

# while lus
# wordt vooral gebruikt als niet gekend is hoeveel keer er herhaald moet worden
"""
Vorm:
while conditie: # dubbelpunt is belangrijk
    commando1 # inspringen van een regel
    commando2  
commando3 # Dit behoort niet meer tot de herhaling
"""

user_name = ""
while user_name != "Stop":
    user_name = input("Geef je naam in: ")
    print("Hallo ", user_name)
print("Eind van de programma")

i = 1
while i <= 10:
    print(i)
    if i % 2 == 0:
        print("even")
    else:
        print("oneven")
    i = i + 1

# break en continue
# continue: stop met de herhaal-code en start de volgende iteratie
# break: stop de herhaal code en ga verder ná de lus

while True:
    i = int(input("Geef een getal tussen 1 en 10: "))
    if i < 1 or i > 10:
        print("Het getal moet tussen 1 en 10 bevatten")
        continue
    print(f"Het getal is {i}")
    if i == 5:
        print("Het getal is 5, dus we stoppen met de herhaal code")
        break
print("De lus is gedaan")

# Schrijf een programma dat de temperatuur vraagt.
# Onder 36.6 is het onderkoeling
# Tot 37.5 is het normaal
# Vanaf 37.5 is het verhoging
# Vanaf 38 is het koorts
# Vanaf 40 is het dodelijk.
# Blijf de temperatuur vragen tot er 0 wordt ingevuld.

while True:
    temp= float(input("Geef de temperatuur in: "))
    if temp == 0:
        break
    if temp < 36.6:
        print("Het is onderkoeling")
    elif temp < 37.5:
        print("Het is normaal")
    elif temp < 38:
        print("Het is verhoging")
    elif temp < 40:
        print("Het is koorts")
    else:
        print("Het is dodelijk")

# break en continu werken ook in een for loop
# debug deze code stap voor stap totdat je begrijpt hoe het werkt.

for i in range(20):
    if i == 5:
        continue
    if i % 10 == 5:
        break
    if i % 2 == 0:
        print(i)

# Een bank automaat kent voor 1 klant de 'geheime' code: Jo heeft code 1234
# De automaat vraag eerst de naam van de klant.
# De naam 'Stop' stop het programma
# Gekende klanten kunnen de code invoeren.
# Niet gekende klanten krijgen een reclame boodschap om klant te worden.
# Een klant mag 3 keer proberen om de code te invoeren, daarna verschijnt alarm.
# Bij een correcte code verschijnt het saldo van de klant (kies zelf)

while True:
    user_name = input("Naam: ")
    if user_name == "Stop":
        break
    if user_name != "Jo":
        print("We hebben een reclame boodschap voor u!")
        continue
    print(f"Hey", user_name,"wat is je code?")
    for i in range(3):
        code = input("Code: ")
        if code == "1234":
            print("De code is correct")
            print("Het saldo van de klant is 30000")
            break
