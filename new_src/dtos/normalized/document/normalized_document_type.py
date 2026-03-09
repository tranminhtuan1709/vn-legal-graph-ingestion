from pydantic import BaseModel


class NormalizedDocumentType(BaseModel):
    id: int
    loai_van_ban: str
    