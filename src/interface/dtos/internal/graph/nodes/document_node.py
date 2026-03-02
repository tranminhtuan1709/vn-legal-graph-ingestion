from pydantic import BaseModel


class DocumentNode(BaseModel):
    node_id: str
    created_at: str
    document_id: int
    document_number: str | None
    document_name: str | None
    issued_date: str | None
    effective_date: str | None
    expiry_date: str | None
    status: str | None
    summary: str | None
