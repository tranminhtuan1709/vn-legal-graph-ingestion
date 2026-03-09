from pydantic import BaseModel


class ImplementAmendmentEdge(BaseModel):
    from_node_id: str
    to_node_id: str
    edge_type: str
    created_at: str
    version_id: int
    from_date: str | None
    to_date: str | None
    abolish_previous_content: bool
    