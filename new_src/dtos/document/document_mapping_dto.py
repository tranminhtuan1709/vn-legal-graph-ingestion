from pydantic import BaseModel


class DocumentMappingDto(BaseModel):
    id: int
    from_document_id: int
    to_document_id: int
    relationship_type: str
    