from csv import DictReader
from oo_17_solution import Meter
import oo_25_pattern_factory_2 as factory


# We hebben een input bestand met verschillende afstanden in verschillende eenheden.
# We willen de totale afstanden in meter berekenen.


# We overlopen het bestand en maken gebruik van de factory om de afstanden te maken.
# Als er ooit type afstanden bijkomen, is het de verantwoordelijkheid van de andere oo_17 en de factory
# om het nieuwe type te ondersteunen. Onderstaande code wordt hierdoor niet beïnvloed.


def main():
    with open("oo_25_pattern_factory_2_data.csv") as f:
        reader = DictReader(f, delimiter=";")
        total = Meter(0)
        for row in reader:
            distance = factory.get_distance(row)
            total += distance
        print("totaal:", total)


if __name__ == "__main__":
    main()
