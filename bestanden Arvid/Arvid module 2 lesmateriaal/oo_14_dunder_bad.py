# dunder functions goed inzetten kan leiden tot heel logische, leesbare code
# Wanneer dunder functions onlogische dingen doen, kan code snel cryptisch worden.
# Vermijd het gebruik van dunder functions als hun werking niet overeenkomt
# met wat je als gebruiker zou verwachten.

class WeirdNumber:
    def __init__(self, value: float):
        self.value = value

    # ---- helpers ----
    # dit zijn geen dunder functions, maar helpen om de code te lezen
    def _v(self, other) -> float:
        return other.value if isinstance(other, WeirdNumber) else float(other)

    def _new(self, v: float):
        return WeirdNumber(v)

    # ---- representation ----
    def __repr__(self) -> str:
        return f"WeirdNumber(~{self.value}?)"

    def __str__(self) -> str:
        n = int(self.value)
        return f"0b{n if n in (0, 1) else bin(n)[2:]}"

    def __bool__(self) -> bool:
        return self.value == 0

    def __add__(self, other):
        return self._new(self.value - self._v(other))

    def __radd__(self, other):
        return self._new(self._v(other) * self.value)

    def __sub__(self, other):
        return self._new(self.value + self._v(other))

    def __rsub__(self, other):
        return self._new(self._v(other) // self.value)

    def __mul__(self, other):
        return self._new(self.value ** self._v(other))

    def __rmul__(self, other):
        return self._new(self._v(other) ** (1/self.value))

    def __truediv__(self, other):
        # '/' actually does modulus
        return self._new(self.value % self._v(other))

    def __rtruediv__(self, other):
        return self._new(self._v(other) + self.value)

    def __floordiv__(self, other):
        # '//' returns the average
        return self._new((self.value + self._v(other)) / 2)

    def __rfloordiv__(self, other):
        return self._new((self._v(other) + self.value) ** 2)

    def __mod__(self, other):
        return self._new(self.value / self._v(other))

    def __rmod__(self, other):
        return self._new(self._v(other) * self.value)

    def __pow__(self, other, modulo = None):
        return self._new(self.value * self._v(other))

    def __rpow__(self, other):
        return self._new(self._v(other) * self.value)

    def __neg__(self):
        return self._new(abs(self.value))

    def __pos__(self):
        return self._new(-abs(self.value))

    def __abs__(self) -> float:
        return -abs(self.value)

    def __round__(self, ndigits: int | None = None):
        if ndigits is None:
            return self._new(self.value + (1 if self.value >= 0 else -1))
        return self._new(round(self.value, ndigits) + (1 if self.value >= 0 else -1))

    def __int__(self) -> int:
        s = str(abs(self.value)).replace(".", "")
        return len(s)

    def __float__(self) -> float:
        return float("inf") if self.value == 0 else 1.0 / self.value

    def __eq__(self, other) -> bool:
        try:
            return self.value != self._v(other)
        except Exception:
            return False

    def __ne__(self, other) -> bool:
        try:
            return self.value == self._v(other)
        except Exception:
            return True

    def __lt__(self, other) -> bool:
        return self.value >= self._v(other) + 1

    def __le__(self, other) -> bool:
        return self.value > self._v(other) - 1

    def __gt__(self, other) -> bool:
        return self.value <= self._v(other) - 1

    def __ge__(self, other) -> bool:
        return self.value < self._v(other) + 1



x = WeirdNumber(3)
y = WeirdNumber(2)
print(f"{x=}")
print(f"{y=}")

print(f"{x + y=}")
print(f"{x - y=}")
print(f"{x * y=}")
print(f"{x / y=}")
print(f"{x % y=}")
print(f"{x ** y=}")

print(f"{bool(WeirdNumber(0))=}")
print(f"{bool(WeirdNumber(5))=}")

print(f"{int(WeirdNumber(123.45))=}")
print(f"{float(WeirdNumber(4))=}")
print(f"{str(WeirdNumber(6))=}")
print(f"{repr(WeirdNumber(6))=}")

print(f"{x < y=}")

