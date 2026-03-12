from pydantic import BaseModel
from datetime import datetime


class Edge(BaseModel):
    from_node_id: str
    to_node_id: str
    edge_type: str
    created_at: datetime
    