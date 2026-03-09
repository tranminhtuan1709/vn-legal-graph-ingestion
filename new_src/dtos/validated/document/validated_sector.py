from pydantic import BaseModel


class ValidatedSector(BaseModel):
    id: int
    linh_vuc: str
    