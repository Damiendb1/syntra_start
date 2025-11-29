# Opdracht 1: maak een functie die print of een zin allitereert.
#      "Slimme slangen sluipen stilletjes slangs sappige struiken."  -> True
#      "Slimme pythons sluipen stilletjes slangs sappige struiken."  -> False
# Hint: String opdelen in verschillende woorden met split()
#       Bepaal de eerste letter van het eerste woord
#       Overloop de andere woorden. Als er 1 woord begint met een andere letter, is er geen sprake van alliteratie.


def alliterates(text: str):
    """
    Check that the text alliterates, e.g. every word starts with the same letter
    :param text: text to be checked
    """
    words = text.split()
    l = len(words)
    if l == 0:
        print("geen tekst gevonden")
    elif l == 1:
        print("1 woord allitereert altijd")
    else:
        first_letter = words[0][0]
        for word in words:
            if word[0] != first_letter:
                print("Zin allitereert niet")
                return
        print("Zin allitereert niet")



# Opdracht 2: maak een functie die bepaalt of een string een palindroom is.
# voorbeeld:  Non  -> True
# voorbeeld:  Papa -> False
# voorbeeld: Koortsmeetsysteemstrook -> True
# in computertaal: controleer of de string gelijk is aan diens omgekeerde.

def is_palindrome1(word: str) -> bool:
    """
    Check if a word is a palindrome
    :param word: word to be checked
    """
    return word == word[::-1]

def is_palindrome2(word: str) -> bool:
    """
    Check if a word is a palindrome
    :param word: word to be checked
    """
    return word.lower() == word.lower()[::-1]


def is_palindrome3(word: str) -> bool:
    """
    Check if a word is a palindrome
    :param word: word to be checked
    """
    left = word.lower()
    right = word.lower()[::-1]
    return left == right

print(f"{is_palindrome1('lepel')=}")
print(f"{is_palindrome1('pollepel')=}")

def p_lang(word: str) -> str:
    p_word = ""
    for letter in word:
        p_word += letter
        if letter.lower() in ['a', 'e', 'i', 'o', 'u']:
            p_word += 'p' + letter
    print(p_word.capitalize())

p_lang("Hello")


# Opdracht 3:
# De P' taal is een speeltaal. Elke klinker of klank wordt verlengd met 'p' en de klank die er vaan vooraf gaat.
# Schrijf een functie die een string krijgt en de P' taal versie teruggeeft
# voorbeeld :  p("zes")  -> "ze"+"pe" +"s" => "zepes"
#              p("dagen') -> "da" + "pa" + "ge" + "pe" + "n"  => "dapagepen"
#              p("Arvid') -> "A"+ "pa" +"rvi" + "pi" +d => "Aparvipid"
# Je hoeft enkel een versie te maken: woorden zonder tweeklanken en enkel open lettergrepen.
#

