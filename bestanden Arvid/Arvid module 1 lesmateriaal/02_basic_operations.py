#  Bewerkingen laten toe om waardes en variabelen te combineren tot een nieuwe waarde.

a = 9
b = 4

# Wanneer bewerkingen worden uitgevoerd op twee ints dan
# is het resultaat opnieuw een int.

# + - *
som = a + b
verschil = a - b
dubbel1 = 2 * a
dubbel2 = a * 2

# // is de gehele deling
# a // b is het kleinste gehele getal als a / benadert
# 29 / 10 = 2.9 => 29 // 10 = 2
# - 29 // 10 = -2.9  => -29 // 10 = -3
29 // 10
-29 // 10

halfb = b // 2
halfa = a // 2


# ** macht
googol = 10 ** 100  # macht

# rest bij gehele deling
rest = a % b
29 % 10
-29 % 10


# - + als unaire operatie
negatiefa = -a
positief = +a


# float operaties
a = 3.44
b = 2.0
som = a + b
verschil = a - b
dubbel1 = 2 * a
dubbel2 = a * 2
halfb = b // 2
halfa = a // 2
negatiefa = -a
googol = 10 ** 100  # macht
rest = a % b

# voer deling uit en rond af naar beneden
deling = a//b

b = -b

twaalf = 3 * 2 * 2
elf = twaalf - 1
tien =  17 - 2 * 4 + 1

31.622776601683793 ** 2

# strings
# Op tekst zijn niet veel bewerkingen mogelijk
naam = "Henk"
naam + ' Jansen'
naam * 3

# bool
# Bij bewerkingen met bool, krijgt True de waarde 1 en False de waarde 0.
True + False
False + False
2 * True

# Vergelijkingen tussen waardes geven ook een bool
True == True

True == False
3 < 2
type(3 < 2)
3 > 2
2 <= 3
2 >= 3
2 != 3  # ! =
naam == "Henk"
naam != "Henk"


# Complex
(0+1j) ** 2

# None
# Op None zijn geen bewerkingen

# Volgorde van bewerkingen:
# prio 1= haakjes
4 * (3-2)

# prio 2: **
2 ** 3 ** 4
(2 ** 3) ** 4
2 ** (3 ** 4)

# prio 3: unaire + -
-3 + 5
-(3+5)
(-3) + 5

# prio 4: *, /, //,% : links naar rechts

3 / 5 * 5 / 5
3 / ( 5* 5 ) / 5

# prio 5: + -
3 * 4 + 5 * 6

3 * 4.5 // 3 % 4 ** 4 + 2 ** 5 / 2
(((3 * 4.5) // 3) % (4 ** 4)) + ((2 ** 5) / 2)
