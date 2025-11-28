# Code is zoals een keuken:
# Als iedereen spullen op een andere plek zet, wordt het chaos
# Conventies maken samenwerken mogelijk


# De meeste coding rules staan opgesomd in PEP 8 – Style Guide for Python Code
# PEP betekent Python Enhancement Proposal.
# Voor wie veel tijd heeft: https://peps.python.org/pep-0008/
# Ze maken code uniforme leesbaar voor andere programmers
# Je toekomstige zelf is ook een "andere programmeur"

# Maak je zelf gewend om PEP8 te volgen.
# Pycharm helpt hierbij.


"""
1/ Voertaal is Engels

Waarom Engels?
Python zelf is Engels: def, while, try, except, return
Internationale samenwerking: Code kan door iedereen gelezen worden
Open source cultuur: Veel Python code wordt gedeeld
Bibliotheek ecosysteem: Alle standaard libraries gebruiken Engels

maar:
Domein-specifieke termen: Nederlandstalig jargon, etc.
Lokale projecten: Intern bedrijfssoftware die nooit internationaal gaat
"""


"""
2/ Naamgeving
    snake_case voor functies en variabelen
    UPPER_CASE voor constanten
    PascalCase voor klassen (later)
    
    Geen speciale karakters in naamgeving
"""


# zonder PEP8
def X():
    mijnVariabele = 5
    MIJNANDEREVAR = 10

# met PEP8
def calc_stats():
    my_var = 5
    CONSTANT = 10


"""
3/ white space
- spatie rond operators
- spatie tussen parameters
- 2 lege regels voor elk functie/klasse/methode
- 1 lege regel aan het einde van een py bestand
"""

# zonder PEP8
x=5+3*2
res=func(a,b,c)

# met PEP8
x = 5 + 3 * 2
res = func(a, b, c)

# zonder PEP8
def func1():
    return 1
def func2():
    return 2
def func3():
    return 3


# met PEP8
def func1():
    return 1


def func2():
    return 2


def func3():
    return 3


"""
4/ lijn lengte
Maximum 79 karakters per regel (voor code)
72 karakters voor comments/docstrings.

Vertical code is eenvoudiger te lezen dan horizontal code.
"""
# zonder PEP8
total = first_variable + second_variable + third_variable - fourth_variable * fifth_variable

# met PEP8
total = (first_variable
         + second_variable
         + third_variable
         - fourth_variable * fifth_variable)

FILES = [ 'file1.txt', 'file2.txt', 'file3.txt']


FILES = [ 'file1.txt',
          'file2.txt',
          'file3.txt']
