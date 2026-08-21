"""All gradebook exceptions live here."""


class GradebookError(Exception):
    """Base class for every error this package raises."""


class StorageError(GradebookError):
    """Raised an error when loading roster data."""