from pydantic import BaseModel
from typing import Any


class ExtractedDocumentMapping(BaseModel):
    id: Any
    from_document_id: Any
    to_document_id: Any
    relationship_type: Any
    