# import random
#
# class Die:
#     def __init__(self, sides):    #sides ipv other?
#         self.sides = sides        #sides ipv other?
#
#     def roll (self):
#         return random.randint(1,self.other)
#
#     def __eq__(self, other):
#         return self.sides == other.sides
#
#     def __ne__(self, other):
#         return self.sides != other.sides
#
#     def __lt__(self, other):
#         return self.sides < other.sides
#
#     def __gt__(self, other):
#         return self.sides > other.sides
#
#
#     def __add__(self, other):
#         return Dobbelsteen(self.sides + other.sides)
#
#     def __sub__(self, other):
#         return Dobbelsteen(self.sides - other.sides)
#
#     def __mul__(self, other):
#         return Dobbelsteen(self.sides * other.sides)
#
#
import random

FAIR_MAX_ROLL = 10000

class Die:
    """
    Representation of a n-sides dice
    """
    def __init__(self,sides: int):
        if sides < 4:
            raise ValueError("Dobbelsteen kan nooit minder dan 4 zijdes hebben")
        self.sides = sides
        self._last_roll = None


    def roll(self) -> int:
        self._last_roll = random.randint(1, self.sides)
        return self._last_roll



    def is_fair(self) -> bool:
        count = self.sides * FAIR_MAX_ROLL
        counters = {i: 0 for i in range(1, self.sides + 1)}
       # counter = {i+1: 0 for i in range(self.sides)}
        for i in range(count):
            roll = self.roll()
            counters[roll] += 1
        expected = FAIR_MAX_ROLL
        #90% * expected <counter[i] <   110%  *  expected
        # lowest = min(counters.values())
        # highest = max(counters.values())
        # if 0.9 * FAIR_MAX_ROLL < lowest and 1.1 * FAIR_MAX_ROLL > highest:
        #     return True
        # return False
        lowest = 0.9 * FAIR_MAX_ROLL
        highest = 1.1 * FAIR_MAX_ROLL
        print(counters.values())
        for value in counters.values():
            if not (lowest <= value <= highest):
                return False
        return True



class D4(Die):
    """
    Representation of a 4-sides dice
    """
    def __init__(self):
        super().__init__(sides=4)

    pass

class D6(Die):
    """
    Representation of a 6-sides dice
    """
    def __init__(self):
        super().__init__(sides=6)

def main():
    d7 = Die(7)
    print(d7.roll())
    d4 = D4()
    print(d4.roll())
    print(d4._last_roll)
    print(d4)
    print(d4)

    d6 = D6()
    print(d6.is_fair())
    my_roll = d4.roll() + d6.roll()
    print("u heeft ", my_roll, "geworpen")

if __name__ == "__main__":
        main()


