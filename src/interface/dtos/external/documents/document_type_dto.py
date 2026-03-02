from pydantic import BaseModel


class DocumentTypeDto(BaseModel):
    id: int
    loai_van_ban: str
