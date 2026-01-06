"""
This is the main module of the test for module 2: Object Oriented Programming
"""

# python imports
import csv
import os
from typing import List

# custom imports
from module02.movie.rating import MovieRating, get_rating
from module02.movie.movie import Movie, create_movie, Horror
from module02.person.person import _PERSOON_CACHE

# These constants must point to the input file reviews.csv,
# and the location of the output file (see item 9)
MOVIE_FILE = "C:/datadev2/reviews.csv"  #"D:/dev/learning/reviews.csv"
EXPORT_FILE = "C:/datadev2/export.csv"  #"D:/dev/learning/export.csv"


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

movies = load_movies(MOVIE_FILE)
if movies is None:
    print("Couldn't load movies.")


def menu_print_count(movies):
    print(f"Aantal films: {len(movies)}")

def menu_movies_per_genre(movies):
    counts = {}
    for movie in movies:
        genre = movie.__class__.__name__
        counts[genre] = counts.get(genre, 0) + 1
    for genre, count in sorted(counts.items(), key=lambda x: x[1], reverse=True):
        print(f"{genre}: {count}")

from module02.person.person import _PERSOON_CACHE

def menu_person_count():
    print(f"Aantal personen: {len(_PERSOON_CACHE)}")

def menu_highest_score(movies):
    relevant_movies = [m for m in movies if m.relevant_score()]

    if not relevant_movies:
        print("Geen relevante scores gevonden.")
        return
    max_score = max(m.score for m in relevant_movies)
    print(f"Highest score: {max_score}")

    for movie in relevant_movies:
        if movie.score == max_score:
            print(f"{movie.title} {movie.score}")

def menu_most_active_regisseur(movies):
    counts = {}
    for movie in movies:
        for director in movie.directors:
            name = director.full_name
            counts[name] = counts.get(name, 0) + 1
    if not counts:
        print("No regisseur founded")
        return
    max_count = max(counts.values())
    print(f"Most active regisseur: with {max_count} films")
    for name, count in sorted(counts.items()):
        if count == max_count:
            print(f"- {name}")

def menu_shortest_longest_movie(movies):
    with_length = [m for m in movies if m.length is not None]

    if not with_length:
        print("no movies with length found.")
        return
    min_length = min(m.length for m in with_length)
    max_length = max(m.length for m in with_length)
    print(f"Shortest movie: {min_length} mins:")
    for m in with_length:
        if m.length == min_length:
            print(f"-> {m.title} ")
    print(f"Longest movie: {max_length} mins:")
    for m in with_length:
        if m.length == max_length:
            print(f"-> {m.title}")

from module02.movie.movie import Horror
def menu_scarry_horror(movies):
    scarry_movies =[]
    for movie in movies:
        if isinstance(movie, Horror):
            scarry_movies.append(movie)
    print("Scary movies:")
    for m in scarry_movies:
        print(f"-{m.title}")

def menu_score_list(movies):
    score_counts = {score: 0 for score in range(101)}
    for movie in movies:
        if movie.score is not None and 0 <= movie.score <= 100:
            score_counts[movie.score] += 1
    for score in range(101):
        print(f"{score}%: {score_counts[score]}")

def menu_export_to_csv(movies):
    export_movies = [m for m in movies if not m.relevant_score()]
    export_movies.sort(key=lambda m: m.title.lower())
    with open(EXPORT_FILE, "w", encoding="UTF-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Titel", "genre", "url", "score", "count"])

        for m in export_movies:
            writer.writerow([
                m.title,
                m.__class__.__name__,
                m.url(),
                m.score,
                m.count
            ])
    print(f"export done ({len(export_movies)} films) -> {EXPORT_FILE}")




def main():
    """
    Load movies and present a menu until the user chooses to stop
    """
    if movies is None:
        print("Couldn't load movies.")
        return

    while True:
        print("                            ******MENU*******")
        print("1) Print number of movies")
        print("2) Print number of movies per genre")
        print("3) Print number of persons")
        print("4) Print highest Score")
        print("5) Print most active regisseur")
        print("6) Print shortest & longest movie")
        print("7) Print Most scared horror")
        print("8) Print Score-list")
        print("9) Export to CSV")
        print("10) Stop")

        choice = input("Maak een keuze 1-10: ").strip()
        if choice == "1":
            menu_print_count(movies)
        elif choice == "2":
            menu_movies_per_genre(movies)
        elif choice == "3":
            menu_person_count()
        elif choice == "4":
            menu_highest_score(movies)
        elif choice == "5":
            menu_most_active_regisseur(movies)
        elif choice == "6":
            menu_shortest_longest_movie(movies)
        elif choice == "7":
            menu_scarry_horror(movies)
        elif choice == "8":
            menu_score_list(movies)
        elif choice == "9":
            menu_export_to_csv(movies)
        elif choice == "10":
            print("Programma stopped.")
            break
        else:
            print("Choose a valid option.")



if __name__ == "__main__":
    main()
