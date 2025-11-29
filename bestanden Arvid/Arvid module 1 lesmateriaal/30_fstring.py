# in fstrings kan je aangeven hoe je het waarde wil weergeven

# int
print(f"{42123:_}")
print(f"{42123:,}")
print(f"'{42123:10}'")
print(f"'{42123:<10}'")  # 10 breed, links aligned
print(f"'{42123:>10}'")  # 10 breed, rechts aligned
print(f"'{42123:^10}'")  # 10 breed, centraal
print(f"'{42123:010}'")  # 10 breed, voorloop nullen

# deze zijn er ook, maar minder gebruikt
print(f"{42:b}")
print(f"{42:o}")
print(f"{42:x}")
print(f"{42:X}")

# Voor float geldt alles van int, plus extra:

print(f"{3.14159:.2f}")  # 2 decimalen
print(f"{3.14159:.0f}")  # 0 decimalen (voorgesteld als een int)
print(f"{3.14159:10.2f}")  # 10 breed, recht aligned, 2 decimalen

"""
Format	Description	Example	Output
.2f	Fixed-point with 2 decimals	f"{3.14159:.2f}"	3.14
.0f	Rounded to integer	f"{3.99:.0f}"	4
>10.2f	Right-align in 10 spaces	f"{3.14:>10.2f}"	' 3.14'
<10.2f	Left-align	f"{3.14:<10.2f}"	'3.14 '
^10.2f	Center-align	f"{3.14:^10.2f}"	' 3.14 '
,.2f	Comma separator	f"{12345.6789:,.2f}"	12,345.68
e / E	Scientific notation	f"{12345.6789:e}"	1.234568e+04
"""

# voor strings
print(f"{'Arvid':.3s}")  # gelimiteerd tot eerste 3 karakters

