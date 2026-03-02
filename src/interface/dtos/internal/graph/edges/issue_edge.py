from pydantic import BaseModel


class IssueEdge(BaseModel):
    created_at: str
