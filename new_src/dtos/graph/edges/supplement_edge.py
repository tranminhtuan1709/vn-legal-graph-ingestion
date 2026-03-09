from pydantic import BaseModel


class SupplementEdge(BaseModel):
    from_node_id: str
    to_node_id: str
    edge_type: str
    created_at: str
    from_date: str | None
    to_date: str | None
    