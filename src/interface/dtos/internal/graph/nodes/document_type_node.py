from pydantic import BaseModel


class DocumentTypeNode(BaseModel):
    node_id: str
    created_at: str
    document_type_id: int
    document_type_name: str | None
