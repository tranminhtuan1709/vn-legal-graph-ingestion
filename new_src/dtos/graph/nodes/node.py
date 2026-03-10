from pydantic import BaseModel


class Node(BaseModel):
    node_id: str
    node_label: str
    created_at: str
    source: str
    