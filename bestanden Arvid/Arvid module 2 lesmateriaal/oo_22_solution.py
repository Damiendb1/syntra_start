# Oefening 1A:
# Maak een class Book met attributen title (str), author (Person) en chapters (list of Chapter)
# Een chapter heeft een titel en een aantal pagina's
# Zorg er voor dat enkel Chapters kunnen worden toegevoegd aan een Book


# Oefening 1B:
# Maak sub klassen van Chapter: Introduction, Conclusion, Index
# Zorg er voor dat een book slechts 1 Introduction, 1 Conclusion en 1 Index kan hebben

# oefening 1C:
# Zorg ervoor dat een introductie steeds vooraan staat, de conclusie steeds achteraan

# oefening 1D
# De index staat ofwel voor de introductie ofwel na de conclusie

# Oefening 1E:
# Zorg er voor dat chapters enkel in stijgende volgorde kunnen worden toegevoegd en dat er geen
# dubbele nummer zijn.
# Maak een class Library met attributen name (str) en books (list of Book)

# Oefening 2:
# Maak een class Library (naam, adres) die een verzameling boeken omvat.
# Boeken mogen meermaals voorkomen.
# Voorzie een function search_book(book_title) die controleert hoeveel keer een boek voorkomt.

class Person:
    known_persons = {}

    def __init__(self, name: str):
        self.name = name


def get_person(name: str) -> Person:
    name_up = name.upper()
    if name_up not in Person.known_persons:
        Person.known_persons[name_up] = Person(name)
    return Person.known_persons[name_up]


class Chapter:
    """
    Chapter is the most general type.
    It has a title and a type
    """

    def __init__(self, title: str, pages: int):
        self.title = title
        self.pages = pages

    def __repr__(self):
        return f"{self.title} ({self.pages} pagina's)"


class NumberedChapter(Chapter):
    """
    A chapter with a specific number.
    """

    def __init__(self, title: str, pages: int, number: int):
        super().__init__(title, pages)
        self.number = number


class Introduction(Chapter):
    def __init__(self, pages: int):
        super().__init__("Introductie", pages)


class Conclusion(Chapter):
    def __init__(self, pages: int):
        super().__init__("Conclusie", pages)


class Index(Chapter):
    def __init__(self, pages: int):
        super().__init__("Index", pages)


class Book:
    def __init__(self, title: str, author: str | Person, chapters: list[Chapter]):
        self.title = title
        if isinstance(author, str):
            author = get_person(author)
        self.author = author
        self.chapters = []
        for chapter in chapters:
            if isinstance(chapter, Chapter):
                self.add_chapter(chapter)
            else:
                raise ValueError("Alle chapters moeten van het type Chapter zijn")

    def add_chapter(self, chapter: Chapter):
        # elke type chapter mag als eerste voorkomen in een book
        if len(self.chapters) == 0:
            self.chapters.append(chapter)
            return
        previous_type = type(self.chapters[-1])
        current_type = type(chapter)
        ok = False
        if current_type == Index:
            ok = previous_type == Conclusion

        if current_type == Introduction:
            ok = previous_type == Index

        if current_type == Conclusion:
            ok = previous_type in (Chapter, Index, Introduction)

        if current_type == Chapter:
            ok = previous_type in (Chapter, Index, Introduction)

        if ok:
            self.chapters.append(chapter)
            return
        raise ValueError(f"{chapter} mag niet toegevoegd worden aan {self.title} omdat het niet voldoet aan de regels")


b = Book("Het verhaal van de vrouw", "Eva",
         [Introduction(100), Chapter("Het verhaal", 100), Chapter("De Vrouw", 10), Conclusion(100)])
b = Book("Het verhaal van de man", "Adam",
         [Introduction(100), Index(2), Chapter("Het verhaal van de vrouw", 100), Conclusion(100)])
b = Book("Het verhaal van de man", "Adam",
         [Introduction(100), Chapter("Het verhaal van de vrouw", 100), Index(2), Conclusion(100)])
b = Book("Het verhaal van de man", "Adam",
         [Introduction(100), Chapter("Het verhaal van de vrouw", 100), Index(2), Conclusion(100), Index(2), ])
b = Book("Het verhaal van de man", "Adam",
         [Introduction(100), Index(2), Chapter("Het verhaal van de vrouw", 100), Conclusion(100)])
