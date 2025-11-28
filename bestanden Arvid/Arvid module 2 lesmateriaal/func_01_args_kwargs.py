# Extra info. Geen leerstof!

# Een function het een voorschrift
# def func(param1, param2, param3):

def print_sep_1(v1, v2, v3) -> None:
    """
    Print 3 values separated by a newline
    :param v1: value 1
    :param v2: value 2
    :param v3: value 3
    """
    print(v1)
    print(v2)
    print(v3)

# Wat als je nu ook 4 waardes will kunnen printen?
# Je kan dit oplossen met default values.
def print_sep_2(v1, v2, v3, v4=None) -> None:
    """
    Print 3 values separated by a newline
    :param v1: value 1
    :param v2: value 2
    :param v3: value 3
    """
    print(v1)
    print(v2)
    print(v3)
    if v4 is not None:
        print(v4)

# probleem is dat je dit dan moet doen voor veel waardes
def print_sep_3(v1, v2, v3, v4=None, v5=None, v6=None, v7=None) -> None:
    """
    Print 3 to 7 values separated by a newline
    :param v1: value 1
    :param v2: value 2
    :param v3: value 3
    """
    print(v1)
    print(v2)
    print(v3)
    if v4 is not None:
        print(v4)
    if v5 is not None:
        print(v5)
    if v6 is not None:
        print(v6)
    if v7 is not None:
        print(v7)

# print_sep_3 werkt nu voor 3 t.e.m. 7 waardes, maar nog steeds niet voor 8 of meer.

def func_with_args(*args) -> None:
    # Het is een conventie om args als naam te gebruiken maar het mag elke waarde zijn van python.
    # Van je docent mag het enkel args zijn.
    print(type(args))  # args is een tuple
    print(args)

func_with_args(1,2,3)
func_with_args(1,2,3, '3', 232, True, {3,3,2})


def print_sep_4(*args) -> None:
    """
    Print values separated by a newline
    :param args: values to print
    """
    for arg in args:
        print(arg)

# je kan print_sep_4 nu met een willekeurige aantal parameters oproepen.
print_sep_4(1,2,3)
print_sep_4(1,2,3, '3', 232, True, {3,3,2})
print_sep_4()


# je kan gewone parameters combineren met *args
def label_print(label:str, *args) -> None:
    """
    Print values with a label and separated by a newline
    :param label: label to print
    :param args: values to print
    """
    print(args)  # ter info
    for arg in args:
        print(f"{label}: {arg}")

label_print("Label", 1,2,3)
label_print("Label", 1,2,3, '3', 232, True, {3,3,2})
label_print("Label")
# label_print()  # dit mag niet. parameter label is verplicht.
# label_print( 1,2,3, label="label") # dit mag ook niet.

# opdracht 1: Schrijf een function maximum die alle parameters optelt:
# print(maximum(5, 2, 9, 1))      # 9
# print(maximum(10, 20, 5))       # 20
# print(maximum(-5, -2, -10))     # -2
# print(maximum(42))              # 42
# print(maximum())                # None

# opdracht 2: Voer een operatie uit op alle getallen.
# def calc(operator:str, *args):
# print(calc('+', 1, 2, 3, 4))      # 10
# print(calc('*', 2, 3, 4))         # 24


def print_person(name: str, age: int, city: str) -> None:
    """
    Print the information about a person
    :param name: Name of the person
    :param age: Age of the person
    :param city: City where the person lives
    """
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"City: {city}")


print_person("Arvid", 50, 'Melle-Merelbeke')
print_person(name= "Arvid", age=50, city='Melle-Merelbeke')
print_person(city='Melle-Merelbeke', name= "Arvid", age=50)

# stel dat je ook straat en nummer wil afdrukken
# je kan deze parameters ook toevoegen
# def print_person(name: str, age: int, city: str, street:str, nr:str) -> None:
# maar ook hier moet je voor elke nieuwe waarde die je meegeven een parameter toevoegen.
# Als je een onbepaald aantal parameters wil meegeven, maar ook de naam van
# de opgegeven parameter wil weten, dan gebruik je **kwargs (twee sterretjes)
# kwargs is de afkorting van 'keyword arguments.'
# verplichte conventie: de naam kwargs is een conventie maar mag voor python elke variabele naam zijn.
# Voor deze cursus is de naam kwargs verplicht


def print_person2(**kwargs) -> None:
    """
    Print the information about a person
    :param kwargs: attributes of the person
    """
    print(type(kwargs))
    print(kwargs)
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_person2(city='Melle-Merelbeke', name= "Arvid", age=50)
print_person2(city='Melle-Merelbeke', name= "Arvid", age=50, street='Docentenlaan', nr=123, male=True, female=False)


# Als je de informatie van een persoon in een bepaalde volgorde wil printen:
# kwargs is een dict, waar je sleutels kan zoeken om waarden te vinden
def print_person_3(**kwargs) -> None:
    """
    Print the information about a person
    :param kwargs: attributes of the person
    """
    print(type(kwargs))
    print(kwargs)
    formatted_keys = ['name', 'street', 'nr', 'city']
    # print eerst de belangrijke waardes in volgorde
    for key in formatted_keys:
        val = kwargs.get(key, "Niet opgegeven")
        print(f"{key}: {val}")
    # print de overblijvende waardes
    for key in kwargs.keys():
        if key not in formatted_keys:
            print(f"{key}: {kwargs[key]}")

print_person_3(city='Melle-Merelbeke', name= "Arvid", age=50, street='Docentenlaan', nr=123, male=True, female=False)

# je kan kwargs ook combineren met gewone parameters:

def print_person_4(label: str, **kwargs) -> None:
    """
    Print the information about a person
    :param label: header to print first
    :param kwargs: attributes of the person
    """
    print(kwargs)
    print(label)
    formatted_keys = ['name', 'street', 'nr', 'city']
    # print eerst de belangrijke waardes in volgorde
    for key in formatted_keys:
        val = kwargs.get(key, "Niet opgegeven")
        print(f"{key}: {val}")
    # print de overblijvende waardes
    for key in kwargs.keys():
        if key not in formatted_keys:
            print(f"{key}: {kwargs[key]}")


print_person_4(label="Hier onder volgen de persoons gegevens", city='Melle-Merelbeke', name= "Arvid", age=50, street='Docentenlaan', nr=123, male=True, female=False)
# bij kwargs mag een vastgelegde parameter wel eender waar in de parameter lisjt voor komen.
print_person_4( city='Melle-Merelbeke', name= "Arvid", age=50, street='Docentenlaan', nr=123, male=True, female=False, label = "een label" )

# args en kwargs kunnen gecombineerd worden.
def print_person_5(label: str, *args, **kwargs):
    """
    Print the information about a person
    :param label: Name of the person
    :param args: Hobbies
    :param kwargs: Other attributes
    """
    print(label)
    formatted_keys = ['name', 'street', 'nr', 'city']
    # print eerst de belangrijke waardes in volgorde
    for key in formatted_keys:
        val = kwargs.get(key, "Niet opgegeven")
        print(f"{key}: {val}")
    # print the hobbies
    for i in range(len(args)):
        print(f"Hobby {i+1}: {args[i]}")
    # print de overblijvende waardes
    for key in kwargs.keys():
        if key not in formatted_keys:
            print(f"{key}: {kwargs[key]}")

print_person_5("Persoonsgegevens",
               "gamen",
               "blokfluiten",
               "ultrawandelen",
               city='Melle-Merelbeke',
               name= "Arvid",
               age=50,
               street='Docentenlaan',
               nr=123,
               male=True,
               female=False )
