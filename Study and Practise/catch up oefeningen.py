# Schrijf een programma dat de temperatuur vraagt.
# Onder 36.6 is het onderkoeling
# Tot 37.5 is het normaal
# Vanaf 37.5 is het verhoging
# Vanaf 38 is het koorts
# Vanaf 40 is het dodelijk.
# Blijf de temperatuur vragen tot er 0 wordt ingevuld.



# Een bank automaat kent voor 1 klant de 'geheime' code: Jo heeft code 1234
# De automaat vraag eerst de naam van de klant.
# De naam 'Stop' stop het programma
# Gekende klanten kunnen de code invoeren.
# Niet gekende klanten krijgen een reclame boodschap om klant te worden.
# Een klant mag 3 keer proberen om de code te invoeren, daarna verschijnt alarm.
# Bij een correcte code verschijnt het saldo van de klant (kies zelf)

while True:
    user=input("naam")
    if user == "stop":
        break
    if user != "jo":
        print("Wil je klant worden?")
        continue
    print("")


# while True:
#     invoer = input("Invoer: ")
#     if invoer == "stop":
#         break
#     temp = float(input("Temperatur: "))
#     if temp == 0:
#         break
#     if temp < 36.6:
#         print("onderkoeling")
#     elif temp < 37.5:
#         print("normaal")
#     elif temp < 38:
#         print("verhoging")
#     elif temp < 40:
#         print("koorts")
#     else:
#         print("dodelijk")

# for i in range(20):
#     if i == 5:
#         continue
#     if i % 10 == 5:
#         break
#     if i % 2 == 0:
#         print(i)

