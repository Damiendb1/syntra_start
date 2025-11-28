# Op async functionaliteiten en object-georienteerde functionaliteiten na hebben
# we quasi alle mogelijkheden van de taal Python gezien
# Tijd om je vleugels uit te slaan.

# Een module is Een Python-bestand (.py) met functies,
# klassen of variabelen
# die je kunt hergebruiken.
# Er zijn drie soorten modules:
#   - ingebouwde modules, worden mee geïnstalleerd bij de Python
#   - externe modules, kunnen worden gedownload van de Internet
#   - eigen modules

# Je kan een module of een deel ervan importeren om de functionaliteiten van die module te gebruiken.
import math
# vanaf nu staan alle functionaliteiten van math ter beschikking
# Zie https://www.w3schools.com/python/module_math.asp
# Zie https://docs.python.org/3/library/math.html
# We komen later terug op wat er in de module zit.
print(math.sqrt(9))

# je kan specifieke zaken importeren van een module
from math import sqrt
print(sqrt(9))  # math. is niet meer nodig

# je kan imports hernoemen
import math as m
print(m.sqrt(36))
# print(m.sqroot(36)) geeft error
print(m.sin(1))

from math import cos as c
print(c(1))

# Hoe kan je weten wat er in elke module zit?
# Ervaring. AI helpt zeker.


import sys
# sys is een module
# door sys te importeren worden alle functionaliteiten van sys bereikbaar
# door er de naam van module voor te zetten.
plt = sys.platform
print(f"Platform: {plt}")

match plt:
    case 'win32':
        print("Je gebruikt Windows")
    case 'linux':
        print("Je gebruikt Linux")
    case 'darwin':
        print("Je gebruikt Mac")
    case _:
        print("We hebben geen idee wat je gebruikt")

# Je kan je eigen code ook importeren
from functional import ex_03
ex_03.print_reverse3(['Z','O', 'T'])


# Het grote voordeel van modules is dat er reeds veel zaken voor jou gemaakt zijn.
# Wil je een grafiek maken van temperatuur pe werkdag?
# Gebruik de juiste module.

import matplotlib.pyplot as plt

# Sample data
days = ['Ma', 'Di', 'Wo', 'Do', 'Vr']
temperatures = [20, 22, 21, 23, 24]

# Create the plot
plt.plot(days, temperatures)
plt.show()

#
# PEP8 over import
# 1/ imports horen bovenaan, voor de code begint.
# 2/ Eerst standaard bibliotheken, dan externe modules, dan eigen modules.
#         Standaard bibliotheek
#         import os
#         import sys
#         from datetime import datetime
#         import numpy as np
#         import pandas as pd
#         from matplotlib import pyplot as plt
#         from my_module import my_function
# 3/ 1 module per regel
#       niet dit:
#         import os, sys, datetime
#       maar dit:
#         import os
#         import sys
#         import datetime
# 4/ meerdere items uit 1 module mogen in 1 regel gescheiden worden.
#           from subprocess import Popen, PIPE, STDOUT
from math import sin, cos, tan

# 5/ aliassen voor lange namen
#       import matplotlib as mpl

# modules die nog niet geïnstalleerd zijn, kan je in PyCharm eenvoudig installeren.
import numpy
import pandas
import matplotlib
import seaborn


