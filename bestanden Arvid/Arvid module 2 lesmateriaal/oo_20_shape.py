"""
Overerving voorbeeld met vormen.

Ik wil een programma dat vormen kan tekenen op een scherm.
Een scherm is een raster van punten.

De function draw() moet een vorm op het scherm tekenen,
zonder te weten hoe die vormen eruit ziet, of hoe die vorm getekend moeten worden.
Het is aan elke vorm op zich om aan te geven hoe die getekend moet worden.
"""
import math
from abc import ABC, abstractmethod
from decimal import Decimal


# We maken een class Coordinate met x en y als attributen
# x en y zijn van het type int
# Coördinaten kunnen vergeleken worden om te kijken of ze aan elkaar gelijk zijn, of niet
#   => __eq__ en __ne__
# Coördinaten kunnen opgeteld en afgetrokkken worden.
#   => __add__ en __sub__
# Het nut van hash() komt in een latere les aanbod.

class Coordinate:
    """
    Represents a two-dimensional coordinate with x and y values.

    The Coordinate class allows for handling and manipulating coordinates in a
    2D space. It supports common operations like addition, subtraction, equality
    checks, inequality checks, and allows for usage in hashed data structures
    like sets.
    """

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"(x={self.x}, y={self.y})"  # (x,y)

    def __eq__(self, other) -> bool:
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self.__eq__(other)

    def __add__(self, other):
        return Coordinate(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Coordinate(self.x - other.x, self.y - other.y)

    def __hash__(self):
        return hash((self.x, self.y))


# Geen enkele vorm is superieur aan een andere vorm.
# Maar elke vorm heeft wel overeenkomstige eigenschappen
#   - positie
#   - kleur
# En overeenkomstige functionaliteit
#   - bereken de punten om de vorm te tekenen: get_dots
#   - omtrek: perimeter
#   - oppervlakte: area
# ....

# Dus we starten met een abstracte klasse Shape
# Shape erft over van ABC

class Shape(ABC):
    """
    Represents an abstract base class for geometric shapes.

    This class serves as a blueprint for various geometric shapes. It
    defines attributes such as position and color, and declares abstract
    methods that must be implemented by subclasses. These abstract methods
    include functionality for representing the shape as a string, calculating
    its area, perimeter, finding the shape's central point, and obtaining its
    defining dots/vertices.
    """

    def __init__(self, position: Coordinate, color: str = "."):
        # Elke vorm heeft een positie en een kleur
        # Die nemen we over van de input parameters

        # We voeren paar controle uit dat de input de juiste types hebben.
        if not isinstance(position, Coordinate):
            raise ValueError("Position must be an instance of Coordinate")
        if not isinstance(color, str) or len(color) != 1:
            raise ValueError("Color must be a single character string")

        self.color = color
        self.position = position

    # Alle andere functies zijn abstracte functies
    # De effectieve subclass moet deze implementeren
    @abstractmethod
    def __repr__(self):
        ...

    @abstractmethod
    def perimeter(self) -> Decimal:
        ...

    @abstractmethod
    def area(self) -> Decimal:
        ...

    @abstractmethod
    def center(self) -> Decimal:
        ...

    @abstractmethod
    def get_dots(self) -> set:
        ...


""""
# We gaan voor deze hiërachie
Shape
 |
 |-- Circle 
 |
 |-- Rectangle
        |
        |----  Square
"""


class Rectangle(Shape):
    """
    Rectangular shape with a specified width and height.
    """

    def __init__(self,
                 position: Coordinate,
                 color: str,
                 width: int,
                 height: int):
        # De init van rectangle het twee extra parameters t.o.v. Shape

        # we roepen de init van Shape aan
        super().__init__(position, color)
        # Shape.__init__(self, position, color) had ook gekund. We komen hierop terug bij multiple inheritance

        # We nemen  de attributen toe die enkel voor een rechthoek gelden over uit de parameters..
        self.width = width
        self.height = height

    def __repr__(self):
        return f"Rectangle(position={self.position}, color={self.color}, width={self.width}, height={self.height})"

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def get_dots(self):
        ret = set()
        for x in range(self.width):
            for y in range(self.height):
                if x == 0 or x == self.width - 1 or y == 0 or y == self.height - 1:
                    ret.add(Coordinate(x, y) + self.position)
        return ret

    def center(self):
        return Coordinate(self.position.x + self.width // 2, self.position.y + self.height // 2)


class Square(Rectangle):
    """
    A square is a rectangle with equal width and height.
    """

    def __init__(self, position: Coordinate, color, side):
        # Het enige verschil tussen een rechthoek en een vierkant is dat bij
        # een vierkant de breedte en hoogte hetzelfde zijn

        # We hebben dus enkel side als extra parameter nodig
        # we kunnen de init van Rectangle aanroepen met height en width gelijk aan side
        super().__init__(position, color, side, side)

    def __repr__(self):
        return f"Square(position={self.position}, color={self.color}, side={self.width})"


class Circle(Shape):

    def __init__(self, position, color, radius):
        # Een cirkel heeft een straal / radius
        super().__init__(position, color)
        self.radius = radius

    def __repr__(self):
        return f"Cirkel met straal {self.radius}"

    def area(self):
        return Decimal("3.14195") * self.radius ** 2

    def perimeter(self) -> Decimal:
        return Decimal("3.14159") * self.radius * 2

    def get_dots(self):
        ret = set()
        for angle in range(360):
            x = int(self.radius * math.cos(math.radians(angle)) + self.position.x)
            y = int(self.radius * math.sin(math.radians(angle)) + self.position.y)
            ret.add(Coordinate(x, y))
        return ret

    def center(self):
        return self.position


# We maken een 'scherm' als een rij van strings bestaand uit puntjes.


SCREENWIDTH = 100
SCREENHEIGHT = 50
screen = [['.' for _ in range(SCREENWIDTH)] for _ in range(SCREENHEIGHT)]


def draw(shape: Shape) -> None:
    """
    Draws a given shape on the screen by updating the screen array based on the
    shape's dots and color.

    :param shape: Shape object that contains the list of dots to be painted
    """
    for dot in shape.get_dots():
        screen[dot.y][dot.x] = shape.color

def print_screen():
    """
    Print the screen line by line
    """
    for row in screen:
        print(''.join(row))

circle = Circle(position=Coordinate(20, 22), color='@', radius=10)
draw(circle)
print_screen()

r = Rectangle(position=Coordinate(23, 4), color='#', width=40, height=13)
draw(r)
print_screen()

r = Square(position=Coordinate(25, 7), color='*', side=10)
draw(r)
print_screen()

fs = FilledSquare(position=Coordinate(2, 2), color='X', side=4)
draw(fs)
print_screen()


# oefening maak een subclass FilledSquare die een volledig gevuld vierkant tekent op het scherm.


