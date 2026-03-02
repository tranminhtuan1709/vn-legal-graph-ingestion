from pydantic import BaseModel


class MiniPartNode(BaseModel):
    node_id: str
    created_at: str
    chapter_id: int
    mini_part_number: str | None
    mini_part_name: str | None
