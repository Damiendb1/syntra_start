# De ingebouwde functie id(waarde) toont technische info of waar in het geheugen een waarde is opgeslagen.
i = 10000
print(id(i))
j = 20000
print(id(j))
i += j
print(id(i))


a = "arvid"
print(a, id(a))
b = "hej"
print(b, id(b))

a += b
print(a, id(a))

a = "arvid is een zero"
print(a, id(a))
a = a.replace("zero", "hero")
print(a, id(a))


print(a.split(" "))

print(a.capitalize())
print(a.upper())

print(a.count("r"))
print(a.find("is"))
print(a.title())

s = "Python 3.13"
print(len(s))              # 10
print(s.isalpha())         # False (spatie/punt/cijfer aanwezig)
print("Hello".isalpha())   # True
print("123".isdigit())  # True
print("abc123".isalnum())  # True
print(" \t".isspace())     # True

# python
print("42".zfill(5))            # "00042"
print("hi".center(6, "-"))      # "--hi--"
print("hi".ljust(5, "."))       # "hi..."
print("hi".rjust(5, "."))       # "...hi"

list = ["Homer", "Marge", "Bart", "Lisa", "Maggie"]
print(", ".join(list))

for ch in "arvid":
    print(ch)

# een string gedraagt zich als een list. Maar het is geen list
string = "BBCD"
print(string[0])  # => B
print(string[-1])  # => D
print(string[2:4])  # => CD

# een string is niet wijzigbaar (immutable)
# string[0] = 'A'  # TypeError: 'str' object does not support item assignment




# Python heeft een paar speciale karakters
# \t tab   \n newline    \\  backslash   \'  '      \"    "

s = "Een regel\nVolgende regel\tmet tab"
s_quote = 'Hij zei: \'ok\''
path = "C:\\Users\\<naam>\\Documents"


# raw string: een string die wordt voorafgegaan door een r
# Hierin worden speciale \ karakters niet verwijderd.
raw_path = r"C:\Users\<naam>\Documents\project"



# formatted strings (f-strings): wordt voorafgegaan door een f
# Waardes tussen accolades worden eerst geëvalueerd
naam = "homer"
score = 13.5
maxi = 20
s = f"Hallo {naam}, je score = {score}/{maxi}. \nDat is  {score/maxi*100}%"  # 2 decimalen
print(s)


# Opdracht: maak een functie die print of een zin allitereert.
#      "Slimme slangen sluipen stilletjes slangs sappige struiken."  -> True
#      "Slimme pythons sluipen stilletjes slangs sappige struiken."  -> False
# Hint: String opdelen in verschillede woorden met split()
#       Bepaal de eerste letter van het eerste woord
#       Overloop de andere woorden. Als er 1 woord begint met een andere letter, is er geen sprake van alliteratie.


# Opdracht: maak een functie die bepaalt of een string een palindroom is.
# voorbeeld:  Non  -> True
# voorbeeld:  Papa -> False
# voorbeeld: Koortsmeetsysteemstrook -> True
# in computertaal: controleer of de string gelijk is aan diens omgekeerde.


# Opdracht met uitdaging
# De P' taal is een speeltaal. Elke klinker of klank wordt verlengd met 'p' en de klank die er vaan vooraf gaat.
# Schrijf een functie die een string krijgt en de P' taal versie teruggeeft
# voorbeeld :  p("zes")  -> "ze"+"pe" +"s" => "zepes"
#              p("dagen') -> "da" + "pa" + "ge" + "pe" + "n"  => "dapagepen"
#              p("Arvid') -> "A"+ "pa" +"rvi" + "pi" +d => "Aparvipid"
# Je hoeft enkel een versie te maken: woorden zonder tweeklanken en enkel open lettergrepen.
#


