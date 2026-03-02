from pydantic import BaseModel


class ChapterNode(BaseModel):
    node_id: str
    created_at: str
    chapter_id: int
    chapter_number: str | None
    chapter_name: str | None
