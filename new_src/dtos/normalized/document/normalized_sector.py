from pydantic import BaseModel


class NormalizedSector(BaseModel):
    id: int
    linh_vuc: str
    