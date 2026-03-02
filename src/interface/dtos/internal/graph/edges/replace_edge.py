from pydantic import BaseModel


class ReplaceEdge(BaseModel):
    created_at: str
    document_mapping_id: int
