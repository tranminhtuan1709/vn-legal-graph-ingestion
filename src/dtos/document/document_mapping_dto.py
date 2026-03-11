from pydantic import BaseModel
from typing import Literal
from datetime import date


class DocumentMappingDto(BaseModel):
    mapping_id: int
    relationship_type: Literal["huong_dan", "sua_doi", "dinh_chinh", "thay_the", "hop_nhat"]

    from_document_id: int
    from_document_number: str | None
    from_document_name: str | None
    from_issued_date: date | None
    from_effective_date: date | None
    from_expiry_date: date | None
    from_status: str | None
    from_small_note: str | None

    to_document_id: int
    to_document_number: str | None
    to_document_name: str | None
    to_issued_date: str | None
    to_effective_date: str | None
    to_expiry_date: str | None
    to_status: str | None
    to_small_note: str | None
    