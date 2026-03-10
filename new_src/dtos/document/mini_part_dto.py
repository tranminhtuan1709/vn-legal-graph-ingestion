from pydantic import BaseModel


class MiniPartDto(BaseModel):
    id: int
    vbpl_id: int
    vbpl_part_id: int | None
    mini_part_number: str | None
    mini_part_name: str | None
    