from pydantic import BaseModel


class AmendEdge(BaseModel):
    created_at: str
    document_mapping_id: int
