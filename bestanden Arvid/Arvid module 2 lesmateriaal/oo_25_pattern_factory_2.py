import csv
from decimal import Decimal

from oo.oo_17_solution import Yard, Meter, Inch, Distance

def get_distance(distance_info) -> Distance:
    unit = distance_info["Unit"]
    value = distance_info["Value"]

    match unit:
        case 'M':
            return Meter(float(value))
        case 'YD':
            return Yard(float(value))
        case 'IN':
            return Inch(float(value))
    raise ValueError(f"Unknown unit: {unit}")

