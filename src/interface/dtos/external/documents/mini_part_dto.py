from pydantic import BaseModel


class MiniPartDto(BaseModel):
    id: int
    vbpl_id: int
    vbpl_part_id: int | None
    mini_part_number: int | None
    mini_part_name: int | None
