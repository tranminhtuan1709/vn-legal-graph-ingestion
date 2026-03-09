from pydantic import BaseModel
from typing import Any


class ExtractedChapter(BaseModel):
    id: Any
    vbpl_id: Any
    vbpl_big_part_id: Any
    chapter_number: Any
    chapter_name: Any
    