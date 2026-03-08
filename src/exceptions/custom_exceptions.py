from typing import Any


class CustomBaseError(Exception):
    def __init__(self, message: str, context: dict[str, Any] | None) -> None:
        super().__init__(message)
        self.context = context


class ValidationError(CustomBaseError):
    pass


class InfrastructureError(CustomBaseError):
    pass


class FetchDataError(CustomBaseError):
    pass


class CreateSubgraphError(CustomBaseError):
    pass


class CreateNodeError(CustomBaseError):
    pass


class CreateEdgeError(CustomBaseError):
    pass


class DetachSubgraphError(CustomBaseError):
    pass


class RebuildSubgraphError(CustomBaseError):
    pass


class IngestionError(CustomBaseError):
    pass
