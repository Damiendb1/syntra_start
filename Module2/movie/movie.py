from __future__ import annotations
from abc import ABC
from datetime import datetime
from typing import Optional
from typing import List

from module02.movie.rating import MovieRating
from module02.person.person import Person
from module02.person.person import get_person
from module02.movie.rating import get_rating

def _parse_int(value: object) -> Optional[int]:
    if value is None:
        return None
    s = str(value).strip()
    if s == "":
        return None
    try:
        return int(s)
    except ValueError:
        return None

def _parse_date(value: object) -> Optional[datetime]:
    if value is None:
        return None
    s = str(value).strip()
    if s == "":
        return None
    try:
        return datetime.strptime(s, "%d %b %Y")
    except ValueError:
        return None

def _parse_directors(value: object) -> List[Person]:
    if value is None:
        return []
    s = str(value).strip()
    if s =="":
        return []
    parts = [p.strip() for p in s.split(",")]
    return [get_person(p) for p in parts if p]


class Movie(ABC):
    """
    abstract class for movie
    """
    def __init__(
            self,
            rt_link: str,
            title: str,
            rating: MovieRating,
            directors: List[Person],
            release_date: Optional[datetime],
            streaming_date:Optional[datetime],
            length: Optional[int],
            company: Optional[str],
            score: Optional[int],
            count: Optional[int],
    ):
        if not rt_link or not rt_link.strip():
            raise ValueError("RT link cannot be empty")
        if not title or not title.strip():
            raise ValueError("Title cannot be empty")
        if rating is None:
            raise ValueError("Rating cannot be empty")

        self.rt_link = rt_link.strip()
        self.title = title.strip()
        self.rating = rating
        self.directors = directors or []
        self.release_date = release_date
        self.streaming_date = streaming_date
        self.length = length
        self.company = company
        self.score = score
        self.count = count

    def relevant_score(self) ->bool:
        """
        score is relevant if it is above 100
        """
        return self.score is not None and self.count is not None and self.count >= 100

    def is_classic(self)->bool:
        """
        Movie is classic if :
        minimum 20yrs old
        score above 80
        """
        if not self.release_date or not self.relevant_score():
            return False

        years_old = datetime.now().year - self.release_date.year
        return years_old >= 20 and self.score > 80

    def is_short(self)->bool:
        """
        Movei is short if shorter than 30min
        """
        return self.length is not None and self.length < 30

    def url(self)->str:
        return f"https://www.rottentomatoes.com/{self.rt_link}"

class ActionAdventure(Movie):
    pass

class Comedy(Movie):
    def is_slapstick(self)->bool:
        return self.relevant_score() and self.score < 40

class Drama(Movie):
    pass

class Horror(Movie):
    def is_scary(self) ->bool:
        return self.rating > get_rating("PG")

class Romance(Movie):
    def is_cosy(self)->bool:
        return self.length is not None and 70 <= self.length <= 100

class ScienceFictionFantasy(Movie):
    pass

class Western(Movie):
    pass

def create_movie(movie_info:dict)->Movie:
    genre = movie_info["genres"]

    genre_map = {
        "Action & Adventure": "ActionAdventure",
        "Comedy": "Comedy",
        "Drama": "Drama",
        "Horror": "Horror",
        "Romance": "Romance",
        "Science Fiction & Fantasy": "ScienceFictionFantasy",
        "Western": "Western"
    }

    cls = genre_map.get(genre)
    if cls is None:
        raise ValueError(f"Unknown genre: {genre}")

    rt_link = (movie_info.get("rotten_tomatoes_link") or "").strip()
    title = (movie_info.get("movie_title") or "").strip()
    if not rt_link:
        raise ValueError("rotten_tomatoes_link cannot be empty")
    if not title:
        raise ValueError("movie_title cannot be empty")

    rating_code = (movie_info.get("content_rating") or "").strip()
    rating = get_rating(rating_code)

    directors = _parse_directors(movie_info.get("directors"))
    release_date = _parse_date(movie_info.get("Original_release"))
    streaming_date = _parse_date(movie_info.get("release_date"))
    length = _parse_int(movie_info.get("runtime_minutes"))
    company_raw = movie_info.get("production_company")
    company = str(company_raw).strip() if company_raw is not None and str(company_raw).strip() else None
    score = _parse_int(movie_info.get("audience_rating"))
    count = _parse_int(movie_info.get("audience_count"))

    return cls(
        rt_link=rt_link,
        title=title,
        rating=rating,
        directors=directors,
        release_date=release_date,
        streaming_date=streaming_date,
        length=length,
        company=company,
        score=score,
        count=count,
    )