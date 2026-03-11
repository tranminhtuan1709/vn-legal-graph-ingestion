from pydantic import BaseModel
from datetime import date


class DocumentDto(BaseModel):
    document_id: int
    document_number: str | None
    document_name: str | None
    issued_date: date | None
    effective_date: date | None
    expiry_date: date | None
    status: str | None
    small_note: str | None
    document_type: str | None
    sector: str | None
    issuing_authorities: list[str]
    document_type_id: int | None
    sector_id: int | None
    issuing_authority_ids: list[int]
    