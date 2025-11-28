# Python heeft een aantal built-in functies
# Bij elke functie staat vermeld of een functie parate kennis moet worden.

# abs: absolute waarde (Parate kennis)
print(f"{abs(-1)=}")
print(f"{abs(1)=}")

# divmod()	Returns quotient and remainder
print(f"{divmod(10, 3)=}")

# pow()	Exponentiation
print(f"{pow(2, 3)=}")
# verschil met ** operator: pow laat ook een 3de parameter toe.
print(f"{pow(2, 10, 1000)=}")  #   2 ** 10 % 1000 = 1024 % 1000 = 24

# round()	Rounds number  (Parate kennis)
print(f"{round(1.23456789, 2)=}")
print(f"{round(1.43456789)=}")
print(f"{round(1.50)=}")
print(f"{round(1.49)=}")


# all() : alle waardes zijn true?
print(f"{all([True, True, True])=}")
print(f"{all([True, False, True])=}")
print(f"{all([1, 2, None])=}")
print(f"{all(['A', 'B'])=}")
print(f"{all(['A', ''])=}")
print(f"{all([ [1,2,3], [4,5,7]   ]   )=}")
print(f"{all([ [], [4,5,7]   ]   )=}")

# any() : ten minste 1 waarde True?
print(f"{any([False, False, False])=}")
print(f"{any([False, False, True])=}")
print(f"{any(['', [], None])=}")
print(f"{any(['A', 'B'])=}")
print(f"{any(['A', ''])=}")
print(f"{any([ [1,2,3], [4,5,7]   ]   )=}")
print(f"{any([ [], []   ]   )=}")

# bin(): binaire voorstelling van een getal
b = bin(13)
print(b)  # '0b1101'
print(type(b))  # str
print(f"{b[2:]=}")

# oct()	Octal string of integer
o = oct(13)
print(o)  # '0o15'
print(type(o))  # str
print(f"{o[2:]=}")

# hex()	Hexadecimal string of integer
h = hex(245)
print(h)  # Oxf5
print(type(h))  # str
print(f"{h[2:]=}")

# chr()	Character from Unicode code   (Parate kennis)
print(chr(97))  # a
print(chr(48))  # 0
print(chr(65))  # A
print(chr(345))  # r met accent

# ascii(): ASCII string of object
print(ascii("65"))  # '65'
print(ascii("ééndelig"))  # '\\xe9\\xe9ndelig'

# ord()	Unicode code of character   (Parate kennis)
print(ord('a'))  # 97
print(chr(97))
lower_cases = [chr(i) for i in range(97,123,1)]
upper_cases  = [chr(i) for i in range(65,91,1)]
digits  = [chr(i) for i in range(48,58,1)]

# enumerate() overloopt items en geeft telkens een tuple (index, value)   (Parate kennis)
lst = ['A', 'C', 'E']
for index, value in enumerate(lst):
    print(f"{index=}, {value=}")

tup = ('A', 'C', 'E')
for index, value in enumerate(tup):
    print(f"{index=}, {value=}")
s = {'A', 'C', 'E'}
for index, value in enumerate(s):
    print(f"{index=}, {value=}")
s = { 1, 2,3}
s_leeg = set()
d=  {}
d1= {3: 4, 6:7}


# filter()	Filters items in iterable   (Parate kennis)
numbers = [1, 2, 3, 4, 5, 6]

def is_even(n) -> bool:
    return n % 2 == 0

filtered = filter(is_even, numbers)  # filteren in python land
#filtered = [value for value in numbers if is_even(value)]
print(list(filtered))  # Output: [2, 4, 6]

# map()	Applies function to iterable   (Parate kennis)
numbers = [1, 2, 3, 4]


def square(n):
    return n ** 2

result = map(square, numbers)  # function toegepast op lijst in pythonland
print(list(result))  # Output: [1, 4, 9, 16]

# zip()	Aggregates iterables
names = ['Alice', 'Bob', 'Charlie']
scores = [88, 94, 72]
paired = zip(names, scores)
print(list(paired))  #  [('Alice', 88), ('Bob', 94), ('Charlie', 72)]

# al de lijsten niet even lang zijn, dan 'wint' de kortste
a = [1, 2, 3]
b = ['x', 'y']

print(list(zip(a, b)))  # Output: [(1, 'x'), (2, 'y')]  waarde 3 gaat verloren

l = [3, 6, 9, 2, 0.45]
# len()	Length of object
print(f"{len(l)=}")
# sum()	Sum of iterable
print(f"{sum(l)=}")
# max()	Largest item
print(f"{max(l)=}")
# min()	Smallest item
print(f"{min(l)=}")

# reversed()	Reversed iterator   (Parate kennis)
for val in reversed(l):
    print(val)

# slice()	Slice object: zie later bij numpy, pandas
numbers = [0, 1, 2, 3, 4, 5, 6]
s = slice(1, 6, 2)
print(numbers[s])  # Output: [1, 3, 5]
print(numbers[1:6:2])

# reeds veelvuldig besproken
#   input()	User input as string
#   open()	Opens file
#   print()	Prints to console
#   range()	Sequence of numbers
#   type()	Type of object
#   sorted()	Returns sorted list


# data constructors
#   bool()	Boolean value of an object
#   complex()	Creates complex number
#   dict()	Creates a dictionary
#   float()	Converts to float
#   int()	Converts to integer
#   list()	Creates a list
#   set()	Creates a set
#   str()	Converts to string
#   tuple()	Creates a tuple
#   bytes()	Immutable bytes object
#   bytearray()


# Zie later bij Object Oriented Programming
#   classmethod()	Converts method to class method
#   delattr()	Deletes attribute from object
#   dir()	Lists attributes of object
#   getattr()	Gets attribute from object
#   hasattr()	Checks if object has attribute
#   isinstance()	Checks instance type
#   hash()	Hash value of object
#   issubclass()	Checks subclass relationship
#   iter()	Returns iterator
#   next()	Next item from iterator
#   object()	Creates base object
#   property()	Property attribute
#   repr()	String representation
#   setattr()	Sets attribute
#   super()	Access superclass methods
#   staticmethod()	Converts method to static method
#   vars()	__dict__ of object

# Python process info
#   breakpoint()	Drops into debugger
#   id()	Identity of object
#   help()	Launches help system
#   __import__()	Low-level import function
#   globals()	Returns global symbol table
#   locals()	Local symbol table
#   memoryview()	Memory view object

# Deze komen niet aan bod in de cursus Data Developer
#   aiter(): voor multitasking programma's
#   anext(): voor multitasking programma's
#   callable() checks if object is callable
#   compile()	Compiles source into code object
#   eval()	Evaluates a string as Python expression
#   exec()	Executes Python code
#   format()	Formats a value
