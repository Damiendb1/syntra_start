# De random module laat je willekeurige getallen genereren
# en elementen kiezen uit lijsten, strings of andere sequenties.
import random

# een willekeurig geheel getal tussen a en b (inclusief beide).
print(random.randint(1, 10))
print(random.randint(1, 10))

# hoe weten we of een dit echte willekeurig is?
# we kunnen niet voorspellen wat het volgende getal zijn, maar gemiddeld
# komt elk getal evenveel keer voor. Zie lotto resultaten door de jaren heen.

min, max = 1, 10
width = max - min + 1
cnt = {i:0 for i in range(min, max + 1,1)}

for i in range(1_000):
    rnd = random.randint(1, 10)
    cnt[rnd] += 1

print(cnt) # als elk getal ongeveer evenveel keer voorkomt, dan is de functie waarschijnlijk willekeurig.

# Geeft een willekeurige float tussen a en b, inclusief beide.
temp = random.uniform(18.0, 25.0)
print(f"Simulatie temperatuur: {temp}°C")

# Kies een willekeurig element uit een lijst
fruit = ['appel', 'banaan', 'kers', 'kiwi']
for _ in range(1000):
    print(random.choice(fruit))

# Schudt een lijst in willekeurige volgorde (in-place).
cards = [ f"{suit}{num}" for num in range(1,14,1) for suit in ['♠', '♥', '♦', '♣']]
# cards is een dubbel comprehension
# je kon ook  for loops gebruiken
# cards = []
# for num in range(1, 14, 1):
#     for suit in range(4):
#         cards.append(f"{suit}{num}")

print(cards)
random.shuffle(cards)
print(cards)  # de kaarten zijn geschud.
print(random.sample(cards, 5))  # Kies 5 willekeurige verschillende kaarten uit de lijst.


# weetje: er zijn 42! mogelijke combinaties.
# Dat zijn 1.405.006.117.752.879.800.000.000.000.000.000.000.000.000.000.000.000 combinaties
# De kans dat iemand jouw geschudde combinatie ooit als eens gehad heeft is quasi onbestaande.

# Geeft een willekeurig getal tussen 0.0 en 1.0.
print(f"{random.random()=}")
print(f"{random.random()=}")


# De les met een paar oefeningen op de random module.

# Een dobbelsteen gooien is hetzelfde als een willekeurig getal
# tussen 1 en 6 genereren met randint()
# opdracht 1: Gooi 100 keer een dobbelsteen. Tel hoeveel keer het een 6 was
# opdracht 2: Gooi 100 keer 3 dobbelstenen. Tel hoeveel keer het 3 dezelfde zijn.
# opdracht 3: Gooi 5 dubbelstenen, herwerp de dubbelstenen verschillend van 6.
# Tel hoeveel worpen je nodig hebt om 5 dobbelstenen met waarde 6 te bekomen.

# opdracht 4: speel blad-steen-schaar tegen de computer.
# https://nl.wikipedia.org/wiki/Steen,_papier,_schaar
# vraag: Blad, Steen, Schaar?
# Ook de computer kiest willekeurig Blad, Steen, Schaar.
# Schaar wint van blad, blad wint van steen, steen wint van schaar.
# Bepaal wie gewonnen heeft.
