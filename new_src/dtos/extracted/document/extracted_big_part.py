from pydantic import BaseModel
from typing import Any


class ExtractedBigPart(BaseModel):
    id: Any
    vbpl_id: Any
    big_part_number: Any
    big_part_name: Any
    