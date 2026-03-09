from pydantic import BaseModel
from typing import Any


class ExtractedPart(BaseModel):
    id: Any
    vbpl_id: Any
    vbpl_chapter_id: Any
    part_number: Any
    part_name: Any
    