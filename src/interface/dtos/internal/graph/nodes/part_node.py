from pydantic import BaseModel


class PartNode(BaseModel):
    node_id: str
    created_at: str
    chapter_id: int
    part_number: str | None
    part_name: str | None
