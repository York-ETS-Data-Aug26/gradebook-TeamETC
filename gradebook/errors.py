"""All gradebook exceptions live here."""


class GradebookError(Exception):
    """Base class for every error this package raises."""


<<<<<<< HEAD
class StorageError(GradebookError):
    """Raised an error when loading roster data."""
=======
class StudentNotFound(GradebookError):
    """Raised when a student is not found."""

class InvalidGrade(GradebookError):
    """Raised when a grade is invalid"""
>>>>>>> 2b9c3dafa7c9959b888b98a704e5b993a8be571d
