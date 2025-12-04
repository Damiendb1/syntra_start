# Er zijn nog een paar tekorten aan de klasse Meter?
# 1/ design: Waarom is in het vorige voorbeeld Meter de super klasse van alle andere afstand klassen?
#            Wat maakt meter speciaal?
# 2/ Je kan onvolledige sub classes van Meter maken. Een programmeur kan bijvoorbeeld enkel get_factor
#    overschrijven maar per ongeluk vergeten om ook get_unit te overschrijven.

class Meter:
    def __init__(self, value: float):
        self.value = value

    def __repr__(self):
        return f"{self.value:.3f}{self.get_unit()}"  # self.unit is vervangen door self.get_unit()

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


# Onderstaande definities zijn onvolledig
class InchWrong1(Meter):
    def get_factor(self):
        return 0.0254
    # Er wordt vergeten om ook get_unit te overschrijven


i1 = InchWrong1(1.2)
print(i1)
print(i1.to_meter())


class InchWrong2(Meter):
    def get_unit(self):
        return "In"
    # Er wordt vergeten om ook get_factor  te overschrijven


i2 = InchWrong2(1.2)
print(i2)
print(i2.to_meter())


# De klasse hiërarchie is nu
# Meter
#  |
#  +-- KiloMeter
#  |
#  +-- Mile

# Vermits Meter op zich niet bijzonder is t.o.v. Mile, Kilometer, Inch hervormen we de hiërarchie
# Met een nieuwe abstracte klasse Distance.

# De klasse opbouw is dan als volgt:
# Distance
#  |
#  +-- Meter
#  |
#  +-- KiloMeter
#  |
#  +-- Mile

class Distance:
    def __init__(self, value: float):
        self.value = value

    def __repr__(self):
        return f"{self.value:.3f}{self.get_unit()}"

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




class Meter(Distance):
    def get_factor(self):
        return 1

    def get_unit(self):
        return "m"


class KiloMeter(Distance):
    def get_factor(self):
        return 1

    def get_unit(self):
        return "m"


# Subclasses van Distances kunnen nog steeds onvolledige definities hebben.
class InchWrong3(Distance):
    def get_factor(self):
        return 0.0254


class InchWrong4(Distance):
    def get_factor(self):
        return 0.0254


# Dit lossen we op door van Distance een abstracte klassen te maken.
# Een klasse is abstract als deze niet alle methods implementeert.
# Een subklasse van Distance is volledig wanneer get_factor en get_unit worden overschreven.
# We maken deze twee functies leeg


class Distance:
    def __init__(self, value: float):
        self.value = value

    def __repr__(self):
        return f"{self.value:.3f}{self.get_unit()}"  # self.unit is vervangen door self.get_unit()

    def get_unit(self):
        raise NotImplementedError("get_unit moet expliciet gemaakt worden door de subclass")

    def get_factor(self):
        raise NotImplementedError("get_factor moet expliciet gemaakt worden door de subclass")

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


class Meter(Distance):
    def get_factor(self):
        return 1

    def get_unit(self):
        return "m"


class Inch(Distance):
    def get_factor(self):
        return 0.0254

    def get_unit(self):
        return "in"


class InchWrong5(Distance):
    def get_factor(self):
        return 0.0254


class InchWrong6(Distance):
    def get_unit(self):
        return "in"


m1 = Meter(1.2)
print(m1 + Inch(10))
print(m1 + InchWrong5(10))
print(m1 + InchWrong6(10))
