from pydantic import BaseModel


class MiniPartDto(BaseModel):
    document_id: int
    part_id: int | None
    mini_part_id: int
    mini_part_number: str | None
    mini_part_name: str | None
    