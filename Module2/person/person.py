class Person:
    """
    Flyweight Factory Pattern for a person
    one person object per name
    """
    def __init__(self, full_name: str):
        """
        Initialize a new Person object
        :param full_name: Full name of the person
        """
        if not full_name or not full_name.strip():
            raise ValueError("Full name cannot be empty")
        self._full_name: str = full_name.strip()

    @property
    def full_name(self) -> str:
        """Return the full name of the person"""
        return self._full_name

    def __repr__(self) -> str:
        """String representation of the Person"""
        return f"Person({self.full_name})"

    def __eq__(self, other: object)-> bool:
        """Check if two Person objects are equal (based on name)"""
        if not isinstance(other, Person):
            return NotImplemented
        return self.full_name.lower() == other.full_name.lower()

    def __hash__(self) -> int:
        return hash(self.full_name.lower())

_PERSOON_CACHE: dict[str, Person] = {}
    
def get_person(full_name: str) -> Person:
    """
    Get an existing person or create a new one 
    :param full_name: Full name of the person
    """
    if not full_name or not full_name.strip():
        raise ValueError("Full name cannot be empty")

    normal = full_name.strip()
    key = normal.lower()

    if key in _PERSOON_CACHE:
        return _PERSOON_CACHE[key]

    person = Person(normal)
    _PERSOON_CACHE[key] = person
    return person

