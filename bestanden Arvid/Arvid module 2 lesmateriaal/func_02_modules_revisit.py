# Delen van andere python files kunnen geïmporteerd worden.

# Als het een standaard python module is:

import sys
import math

# nu kan je de classes en functions uit sys en math gebruiken als volgt:

x = math.floor(1.1)
args = sys.argv

# je kan ook delen van een class importeren
# om de class Decimal uit de module decimal te gebruiken
from decimal import Decimal
from csv import DictReader

D100 = Decimal(100)

# om je eigen files te importeren
# Stel dat jouw project zich bevindt in C:\Users\raque\PycharmProjects\Syntra_start_2
# met deze structuur
# |
# +-- oo +-- les (met class Book)
# |      |
# |      +-- oo_21_composition_attributes (met class Person)
# |
# +-- lib +-- les23.py
#         |
#         +-- les24.py

# Als je in les24.py gebruik wel maken van Book en Person
from oo.oo_21_composition_attributes import Person, DutchAddress
from oo.oo_21_composition_attributes import DutchAddress as Dadr

p = Person("Arvid")
dutch_add = DutchAddress(street="EE", ....)

