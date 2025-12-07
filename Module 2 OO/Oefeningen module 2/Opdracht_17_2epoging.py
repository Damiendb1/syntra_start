from abc import ABC, abstractmethod


# from decimal import Decimal

class Distance(ABC):
    """
    .....
    """

    def __init__(self, value: float):
        self.value = value

    def __repr__(self):
        return f"{self.value:.3f}{self.get_unit()}"

    def __lt__(self, other):
        return self.to_meter() < other.to_meter()

    def __le__(self, other):
        return self < other or self == other

    def __gt__(self, other):
        return self.to_meter() > other.to_meter()

    def __ge__(self, other):
        return self > other or self == other

    @abstractmethod
    def get_unit(self):
        ...

    @abstractmethod
    def get_factor(self):
        ...

    def to_meter(self):
        return self.value * self.get_factor()

    def from_meter(self, value):
        return value / self.get_factor()

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
        in_meter = self.to_meter() * other.to_meter()
        in_own_unit = in_meter / self.get_factor()
        return self.__class__(in_own_unit)

    def __truediv__(self, other):
        in_meter = self.to_meter() / other.to_meter()
        in_own_unit = in_meter / self.get_factor()
        return self.__class__(in_own_unit)


class KiloMeter(Distance):
    """
    .....
    """

    def get_factor(self):
        return 1000

    def get_unit(self):
        return "km"


class Micrometer(Distance):
    def get_factor(self):
        return 1e-6

    def get_unit(self):
        return "Micrometer"


class Foot(Distance):
    def get_factor(self):
        return 0.3048

    def get_unit(self):
        return "foot"


class Yard(Distance):
    def get_factor(self):
        return 0.9144

    def get_unit(self):
        return "yard"


class Nautische_mijl(Distance):
    def get_factor(self):
        return 1852

    def get_unit(self):
        return "nautische-mijl"


class Lichtjaar(Distance):
    def get_factor(self):
        return 9.4607e15

    def get_unit(self):
        return "Lichtjaar"

