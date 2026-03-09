from pydantic import BaseModel


class ValidatedDocumentType(BaseModel):
    id: int
    loai_van_ban: str
    