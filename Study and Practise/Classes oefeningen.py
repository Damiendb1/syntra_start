class Person:
    def __init__(self, age, weight, height, first_name, last_name, catch_phrase):
        self.age = age
        self.weight = weight
        self.height = height
        self.first_name = first_name
        self.last_name = last_name
        self.catch_phrase = catch_phrase

    def walk(self):
        print("I walk like a duck")

    def run(self):
        print("I run like a horse")


user = Person(29, 100, 192, "John", "Snow", "You know nothing, John Snow")

print(user.catch_phrase)

user.walk()
user.run()


class Bottle:
    def __init__(self, color, size, brand):
        self.color = color
        self.size = size
        self.brand = brand

    def fill(self):
        print("I fill my bottle with water")

    def empty(self):
        print("I empty my bottle")

    def drink(self):
        print("I drink from my bottle")


bottle = Bottle("rood", "Groot", "Coca Cola")
bottle.fill()
bottle.drink()
bottle.empty()


class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return f"{self._width:.1f} cm"

    @property
    def height(self):
        return f"{self._height:.1f} cm"

    @width.setter
    def width(self, new_width):
        if new_width >= 0:
            self._width = new_width
        else:
            print("Width must be groter dan 0")

    @height.setter
    def height(self, new_height):
        if new_height >= 0:
            self._height = new_height
        else:
            print("height must be groter dan 0")




rectangle = Rectangle(3, 4)

rectangle.width = 5
rectangle.height = 10

# del rectangle.width
# del rectangle.height

print(rectangle.width)
print(rectangle.height)
