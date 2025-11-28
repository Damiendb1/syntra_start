# We maken een class Product met name en price als attributen

from decimal import Decimal


class Product:
    def __init__(self, name:str, price: Decimal ):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Product '{self.name}' met prijs {self.price}€"

    def price_with_vat(self, vat: Decimal = Decimal('0.21')):
        return self.price * (1+vat)

# instantie maken en spelen met de attributen en function
p = Product("Pizza", Decimal('12.50'))
print(p)
print(p.price)
print(p.price_with_vat())

# wistjedatje
print(vars(p))  # print een dict met alle attributen en bijhorende waarde van een object
print(dir(p)) # print alle dunder functions, alle functions en attributen

