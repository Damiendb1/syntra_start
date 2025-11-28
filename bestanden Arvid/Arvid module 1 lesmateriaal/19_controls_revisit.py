# Met match / case kan je een hele rits if / elif / else instructies vervangen door
# overzichtelijkere code, met de match-case-instructie

def pension_age(occupation: str) -> int:
    """
    Determine the pension age for a given occupation
    :param occupation: Name of the occupation
    :return: Pension age
    """
    match occupation:
        case "Arbeider":
            res = 62
        case "Bediende" | "Kader":  # Dit is een of-instructie
            res = 63
        case "Ambtenaar":
            res = 64
        case "Zelfstandige":
            res = 65
        case "Volksvertegenwoordiger":
            res = 50
        case _:  # Als er niets anders gematcht is, dan komen we hier
            res = 67
    return res


for occ in ["Arbeider", "Bediende", "Kader", "Ambtenaar", "Zelfstandige", "Volksvertegenwoordiger", "Werkloze"]:
    print(f"Je mag als {occ} op {pension_age(occ)} jaar op pensioen")

# Match is een bijzonder krachtig mechanisme, dat sinds python 3.10 bestaat.
# Versie voor 3.10 kennen match niet.

def pension_age2(occupation: str) -> int:
    """
    Determine the pension age for a given occupation
    :param occupation: Name of the occupation
    :return: Pension age
    """
    match occupation:
        case "Arbeider":
            res = 62
        case "Bediende" | "Kader":  # Dit is een of-instructie
            res = 63
        case "Ambtenaar":
            res = 64
        case "Zelfstandige":
            res = 65
        case "Volksvertegenwoordiger":
            res = 50
        case unknown:  # Als er niets anders gematcht is, dan komen we hier
            print(f"Onbekende occupation: {unknown}")
            res = 67
    return res

occ = "Militair"
print(f"Je mag als {occ} op {pension_age2(occ)} jaar op pensioen")

# opdracht: schrijf een function die S, M, L, XL, XXL omzet naar de bijbehorende maten.
# oplossing:
def invert_size_label(label: str)-> tuple:
    """
    Returns the min and max size of a give size label.
    :param label: Size label
    :param: return min, max size  or None None
    """
    match label:
        case 'Small':
            return 20,40
        case 'Medium':
            return 40, 50
        case 'Large':
            return 50, 60
        case 'XL':
            return 60, 70
        case 'XXL':
            return 70,120
        case _:
            return None, None

def menu_choice(choice:int):
    """
    ATM menu
    :param choice: Choice selected by customer
    """
    match choice:
        case 1:
            print("Voer de code uit om een rekening te openen")
            # create_new_account()

        case 2:
            print("Voer de code uit om een overschrijving uit te voeren")
            # transfer_money()
        case 3:
            print("Voer de code uit om de pin code te veranderen")
            # change_code()
        case _:
            print("Geen gekend optie")

    print("eerste lijn na de match")


# Een for-loop en een while-loop kunnen kunnen ook een else: deel hebben.
#Als een loop volledig werd afgewerkt, dus niet onderbroken door break,
#dan wordt de else-instructie uitgevoerd.

secret = "4321"

def ask_pin_for(secret: str) -> bool:
    """
    Ask a pin code and compare it to a secret
    :param secret: expected pin
    :return: True if user successfully entered the correct code
    """
    for i in range(3):
        pin = input(f"Pin poging {i+1}: ")
        if pin == secret:
            break
    else:
        print('Alarm te veel pogingen!!!!')
        return False
    print("Code correct in gegeven")
    return True

# ask_pin_for('1234')

def ask_pin_while(secret: str) -> bool:
    """
    Ask a pin code and compare it to a secret
    :param secret: expected pin
    :return: True if user successfully entered the correct code
    """
    i = 0
    while i < 3:
        i += 1
        pin = input(f"Pin poging {i}: ")
        if pin == secret:
            break
        print("Einde van een iteratie")
    else:
        print('Alarm te veel pogingen!!!!')
        return False
    print("Code correct in gegeven")
    return True
ask_pin_while('1234')

# Veilig itereren

def print_list(lst: list):
    for item in lst:
        print(item)

print_list([1,2,3])
print_list([])
print_list(None) # dit is een fout. Dit geeft een fout


# We kunnen gebruik maken van een python eigenschap
#  None or [] => []
#  None or [1,2,3] => [1,2,3]
#  [3,4,5] or [1,2,3] => [3,4,5]
# Analoog voor sets, tupples en dicts

def print_list_safe_for_none(lst: list):
    for item in lst or []:
        print(item)

print_list_safe_for_none(None)


# Ternary assignment
# value =  val_1 if expression == True else val_2

value= 2
if value % 2 ==0:
    res = "even"
else:
    res = "oneven"
res = "even" if value % 2 ==0 else 'oneven'

# dit kan ingekort worden:
# Dit kort code in, maar maakt ze niet noodzakelijk leesbaarder.
value = "even" if value % 2 == 0 else "oneven"
