"""All gradebook exceptions live here."""


class GradebookError(Exception):
    """Base class for every error this package raises."""


class StudentNotFound(GradebookError):
    """Raised when a student is not found."""

class InvalidGrade(GradebookError):
    """Raised when a grade is invalid"""