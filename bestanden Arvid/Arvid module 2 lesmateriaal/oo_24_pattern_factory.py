from oo_22_composition_collections import Room, PremiumRoom, Suite, BasicRoom

# Voor een hotel management systeem  moet je flexibel Room-objecten kunnen maken.
# Je kan de verantwoordelijkheid voor het maken van de objecten verdelen
# volledig bij de gebruiker van de class laten.
# Dat betekent dat als er een Room-sub klasse bijkomt de gebruiker van de klassen
# impact ondervindt.
# Je kan hier op verschillende manieren mee omgaan.
# 1/ Niets doen. De gebruiker moet dan voor elke nieuwe sub klasse code voorzien.
# 2/ Een erg uitgebreide klasse hiërarchie maken zodat de kans klein is dat er een nieuwe klasse bijkomt.
# 3/ Een factory functie / class maken die de instructie krijgt om onjecten van een specifiek type
# te maken.

def room_factory_ifs(room_type: str, number:str, floor: int) -> Room:
    if room_type == "Suite":
        return Suite(number, floor)
    if room_type == "Premium":
        return PremiumRoom(number, floor)
    if room_type == "Basic":
        return BasicRoom(number, floor)
    raise ValueError(f"Invalid room type: {room_type}")

# het kan nog een stukje efficienter door een dict te gebruiken
# wanneer en nog kamertypes bijkomen, moet je enkel de dict aanvullen
# en werkt de factory meteen voor het nieuwe kamertype
FACTORY_MAPPING : dict[str, type[Room]] = {
    "Suite": Suite,
    "Premium": PremiumRoom,
    "Basic": BasicRoom
}

def room_factory_dict(room_type: str, number:str, floor: int) -> Room:
    type_ = FACTORY_MAPPING.get(room_type)
    if type_:
        return type_(number, floor)
    raise ValueError(f"Invalid room type: {room_type}")


