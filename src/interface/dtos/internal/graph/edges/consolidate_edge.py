from pydantic import BaseModel


class ConsolidateEdge(BaseModel):
    created_at: str
    document_mapping_id: int
