from pydantic import BaseModel


class DocumentTypeNode(BaseModel):
    node_id: str
    node_label: str
    created_at: str
    source: str
    document_type_id: int
    document_type_name: str
    