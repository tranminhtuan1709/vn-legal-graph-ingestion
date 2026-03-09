from pydantic import BaseModel


class BigPartNode(BaseModel):
    node_id: str
    node_label: str
    created_at: str
    source: str
    big_part_id: int
    big_part_number: str | None
    big_part_name: str | None
    