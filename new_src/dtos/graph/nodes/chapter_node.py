from pydantic import BaseModel


class ChapterNode(BaseModel):
    node_id: str
    node_label: str
    created_at: str
    source: str
    chapter_id: int
    chapter_number: str | None
    chapter_name: str | None
    