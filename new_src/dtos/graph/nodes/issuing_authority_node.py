from pydantic import BaseModel


class IssuingAuthorityNode(BaseModel):
    node_id: str
    node_label: str
    created_at: str
    source: str
    issuing_authority_id: int
    issuing_authority_name: str
