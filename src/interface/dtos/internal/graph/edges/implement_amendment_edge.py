from pydantic import BaseModel


class ImplementAmendmentEdge(BaseModel):
    created_at: str
    version_id: int
    from_date: str | None
    to_date: str | None
    abolish_previous_content: bool | None
