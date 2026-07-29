class UserAlreadyExistsError(Exception):
    """Raised when a user already exists in the database."""


class UserNotFoundError(Exception):
    """Raised when a user is not found in the database."""
