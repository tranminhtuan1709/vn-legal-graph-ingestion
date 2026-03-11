from pydantic import BaseModel
from datetime import date


class ArticleDto(BaseModel):
    document_id: int
    big_part_id: int | None
    chapter_id: int | None
    part_id: int | None
    mini_part_id: int | None
    article_id: int
    article_number: str | None
    article_name: str | None
    article_content: str | None
    appendix_number: str | None
    effective_date: date | None
    