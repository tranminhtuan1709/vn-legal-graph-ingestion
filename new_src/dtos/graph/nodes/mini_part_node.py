from pydantic import BaseModel


class MiniPartNode(BaseModel):
    node_id: str
    node_label: str
    created_at: str
    source: str
    mini_part_id: int
    mini_part_number: str | None
    mini_part_name: str | None
    