from pydantic import BaseModel


class ValidatedIssuingAuthority(BaseModel):
    id: int
    co_quan_ban_hanh: str
    