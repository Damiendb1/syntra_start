# Bij overerving neemt de subklasse alle attributen en functies over van de superklasse
# De subklasse kan dan attributen en functies toevoegen en/of overschrijven.
# Meestal is de subklasse een specifiek geval van de superclass.
# DutchAdress(Address) : een adres met een specifiek formaat voor zip_code
# Manager(Employee): een werknemer met een specifiek verloning systeem
# VIP(Person): een persoon die meer voordelen krijgt tijdens een concert

# We maken een class om een afstand voor te stellen.

class KiloMeter:
    """Represents a distance in meters."""

    def __init__(self, value: float):
        self.value = value

    def __repr__(self):
        return f"Afstand({self.value} km)"

    def __eq__(self, other):
        return self.value == other.value

    def __add__(self, other):
        return KiloMeter(self.value + other.value)

    # andere dunders zijn weggelaten voor de leesbaarheid


class Mile(KiloMeter):
    def __init__(self, value: float):
        super().__init__(value * 1.60934)


d1 = KiloMeter(10)
d2 = Mile(10)
print(d1 + d2)
print(d2 + d1)


# Is Mile een specifiek geval van KiloMeter?  Amerikanen zullen dat tegenspreken.
# In bovenstaand voorbeeld wordt een Mile sowieso omgezet naar een KiloMeter. Een mile verliest dus diens eigenheid.

# De wetenschap hanteert 'meter' als universele eenheid.
# Alle andere eenheden worden kunnen omgezet naar meter.


class Meter:
    def __init__(self, value: float):
        self.value = value
        self.unit = "m"

    def __repr__(self):
        return f"{self.value:.3f}{self.unit}"

    def to_meter(self):
        return self.value

    def from_meter(self, value):
        return self.value

    def __eq__(self, other):
        return self.to_meter() == other.to_meter()

    def __add__(self, other):
        return self.__class__(self.from_meter(self.to_meter() + other.to_meter()))


class KiloMeter(Meter):
    def __init__(self, value: float):
        super().__init__(value)
        self.unit = "km"

    def to_meter(self):
        return self.value * 1000

    def from_meter(self, value):
        return value / 1000

class CentiMeter(Meter):
    def __init__(self, value: float):
        super().__init__(value)
        self.unit = "cm"

    def to_meter(self):
        return self.value / 100

    def from_meter(self, value):
        return value * 100

class Mile(Meter):
    def __init__(self, value: float):
        super().__init__(value)
        self.unit = "M"

    def to_meter(self):
        return self.value * 1609.34

    def from_meter(self, value):
        return value / 1609.34


km = KiloMeter(10)
print(km)
print(km.to_meter())

cm = CentiMeter(10)
print(cm)
print(cm.to_meter())

m = Mile(2)
print(m)
print(m.to_meter())

k1 = KiloMeter(1)
m1 = Mile(1)
print(k1.to_meter())
print(m1.to_meter())
print(k1 == m1)

print(k1+m1)  # geeft Kilometer object  terug
print(m1+k1)  # geeft Mile object terug


# Wanneer we een nieuwe eenheid toevoegen, dan moeten we zeer goed opletten:
# 1. De call naar super moet met de juiste eenheid aangeroepen worden
# 2. De omzetting van in to_meter en from_meter moet met dezelfde eenheid uitgevoerd worden
# 3. We mogen niet vergeten om ook de unit goed te zetten.

class HectoMeter(KiloMeter):
    def __init__(self, value: float):
        super().__init__(value / 10)  # fout moet 100 zijn
        self.unit = "cm"  # fout: moet hm zijn

    def to_meter(self):
        return self.value # fout: moet / 100

    def from_meter(self, value):
        return value * 1000 # fout: moet * 100 zijn

# We kunnen de super class Meter hiervoor aanpassen:
# Voeg een method toe om de factor die in __init__, to_meter en from_meter gebruikt wordt, terug te geven.
# Pas __init__, to_meter en from_meter aan zodat ze de juiste factor gebruiken.
# Maak ook een function aan die de eenheid teruggeeft.

class Meter:
    def __init__(self, value: float):
        self.value = value

    def __repr__(self):
        return f"{self.value:.3f}{self.get_unit()}" #   self.unit is vervangen door self.get_unit()

    def get_unit(self):
        return "m"

    def get_factor(self):
        return 1

    def to_meter(self):
        return self.value * self.get_factor()

    def from_meter(self, value):
        return self.value / self.get_factor()

    def __eq__(self, other):
        return self.to_meter() == other.to_meter()

    def __add__(self, other):
        in_meter = self.to_meter() + other.to_meter()
        in_own_unit = in_meter / self.get_factor()
        return self.__class__(in_own_unit)


# De super klasse wordt ingewikkelder, maar elke sub klasse wordt eenvoudiger.

class KiloMeter(Meter):
    def get_factor(self):
        return 1000

    def get_unit(self):
        return "km"

class Mile(Meter):
    def get_factor(self):
        return 1609.34

    def get_unit(self):
        return "M"


k10 = KiloMeter(10)
m10 = Mile(10)
print(k10)
print(m10)
print(k10 + m10)
print(m10 + k10)




#
#
#
# from abc import ABC, abstractmethod
#
#
# class Temperature(ABC):
#     """Abstract base class for temperature scales."""
#
#     def __init__(self, value: float):
#         self.value = value
#         self.label = None
#
#     @abstractmethod
#     def to_kelvin(self) -> float:
#         """Convert to Kelvin."""
#         pass
#
#     @abstractmethod
#     def __rep__(self) -> str:
#         """Human-readable representation."""
#         return f"{self.value:.2f} °C"
#
#     def __eq__(self, other):
#         # Compare based on Kelvin value
#         if isinstance(other, Temperature):
#             return self.to_kelvin() == other.to_kelvin()
#         return NotImplemented
#
#     def __lt__(self, other):
#         # Less-than comparison based on Kelvin
#         if isinstance(other, Temperature):
#             return self.to_kelvin() < other.to_kelvin()
#         return NotImplemented
#
#     def __gt__(self, other):
#         # Less-than comparison based on Kelvin
#         if isinstance(other, Temperature):
#             return self.to_kelvin() > other.to_kelvin()
#         return NotImplemented
#
#
# class Celsius(Temperature):
#     def __init__(self, value):
#         super().__init__(value)
#         self.label = "°C"
#
#     def to_kelvin(self) -> float:
#         return self.value + 273.15
#
#
# class Fahrenheit(Temperature):
#     def __init__(self, value):
#         super().__init__(value)
#         self.label = "°F"
#
#     def to_kelvin(self) -> float:
#         return (self.value - 32) * 5 / 9 + 273.15
#
#
# class Kelvin(Temperature):
#     def __init__(self, value):
#         super().__init__(value)
#         self.label = "K"
#
#     def to_kelvin(self) -> float:
#         return self.value
