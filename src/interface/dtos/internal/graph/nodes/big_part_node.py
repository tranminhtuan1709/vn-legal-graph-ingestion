from pydantic import BaseModel


class BigPartNode(BaseModel):
    node_id: str
    created_at: str
    big_part_id: int
    big_part_number: str | None
    big_part_name: str | None
