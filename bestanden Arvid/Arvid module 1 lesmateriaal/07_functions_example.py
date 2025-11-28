# Een uitgebreid voorbeeld van functies
# Een bank automaat heeft een keuze-menu. Dat telkens wordt afgedrukt.

while True:
    print("U kan kiezen uit volgende opties:")
    print()
    print("===================================")
    print("1: Toon saldo")
    print("2: Haal geld af")
    print("3: Schrijf geld over")
    print("4: Wijzig pin code")
    print("9: Sluit sessie")
    print("===================================")

    choice = int(input("Kies een optie: "))
    if choice == 1:
        continue
    elif choice == 2:
        continue
    elif choice == 3:
        continue
    elif choice == 4:
        continue
    elif choice == 9:
        print("Bedankt tot ziens.")
        break
    else:
        print("Optie niet gekend")

# We vullende ontbrekende stukken code alvast in met
# beschrijvende taal.

while True:
    print("U kan kiezen uit volgende opties:")
    print()
    print("===================================")
    print("1: Toon saldo")
    print("2: Haal geld af")
    print("3: Schrijf geld over")
    print("4: Wijzig pin code")
    print("9: Sluit sessie")
    print("===================================")

    choice = int(input("Kies een optie: "))
    if choice == 1:
        print("Toon saldo")
        # Als de klant meerdere rekeningen heeft,
        # vraag dan eerst van welke rekening
        # het saldo getoond moet worden.
        # Toon het saldo van de klant
    elif choice == 2:
        print("Haal geld af")
        # Als de klant meerdere rekeningen heeft,
        # vraag dan eerst van welke rekening
        # Vraag het bedrag dat de klant wil afhalen
        # in briefjes van 20 en 50 euro
        # Controleer dat het bedrag de daglimit niet
        # overschrijdt. Zoja, stop.
        # Controleer of het saldo op de rekening hoog
        # genoeg is. Zoniet, stop.
        # Vraag de pincode: 3 pogingen
        # Indien code correct is, geef de klant
        # het gevraagde bedrag.
        # Verlaag het saldo op de rekening
    elif choice == 3:
        print("Schrijf geld over")
        # Als de klant meerdere rekeningen heeft,
        # vraag dan eerst van welke rekening
        # Vraag het bedrag dat de klant wil overschrijven.
        # Controleer dat het bedrag de daglimit niet
        # overschrijdt. Zoja, stop.
        # Controleer of het saldo op de rekening hoog
        # genoeg is. Zoniet, stop.
        # Vraag de rekening waarnaar wordt overgeschreven.
        # Vraag de pincode: 3 pogingen
        # Indien code correct is,
        # Verlaag het saldo op de rekening
        # Verhoog het bedrag op de doelrekening.

    elif choice == 4:
        print("Wijzig pin code")
        # Als de klant meerdere kaarten  heeft,
        # vraag dan eerst van welke kaart.
        # Vraag een nieuwe code.
        # Controleer dat de nieuwe code niet te eenvoudig is.
        # => Geen 1111, 1234, 4321, ...
        # Vraag de code opnieuw
        # Vergelijk de twee codes.
        # Indien verschillend: probeer opnieuw
        # Indien indien identiek: wijzig code
    elif choice == 9:
        print("Bedankt tot ziens.")
        break
    else:
        print("Optie niet gekend")


# wanneer we de beschrijvende taal bekijken, dan zien we veel
# stappen terugkomen:
#   - vraag welke rekening
#   - controleer saldo
#   - vraag het bedrag
# Terugkomende stappen zijn dikwijls goede kandidaten om functie van te maken.


balance = [900.0, 1400]  # giro rekening, spaarboekje
LIMIT = 300
pin = "3445"

def print_menu():
    """
    Prints the choices
    """
    print("U kan kiezen uit volgende opties:")
    print()
    print("===================================")
    print("1: Toon saldo")
    print("2: Haal geld af")
    print("3: Schrijf geld over")
    print("4: Wijzig pin code")
    print("9: Sluit sessie")
    print("===================================")

