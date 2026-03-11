from pydantic import BaseModel


class BigPartDto(BaseModel):
    document_id: int
    big_part_id: int
    big_part_number: str | None
    big_part_name: str | None
    