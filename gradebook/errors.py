"""All gradebook exceptions live here."""


class GradebookError(Exception):
    """Base class for every error this package raises."""

class ReportError(GradebookError):
    """Custom Error class based off of GradebookError."""