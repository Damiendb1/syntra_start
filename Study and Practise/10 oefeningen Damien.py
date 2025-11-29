class Gender2:
    def __init__(self, value: str):
        if value not in ["M", "V", "X"]:
            raise ValueError("Value must be M, V, of X")
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        raise AttributeError("Value mag niet gewijzigd worden")


    def __repr__(self):
        if self._value == "X":
            return "onbekend"
        if self._value == "M":
            return "man"
        if self._value == "V":
            return "vrouw"


M = Gender2("M")
M.value = "X"