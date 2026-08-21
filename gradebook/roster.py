"""Student roster operations. Owner: A."""
from gradebook.errors import InvalidGrade, StudentNotFound


def find_student(roster, name):
    try:
        return roster[name]
    except KeyError as e:
        raise StudentNotFound(f"no student named {name!r}") from e


def add_student(roster, name, scores):
    for score in scores:
        if score < 0 or score > 100:
            raise InvalidGrade(f'{score} is not in valid range')
    roster[name] = scores