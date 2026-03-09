from pydantic import BaseModel


class NormalizedArticle(BaseModel):
    id: int
    vbpl_id: int
    vbpl_big_part_id: int | None
    vbpl_chapter_id: int | None
    vbpl_part_id: int | None
    vbpl_mini_part_id: int | None
    section_number: str | None
    section_name: str | None
    section_content: str | None
    so_phu_luc: str | None
    effective_date: str | None
    