from pydantic import BaseModel


class IssuingAuthorityDto(BaseModel):
    id: int
    co_quan_ban_hanh: str
