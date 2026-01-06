import code
from typing import Optional

class MovieRating:
    """klasse predefined flyweight for movie conrtent rating. with code and description"""

    _Ratingvolgorde = {
            "NR": 0,
            "G": 1,
            "PG": 2,
            "PG-13": 3,
            "R": 4,
            "NC17": 5
        }

    def __init__(self, description: str, code: str):
        """Initialize a new MovieRating object."""
        if not description or not description.strip():
            raise ValueError("Description cannot be empty")
        if not code or not code.strip():
            raise ValueError("Code cannot be empty")

        self.description = description
        self.code = code


    def __repr__(self) -> str:
        return f"Rating({self.code})"

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, MovieRating):
            return NotImplemented
        return self._Ratingvolgorde[self.code] < self._Ratingvolgorde[other.code]

    def __gt__(self, other):
        return self._Ratingvolgorde[self.code] > self._Ratingvolgorde[other.code]

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, MovieRating):
            return NotImplemented
        return self.code == other.code


RATINGS= {
    "NR": MovieRating("NR, Niet gekeurd", "NR"),
    "G": MovieRating("G, Alle leeftijden", "G"),
    "PG": MovieRating("PG, Ouderlijk toezicht aangeraden", "PG"),
    "PG-13": MovieRating("PG-13, Ouderlijk toezicht ten zeerste aangeraden", "PG-13"),
    "R": MovieRating("R, Onder 17 is ouderlijk toezicht aangeraden", "R"),
    "NC17": MovieRating("NC17, Enkel voor volwassenen", "NC17")
}

def get_rating(code: str) -> MovieRating:
    """
    Return a rating object for a given code
    :param code: rating code
    :return: MovieRating object
    """
    if not code or not code.strip():
        raise ValueError("Code cannot be empty")

    normal_code = code.strip().upper()
    rating = RATINGS.get(normal_code)
    if rating is None:
       raise ValueError(f"Rating {code} is niet gedefinieerd")

    return rating

