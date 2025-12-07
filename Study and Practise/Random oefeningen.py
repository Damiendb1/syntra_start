# user_number_a = int(input("Geef het eerste getal in: "))
# user_number_b = int(input("Geef het tweede getal in: "))
#
# a = user_number_a
# b = user_number_b
#
# for i in range(0, user_number_a):
#     print(i)
#
# print("a + b =", a + b)
# print("a - b =", a - b)
# print("a * b =", a * b)
# print("a / b =", a / b)
# print("a % b =", a % b)
# print("a // b =", a // b)
#

# user_number = int(input("Geef een getal om tot te tellen: "))
#
# for i in range(0, 20):  # <-- begin en eind invullen
#     print(i)              # <-- wat wil je printen?
#
# # Oefening 2
# a = int(input("Geef getal 1: "))
# b = int(input("Geef getal 2: "))
#
# print("a + b =", a + b)
# print("a - b =", a - b)
# print("a * b =", a * b)
# print("a / b =", a / b)
# print("a % b =", a % b)
# print("a // b =", a // b)



while True:
    user_name = input("Naam: ")
    if user_name == "Stop":
        break
    if user_name != "Jo":
        print("We hebben een reclame boodschap voor u!")
        continue
    print(f"Hey", user_name,"wat is je code?")
    for i in range(3):
        code = input("Code: ")
        if code == "1234":
            print("De code is correct")
            print("Het saldo van de klant is 30000")
            break








