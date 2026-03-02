from pydantic import BaseModel


class SupplementEdge(BaseModel):
    created_at: str
    version_id: int
    from_date: str | None
    to_date: str | None
