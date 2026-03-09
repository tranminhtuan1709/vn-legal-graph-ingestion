from pydantic import BaseModel


class NormalizedIssuingAuthority(BaseModel):
    id: int
    co_quan_ban_hanh: str
    