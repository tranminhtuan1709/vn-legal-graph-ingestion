from pydantic import BaseModel


class SectorDto(BaseModel):
    id: int
    linh_vuc: str
