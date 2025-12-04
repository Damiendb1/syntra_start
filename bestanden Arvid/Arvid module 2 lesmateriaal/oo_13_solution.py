# Oefening 1
# Maak een class UppercaseString die een string bewaart.
# Twee instanties  zijn gelijk wanneer ze in uppercase gelijk zijn
#   s1 = UppercaseString("Hello World")
#   s2 = UppercaseString("hello WOrld")
#   print(s1 == s2)  # => True

# De som van twee UppercaseStrings is:
#   de concatenatie van de eerste letter van s1, dan de eerste letter van s2,
#   dan de tweede letter van s1, dan de tweede letter van s2, enz.
#   Alles in uppercase.
#   UppercaseString("Hallo") + UppercaseString("Claassen")  => HCALLALAOSSEN
#   UppercaseString("Claassen" + UppercaseString("arVId")  => CALRAVAISDSEN

# De gehele deling van twee UppercaseString's is s1 zonder alle letters van s2
#   UppercaseString("Hallo") // UppercaseString("Claassen")  => HO
#   UppercaseString("Claassen") // UppercaseString("hello")  => CAASSN

from itertools import zip_longest


class UppercaseString:
    def __init__(self, value: str):
        self.value = value

    def __eq__(self, other):
        return self.value.upper() == other.value.upper()

    def __add__(self, other):
        res = ""
        for a, b in zip_longest(self.value, other.value):
            if a is not None:
                res += a.upper()
            if b is not None:
                res += b.upper()
        return res

    def __truediv__(self, other):
        return "".join([ch.upper() for ch in self.value if ch not in other.value])


s1 = UppercaseString("Hello World")
s2 = UppercaseString("hello WOrld")
print(s1 == s2)  # => True
print(UppercaseString("Hallo") + UppercaseString("Claassen"))
print(UppercaseString("Claassen") + UppercaseString("arVId"))
print(UppercaseString("Hallo") / UppercaseString("Claassen"))
print(UppercaseString("Claassen") / UppercaseString("hello"))

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


TRUE = "True"
FALSE = "False"
MAYBE = "Maybe"

VALID = {TRUE, FALSE, MAYBE}


class ThreeBool:
    """
    Three value boolean
    """

    def __init__(self, value: str):
        if value not in VALID:
            raise ValueError("Value must be 'True', 'False', or 'Maybe'")
        self.value = value

    def __and__(self, other):
        if self.value == FALSE or other.value == FALSE:
            return ThreeBool(FALSE)
        if self.value == MAYBE or other.value == MAYBE:
            return ThreeBool(MAYBE)
        return ThreeBool(TRUE)

    def __or__(self, other):
        # OR truth table
        if self.value == TRUE or other.value == TRUE:
            return ThreeBool(TRUE)
        if self.value == MAYBE or other.value == MAYBE:
            return ThreeBool(MAYBE)
        return ThreeBool(FALSE)

    def __eq__(self, other):
        return self.value == other.value

    def __ne__(self, other):
        return self.value != other.value

    def __repr__(self):
        return f"ThreeBool('{self.value}')"


a = ThreeBool("True")
b = ThreeBool("Maybe")
c = ThreeBool("False")

print(a and b)  # ThreeBool('Maybe')
print(a or c)  # ThreeBool('True')
print(b and c)  # ThreeBool('Maybe')
print(a == b)  # False
print(b != c)  # True
