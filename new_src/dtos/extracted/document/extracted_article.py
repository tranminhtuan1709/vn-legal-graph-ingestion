from pydantic import BaseModel
from typing import Any


class ExtractedArticle(BaseModel):
    id: Any
    vbpl_id: Any
    vbpl_big_part_id: Any
    vbpl_chapter_id: Any
    vbpl_part_id: Any
    vbpl_mini_part_id: Any
    section_number: Any
    section_name: Any
    section_content: Any
    so_phu_luc: Any
    effective_date: Any
    