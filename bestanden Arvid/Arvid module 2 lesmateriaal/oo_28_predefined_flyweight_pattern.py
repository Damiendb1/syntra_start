# Het flyweight pattern is een factory pattern waarbij wordt geprobeerd om zo weinig mogelijk identieke objecten
# te maken.

# Er zijn gevallen waarbij je op voorhand weet welke objecten je wilt maken.
# Deze objecten kunnen dan ook op voorhand gemaakt worden.
# Wanneer je alle mogelijk objecten wil laten wijzen naar


class Grade:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    def __repr__(self):
        return f"{self.name}"


GRADES = {
    "A+": Grade("A+", description="Outstanding"),
    "A": Grade("A", description="Excellent"),
    "A−": Grade("A−", description="Very good"),
    "B+": Grade("B+", description="Good"),
    "B": Grade("B", description="Above average"),
    "B-": Grade("B−", description="Fair"),
    "C+": Grade("C+", description="Satisfactory"),
    "C": Grade("C", description="Average"),
    "C−": Grade("C−", description="Below average"),
    "D+": Grade("D+", description="Poor"),
    "D": Grade("D", description="Barely passing"),
    "D−": Grade("D−", description="Lowest passing"),
    "F": Grade("F", description="Fail"),
}

def get_grade(code:str) -> Grade:
    grade = GRADES.get(code)
    if grade:
        return grade
    raise ValueError(f"Invalid grade code: {code}")


b_minus = get_grade("B-")
print(b_minus.description)
