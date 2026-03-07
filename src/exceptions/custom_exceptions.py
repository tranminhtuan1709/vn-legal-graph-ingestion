from typing import Any


class BaseError(Exception):
    def __init__(self, message: str, context: dict[str, Any] | None) -> None:
        super().__init__(message)
        self.context = context


class ValidationError(BaseError):
    pass


class InfrastructureError(BaseError):
    pass


class FetchDataError(BaseError):
    pass


class CreateSubgraphError(BaseError):
    pass


class CreateNodeError(BaseError):
    pass


class CreateEdgeError(BaseError):
    pass


class DetachSubgraphError(BaseError):
    pass


class RebuildSubgraphError(BaseError):
    pass


class IngestionError(BaseError):
    pass
