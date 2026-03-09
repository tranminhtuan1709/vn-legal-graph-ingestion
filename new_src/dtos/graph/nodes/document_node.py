from pydantic import BaseModel


class DocumentNode(BaseModel):
    node_id: str
    node_label: str
    created_at: str
    source: str
    document_id: int
    document_number: str
    document_name: str
    issued_date: str | None
    effective_date: str | None
    expiry_date: str | None
    status: str | None
    small_node: str | None
    