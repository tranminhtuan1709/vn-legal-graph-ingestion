from typing import Any


class BaseError(Exception):
    def __init__(self, message: str, context: dict[str, Any] | None) -> None:
        """
        Init `BaseError` with provided error message and context.
        This inherits the standard Python class `Exception`.

        Args:
            message (str): Error message.
            context (dict[str, Any] | None): Additional context about the error.
        """

        super().__init__(message)
        self.context = context


class ValidationError(BaseError):
    pass


class InfrastructureError(BaseError):
    pass
