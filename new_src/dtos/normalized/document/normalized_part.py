from pydantic import BaseModel


class NormalizedPart(BaseModel):
    id: int
    vbpl_id: int
    vbpl_chapter_id: int | None
    part_number: str | None
    part_name: str | None
    