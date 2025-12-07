from decimal import Decimal


# Maak een klasse die een gewicht in gram weergeeft.
#
# class Gram:
#     """
#     Class to represent a weight in grams
#     """
#
#     def __init__(self, value: Decimal = Decimal(0)):
#         self.value = value
#
#     def __repr__(self) -> str:
#         if self.value is None:
#             return "None"
#         return f"{self.value:_}g"
#
#     def __eq__(self, other):
#         return self.value == other.value
#
# g1 = Gram(Decimal('100'))
# g2 = Gram(Decimal('100'))
#
# print(f"{g1 == g2=}")


class Car:
    """
    class to represent an car
    """
    def __init__(self, price, brand):
        self.price = price
        self.brand = brand

    def __repr__(self):
        return f"price= {self.price}€, brand= {self.brand}"

    def __eq__(self, other):
        return self.price == other.price

    def __lt__(self, other):
        return self.price < other.price

    def __le__(self, other):
        return self.price <= other.price

    def __gt__(self, other):
        return self.price > other.price

    def __ge__(self, other):
        return self.price >= other.price

    def __ne__(self, other):
        return self.price != other.price



a = Car(55000, "Tesla")
b= Car(50000, "volkswagen")

print(a > b )
print(a < b )
print(a == b )


7