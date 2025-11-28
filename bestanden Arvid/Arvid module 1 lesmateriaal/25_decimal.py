# De Decimal class in Python is een speciale manier om met decimale getallen
# te werken wanneer je exacte precisie nodig hebt.
import sys

# Met gewone floats (float):
# Computers slaan getallen op in binair (0 en 1),
# en sommige decimale getallen kunnen niet exact worden weergegeven.
print(0.1 + 0.2)  # Resultaat: 0.30000000000000004
print(0.1 + 0.1 + 0.1)  # Resultaat: 0.30000000000000004

from decimal import Decimal

# Je kan een Decimal aanmaken met een komma getal als string
# (BESTE MANIER):
price1 = Decimal('19.99')
price2 = Decimal('5.59')
vat = Decimal('0.21')

# Voor een int kan het ook als volgt (zodner quotes)
aantal = Decimal(5)

# Alle bewerkingen zijn tussen decimals zijn mogelijk
print(f"{price1 + price2=}")
print(f"{price1 - price2=}")
print(f"{price1 * (1+vat)=}")

print(f"            {19.99/5.59=}")
print(f"{price1/price2=}")  # meer correct decimalen
res = price1/price2
res = res.quantize(Decimal('0.01'))
print(f"{res=}")
print(f"{price1**100=}")
print(f"{price1 < price2=}")
print(f"{price1 == price2=}")
print(f"{price1 > price2=}")




to_int = int(price1)  # conversie naar int (verliest decimalen)
print(to_int)
to_str = str(price1)
print(to_str)
to_float = float(price1)  # niet gebruiken: weer kans op fouten
print(to_float)


# De floating point fout komt niet voor bij decimal
print(Decimal('0.1') + Decimal('0.2'))  # Resultaat: 0.3
print(Decimal('0.1') + Decimal('0.1') + Decimal('0.1'))  # Resultaat: 0.3
res = price1 * 100.0  # type error

"""
Gebruik Decimal wanneer exacte precisie cruciaal is
    Financiële berekeningen (geld, prijzen)
    Boekhoudkundige toepassingen
    Banktransacties

Gebruik float wanneer kleine onnauwkeurigheden geen probleem zijn.
Decimal mag uiteraard ook.
    Wetenschappelijke berekeningen
    Geometrie en fysica
    Game development
"""



# Alle code hieronder is louter ter informatie voor wie meer wil weten / uitdaging wil

# de standaard precisie
from decimal import getcontext
print(getcontext().prec)
res = price1/price2
print(f"{res}")
print(f"{price1/price2}")  # meer correct decimalen
getcontext().prec = 8
print(f"{res}")
print(f"{price1/price2}")  # meer correct decimalen
getcontext().prec = 50
print(f"{res}")
print(f"{price1/price2}")  # meer correct decimalen

f = 123.456
d = Decimal('123.456')

print(f"Float grootte: {sys.getsizeof(f)} bytes")     # ~24 bytes
print(f"Decimal grootte: {sys.getsizeof(d)} bytes")   # ~104 bytes
print(f"Decimal is {sys.getsizeof(d) / sys.getsizeof(f):.1f}x groter")

#

