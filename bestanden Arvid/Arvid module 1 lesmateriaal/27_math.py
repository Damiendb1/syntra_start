# Veel wiskundige functies zitten in de math module

import math

# Belangrijke wiskundige constantes

print(f"{math.sqrt(25)=}")  # vierkantswortel
print(f"{math.cbrt(27)=}")  # derdemacht wortel
print(f"{math.trunc(1.12345)=}")

# Alle code hieronder is louter ter informatie voor wie meer wil weten / uitdaging wil


print(f"{math.ceil(1.1)=}")  # eerstvolgende geheel getal
print(f"{math.ceil(-1.1)=}")  # eerstvolgende geheel getal
print(f"{math.floor(1.1)=}")  # vorige natuurlijke geheel getal
print(f"{math.floor(-1.1)=}")  # vorige natuurlijke geheel getal

# logaritmische functies
print(f"{math.e=}")
print(f"{math.log(math.e**2)=}")
print(f"{math.log10(100)=}")
print(f"{math.log2(128)=}")
print(f"{math.exp(2)=}")  #  e ** n
print(f"{math.exp2(6)=}")  # 2 ** n

print(f"{math.factorial(8)=}")  # faculteit
print(f"{math.gcd(25,15)=}")  # grootste gemene delete
print(f"{math.lcm(15,25)=}")  # kleinste gemeen veelvoud

# goniometrische functies
radians = math.pi / 6
print(f"{math.pi=}")
print(f"{math.sin(radians)=}")
print(f"{math.cos(radians)=}")
print(f"{math.tan(radians)=}")
print(f"{math.radians(2)=}")
