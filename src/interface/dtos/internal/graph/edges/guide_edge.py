from pydantic import BaseModel


class GuideEdge(BaseModel):
    created_at: str
    document_mapping_id: int
