from abc import ABC, abstractmethod

class Distance(ABC):
    """
    Abstract base class for distances
    """

    def __init__(self, value: float):
        self.value = value

    def __repr__(self):
        return f"{self.value:.3f}{self.get_unit()}"

    def __lt__(self, other):
        if not isinstance(other, Distance):
            return NotImplemented
        return self.to_meter() < other.to_meter()

    def __le__(self, other):
        if not isinstance(other, Distance):
            return NotImplemented
        return self < other or self == other

    def __gt__(self, other):
        if not isinstance(other, Distance):
            return NotImplemented
        return self.to_meter() > other.to_meter()

    def __ge__(self, other):
        if not isinstance(other, Distance):
            return NotImplemented
        return self > other or self == other



    @abstractmethod
    def get_unit(self):
        ...

    @abstractmethod
    def get_factor(self):
        ...

    def to_meter(self):
        return self.value * self.get_factor()

    def from_meter(self, value_in_meter):
        return value_in_meter / self.get_factor()

    def __eq__(self, other):
        if not isinstance(other, Distance):
            return NotImplemented
        tolerance = 1e-5
        return abs(self.to_meter() - other.to_meter()) < tolerance


    def __add__(self, other):
        in_meter = self.to_meter() + other.to_meter()
        in_own_unit = in_meter / self.get_factor()
        return self.__class__(in_own_unit)

    def __sub__(self, other):
        in_meter = self.to_meter() - other.to_meter()
        in_own_unit = in_meter / self.get_factor()
        return self.__class__(in_own_unit)

    def __mul__(self, other):
        return self.__class__(self.value * other)

    def __truediv__(self, other):
        return self.__class__(self.value / other)

class MetricDistance(Distance):
    """class voor metrische afstanden"""
    def __repr__(self):
        return f"Metric [{self.value:.3f}{self.get_unit()}]"


class ImperialDistance(Distance):
    """class voor imperiale afstanden"""
    def __repr__(self):
        return f"Imp [{self.value:.3f}{self.get_unit()}]"



class KiloMeter(MetricDistance):
    def get_factor(self):
        return 1000
    def get_unit(self):
        return "km"

class Micrometer(MetricDistance):
    def get_factor(self):
        return 1e-6
    def get_unit(self):
        return "Micrometer"

class Foot(ImperialDistance):
    def get_factor(self):
        return 0.3048
    def get_unit(self):
        return "foot"

class Yard(ImperialDistance):
    def get_factor(self):
        return 0.9144
    def get_unit(self):
        return "yard"

class NautischeMijl(MetricDistance):
    def get_factor(self):
        return 1852
    def get_unit(self):
        return "nautische-mijl"

class Lichtjaar(MetricDistance):
    def get_factor(self):
        return 9.4607e15
    def get_unit(self):
        return "Lichtjaar"




d1 = KiloMeter(10)
d2 = Foot(135)

print(d1)
print(d2)
print(d1 + d2)  #3
print(d2 + d1)
print(d1 - d2)  #4
print(d2 - d1)
print(d1,Distance, "gelukt")
print(d2,Distance, "gelukt")
print(d1 * 3)   #5
print(d2 * 3)
print(d1 / 2)   #6
print(d2 / 2)



class Weight(ABC):
    """Abstracte class voor weights"""
    def __init__(self, value: float):
        self.value = value

    @abstractmethod
    def get_unit(self):
        ...
    @abstractmethod
    def get_factor(self):
        ...
    def __repr__(self):
        return f"{self.value:.3f}{self.get_unit()}"

    def to_gram(self):
        return self.value * self.get_factor()

class Gram(Weight):
    def get_factor(self):
        return 1
    def get_unit(self):
        return "g"

class Kilogram(Weight):
    def get_factor(self):
        return 1000
    def get_unit(self):
        return "kg"

class Ton(Weight):
    def get_factor(self):
        return 1000000
    def get_unit(self):
        return "ton"

class Ounce(Weight):
    def get_factor(self):
        return 28.349523125
    def get_unit(self):
        return "oz"

class Pound(Weight):
    def get_factor(self):
        return 453.59237
    def get_unit(self):
        return "pound"

class Stone(Weight):
    def get_factor(self):
        return 6350.29318
    def get_unit(self):
        return "stone"


w1 = Gram(500)
w2 = Kilogram(2)
w3 = Ton(1)
w4 = Ounce(3)
w5 = Pound(5)
w6 = Stone(1)

print(w1)
print(w2)
print(w3)
print(w4)
print(w5)
print(w6)

print("500 g in gram:", w1.to_gram())
print("2 kg in gram:", w2.to_gram())
print("1 ton in gram:", w3.to_gram())
print("3 oz in gram:", w4.to_gram())
print("5 lb in gram:", w5.to_gram())
print("1 stone in gram:", w6.to_gram())