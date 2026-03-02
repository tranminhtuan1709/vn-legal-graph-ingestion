from pydantic import BaseModel


class CorrectEdge(BaseModel):
    created_at: str
    document_mapping_id: int
