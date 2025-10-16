


# #Opdracht 2
# dubbel = set()
# word = input
#
# while True:
#     word = input ('Enter a word:")
#     if word = "stop":
#         break
#     if word in dubbel:
#         print("woord is al gegeven"):
#     else:
#         print

woorden = []

while True:
    woord = input("geef een woord in ")

    if woord.lower() == "stop":
        break

    woorden.append(woord)

double_list = []
for w in woorden:
    if woorden.count(w) > 1:
        double_list.append(w)

double_list = set([w for w in woorden if woorden.count(w) > 1])

if double_list:
    print("Je hebt een woord ingegeven dat al ingegeven is")
    for w in double_list:
        print(f"- {w}")
else: print ("Geen dubbele woorden")









