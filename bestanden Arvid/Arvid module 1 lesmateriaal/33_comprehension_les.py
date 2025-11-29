
lst = [i+1 for i in range(10) if i % 2 == 0]

print(lst)
lst = []
for i in range(10):
    if i % 2 == 0:
        lst.append(i+1)

print(lst)

set1 = {i+1 for i in range(10)}
tup = (i+1 for i in range(10))

lst = [(i, i >= 0) for i in range(-5, 6, 1)]
print(lst)

lst = []
for i in range(-5, 6, 1):
    lst.append((i, i >= 0))

zipcode = {
    "9090": "Melle",
    "9080": "Lochristi",
    "9000": "Gent",
    "1000": "Brussel",
    "2000": "Antwerpen"
}

inverted = {city: zipcode for zipcode, city in zipcode.items() if zipcode[0] == "9"}

inverted = {}
for zipcode, city in zipcode.items():
    if zipcode[0] == "9":
        inverted[city] = zipcode
print(inverted)


zipcode = {
    9090: "Melle",
    9080: "Lochristi",
    9000: "Gent",
    1000: "Brussel",
    2000: "Antwerpen"
}

inverted = {city: zipcode for zipcode, city in zipcode.items() if zipcode[0] == "9"}

inverted = {}
for zipcode, city in zipcode.items():
    zipstr = str(zipcode)
    if zipstr[-2] == "9":
        inverted[city] = zipcode
print(inverted)