def print_balance(index: int):
    """
    Prints the balance of a specific account
    :param index: index of the account
    """
    print("Het saldo van rekening", i+1, "is", balance[index])

def choose_account() -> int:
    """
    Asks the user to choose an account
    :return: correct index of the account
    """
    cnt = len(balance)
    if cnt == 1:
        return 0
    while True:
        cnt = len(balance)
        print("U heeft", cnt, "rekeningen")
        choice = int(input("Welke rekening kiest u?"))
        if 1 < choice <= cnt:
            # De eerste rekening heeft index 0, dus keuze -1
            return choice - 1
    # Deze plaats kan nooit bereikt worden

def ask_amount(account:int) -> float:
    """
    Asks the user to choose an amount for an account
    :param account: index of the account
    :return: specific amount
    """
    maximum = balance[account]
    amount = float(input("Welke bedrag?"))
    if amount <= maximum:
        return amount
    else:
        print("Er staat slechts", maximum, "euro op je rekening")
        return 0.0

def check_limit(amount:float) -> bool:
    """
    Check if an amount is not above the limit
    :param amount: amount to check
    :return: True if amount is not above the limit
    """
    return amount <= LIMIT

def check_20_or_50(amount:float) -> bool:
    """
    Check if an amount can be divided in bills of 20 and 50 euro
    IMPORTANT: this functions has not been tested and does not always
            return the correct result.
    :param amount: Amount to be checked
    :return: True if correctly divisable
    """
    count_50 = amount // 50
    remainder = amount % 50
    count_20 = remainder // 20
    remainder = remainder % 20
    if remainder == 0:
        return True
    print("Bedrag is niet leverbaar in briefjes van 20 of 50")
    return False

def check_balance(account:int, amount:float) -> bool:
    """
    Check if an amount can be withdrawn from the account
    :param account: Account index
    :param amount: Ammount to be checked
    :return: True if customer is allowed to withdraw the amount
    """
    return amount <= balance[account]

def correct_pin() -> bool:
    """
    Ask the customer to enter the correct pin.
    After 3 unsuccessful attempts, an alarm is generated
    :return: True if correct pin was provided
    """
    for i in range(1,4,1):
        attempt = input("Geef je pin code?")
        if attempt == pin:
            return True
    # 3 foute pogingen
    return False



while True:
    print_menu()
    choice = int(input("Kies een optie: "))
    if choice == 1:
        print("Toon saldo")
        account_no = choose_account()
        print_balance(account_no)
    elif choice == 2:
        print("Haal geld af")
        account_no = choose_account()
        amount = ask_amount(account_no)
        if amount == 0.0:
            continue
        if not check_20_or_50(amount):
            continue
        if not check_limit(amount):
            continue
        if not check_balance(account_no, amount):
            continue
        if not correct_pin():
            continue
        print("Haal het gevraagde bedrag uit de geldlade")
        balance[account_no] -= amount
        print_balance(account_no)
    elif choice == 3:
        print("Schrijf geld over")
        account_no = choose_account()
        amount = ask_amount(account_no)
        if amount == 0.0:
            continue
        if not check_limit(amount):
            continue
        if not check_balance(account_no, amount):
            continue
        target = input("Geef het rekening number van de begunstigde?")
        if not correct_pin():
            continue
        balance[account_no] -= amount
        # Verhoog het bedrag op de doelrekening.
        print_balance(account_no)
    elif choice == 4:
        print("Wijzig pin code")
        # Als de klant meerdere kaarten  heeft,
        # vraag dan eerst van welke kaart.
        # Vraag een nieuwe code.
        # Controleer dat de nieuwe code niet te eenvoudig is.
        # => Geen 1111, 1234, 4321, ...
        # Vraag de code opnieuw
        # Vergelijk de twee codes.
        # Indien verschillend: probeer opnieuw
        # Indien indien identiek: wijzig code
    elif choice == 9:
        print("Bedankt tot ziens.")
        break
    else:
        print("Optie niet gekend")
