
# https://www.scrabblehelper.nl/scrabble-letters

import random

SCORES = {
"A" : 1,
"B" : 3,
"C" : 5,
"D" : 2,
"E" : 1,
"F" : 4,
"G" : 3,
"H" : 4,
"I" : 1,
"J" : 4,
"K" : 3,
"L" : 3,
"M" : 3,
"N" : 1,
"O" : 1,
"P" : 3,
"Q" : 10,
"R" : 2,
"S" : 2,
"T" : 2,
"U" : 4,
"V" : 4,
"W" : 5,
"X" : 8,
"Y" : 8,
"Z" : 4,
" " : 0
}

def calc_score(word):
    score = 0
    for letter in word:
        score += SCORES[letter]
    return score

while True:
    input_word = input("Enter a word: ")
    if input_word.upper() == "STOP":
        break
    print(f"score voor {input_word} is {calc_score(input_word.upper())}")


###################

cnt_terms = {}
filename = r"d:\dev\learning\functional\examen_01.py"
f = open(filename, "r")
for line in f:
    parts = line.split()
    for part in parts:
        if part in cnt_terms:
            cnt_terms[part] += 1
        else:
            cnt_terms[part] = 1
        # korter: cnt_terms[part] = word_counts.get(part, 0) + 1


for term, freq in sorted(cnt_terms.items(), key=lambda x: x[1]):
    print(term, "komt", freq, "keer voor")

