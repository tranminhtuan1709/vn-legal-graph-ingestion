from pydantic import BaseModel


class SuspendEdge(BaseModel):
    from_date: str | None
    to_date: str | None
