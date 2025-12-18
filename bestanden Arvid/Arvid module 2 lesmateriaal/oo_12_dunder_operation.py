from decimal import Decimal


# we hernemen de class Gram. Voor de bondigheid zijn de comparison dunder methods weggelaten.
# We willen kunnen rekenen met gewichten
# w1 + w2 : De som van twee gewichten is een nieuw gewicht.
# w1 - w2:  Het verschil van twee gewichten is een nieuw gewicht.

# Hiertoe dienen we de dunder methods __add__, __sub__
# w1 * w2 is niet mogelijk. Hoeveel is 1kg * 30g.
# w1 * int is wel mogelijk: 30g * 2 = 60g
# w1 / w2 is niet mogelijk  mogelijk: 1kg / 30g  is zin loog
# w1 / int of is wel mogelijk 30g/6 = 5g


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

    def __eq__(self, other):
        return self.value == other.value

    # Voor de bondigheid zijn de comparison dunder methods weggelaten.

    def __add__(self, other):
        # tel de waarden van beide gewichten samen en maak een nieuw gewicht aan
        return Gram(self.value + other.value)

    def __sub__(self, other):
        # trak de waarden van beide gewichten af en maak een nieuw gewicht aan
        return Gram(self.value - other.value)

    def __mul__(self, other):
        # maak een nieuw gewicht aan met de waarde van self.value * other
        return Gram(self.value * other)

    def __truediv__(self, other):
        # maak een nieuw gewicht aan met de waarde van self.value * other
        return Gram(self.value / other)

    def __floordiv__(self, other):
        # maak een nieuw gewicht aan met de waarde van self.value * other
        return Gram(self.value // other)

    def __mod__(self, other):
        # maak een nieuw gewicht aan met de waarde van self.value * other
        return Gram(self.value % other)

w1 = Gram(Decimal('10'))
w2 = Gram(Decimal('15'))
w3 = Gram(Decimal('30'))



print(f"{w1 + w2=}")
print(f"{w3 - w2=}")
w1 += w3
print(w1)
print(f"{w3 * Decimal('3')}")
print(f"{w3 /  Decimal('3.3')}")
print(f"{w3 // Decimal('3')}")
print(f"{w3 % Decimal('3')}")


# We hebben __mul__ gedefinieerd, maar toch werkt 3 * w3 niet.
try:
    print(f"{3 * w3}")
except TypeError:
    print("TypeError:  int * Weight is niet ondersteund")

# w3 * 3 wordt onderliggend omgezet naar Weight.__mul__(w3, 3)
# 3 * w3 wordt onderliggend omgezet naar int.__mul__(3, w3)
# De int.__mul__() ondersteunt geen vermenigvuldiging met  Weight.

# Wanneer v een object is van class Other   en    Other.__mul(self, Weight) is niet gedefinieerd,
# dan probeert python Weight.__rmul__(Weight, v) op te roepen.
# Hetzelfde geldt voor de andere operatoren:

# +	    __add__	        __radd__
# -	    __sub__	        __rsub__
# *	    __mul__	        __rmul__
# /	    __truediv__	    __rtruediv__
# //	__floordiv__	__rfloordiv__
# %	    __mod__	        __rmod__
# **	__pow__     	__rpow__


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

    def __mul__(self, other):

        return Gram(self.value * other)

    def __rmul__(self, other):

        return Gram(self.value * other)

w1 = Gram(Decimal('10'))
d1 = Decimal('3')

# vermits __rmul__ is gedefinieerd, dan wordt 3 * w1 geconverteerd naar Gram.__rmul__(w1, 1)
# en werkt onderstaande code
print(f"{Decimal('3')* w1=}")

