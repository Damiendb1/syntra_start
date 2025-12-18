# python heeft een module specifiek voor abstracte classes, nl. module abc.
# abc staat voor abstract base classes.
# om aan te geven dat een class abstract is, kan je ABC als superclass gebruiken.
# Elke function die expliciet niet geïmplementeerd is, wordt aangegeven door er @abstractmethod voor te zetten.
# De body van dergelijk function kan je vullen met ... (3 puntjes)

from abc import ABC, abstractmethod


class Distance(ABC):
    def __init__(self, value: float):
        self.value = value

    def __repr__(self):
        return f"{self.value:.3f}{self.get_unit()}"  # self.unit is vervangen door self.get_unit()

    @abstractmethod
    def get_unit(self):
        ...

    @abstractmethod
    def get_factor(self):
        ...

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


# Voor goede subclasses verandert er niets
class KiloMeter(Distance):
    def get_factor(self):
        return 1000

    def get_unit(self):
        return "km"


# # Bij onvolledige subclasses, kan pycharm helpen:
# # pycharm duidt aan: class InchWrong7 must implement all abstract methods
#
# class InchWrong7(Distance):
#     def get_factor(self):
#         return 0.0254
#     # get unit is niet gedefinieerd
#
# # Bij een instance van InchWrong7, geeft python als een boodschap: can not instantiate abstract class.
# i1 = InchWrong7(1.2)
# print(i1)



# Oefeningen bij distance
# 1: Maak een subklasse van Distance voor MicroMeter, Foot, Yard, Nautische Mijl, Lichtjaar. Zoek de definities maar op
# 2: Er wordt met floats gewerkt. Er is dus kans op rekenfouten. Zorg ervoor dat twee afstanden gelijk zijn
#    wanneer het verschil in meter kleiner is dan 0.00001m
#    Hiervoor moet je de __eq__() methode in Distance overschrijven.
# 3: Maak het mogelijk om twee afstanden te vergelijken ( <, <=, >, >=)
# 4: Maak het mogelijk om twee afstanden af te trekken.
# 5: Maak het mogelijk om een afstand te vermenigvuldigen met een getal.
# 6: Maak het mogelijk om een afstand te delen door een getal.
# 7A: Inch, Yard, Foot, Mijl behoren tot het imperial systeem.
#     Meter, kilometer, nautische mijl behoren tot het metric system.
#     Maak hiervoor twee afzonderlijke abstract classes MetricDistance en ImperialDistance.
#
#           Distance
#            |
#            +-- MetricDistance
#            |    |
#            |    +-- Meter
#            |    |
#            |    +-- KiloMeter
#            |    |
#            |    +-- Lichtjaar
#            |
#            +-- ImperialDistance
#                 |
#                 +-- Inch
#                 |
#                 +-- Foot
#                 |
#                 +-- Mile
# 7B: Zorg er voor dat elke Metric Distance wordt afgedrukt als "Metric[xxx]" met xxx de waarde en unit van de afstand.
#      bv:  Kilometer(10)  wordt afgedrukt als "Metric[10km]"
#     Zorg er voor dat elke Imperial Distance wordt afgedrukt als "Imp[xxx]"  met xxx de waarde en unit van de afstand.


# Oefening 8: Maak een abstract class Weight met subclasses: Gram, KiloGram, Ton, Ounch, Pound, Stone

