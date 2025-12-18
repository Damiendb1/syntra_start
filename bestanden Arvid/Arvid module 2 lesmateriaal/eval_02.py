"""
This is the main module of the test for module 2: Object Oriented Programming
"""

# python imports
import csv
import os
from typing import List

# custom imports
from module02.movie.movie import Movie, create_movie

# These constants must point to the input file reviews.csv,
# and the location of the output file (see item 9)
MOVIE_FILE = "D:/dev/learning/reviews.csv"
EXPORT_FILE = "D:/dev/learning/export.csv"


def load_movies(file_location: str) -> List[Movie] | None:
    """
    Load all movies from a csv file into a list of Movie objects.
    :param file_location: Location of the csv file
    :raise FileNotFoundError: When the file cannot be found
    :return: List of Movie objects or None in case of error
    """
    if not os.path.exists(file_location):
        raise FileNotFoundError("Bestand niet gevonden: {file_location}")
    try:
        errors = 0
        movies = []
        with (open(file_location, 'r', encoding="UTF-8") as file):
            reader = csv.DictReader(file, delimiter=",")
            for i, row in enumerate(reader):
                try:
                    movie = create_movie(row)
                    movies.append(movie)
                except ValueError as e:
                    errors += 1
                    print(f"Probleem met Lijn {i} : '{e}' => {row}")
        if errors:
            print(f"{errors} films konden niet geladen worden")
    except Exception as e:
        # Exception is a good choice
        print(f"Probleem bij het inlezen van bestand: {file_location} => {e}")
        return None
    return movies


def main():
    """
    Load movies and present a menu until the user chooses to stop
    """
    pass


if __name__ == "__main__":
    main()
