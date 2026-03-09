from pydantic import BaseModel
from typing import Any


class ExtractedDocumentType(BaseModel):
    id: Any
    loai_van_ban: Any
    