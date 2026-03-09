from pydantic import BaseModel


class GuideEdge(BaseModel):
    from_node_id: str
    to_node_id: str
    edge_type: str
    created_at: str
    document_mapping_id: int
    