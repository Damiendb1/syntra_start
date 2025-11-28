# Python heeft 6 basis data types
# Gehele getallen, komma-getallen, tekst, logisch, complex, NoneType
from operator import truediv

# 1 - Gehele getallen: int
# Positief en negatief: tot zeker 1000 cijfers lang.
42 # geheel getal
type(42)

# Gehele getallen: int
geheel = 42
type(geheel)

negatief = -42
positief = +42
positief2 = 42

miljard1 = 1000000000
miljard2 = 2_000_000_000
miljard3 = 3_0_0_0_0_00_000
heel_veel = 23425456547673213423498765432345657874232413200281314856595799667356254254235625635462356232111343

# 2 - Komma-getallen: float
# Als je zelf een punt vermeldt, dan wordt een getal een float.
# Ook als is 1.0 (float) eigenlijk gelijk aan 1
99.95
type(99.95)

pi = 3.14
type(pi)

bijna1 = 9_990.99_9_999
bijna2 = 0.999999

# e-notatie
1e3
1e9 # miljard (NL) - billion (EN)
1e12 # biljoen (NL) - trillion (EN)
1e15 # biljard (NL) - quadrillion (EN)
1e16 # sprong naar e notatie

602200000000000000000000.0
avogadro1 = 602200000000000000000000.0
avogadro2 = 6.022e23
electronvolt = 1.602e-19


# Bij float verliezen we precisie.
# Er kunnen maar een beperkt aantal decimale cijfers exact 'onthouden' worden
a = 0.9
b = 0.99
c = 0.999
d = 0.9999
e = 0.99999
f = 0.999999
g = 0.9999999
h = 0.99999999
i = 0.999999999
j = 0.9999999999
k = 0.99999999999
l = 0.999999999999
m = 0.9999999999999
n = 0.99999999999999
o = 0.999999999999999
p = 0.9999999999999999
q = 0.99999999999999999
r = 0.999999999999999999

# Meestal kan het geen kwaad om precisie te verliezen.
# Maar hou het altijd in je achterhoofd.

# Voor int is onderstaande bewerking exact.
# 10 ^ 100 + 1 - 10 ^ 100 = 1
10 ** 100 + 1 - (10 ** 100)
1
# Bij float verliezen we precisie en dus krijgen we een rekenfout.
10.0 ** 100 + 1 - (10 ** 100)
10.0 ** 100


# Bij float krijg je al snel rekenfouten. Meestal is het niet erg, maar het is onhandig.
fout_marge = 0.1 + 0.2

# 3 - Tekst: string
# Er zijn 4 manieren om tekst te schrijven.

# Dubbele quotes: "weglatingsteken"
"Anna"
type("Anna")

# Enkele quotes: 'weglatingsteken'
'Anna'
type("Anna")

# Drie enkele quotes: '''weglatingsteken'''
'''Anna'''
type('''Anna''')

# Drie dubbele quotes: """weglatingsteken"""
"""Anna"""
type("""Anna""")

# """  of ''' laten toe om over meer
#

adres = """Dorpstraat"""
veel_tekst = """Arvid Claassen
van de firma 12test 
lesgever bij Syntra"""

andere_tekst = '''Syntra Midden Vlaanderen
Eerste straat links en dan tweede rechts
'''

# 4 - logisch: bool
# Om aan te geven of iets waar of onwaar is.
# Komt later zeer veel terug doorheen
True
type(True)
true
False
false
waar = True
niet_waar = False

# 5 - complexe getallen: complex
# Complexe getallen zijn zeer belangrijk in de wiskunde.
# Ze hebben een reëel deel en een imaginaire deel:   2+4i  met i gelijk aan wortel van -1
# In python wordt het imaginair deel voorgesteld met een j.
# We gaan deze cursus niet werken met complexe getallen.
2.2 + 4.5j
type(2.2 + 4.5j)
complex = 2.2 + 4.5j

# 6 - None: NoneType
# Dit wordt gebruikt als een waarde (nog) niet gekend is.
None
type(None)

"""
Variable namen
- beginnnen met een letter of _ (underscore)
- mogen hoofdletters,  kleine letters, cijfers en under_score bevatten
- mogen speciale letters bevatten é, è (beter niet voor leesbaarheid en printbaarheid)
"""

"""
Deze namen zijn niet toegelaten als variable-namen.
Omdat ze een keyword zijn van python.
Leer de lijst niet van buiten. 

False      class      finally    is         return
None       continue   for        lambda     try
True       def        from       nonlocal   while
and        del        global     not        with
as         elif       if         or         yield
assert     else       import     pass       
async      except     in         raise      
await      break

Deze namen gebruik je beter niet: match     case
Sinds Python 3.10 zijn dit ook keywords.
Maar om te vermijden dat oude code niet meer 
zou werken zijn ze eigenlijk wel toegelaten.  
"""
