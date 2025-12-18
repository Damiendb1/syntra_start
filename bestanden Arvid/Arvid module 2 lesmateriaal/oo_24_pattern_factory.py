import csv

from oo_22_composition_collections import Room, PremiumRoom, Suite, BasicRoom, Hotel, Excelsior, factory_ifs, factory_dict


# Voor een hotel management systeem moet je flexibel Room-objecten kunnen maken.
# Je kan de verantwoordelijkheid voor het maken van de objecten verdelen
# volledig bij de gebruiker van de class laten.
# Dat betekent dat als er een Room-sub klasse bijkomt de gebruiker van de klassen
# impact ondervindt.
# Je kan hier op verschillende manieren mee omgaan.
# 1/ Niets doen. De gebruiker moet dan voor elke nieuwe sub klasse code voorzien.
# 2/ Een erg uitgebreide klasse hiërarchie maken zodat de kans klein is dat er een nieuwe klasse bijkomt.
# 3/ Een factory functie / class maken die de instructie krijgt om objecten van een specifiek type
# te maken.

def room_factory_ifs(room_type: str, number: str, floor: int) -> Room:
    if room_type == "S":
        return Suite(number, floor)
    if room_type == "P":
        return PremiumRoom(number, floor)
    if room_type == "B":
        return BasicRoom(number, floor)
    raise ValueError(f"Invalid room type: {room_type}")


# het kan nog een stukje efficienter door een dict te gebruiken
# wanneer en nog kamertypes bijkomen, moet je enkel de dict aanvullen
# en werkt de factory meteen voor het nieuwe kamertype
FACTORY_MAPPING: dict[str, type[Room]] = {
    "S": Suite,
    "P": PremiumRoom,
    "B": BasicRoom
}


def room_factory_dict(room_type: str, number: str, floor: int) -> Room:
    type_ = FACTORY_MAPPING.get(room_type)
    if type_:
        return type_(number, floor)
    raise ValueError(f"Invalid room type: {room_type}")


def option1_no_factory():
    total_price = 0
    with open(r"C:\Users\arvid\PycharmProjects\learning2\filedata\rooms.csv") as infile:
        reader = csv.reader(infile, delimiter=";")
        hotel = Hotel("FactoryHotel")
        for line in reader:
            room_type, number, floor = line
            if room_type == 'B':
                room = BasicRoom(number, floor)
            elif room_type == 'P':
                room = PremiumRoom(number, floor)
            elif room_type == 'S':
                room = Suite(number, floor)
            elif room_type == 'E':
                room = Excelsior(number, floor)
            else:
                raise ValueError(f"Type {room_type} is niet gekend.")
            hotel.add_room(room)
            # room = get_correct_object(room_type, number, floor)
            total_price += room.price_per_night()
        print("De totale prijs is ", total_price, "€")
        print(hotel)
        print(hotel.full_description())


def option1_factory_ifs():
    total_price = 0
    with open(r"C:\Users\arvid\PycharmProjects\learning2\filedata\rooms.csv") as infile:
        reader = csv.reader(infile, delimiter=";")
        hotel = Hotel("FactoryHotel")
        for line in reader:
            room_type, number, floor = line
            room = factory_ifs(room_type, number, floor)
            hotel.add_room(room)
            # room = get_correct_object(room_type, number, floor)
            total_price += room.price_per_night()
        print("De totale prijs is ", total_price, "€")
        print(hotel)
        print(hotel.full_description())


def option1_factory_dict():
    total_price = 0
    with open(r"C:\Users\arvid\PycharmProjects\learning2\filedata\rooms.csv") as infile:
        reader = csv.reader(infile, delimiter=";")
        hotel = Hotel("FactoryHotel")
        for line in reader:
            room_type, number, floor = line
            room = factory_dict(room_type, number, floor)
            hotel.add_room(room)
            # room = get_correct_object(room_type, number, floor)
            total_price += room.price_per_night()
        print("De totale prijs is ", total_price, "€")
        print(hotel)
        print(hotel.full_description())

# option1_no_factory()


# option1_factory_ifs()

# option1_factory_dict()
