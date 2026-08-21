"""All gradebook exceptions live here."""


class GradebookError(Exception):
    """Base class for every error this package raises."""

class StorageError(GradebookError):
    """Raised an error when loading roster data."""

class StudentNotFound(GradebookError):
    """Raised when a student is not found."""

class InvalidGrade(GradebookError):
    """Raised when a grade is invalid"""
