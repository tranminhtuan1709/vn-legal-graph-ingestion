from pydantic import BaseModel


class ChapterDto(BaseModel):
    id: int
    vbpl_id: int
    vbpl_big_part_id: int | None
    chapter_number: str | None
    chapter_name: str | None
