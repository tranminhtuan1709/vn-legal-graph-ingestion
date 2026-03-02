from pydantic import BaseModel


class SectorNode(BaseModel):
    node_id: str
    created_at: str
    sector_id: int
    sector_name: str | None
