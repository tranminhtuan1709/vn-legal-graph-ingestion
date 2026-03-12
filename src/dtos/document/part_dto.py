from pydantic import BaseModel


class PartDto(BaseModel):
    document_id: int
    chapter_id: int | None
    part_id: int
    part_number: str | None
    part_name: str | None
    