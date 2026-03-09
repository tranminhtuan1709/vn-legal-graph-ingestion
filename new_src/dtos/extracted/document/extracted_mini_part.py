from pydantic import BaseModel
from typing import Any


class ExtractedMiniPart(BaseModel):
    id: Any
    vbpl_id: Any
    vbpl_part_id: Any
    mini_part_number: Any
    mini_part_name: Any
    