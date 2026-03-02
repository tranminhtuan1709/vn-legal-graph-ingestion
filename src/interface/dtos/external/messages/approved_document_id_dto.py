from pydantic import BaseModel


class ApprovedDocumentIdDto(BaseModel):
    message_id: str
    document_id: int
    event_type: str
    approved_at: str
    source: str
