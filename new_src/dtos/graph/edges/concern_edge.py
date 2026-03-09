from pydantic import BaseModel


class ConcernEdge(BaseModel):
    from_node_id: str
    to_node_id: str
    edge_type: str
    created_at: str
    