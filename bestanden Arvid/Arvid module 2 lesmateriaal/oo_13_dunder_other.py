# python heeft nog heel wat andere dunder methods
# voor de volledige opliisting: https://www.pythonmorsels.com/every-dunder-method/
# Heel wat dunders zal je zelden of nooit nodig hebben.
from decimal import Decimal


# Nog enkele bruikbare dunder methods voor de  klasse Gram

class Gram:
    """
    Class to represent a weight in grams
    """

    def __init__(self, value: Decimal = Decimal(0)):
        self.value = value

    def __repr__(self) -> str:
        if self.value is None:
            return "None"
        return f"{self.value:_}g"

    def __neg__(self):
        return Gram(-self.value)

    def __pos__(self):
        return Gram(self.value)

    def __abs__(self):
        return Gram(abs(self.value))

    def __round__(self, ndigits: int | None = None):
        return Gram(round(self.value, ndigits))
    

w1 = Gram(Decimal('-250.3'))
print(-w1)
print(+w1)
print(abs(w1))
print(round(w1))


# Oefening 1
# Maak een class UppercaseString die een string bewaart.
# Twee instanties  zijn gelijk wanneer ze in uppercase gelijk zijn
#   s1 = NoCaseString("Hello World")
#   s2 = NoCaseString("hello WOrld")
#   print(s1 == s2)  # => True

# De som van twee UppercaseStrings is:
#   de concatenatie van de eerste letter van s1, dan de eerste letter van s2,
#   dan de tweede letter van s1, dan de tweede letter van s2, enz.
#   Alles in uppercase.
#   UppercaseString("Hallo") + UppercaseString("Hallo")  => HCALLALAOSSEN
#   UppercaseString("Claassen" + UppercaseString("arVId")  => CALRAVAISDSEN

# De gehele deling van twee UppercaseString's is s1 zonder alle letters van s2
#   UppercaseString("Hallo") // UppercaseString("Claassen")  => HLLO
#   UppercaseString("Claassen") // UppercaseString("hello")  => CAASSN

# Oefening 2
# Maak een class ThreeBool die de waardes True, False of Maybe  omvat.
# Je overschrijft de  dunder methods: __and__, __or__, __invert__
# Probeer elke function met zo weinig mogelijk if statements.
#        __and__(self, other)
#             False and False = False
#             False and True = False
#             False and Maybe = False
#             True and False = False
#             True and True  = True
#             True and Maybe = Maybe
#             Maybe and False = False
#             Maybe and True = Maybe
#             Maybe and Maybe = Maybe
#        __or__(self, other):
#             False or False = False
#             False or True = True
#             False or Maybe = Maybe
#             True or False = True
#             True or True  = True
#             True or Maybe = True
#             Maybe or False = Maybe
#             Maybe or True =True
#             Maybe or Maybe= Maybe

#        __invert__(self):
#             not False = True
#             not True = False
#             not Maybe = Maybe


