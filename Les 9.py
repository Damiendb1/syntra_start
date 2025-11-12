history= set()

while True:
    word = input('Geef een woord')
    if word == 'stop':
        print('programma gestopt')
        break
     if word in history:
        print("woord is al gegeven")
        break
    else:
        print("woord is al gegeven")
        history.add(word)


word_set= set()
while True:
    word = input('Geef een woord')
    if word.lower() == "stop":
        break
    elif word in word_set:
        print("woord is al gegeven")
    else:
        print(f"{word} is a new word")
        word_set.add(word)
    print(word_set)

