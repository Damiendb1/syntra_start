# Lambda function zijn korte functies, meestal voor eenmalige gebruik.


import datetime



def is_even(number:int) -> bool:
    """
    Check if a number is even
    :param number: Value to check
    :return: True if number is even
    """
    return number % 2 == 0

is_even2 = lambda x: x % 2 == 0

N = 100_000_00

n = datetime.datetime.now()
for i in range(N):
    if is_even(i):
        pass
m=datetime.datetime.now()
print(m-n)

n = datetime.datetime.now()
for i in range(N):
    if is_even2(i):
        pass
m=datetime.datetime.now()
print(m-n)


WORDS = ["There", "can", "be", "many", "words", "in", "a", "sentence"]
for word in WORDS:
    cnt = len(word)
    print(f"{word} telt {cnt} karakters")



for word in WORDS:
    cnt = len(word)
    if cnt == 1:
        print(f"{word} telt 1 karakter")
    else:
        print(f"{word} telt {cnt} karakters")


def pluralize(word:str, cnt:int) -> str:
    if cnt == 1:
        return f"{word}"
    else:
        return f"{word}s"

for word in WORDS:
    cnt = len(word)
    print(f"{word} telt {cnt} {pluralize("karakter", cnt)}")

pluralize2 = lambda word, cnt: word if cnt == 1 else f"{word}s"
for word in WORDS:
    cnt = len(word)
    print(f"{word} telt {cnt} {pluralizeé("karakter", cnt)}")


