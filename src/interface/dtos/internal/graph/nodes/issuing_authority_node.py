from pydantic import BaseModel


class IssuingAuthorityNode(BaseModel):
    node_id: str
    created_at: str
    issuing_authority_id: int
    issuing_authority_name: str | None
