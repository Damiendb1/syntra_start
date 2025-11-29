import random

lst = []
for i in range(10):
    lst.append(random.randint(-10,10))
print(lst)

lst = [random.randint(-10,10) for i in range(10)]

print(lst)

# maak een lijst met alle medeklinkers
# stap 1: maak een (lambda) function die bepaalt of een letter een medeklinker is
# stap 2: maak een lijst met alle letters
# stap 3: maak een lijst met alle medeklinkers

is_vowel = lambda letter: letter.lower() in "aeiou"
is_consonant = lambda letter: not is_vowel(letter)


letters = [chr(i) for i in range(97, 123)]
print(letters)
consonants = []
for letter in letters:
    if is_consonant(letter):
        consonants.append(letter)
print(consonants)

consonants = [letter for letter in letters if is_consonant(letter)]
print(consonants)

u_l_consonants = [(letter.lower(), letter.upper()) for letter in letters if is_consonant(letter)]
print(u_l_consonants)


compact = [(letter.lower(), letter.upper()) for letter in [chr(i) for i in range(97, 123)] if letter.lower() not in "aeiou"]
print(compact)





postcodes_be = {
    1000: "Brussel",
    2000: "Antwerpen",
    9000: "Gent",
    3000: "Leuven",
    4000: "Luik",
    8000: "Brugge",
    3500: "Hasselt",
    5000: "Namen",
    6000: "Charleroi",
    7000: "Bergen",
    8400: "Oostende",
    2800: "Mechelen",
    3800: "Sint-Truiden",
    9300: "Aalst",
    8500: "Kortrijk"
}

reverse = { v:k for k,v in postcodes_be.items()}
print(reverse)

# make een list of list van de vorm:
#  1, 2, 3, 4
# 11, 12, 13, 14
# ...
# 91, 92, 93, 94

rows = []
for row  in range(1, 10):
    lst = []
    for col in range(1, 5):
        lst.append(row *10 + col)
    rows.append(lst)

print(rows)


rows = [[row * 10 + col for col in range(1, 5)] for row in range(1, 10)]
print(rows)





