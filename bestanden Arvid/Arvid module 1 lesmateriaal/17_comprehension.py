# Maak een lijst van de eerste n getallen

n = 10
lst = []
for i in range(n):
    lst.append(i+1)
print(lst)

# dit kan korter in python d.m.v. list comprehension
# de basisvorm [expression for item in iterable]
lst = [i+1 for i in range(n)]  # alle getallen in range(n)
print(lst)

letters = [letter for letter in 'Python']
print(letters)

letters_up = [letter.upper() for letter in 'Python']
print(letters_up)


names = ['Homer', 'Bart', 'Lisa', 'Marge', 'Maggie', 'Moo']
lens = [len(word) for word in names]
print(lens)

word_lens = [(word, len(word)) for word in names]
print(word_lens)

# opdracht
# names = ['Homer', 'Bart', 'Lisa', 'Marge', 'Maggie']
# maak een lijst met alle namen en familie namen:
# ['Homer Simpson', 'Bart Simpson', 'Lisa Simpson', 'Marge Simpson', 'Maggie Simpson']


full_names = [name + " Simpson" for name in names]
print(full_names )

# alle letters van 'A' to 'Z'
# chr(n) zet een getal naar een letter volgens de ASCII code
# https://nl.wikipedia.org/wiki/ASCII_(tekenset)
# chr(65) => 'A'
# chr(66) => 'B'

lst = [chr(i) for i in range(65, 91)]
print(lst)

# Maak een lijst van de even getallen kleiner dan n
lst = []
for i in range(n):
    if i %2 == 0:
        lst.append(i)
print(lst)

# met comprehension
lst = [i for i in range(n) if i %2 == 0]
print(lst)
pass
# de algemene vorm is
#  lst = [expression for item in iterable if condition]


even = [i for i in range(n) if i % 2 == 0]
print(even)
odd = [ i for i in range(n) if i%2 == 1]
print(odd)
even_odd = [ (i, i+1)  for i in range(n) if i%2 == 0]

a_names = [name for name in names if 'a' in name or 'A' in name]
print(a_names)

# comprehension werkt ook voor tuples
even = tuple(i for i in range(n) if i % 2 == 0)
print(even)

# comprehension werkt ook voor sets
even = {i for i in range(n) if i % 2 == 0}
print(even)


# comprehension werkt ook voor dicts

simp_info = {name: (len(name), name + " Simpson") for name in names}
print(simp_info),

simp_info = {name: (len(name), name+" Simpson") for name in names}
print(simp_info)
pass
# op basis van simp_info, print de namen met lengte 4
for name, (length, full_name) in simp_info.items():
    if length == 4:
        print(full_name)

pass
# oefeningen
# maak een comprehension voor
#  1/ list van alle kwadraten van 1 tot 10: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print([n*n for n in range(1,11,1)])
#  2/ set {(0,0), (1,1), (2,4), (3,9), (4,16), (5,25), (6,36), (7,49), (8,64), (9,81), (10,100)}
print({(n,n**2) for n in range(0,11)})
s = {(n,n**2) for n in range(0,11)}
s2 = {(0,0), (1,1), (2,4), (3,9), (4,16), (5,25), (6,36), (7,49), (8,64), (9,81), (10,100)}
print(f"{s==s2=}")
#  3/ tuple met  alle getallen tussen 1 en 100, deelbaar door 7 en even
print((i for i in range(1,101) if i % 7 == 0 and i % 2 == 0))
#  4/ dict {naam: lengte van de naam}
print({name: len(name) for name in names})
#  5/ uitdaging: dict {naam: aantal klinkers in de naam}
vowel = lambda x: [letter for letter in x if letter in 'aeiouAEIOU']
print({name: len(vowel(name)) for name in names})





