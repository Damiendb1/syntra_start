

#opdracht 2

# woorden = []
#
# while True:
#     woord = input("geef een woord in ")
#
#     if woord.lower() == "stop":
#         break
#
#     woorden.append(woord)
#
# double_list = []
# for w in woorden:
#     if woorden.count(w) > 1:
#         double_list.append(w)
#
# double_list = set([w for w in woorden if woorden.count(w) > 1])
#
# if double_list:
#     print("Je hebt een woord ingegeven dat al ingegeven is")
#     for w in double_list:
#         print(f"- {w}")
# else: print ("Geen dubbele woorden")
#


#opdracht 3

familienamen = set()
dct={ "Arvid": "Claassen",
      "Nico" : "Van den Branden",
      "Patrick" : "Heirwegh",
      "Alexander": "Van den Branden",
      "Sofie": "Agten",
      "Karel": "De Rammelaere",
      "Arvid": "Van Tychem",
      "Homer": "Simpson"
      }
#keys(voornaam) : values(achternaam)
#dct.items = keys + values
# familienamen = set(dct.values())
# print (familienamen)
# voor_achternaam = set(dct.items())
# print (voor_achternaam)


#opdracht 4
# unieke_familyn = set(familienamen)
# familienamen = list(dct.values())
# totaal = len(familienamen)
# uniek = len(set(familienamen))
# if totaal != uniek:
#     print("True")
# else:
#     print("False")

#opdracht 5
voornamen = list(dct.keys())
print(voornamen)
print(dct)







