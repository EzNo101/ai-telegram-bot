class UserAlreadyExistsError(Exception):
    """Raised when a user already exists in the database."""


class UserNotFoundError(Exception):
    """Raised when a user is not found in the database."""


class ChatNotFoundError(Exception):
    """Raised when a chat is not found in the database."""


class ChatAlreadyExistsError(Exception):
    """Raised when a chat already exists in the database."""


class MessageNotFoundError(Exception):
    """Raised when a message is not found in the database."""
