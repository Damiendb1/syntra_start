import datetime

letter_values ={
  "A": 1,
  "B": 3,
  "C": 3,
  "D" :1,
  "I": 1,
  "R": 1,
  "V": 4,
  "W": 4,
  "X": 8,
  "Y": 8,
  "Z": 6,
  "1": datetime.datetime.now().year
}

# while True:
#     word = input("Enter a word: ")
#     if word.upper() == "STOP":
#         exit()
#     score = 0
#     for letter in word:
#         upper = letter.upper()
#         letter_score = letter_values.get(upper, 0)
#         print("De score voor letter", letter, "is", letter_score)
#         score += letter_score
#     print("De score voor", word, "is", score)

strange_dict = {
    (0,0) : 'NULPUNT',
    (1,1) : 'EENPUNT',
    (2,2) : 'TWEEPUNT',
    None: "NONEPUNT",
    "Arvid": 1975
}

for key, value in strange_dict.items():
    print(key, value)
print(strange_dict.get(None, 'niet gevonden'))
print(strange_dict.get('Arvid', 'niet gevonden'))

for i in strange_dict:
    print(i)
for i in strange_dict.keys():
    print(i)
for i in strange_dict.values():
    print(i)

count = {}
file = open("C:/Users/arvid/OneDrive/Documenten/dec.txt", "r", encoding="utf-8")
for line in file:
    parts=line[:-1].split(" ")
    for part in parts:
        up_part = part.upper()
        if up_part in count.keys():
            # count[part] += 1
            cnt = count[up_part]
            count[up_part] = cnt + 1
        else:
            count[up_part] = 1
# file.flush()
file.close()
for key, value in count.items():
    print(key, "komt ", value, " keer voor")