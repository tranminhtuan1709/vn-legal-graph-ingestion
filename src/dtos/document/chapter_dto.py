from pydantic import BaseModel


class ChapterDto(BaseModel):
    document_id: int
    big_part_id: int | None
    chapter_id: int
    chapter_number: str | None
    chapter_name: str | None
    