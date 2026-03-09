from pydantic import BaseModel


class Sector(BaseModel):
    node_id: str
    node_label: str
    created_at: str
    source: str
    sector_id: int
    sector_name: str
    