from pydantic import BaseModel


class PartNode(BaseModel):
    node_id: str
    node_label: str
    created_at: str
    source: str
    part_id: int
    part_number: str | None
    part_name: str | None
    