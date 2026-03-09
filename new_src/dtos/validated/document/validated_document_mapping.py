from pydantic import BaseModel
from typing import Literal


class ValidatedDocumentMapping(BaseModel):
    id: int
    from_document_id: int
    to_document_id: int
    relationship_type: Literal["huong_dan", "dinh_chinh", "sua_doi", "thay_the", "hop_nhat"]
    